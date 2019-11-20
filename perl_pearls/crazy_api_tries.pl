
sub waitForElementPresent
{
   my $element = shift;
   my $arg1 = shift;
   print "waited for $element\n";
   print "arg1 = $arg1\n";
}

sub assertElementPresent
{
   my $element = shift;
   my $arg1 = shift;
   print "asserted :$element:\n";
   print "arg1 = :$arg1:\n";
}

sub lets_see_if_this_works
{
   my $sel_object = shift;
   my $sel_action = shift; 
   print "$sel_object - $sel_action\n";
   my $last_arg = pop( @_);
   print "last_arg = :$last_arg:\n";
   if ( $last_arg =~ /LOG/ ) {
	print "last_arg has LOG\n";
   } else {
	#Append it back to end if its not empty.
	push( @_, "$last_arg");
   }
  my $sel_api = "waitFor$sel_action";
  eval &$sel_api( @_);
  my $sel_api = "assert$sel_action";
  eval &$sel_api( @_);
}


lets_see_if_this_works( 1, "ElementPresent", "" );
lets_see_if_this_works( 1, "ElementPresent", 5);
lets_see_if_this_works( 1, "ElementPresent", 8, 9);
lets_see_if_this_works( 1, "ElementPresent", c, d, LOG);

