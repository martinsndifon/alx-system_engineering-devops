#!/usr/bin/env ruby
# Outputs sender's and receiver's information and flags from test messages

print ARGV[0].scan(/from:(\+?[a-zA-Z0-9]*)/).join
print ","
print ARGV[0].scan(/to:(\+?\w*)/).join
print ","
print ARGV[0].scan(/flags:(\+?[:\-0-9]*)/).join
print "\n"
