#!/usr/bin/env python
import sys, getopt, os
import webbrowser

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def verbose_task():
    try:
        with open(os.path.join(BASE_PATH, 'task.csv'),'r', encoding='utf-8') as task_file:
            for line in task_file:
                task = line.strip().split(',')
                print(task[0])
    except FileNotFoundError:
        assert False, 'buat task terlebih dahulu'

def save_to_file_csv(task):
    urls = []
    print('please input your urls, if you are done just type "done"')
    while True:
        url = input('[*] urls: ')
        if url == 'done':
            break
        urls.append(url)
    with open(os.path.join(BASE_PATH, 'task.csv'), 'a+', encoding='utf-8') as outfile:
        line = '%s' % (task)
        for link in urls:
            line += ',%s'%(link)
        outfile.write(line + '\n')

def remove_task(task):
    with open(os.path.join(BASE_PATH, 'task.csv'), 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    with open(os.path.join(BASE_PATH, 'task.csv'), 'w', encoding='utf-8') as outfile:
        for line in lines:
            task_line = line.strip().split(',')
            if task_line[0] != task:
                outfile.write(line)


def open_browser(task):
    try:
        with open(os.path.join(BASE_PATH, 'task.csv'), 'r', encoding='utf-8') as infile:
            for line in infile:
                task_line = line.strip().split(',')
                if task == task_line[0]:
                    for link in task_line[1:]:
                        webbrowser.open(link)
    except FileNotFoundError:
        assert False, 'buat task terlebih dahulu'

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vt:r:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)

    for o, v in opts:
        if o == '-v':
            verbose_task()
        elif o == '-t':
            save_to_file_csv(v)
        elif o == '-r':
            remove_task(v)
    
    if opts == []:
        open_browser(args[0])

if __name__ == "__main__":
    main()