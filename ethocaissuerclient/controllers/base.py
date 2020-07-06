
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version

VERSION_BANNER = """
An API client allowing an Issuer to use Ethoca %s
%s
""" % (get_version(), get_version_banner())

class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'An API client allowing an Issuer to use Ethoca'

        # text displayed at the bottom of --help output
        epilog = 'Usage: ethocaissuerclient command1 --foo bar'

        # controller level arguments. ex: 'ethocaissuerclient --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    #  @ex(
    #      help='example sub command1',
    #
    #      # sub-command level arguments. ex: 'ethocaissuerclient command1 --foo bar'
    #      arguments=[
    #          ### add a sample foo option under subcommand namespace
    #          ( [ '-f', '--foo' ],
    #            { 'help' : 'notorious foo option',
    #              'action'  : 'store',
    #              'dest' : 'foo' } ),
    #      ],
    #  )
    #  def command1(self):
    #      """Example sub-command."""
    #
    #      data = {
    #          'foo' : 'bar',
    #      }
    #
    #      ### do something with arguments
    #      if self.app.pargs.foo is not None:
    #          data['foo'] = self.app.pargs.foo
    #
    #      self.app.render(data, 'command1.jinja2')

    @ex(
        help='dump config to screen (WARNING will leak information)',
    )
    def dump_config(self):
        """Dump config to screen."""

        # https://docs.builtoncement.com/core-foundation/configuration-settings
        data = {
            'sections': self.app.config.get_sections(),
            'debug': self.app.config.get('ethocaissuerclient', 'debug'),
            'sandbox': self.app.config.get('ethocaissuerclient', 'sandbox'),
            'prod': self.app.config.get('ethocaissuerclient', 'prod'),
        }

        self.app.render(data, 'dump_config.jinja2')
