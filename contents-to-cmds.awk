# How to use:
# mutool clean DEN0137_1.0-rel0_rmm-arch_external.pdf rmm-contents.pdf 9-16
# docling --to md --image-export-mode placeholder rmm-contents.pdf
# gawk -f contents-to-cmds.awk rmm-contents.md > rmm-chaps.tsv
# manually fix rmm-chaps.tsv
# bash gen_mds.sh rmm-chaps.tsv DEN0137_1.0-rel0_rmm-arch_external.pdf rmm

BEGIN {
	prev_page = 0;
	prev_title = "";
}

function emit(title, start_page) {
	out_pdf = out_prefix "-" prev_title ".pdf";
	if (prev_page != 0 && prev_page != start_page)
		print prev_page "\t" (start_page-1) "\t" prev_title
	if (prev_page != start_page) {
		prev_page = start_page;
		prev_title = title;
	}
}

/\| [A-Z][1-9][0-9.]* .*\| [1-9]/ {
	match($0, /\| ([A-Z][1-9][0-9.]*) .*\| ([1-9][0-9]*) /, a);
	emit(a[1], a[2]);
	next;
}

/\| [A-Z][1-9][0-9.]* .*\.\.\. [1-9]/ {
	match($0, /\| ([A-Z][1-9][0-9.]*) .*\.\.\. ([1-9][0-9]*) /, a);
	emit(a[1], a[2]);
}

/\| [A-Z][1-9][0-9.]* .*\. \. \. [1-9]/ {
	match($0, /\| ([A-Z][1-9][0-9.]*) .*\. \. \. ([1-9][0-9]*) /, a);
	emit(a[1], a[2]);
}

END {
	emit("phoney", 99999);
}
