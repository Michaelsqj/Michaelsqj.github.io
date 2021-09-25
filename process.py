"""
This is the script to convert and process the notion/ typora format markdown file to jekyll acceptable files
"""
import os
import sys
import time

def gen_header(dict):
    header = ''
    for key, value in dict.items():
        header = header + key + ': ' + value + '\n'
    header = '---\n' + header + '---\n'
    return header

def delspace(tags):
    for i in range(len(tags)):
        tags[i] = '_'.join(tags[i].split(' '))
    return tags

def processSpecialChar(line):
    CharList = ['*','_','|','[',']']        # special characters that will errorly be translated by markdown rather than equation
    # find equation
    isEq = False
    output = ''
    for i in range(len(line)):
        if line[i] == "$":
            if i == len(line):
                return output + line[i]
            elif line[i+1] == '$':
                return line
            else:
                isEq = ~isEq
        elif isEq and (line[i] in CharList):
            if line[i-1] != "\\":
                output = output + '\\'
        output = output + line[i]
    return output

base_dir = "/Users/michael/Desktop/Export/Literature 503c6e128c5a48f79aaaf3c07b6576b9/";
os.chdir(base_dir)
print(os.getcwd())
date = time.strftime("%Y-%m-%d", time.localtime())
for file in os.listdir(base_dir):
    isfile = (file[-2:] == 'md')
    ori_name = file
    if isfile:
        fileHandler = open(ori_name, 'r')
        listofLines = fileHandler.readlines()

        img1 = r'''<div class="row mt-3"><div class="col-sm mt-3 mt-md-0"><img class="img-fluid rounded z-depth-1" src="{{ site.baseurl }}/assets/img/'''
        img2 = r'''" data-zoomable></div></div>'''
        # Generate the YAML head
        numnullline = 0
        dict = {'layout': 'post',
                'title' :  '',
                'date'  :  date,
                'description': '',
                'tags'  : '',
                'status': ''}
        modified = ''
        isHeadAdd = False
        for linenum, line in enumerate(listofLines):
            if line == '\n':                                # new line
                numnullline = numnullline + 1
            if (not isHeadAdd) and numnullline < 2:                             # this part don't write in to new file
                if line != "\n":
                    line = line.replace("\n", "")
                if line[0] == '#':                          # title
                    temp = line[2:]
                    if ":" in temp:
                        temp = temp.replace(":", "")
                    dict['title'] = temp              # delete the \n at the end
                elif line[:len('Status: ')] == 'Status: ':      # status
                    dict['status'] = line[len('Status: '):]
                elif line[:len('Type: ')] == 'Type: ':          # tags
                    tags = line[len('Type: '):].split(', ')
                    tags = delspace(tags)
                    dict['tags'] = ' '.join(tags)
                elif line[:len('Comment: ')] == 'Comment: ':
                    dict['description'] = line[len('Comment: '):]
            elif numnullline == 2 and not isHeadAdd:                          # write the header to the text
                modified = modified + gen_header(dict) + '\n'
                isHeadAdd = True
            elif isHeadAdd:
                if ('png' in line or 'jpg' in line) and ('![' in line) and ('](' in line):     # image 
                    imgname = line[line.find('(')+1:line.find(')')]
                    line = ' '*line.find('!') + img1 + imgname + img2 + '\n'
                else:                                                                           # deal with special characters in equation
                    line = processSpecialChar(line)

                modified = modified + line

        if numnullline < 2 and not isHeadAdd:                          # for file doesnt have content
            modified = modified + gen_header(dict)
            isHeadAdd = True

        new_name = date + '-' + ori_name
        f = open(new_name, 'w')
        f.write(modified)
        print(file)
