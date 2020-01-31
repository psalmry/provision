from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		check = str(user.pk) + str(timestamp) + str(user.profile.signup_confirmation)
		print (check)
		return (
			check

				)

account_activation_token = AccountActivationTokenGenerator()