from cement import Controller, ex

# import time
import hmac
import hashlib
import datetime
import uuid
import requests
import base64
import json
# import os

class Receipts(Controller):
    class Meta:
        label = 'receipts'
        stacked_type = 'nested'
        stacked_on = 'base'

    @ex(
        help='get receipt url',
        arguments=[
            (['-e', '--env' ],
             {'help' : 'environment: [sandbox, prod]',
              'action'  : 'store',
              'dest' : 'env' } ),
            (['-t', '--trn' ],
             {'help' : 'TRN to use for lookup (require this or ARN)',
              'action'  : 'store',
              'dest' : 'trn' } ),
            (['-a', '--arn' ],
             {'help' : 'ARN to use for lookup (require this or TRN)',
              'action'  : 'store',
              'dest' : 'arn' } ),
            (['-c', '--auth_code' ],
             {'help' : 'Auth Code to use for lookup (required)',
              'action'  : 'store',
              'dest' : 'auth_code' } ),
        ],
    )
    def get(self):
        # CLI args
        env = self.app.pargs.env
        trn = self.app.pargs.trn or ''
        arn = self.app.pargs.arn or ''
        auth_code = self.app.pargs.auth_code or ''

        # we will use either an ARN or a TRN as the lookup ID
        idtype = 'trn' if len(trn) > 0 else 'arn'
        id = trn if len(trn) > 0 else arn

        if env != 'sandbox' and env != 'prod':
            msg = 'Receipts environment must be sandbox or prod'
            self.app.log.error(msg)
            return msg
        if len(trn) == 0 and len(arn) == 0:
            msg = 'Receipts requires either a TRN or an ARN arguement'
            self.app.log.error(msg)
            return msg
        if len(auth_code) < 4:
            msg = 'Receipts requires an AUTH_CODE arguement'
            self.app.log.error(msg)
            return msg

        self.app.log.info(
            'Receipts <- {idtype} {id} & auth_code {auth_code}'
            .format(idtype=idtype, id=id, auth_code=auth_code))

        # TODO consider moving this to a shared client

        # config
        config = self.app.config.get('ethocaissuerclient', env)
        apikey = config.get('apikey')
        keyid = config.get('keyid')
        host = config.get('host')
        merchantid = config.get('merchantid', 'unspecifed_merchant')

        # functionality
        issuerToken = uuid.uuid4()
        traceId = uuid.uuid4()
        ethDate = datetime.datetime.utcnow().isoformat()[:-3] + 'Z'

        payload = {
            'merchantId': merchantid,
            'issuerToken': str(issuerToken),
            'issuerAuthorizationCode': auth_code,
            'traceId': str(traceId),
            'locale': 'en-US'
        }
        if idtype == 'trn':
            payload.update({'tranId': trn})
        else:
            payload.update({'arn': arn})

        bodyStr = json.dumps(payload)

        uri = 'https://' + host + '/api/v1/orders'
        signing_template = '%s\n%s\n%s\n%s\n%s\n%s'
        text_to_sign = signing_template % (host,
                                           uri,
                                           'POST',
                                           'application/json',
                                           ethDate,
                                           bodyStr)
        signature = hmac.new(b'{apikey}',
                             text_to_sign.encode('utf-8'),
                             hashlib.sha1)
        sig_base64 = base64.urlsafe_b64encode(signature.digest())
        authText = 'ETHOCA-SHA1 KeyRef=%s,Signature=%s' % (keyid, sig_base64)


        getHeaders = {
            'Accept': 'application/json',
            'Authorization': authText,
            'X-Eth-Date': ethDate,
            'Content-Type': 'application/json'
        }
        r = requests.post(uri, headers=getHeaders, data=bodyStr)

        self.app.log.info(
            'Receipts -> {status_code}'
            .format(status_code=r.status_code))
        self.app.log.info(r.text)

        return r
