import re

with open('test.txt') as f:
    contents = f.read()

contents.strip()
line_length =  len(contents.splitlines()[0])
contents = ''.join(contents.splitlines())
print (contents)
pattern_h_r = r'XMAS'
pattern_h_l = r'SAMX'
pattern_v_d = fr"X.{{{line_length-1}}}M.{{{line_length-1}}}A.{{{line_length-1}}}S"
pattern_v_u = fr"S.{{{line_length-1}}}A.{{{line_length-1}}}M.{{{line_length-1}}}X"
pattern_d_dr = fr"X.{{{line_length}}}M.{{{line_length}}}A.{{{line_length}}}S"
pattern_d_ul = fr"S.{{{line_length}}}A.{{{line_length}}}M.{{{line_length}}}X"

pattern_d_dl = fr"X.{{{line_length-2}}}M.{{{line_length-2}}}A.{{{line_length-2}}}S"
pattern_d_ur = fr"S.{{{line_length-2}}}A.{{{line_length-2}}}M.{{{line_length-2}}}X"

sum=0
matches_h_r = re.findall(pattern_h_r, contents)
sum += len(matches_h_r)
print (f'matches_h_r: {len(matches_h_r)}')

matches_h_l = re.findall(pattern_h_l, contents)
sum += len(matches_h_l)
print (f'matches_h_l: {len(matches_h_l)}')

matches_v_d = re.findall(pattern_v_d, contents)
sum += len(matches_v_d)
print (f'matches_v_d: {len(matches_v_d)}')

matches_v_u = re.findall(pattern_v_u, contents)
sum += len(matches_v_u)
print (f'matches_v_u: {len(matches_v_u)}')

matches_d_dr = re.findall(pattern_d_dr, contents)
sum += len(matches_d_dr)
print (f'matches_d_dr: {len(matches_d_dr)}')

matches_d_ur = re.findall(pattern_d_ur, contents)
sum += len(matches_d_ur)
print (f'matches_d_ur: {len(matches_d_ur)}')

matches_d_dl = re.findall(pattern_d_dl, contents)
sum += len(matches_d_dl)
print (f'matches_d_dl: {len(matches_d_dl)}')

matches_d_ul = re.findall(pattern_d_ul, contents)
sum += len(matches_d_ul)
print (f'matches_d_ul: {len(matches_d_ul)}')

print (f'sum    : {sum}')
