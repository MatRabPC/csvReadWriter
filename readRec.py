import csv

with open('collection.csv', 'rb') as f:
    reader = csv.DictReader(f)

    #fieldnames = ['Catalog#', 'Artist', 'Title', 'Label', 'Format', 'Rating', 'Released', 'release_id', 'CollectionFolder', 'Date Added', 'Collection Media Condition', 'Collection Sleeve Condition', 'Collection Notes']

    output = []#array that Artists and Titles are saved in
    classes = []#list of folders in csv

    classRequest = raw_input('Which field would you like to organize by? ' + f.next()) #user picks field

    #Add all unique entries to array folders
    f.seek(0)
    for row in reader:
        if row[classRequest] not in classes:
            classes.append(row[classRequest])

    field = raw_input('What ' + classRequest + ' do you want printed?\n' + ' '.join(classes) + '\n')

    #Add all Artists and Album titles in a field to array titles in Artist order
    f.seek(0)
    for row in reader:
        if row[classRequest] == field:
            output.append([row['Artist'], row["Title"]])
            print row['Artist'], "-", row['Title']
        output.sort()

#write all items in array to file 'output.txt'
with open('output.txt', 'w') as w:
    i = 0
    while i < len(output):
        w.write("%s - %s\n" % (output[i][0], output[i][1]))
        i += 1