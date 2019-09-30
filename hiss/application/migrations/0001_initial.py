# Generated by Django 2.2.4 on 2019-09-30 20:02

import application.models
import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime_submitted', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=255, validators=[application.models.is_alpha], verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, validators=[application.models.is_alpha], verbose_name='last name')),
                ('major', models.CharField(choices=[(None, '-- Select Option --'), ('Accounting', 'Accounting'), ('Actuarial Science', 'Actuarial Science'), ('Advertising', 'Advertising'), ('Agriculture', 'Agriculture'), ('Agricultural and Biological Engineering', 'Agricultural and Biological Engineering'), ('Agricultural Business Management', 'Agricultural Business Management'), ('Agriculture Economics', 'Agriculture Economics'), ('Animal Bioscience', 'Animal Bioscience'), ('Animal Sciences', 'Animal Sciences'), ('Anthropology', 'Anthropology'), ('Applied Mathematics', 'Applied Mathematics'), ('Archaeology', 'Archaeology'), ('Architectural Engineering', 'Architectural Engineering'), ('Architecture', 'Architecture'), ('Art History', 'Art History'), ('Studio Art', 'Studio Art'), ('Art Education', 'Art Education'), ('Biobehavioral Health', 'Biobehavioral Health'), ('Biochemistry', 'Biochemistry'), ('Bioengineering', 'Bioengineering'), ('Biology', 'Biology'), ('Biophysics', 'Biophysics'), ('Biotechnology', 'Biotechnology'), ('Business Administration and Management', 'Business Administration and Management'), ('Business Logistics', 'Business Logistics'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Children', 'Children'), ('Civil Engineering', 'Civil Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Computer Science', 'Computer Science'), ('Crime, Law, and Justice', 'Crime, Law, and Justice'), ('Dance', 'Dance'), ('Earth Sciences', 'Earth Sciences'), ('Economics', 'Economics'), ('Electrical Engineering', 'Electrical Engineering'), ('Elementary and Kindergarten Education', 'Elementary and Kindergarten Education'), ('Engineering Science', 'Engineering Science'), ('English', 'English'), ('Environmental Systems Engineering', 'Environmental Systems Engineering'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Resource Management', 'Environmental Resource Management'), ('Film and Video', 'Film and Video'), ('Finance', 'Finance'), ('Food Science', 'Food Science'), ('Forest Science', 'Forest Science'), ('Forest Technology', 'Forest Technology'), ('General Science', 'General Science'), ('Geography', 'Geography'), ('Geosciences', 'Geosciences'), ('General Engineering', 'General Engineering'), ('Graphic Design and Photography', 'Graphic Design and Photography'), ('Health and Physical Education', 'Health and Physical Education'), ('Health Policy and Administration', 'Health Policy and Administration'), ('History', 'History'), ('Horticulture', 'Horticulture'), ('Hotel, Restaurant, and Institutional Management', 'Hotel, Restaurant, and Institutional Management'), ('Human Development and Family Studies', 'Human Development and Family Studies'), ('Individual and Family Studies', 'Individual and Family Studies'), ('Industrial Engineering', 'Industrial Engineering'), ('Information Sciences and Technology', 'Information Sciences and Technology'), ('Journalism', 'Journalism'), ('Kinesiology', 'Kinesiology'), ('Landscape Architecture', 'Landscape Architecture'), ('Law Enforcement and Correction', 'Law Enforcement and Correction'), ('Marine Biology', 'Marine Biology'), ('Marketing', 'Marketing'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Media Studies', 'Media Studies'), ('Meteorology', 'Meteorology'), ('Microbiology', 'Microbiology'), ('Mineral Economics', 'Mineral Economics'), ('Modern Languages', 'Modern Languages'), ('Music Education', 'Music Education'), ('Nuclear Engineering', 'Nuclear Engineering'), ('Nursing', 'Nursing'), ('Nutrition', 'Nutrition'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Physiology', 'Physiology'), ('Political Science', 'Political Science'), ('Pre-medicine', 'Pre-medicine'), ('Psychology', 'Psychology'), ('Public Relations', 'Public Relations'), ('Real Estate', 'Real Estate'), ('Recreation and Parks', 'Recreation and Parks'), ('Rehabilitation Services', 'Rehabilitation Services'), ('Religious Studies', 'Religious Studies'), ('Secondary Education', 'Secondary Education'), ('Sociology', 'Sociology'), ('Social Work', 'Social Work'), ('Special Education', 'Special Education'), ('Speech Communication', 'Speech Communication'), ('Speech Pathology and Audiology/Communication Disorder', 'Speech Pathology and Audiology/Communication Disorder'), ('Statistics', 'Statistics'), ('Telecommunications', 'Telecommunications'), ('Theater', 'Theater'), ('Wildlife and Fishery Science', 'Wildlife and Fishery Science'), ('Wildlife Technology', 'Wildlife Technology'), ("Women's Studies", "Women's Studies")], max_length=255, verbose_name="What's your major?")),
                ('gender', models.CharField(choices=[(None, '-- Select Option --'), ('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('NA', 'Prefer not to disclose'), ('O', 'Other')], max_length=2, verbose_name="What's your gender?")),
                ('race', multiselectfield.db.fields.MultiSelectField(choices=[('American Indian', 'American Indian or Alaskan Native'), ('Asian', 'Asian'), ('Black', 'Black or African-American'), ('Hispanic', 'Hispanic or Latino White'), ('Native Hawaiian', 'Native Hawaiian or other Pacific Islander'), ('White', 'White or Caucasian'), ('NA', 'Decline to self-identify'), ('Other', 'Other')], max_length=41, verbose_name='What race(s) do you identify with?')),
                ('classification', models.CharField(choices=[(None, '-- Select Option --'), ('Fr', 'Freshman'), ('So', 'Sophomore'), ('Jr', 'Junior'), ('Sr', 'Senior'), ('Ot', 'Other')], max_length=2, verbose_name='What classification are you?')),
                ('grad_term', models.CharField(choices=[(None, '-- Select Option --'), ('Fall 2019', 'Fall 2019'), ('Spring 2020', 'Spring 2020'), ('Fall 2020', 'Fall 2020'), ('Spring 2021', 'Spring 2021'), ('Fall 2021', 'Fall 2021'), ('Spring 2022', 'Spring 2022'), ('Fall 2022', 'Fall 2022'), ('Spring 2023', 'Spring 2023'), ('Other', 'Other')], max_length=11, verbose_name='What is your anticipated graduation date?')),
                ('num_hackathons_attended', models.CharField(choices=[(None, '-- Select Option --'), ('0', 'This will be my first!'), ('1-3', '1-3'), ('4-7', '4-7'), ('8-10', '8-10'), ('10+', '10+')], max_length=22, verbose_name='How many hackathons have you attended?')),
                ('previous_attendant', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Have you attended HowdyHack before?')),
                ('tamu_student', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Are you a Texas A&M student?')),
                ('extra_links', models.CharField(blank=True, max_length=200, verbose_name="Point us to anything you'd like us to look at while considering your application")),
                ('question1', models.TextField(max_length=500, verbose_name='Tell us your best programming joke')),
                ('question2', models.TextField(max_length=500, verbose_name="What is the one thing you'd build if you had unlimited resources?")),
                ('question3', models.TextField(max_length=500, verbose_name="What is a cool prize you'd like to win at HowdyHack?")),
                ('approved', models.NullBooleanField()),
                ('agree_to_coc', models.BooleanField(choices=[(True, 'Agree')], default=None)),
                ('is_adult', models.BooleanField(choices=[(True, 'Agree')], default=None, help_text='Please note that freshmen under 18 must be accompanied by an adult or prove that they go to Texas A&M.', verbose_name='Please confirm you are 18 or older')),
                ('transport_needed', models.CharField(choices=[('drive', 'Driving'), ('th-bus', 'TAMUhack Bus'), ('fly', 'Flying'), ('public', 'Public Transportation'), ('walk-cycle', 'Walking/Biking')], max_length=11)),
                ('additional_accommodations', models.TextField(blank=True, max_length=500, verbose_name='Do you require any special accommodations at the event?')),
                ('resume', models.FileField(help_text='Companies will use this resume to offer interviews for internships and full-time positions.', upload_to=application.models.uuid_generator, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Upload your resume')),
                ('notes', models.TextField(blank=True, max_length=300, verbose_name='Anything else you would like us to know?')),
            ],
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('num_days_to_rsvp', models.IntegerField()),
            ],
        ),
    ]
