import json

# Open the JSON file and load the data
with open('user_interactions.json') as f:
    data = json.load(f)

# Open the markdown file for writing
with open('tutorial.md', 'w') as f:

    # Write the header
    f.write('# Tutorial for Using ' + data['metadata']['software'] + '\n\n')

    # Loop through each interaction and write the markdown
    for interaction in data['interactions']:

        # Write the section header with the human-readable description of the action
        if interaction['type'] == 'click':
            f.write('## Click the ' + interaction['label'] + ' Button\n\n')
            f.write('To perform the following action:\n\n')
            f.write('* Load an image\n\n')
            if interaction['label'] == 'Process Image':
                f.write('* Process the loaded image\n\n')
            elif interaction['label'] == 'Zoom In':
                f.write('* Zoom in on the loaded image\n\n')
            elif interaction['label'] == 'Zoom Out':
                f.write('* Zoom out on the loaded image\n\n')
            elif interaction['label'] == 'Rotate Left':
                f.write('* Rotate the loaded image left\n\n')
            elif interaction['label'] == 'Rotate Right':
                f.write('* Rotate the loaded image right\n\n')
        elif interaction['type'] == 'key_press':
            f.write('## Press the ' + interaction['key'].upper() + ' Key\n\n')
            f.write('To perform the following action:\n\n')
            f.write('* Save the current image\n\n')
        elif interaction['type'] == 'scroll':
            f.write('## Scroll ' + interaction['direction'].title() + '\n\n')
            f.write('To perform the following action:\n\n')
            f.write('* Scroll the loaded image ' + interaction['direction'].lower() + '\n\n')
        elif interaction['type'] == 'hover':
            f.write('## Hover over the ' + interaction['label'] + ' Button\n\n')
            f.write('To view the tooltip for the following action:\n\n')
            f.write('* Zoom in on the loaded image\n\n')
        elif interaction['type'] == 'drag':
            f.write('## Drag the Loaded Image\n\n')
            f.write('To perform the following action:\n\n')
            f.write('* Move the loaded image from the starting position to the ending position\n\n')

        # Write the screenshot and pointer location
        f.write('![Screenshot](' + interaction['screenshot'] + ')\n\n')
        f.write('Pointer Location: (' + str(interaction['pointer_location']['x']) + ', ' + str(interaction['pointer_location']['y']) + ')\n\n')
