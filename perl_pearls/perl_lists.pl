
# Stat returns list value.
$modification_time = (stat($0))[9];
print "modification_time = $modification_time\n";
# SYNTAX ERROR HERE.
#$modification_time = stat($file)[9];  # OOPS, FORGOT PARENS

# Find a hex digit.
$digit = 12;
$hexdigit = ('a','b','c','d','e','f')[$digit-10];
print "hexdigit = $hexdigit\n";

# A "reverse comma operator".
#return (pop(@foo),pop(@foo))[0];


# Get multiple values as a slice.
($day, $month, $year) = (localtime)[3,4,5];

print "$day, $month, $year\n";

