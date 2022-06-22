#!/usr/bin/env ruby
puts ARGV[0].scan(/^[htbn]{3}.{1,}*$/).join
