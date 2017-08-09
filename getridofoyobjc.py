import subprocess

all_sentences = """
pyobjc-framework-NetFS (3.2.1)
pyobjc-framework-NetworkExtension (3.2.1)
pyobjc-framework-NotificationCenter (3.2.1)
pyobjc-framework-OpenDirectory (3.2.1)
pyobjc-framework-Photos (3.2.1)
pyobjc-framework-PhotosUI (3.2.1)
pyobjc-framework-PreferencePanes (3.2.1)
pyobjc-framework-PubSub (3.2.1)
pyobjc-framework-QTKit (3.2.1)
pyobjc-framework-Quartz (3.2.1)
pyobjc-framework-SafariServices (3.2.1)
pyobjc-framework-SceneKit (3.2.1)
pyobjc-framework-ScreenSaver (3.2.1)
"""

sentence = all_sentences.split('\n')

# Get rid of a list element like ''
for element in sentence:
    if element is '':
        sentence.remove('')

# Get rid of version descrption like (3.2.1)
for index, element in enumerate(sentence):
    sentence[index] = element.split(' ')[0]

for element in sentence:
    res = subprocess.check_call(['pip3', 'uninstall', element])
    if res is 0:
        print('Success: Uninstall of' + element)
    else:
        print('Fail: Uninstall of' + element)

print('END OF PROGRAM.\n')
