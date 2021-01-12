# vlan_workbook_formatter

Script to filter ranges in excel workbooks (used by migration tool) converts an output like this:

- 1,2,3-10

into:

- 1,2,3,4,5,6,7,8,9,10

## Examples

<pre>
python items_from_range.py [path_to_file] [column to filter]
</pre>
