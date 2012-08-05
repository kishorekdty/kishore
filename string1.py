# A. donuts

def donuts(count):
  if count < 10:
    return 'Number of donuts: ' + str(count)
  else:
    return 'Number of donuts: many'


# B. both_ends

def both_ends(s):
  
  if len(s) < 2:
    return ''
  f2 = s[0:2]
  l2 = s[-2:]
  nwstr=f2+l2
  return nwstr


# C. fix_start

def fix_start(s):
  head=s[0]
  tail=s[1:]
  nwstr=tail.replace(head,'*')
  return head+nwstr


# D. MixUp

def mix_up(a, b):
  hd_b=b[:2]
  tl_a=a[2:]
  nw_a=hd_b+tl_a
  hd_a=a[:2]
  tl_b=b[2:]
  nw_b=hd_a+tl_b
  return nw_a+' '+nw_b

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
  print 'donuts'
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print
  print 'both_ends'
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  
  print
  print 'fix_start'
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print
  print 'mix_up'
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')

if __name__ == '__main__':
  main()
