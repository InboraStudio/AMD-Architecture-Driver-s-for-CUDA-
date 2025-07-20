#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <RELEASE_VERSION>" >&2
    exit 1;
fi

python3 tag_script.py --no-pulls --no-release --no-previous -x MIVisionX --branch release/rocm-rel-${1} ${1} .changelogs.txt
sed -i 's/^#{3} /##### /g' .changelogs.txt
sed -i 's/^# /#### /g' .changelogs.txt

[ -d ROCm ] && rm -rf ROCm
git clone git@github.com:ROCm/ROCm.git

awk -f- ROCm/README.md .changelogs.txt >.tmp.txt <<-'EOF'
BEGIN {
    started_rocm_libraries = 0
    while (getline <ARGV[2]) {
        logfile = logfile $0 "\n"
    }
    delete ARGV[2]
}

{
    line_processed = 0
}

/^###[^#]/ {
    line_processed = 1
    if (started_rocm_libraries == 0) {
        print $0
        if ($0 == "### ROCm Libraries") {
            print ""
            started_rocm_libraries = 1
        }
    } else {
        print logfile "\n" $0
        started_rocm_libraries = 0
    }
}

line_processed == 0 {
    if (started_rocm_libraries == 0) {
        print $0
    }
}
EOF

rm ROCm/README.md .changelogs.txt
mv .tmp.txt ROCm/README.md

cd ROCm
branch="roc-${1:0:3}.x"
if [[ -z "$(git ls-remote --heads origin ${branch})" ]]; then
    git checkout -b ${branch}
    git add README.md
    git commit -m "Updated README.md for ROCm ${1}"
    git push -u origin ${branch}
else
    git checkout ${branch}
    git add README.md
    git commit -m "Updated README.md for ROCm ${1}"
    git push -u origin ${branch}
fi
