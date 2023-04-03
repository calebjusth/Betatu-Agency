from django.db import models

# Create your models here.


#testimonials area
class testimonial(models.Model):
	experience = models.TextField()
	name_of_testifier = models.CharField(max_length=200, null=False, blank=False)

	def __str__(self):
		return self.name_of_testifier

#blog area
class blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    main = models.CharField(max_length=20, null=True)
    body = models.TextField(default=True)
    image = models.ImageField(upload_to='blogs/', null=False, blank=False)
    def __str__(self):
        return self.title


    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
#team
class team(models.Model):
	name =models.CharField(max_length=20, null=True)
	profession = models.CharField(max_length=150, null=True)
	position_in_betatu = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.position_in_betatu


	@property
	def imageUrl(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

#setting up user profile 


#user_profiles
class user_profile(models.Model):
	profile_pic = models.ImageField(upload_to='profiles/', null=False, blank=False)
	profession = models.CharField(max_length=30, null=True)
	educational_background = models.CharField(max_length=200, null=True)
	mobile = models.CharField(max_length=10, null=True)
	experience = models.CharField(max_length=200, null=True)
	user_bio = models.CharField(max_length=200, null=True)
	user_cv = models.CharField(max_length=200, null=False, default=False)

	def __str__(self):
		return self.mobile

	@property
	def imageUrl(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url