from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        url = super(AccountAdapter, self).get_login_redirect_url(request)
        user = request.user