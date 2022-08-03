#Translations

### Create and update translation files 
Go to /blog directory
`cd blog`

Specify language with parameter -l
`django-admin makemessages -l de`
`django-admin makemessages -l en`

### Translate
In locale directory find directories with language (e.g. de, en)
Open django.po files and add translations to msgstr

### Compile translations
After you created translation files and added translations, compile it:
`django-admin compilemessages`
