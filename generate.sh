#!/bin/sh

# Runs all generator scripts, commits and pushes generated changes.
#
# This scripts assumes that a clone of the Remuco source repository (Mercurial)
# is located at `../`

die() {
        [ -n "$1" ] && echo "abort: $1" || echo "abort"
        exit 1
}

REMUCO_REPO_ID_EXP="de215cd2c943a688a03c520d92bb3f501af3a1c0"
REMUCO_REPO_ID_REAL="`hg -R .. id --debug -r 0 2>/dev/null`"
if [ "$REMUCO_REPO_ID_REAL" != "$REMUCO_REPO_ID_EXP" ] ; then
	die "need a local (and up-to-date) remuco source repository at ../"
fi

[ -z "`hg st | grep -v "^\?"`" ] || die "uncommited changes"

hg fetch || die "pull failed"

for GEN in `ls *.py` ; do
    PAGE=`echo $GEN | sed -e "s/\.py$/.wiki/"`
    if [ -e $PAGE ] ; then
        echo "generate $PAGE"
        python $GEN || die "generator failed"
    fi
done

echo -n "press ENTER to commit and push wiki changes .."
read X

echo "commit wiki changes"
hg ci -m "Generator update" || die "commit failed"

hg push || die "push failed"

echo "done"
