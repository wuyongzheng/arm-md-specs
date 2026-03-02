import sys

def emit(pdf, tmp_pdf, start_page, end_page):
    print('mutool clean {} "{}" {}-{} ; '.format(pdf, tmp_pdf, start_page, end_page), end="")
    print('docling --to md --image-export-mode placeholder "{}" ; '.format(tmp_pdf), end="")
    print('rm "{}"'.format(tmp_pdf))

def main(argv):
    if len(argv) != 4:
        print("Usage:   python3 outline2cmds.py prefix in-outline.tsv in-pdf.pdf")
        print("Example: python3 outline2cmds.py rmm2 rmm2-outline.tsv DEN0137_2.1-alp0_rmm-arch_external.pdf")
        return
    prefix = argv[1]
    outline = argv[2]
    pdf = argv[3]

    title_seen = {}
    prev_page = -1
    prev_title = None
    with open(outline) as fp:
        for line in fp:
            arr = line.strip().split("\t")
            page = int(arr[1])
            title = arr[2]
            if prev_title:
                if prev_page == page:
                    print("echo WARNING: repeated page", page)
                if title in title_seen:
                    print("echo WARNING: repeated title", title)
                emit(pdf, '{}-{}.pdf'.format(prefix, prev_title.split()[0]), prev_page, page-1)
            title_seen[title] = True
            prev_page = page
            prev_title = title
    if prev_title:
        emit(pdf, '{}-{}.pdf'.format(prefix, prev_title.split()[0]), prev_page, 9999)

if __name__ == '__main__':
    main(sys.argv)
