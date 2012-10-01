#
# This script should write the subject used for the emails sent by pcull when 
# it renices processes.  Note that this is sourced from the main script, so any 
# variables defined there are available for use here.
#

echo "[$user] Odyssey access node load manager lowered the priority of process [$cmd] running on [$(hostname | awk -F. '{print $1}')]"
