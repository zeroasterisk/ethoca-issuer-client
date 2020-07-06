from cement import Controller, ex

class Receipts(Controller):
    class Meta:
        label = 'receipts'
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(help='get receipt url')
    def get(self):
        pass
