# gitTopRepoCommitters
get top repo's and their committers along with their commit counts for an organisation

usage : python gitrepocommits.py  -o <orgname> -r <r top repos> -c <c top commits>

example : python gitrepocommits.py -o google -r 10 -c 5

when no arguments specified: org=google, r=5, c=3

Example :
$python gitrepocommits.py -o google -r 5 -c 3

      dagger Ron|Shapiro|30
      ios-webkit-debug-proxy|artygus|11
      ios-webkit-debug-proxy|GitHub|10
      ios-webkit-debug-proxy|Arty Gus|4
      tracing-framework Stella|Laurenzo|14
      tracing-framework|Ben Vanik|8
      tracing-framework|GitHub|4
      google-api-ruby-client|Sai Cheemalapati|9
      google-api-ruby-client|GitHub|8
      google-api-ruby-client|Thomas Coffee|7
      signet|Steven Bazyl|23
      signet|Yosuke Kabuto|3
      signet|GitHub|2
