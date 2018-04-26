import re
name = "Jianlong Fu"
def print_paper_head(index):
    print (r'''<TR> <TD class="pubindex"><FONT>[%d]&nbsp</FONT></TD> <TD STYLE ="VERTICAL-ALIGN: TOP">''' % index)
def print_paper_name(paper_name):
    paper_name = paper_name.strip()
    print (r'''<FONT class="pubtitle">%s. </FONT>''' % paper_name)
def print_authors_list(authors_list):
    authors_list = authors_list.strip()
    authors_list = authors_list.replace(name, '''<b>%s</b>''' % name)
    print (r'''<FONT >%s. </FONT>''' % authors_list)
def print_conference(conference):
    conference = conference.strip()
    print (r'''<FONT class="pubbooktitle">%s. </FONT>''' % conference)
link_reg = re.compile(r'''\[(.*?)\]\((.*?)\)''')
def print_link(link):
    u = link_reg.search(link)
    g = u.groups()
    print (r'''<FONT> &nbsp;[<a href="%s" target="_blank">%s</a>]</FONT>''' % (g[1], g[0]))
def print_paper_tail():
    print (r'''</TD></TR>''')
    print ('\n')

count = 0
fin = open('paper.md')
for line in fin.readlines():
    if line[0] == '-':
        count += 1

fin = open('paper.md')
try:
    line = fin.readline()
    while len(line):
        if line[0] == '#' or line[0] == ' ':
            line = fin.readline()
            continue
        if line[0] == '-':
            paper_name = line.split('- ')[1]
            authors_list = fin.readline()
            conference = fin.readline()
            line = fin.readline()
            print_paper_head(count)
            count -= 1
            print_paper_name(paper_name)
            print_authors_list(authors_list)
            print_conference(conference)
            try:
                while len(line) > 0 and line[0] == '[':
                    print_link(line)
                    line = fin.readline()
            except EOFError:
                break
            print_paper_tail()

except EOFError:
    pass
