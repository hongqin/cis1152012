#! /usr/bin/perl -w
# simple_reciprocal_best_hits.00.pl -m9 output?

BEGIN { unshift(@INC,"/home/hqin/lib/perl/", "/Users/hongqin/lib/perl");   }

#052908 bug, missing last hit.

# v0.00 April 13, 2004 Primitive version, take only the top hit

use strict; use warnings; 
use Getopt::Long;   
use Util;  use FASTA; use moran; 

my $in_blast_fl1 = undef; 	
my $in_blast_fl2 = undef; 	
my $out_tab_fl = undef;	
my $parsing_levels = 0; # 0 primitive, 1 check for duplicates, 2 Z-score evaluation
my $verbose = 0;	
my $debug = 0; 	

# temporary variables
 my ($num, $i, $flag, $line, @lines, @buffers) = ();

 if ( ! $ARGV[0]) { _help(); exit(1); }

 GetOptions('in_blast_fl1|i1=s' => \$in_blast_fl1,
 	    'in_blast_fl2|i2=s' => \$in_blast_fl2,
 	    'out_tab_fl|o=s' => \$out_tab_fl,
            'parsing_levels|l=i' => \$parsing_levels, 
            'verbose|v=i' => \$verbose, 
            'debug|d=i' => \$debug);

 if ( ( ! $in_blast_fl1 ) or ( ! $in_blast_fl2 ) ) { _help(); exit(1); }    
 my $alias_1 =  get_shortened_name ( $in_blast_fl1 );  
 my $alias_2 =  get_shortened_name ( $in_blast_fl2 );   
 my $short_time_stamp =  get_short_time_stamp_US();

 if ( !(defined $out_tab_fl) ) {
    $out_tab_fl = "reciprocal_best_hits_from_$alias_1.AND.$alias_2";  
 }

# key variables
 my %hits_1 = ();	
 my %hits_2 = ();
 my %shared_hits = ();

# other variables
 my ( $current_query_id, $current_subject_id, $current_bit_score ) = ( 'NA', 'NA', 0 );
 
 open (IN1, "<$in_blast_fl1");
 while ( $line =<IN1> ) {
   if ( $line !~ /^#/ ) {
      chomp $line;
      my @tokens = split ( /\t/, $line );
      if ( $tokens[0] ne $current_query_id ) { # first line of this query results
         # store current results here
	 #if ( $current_query_id ne 'NA' ) {  
	   $hits_1{ $tokens[0] } = $tokens[1]; # 052908 there is a logical error here. 
	 #}
	 
	 # parse new results
         $current_query_id = $tokens[0];
	 #$current_subject_id = $tokens[1];
	 #$current_bit_score = $tokens[ $#tokens ]; 
      } else { # continuous lines of the current query
         # implement advanced parsing levels here
	 
      }
   }
 }
 

 open (IN2, "<$in_blast_fl2");
 while ( $line =<IN2> ) {
   if ( $line !~ /^#/ ) {
      chomp $line;
      my @tokens = split ( /\t/, $line );
      if ( $tokens[0] ne $current_query_id ) { # first line of this query results
         # store current results here
	 #if ( $current_query_id ne 'NA' ) {
	   #$hits_2{ $current_query_id } = $current_subject_id; #052908
	   $hits_2{ $tokens[0] } = $tokens[1]; #052908
	 #}
	 
	 # parse new results
         $current_query_id = $tokens[0];
	 #$current_subject_id = $tokens[1];
	 #$current_bit_score = $tokens[ $#tokens ]; 
      } else { # continuous lines of the current query
         # implement advanced parsing levels here
	 
      }
   }
 }

if ($debug) { showHashTable( \%hits_1 ); }
if ($debug) { showHashTable( \%hits_2 ); }
   
# get reciprocal best hits
 foreach my $id1 ( keys %hits_1 ) {
   if ( ( exists $hits_2{ $hits_1{$id1} } ) and ( $hits_2{ $hits_1{$id1} } eq $id1 ) ) {
      $shared_hits{ $id1 } = $hits_1{ $id1 };
   }
 }

if ($debug) { showHashTable( \%shared_hits); }
  
write_hash2file(\%shared_hits, $out_tab_fl, "\t");

# clean garbage files

exit;

#------------------------------
sub _help {
print "
 $0

 GetOptions('in_blast_fl1|i1=s' => \$in_blast_fl1,
 	    'in_blast_fl2|i2=s' => \$in_blast_fl2,
 	    'out_tab_fl|o=s' => \$out_tab_fl,
            'verbose|v=i' => \$verbose, 
            'debug|d=i' => \$debug);
 Note: this primitive version only take the single top hit.

";
}

