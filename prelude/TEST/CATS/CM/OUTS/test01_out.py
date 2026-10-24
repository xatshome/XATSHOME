## Thu Aug  6 10:48:55 PM EDT 2026
########################################################################.
########################################################################.
##
## HX-2025-01-02:
## ATS3-XANADU/srcgen2/xats2py/srcgen1
##
########################################################################.
########################################################################.
##
XATSVOID = None
XATSTOP0 = None
##
########################################################################.
##
def XATSINT0(i0): return i0
def XATSINT1(i0): return i0
##
def XATSBTF0(b0): return b0
def XATSBOOL(b0): return b0
##
def XATSCNUL(  ): return (0)
def XATSCHR1(  ): return (0)
##
def XATSCHR0(ch):
  return ord(ch[0]) ## acsii
def XATSCHR2(ch):
  return ord(ch[0]) ## acsii
##
def XATSCHR3(ch):
  x1 = ch[1]
  c1 = ord(x1)
  ## ord('0') = 48
  ## ord('7') = 55
  if c1 < 48:
    ## EG: '\(', '\)'
    return c1 ## acsii
  elif c1 > 55:
    return c1 ## acsii
  else: ## '\ddd': octal
    i1 = 2
    ds = c1 - 48
    while (i1 < len(ch)):
      x1 = ch[i1]
      if (x1 == "'"):
        return ds
      else:
        i1 = i1 + 1
        ds = 8*ds + ord(x1)-48
    return d1 ## ascii code of [ch]
##
def XATSFLT0(f0): return (f0)
def XATSFLT1(f0): return (f0)
##
def XATSSTR0(cs): return (cs)
def XATSSTRN(cs): return (cs)
##
def XATSSFLT(sf): return float(sf)
def XATSDFLT(df): return float(df)
##
########################################################################.

def XATSDAPP(dapp): return dapp
def XATSCAPP(_, capp): return capp
def XATSCAST(_, args): return args[0]

########################################################################.
##
def XATSPFLT(pflt): return pflt
def XATSPROJ(proj): return proj
def XATSP0RJ(p0rj): return p0rj
def XATSP1RJ(_, p1rj): return p1rj
def XATSP1CN(_, p1cn): return p1cn
##
def XATSPCON(pcon, argi): return pcon[argi+1]
##
########################################################################.
##
def XATSTRCD(knd0): return knd0
##
def XATSTUP0(tpl0): return tpl0
def XATSTUP1(knd0, tpl1): return tpl1
def XATSRCD2(knd0, rcd2): return rcd2
##
########################################################################.
##
def XATSROOT(x): return [0, x]
def XATSLPFT(i, x): return [1+0, x, i]
def XATSLPBX(i, x): return [1+1, x, i]
def XATSLPCN(i, x): return [1+2, x, i+1]
##
def XATSVAR0(    ): return XATSROOT([None])
def XATSVAR1(init): return XATSROOT([init])
##
def XATSADDR(addr): return addr ## HX: no-op
def XATSFLAT(addr): return XATS000_lvget(addr)
##
########################################################################.
##
def XATSCTAG(_, t): return t
##
def XATS000_inteq(x, y): return (x == y)
def XATS000_btfeq(x, y): return (x == y)
def XATS000_chreq(x, y): return (x == y)
##
def XATS000_streq(x, y): return (x == y)
##
def XATS000_ctgeq(v, t): return (v[0] == t)
##
########################################################################.
##
def XATS2PY_optn_nil():
  return XATSCAPP("optn_nil", [0])
def XATS2PY_optn_cons(x0):
  return XATSCAPP("optn_cons", [1, x0])
##
def XATS2PY_list_nil():
  return XATSCAPP("list_nil", [0])
def XATS2PY_list_cons(x0, xs):
  return XATSCAPP("list_cons", [1, x0, xs])
##
def XATS2PY_optn_vt_nil():
  return XATSCAPP("optn_vt_nil", [0])
def XATS2PY_optn_vt_cons(x0):
  return XATSCAPP("optn_vt_cons", [1, x0])
##
def XATS2PY_list_vt_nil():
  return XATSCAPP("list_vt_nil", [0])
def XATS2PY_list_vt_cons(x0, xs):
  return XATSCAPP("list_vt_cons", [1, x0, xs])
##
########################################################################.
##
def XATS000_casef():
  raise Exception("XATS000_casef")
##
def XATS000_patck(pck):
  if not(pck):
    raise Exception("XATS000_patck")
  ## end-of(if)
##
########################################################################.
##
def XATS000_fold(pcon): return None
def XATS000_free(pcon): return None
##
########################################################################.
##
def XATS000_dp2tr(p2tr):
  return XATS000_lvget(p2tr)
##
def XATS000_l0azy(lfun):
  return [0, lfun] # unevaled
def XATS000_dl0az(l0az):
  res = None
  if (l0az[0] > 0):
    l0az[0] += 1;
    res = l0az[1]; return res
  else:
    l0az[0] = 0+1;
    res = l0az[1]()
    l0az[1] = res; return res
##
def XATS000_l1azy(lfun): return lfun
def XATS000_dl1az(l1az): return l1az(1)
##
def XATS000_assgn(lval, rval):
  return XATS000_lvset(lval, rval)
##
########################################################################.
##
def XATS000_lvget(lval):
  ctag = lval[0]
  if (ctag == 0):
    return lval[1][0]
  if (ctag == 1+0):
    return XATS000_lvget(lval[1])[lval[2]]
  if (ctag == 1+1):
    return lval[1][lval[2]]
  if (ctag == 1+2):
    return lval[1][lval[2]]
##
def XATS000_lvset(lval, rval):
  ctag = lval[0]
  if (ctag == 0):
    lval[1][0] = rval; return
  if (ctag == 1+0):
    return XATS000_lvset(lval[1], XATS000_ftset(XATS000_lvget(lval[1]), lval[2], rval))
  if (ctag == 1+1):
    lval[1][lval[2]] = rval; return
  if (ctag == 1+2):
    lval[1][lval[2]] = rval; return
##
def XATS000_ftset(tpl0, idx1, rval):
  tpl1 = tpl0.copy(); tpl1[idx1] = rval; return tpl1
##
########################################################################.
class X2PYExcptn(Exception):
    pass
## end of [class X2PYExcptn]
########################################################################.
##
def XATS000_raise(xcon): raise(X2PYExcptn(xcon))
##
########################################################################.
########################################################################.
##
## the end of
## [ATS3-XANADU/srcgen2/xats2py/srcgen1/xshared/runtime/xats2py_py1emit.py]
##
########################################################################.
########################################################################.
## Wed Aug  5 06:17:56 PM EDT 2026
########################################################################
########################################################################
##
## the beg of
## [ATS3-XANADU
## /srcgen2/xats2py/srcgen1/xshared/runtime/srcgen2_prelude.py]
##
########################################################################
########################################################################
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:38:30 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
import sys
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_xtop000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:43:18 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_gbas000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:49:44 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_bool_assert_errmsg(cond, emsg):
  if not(cond):
    raise Exception("XATS2PY_bool_assert_errmsg: emsg = " + emsg)
  return ## HX: void is returned!
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_gdbg000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:50:50 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_sint_neg(i1):
  return ( -i1 ) ## HX: neg
##
########################################################################.
##
def XATS2PY_sint_lt_sint(i1, i2):
  return (i1 < i2) ## HX: lt
def XATS2PY_sint_gt_sint(i1, i2):
  return (i1 > i2) ## HX: gt
##
def XATS2PY_sint_lte_sint(i1, i2):
  return (i1 <= i2) ## HX: lte
def XATS2PY_sint_gte_sint(i1, i2):
  return (i1 >= i2) ## HX: gte
##
def XATS2PY_sint_eq_sint(i1, i2):
  return (i1 == i2) ## HX: equal
def XATS2PY_sint_neq_sint(i1, i2):
  return (i1 != i2) ## HX: noteq
##
########################################################################.
##
def XATS2PY_sint_add_sint(i1, i2):
  return (i1 + i2) ## HX: add
def XATS2PY_sint_sub_sint(i1, i2):
  return (i1 - i2) ## HX: sub
def XATS2PY_sint_mul_sint(i1, i2):
  return (i1 * i2) ## HX: mul
def XATS2PY_sint_mod_sint(i1, i2):
  return (i1 % i2) ## HX: mod
def XATS2PY_sint_div_sint(i1, i2):
  return (i1 // i2) ## HX: int div
##
########################################################################.
##
def XATS2PY_sint_print(i0):
  sys.stdout.write(str(i0)); return None
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_gint000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:48:20 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_bool_lt(b1, b2):
  return (b1 < b2) ## HX: lt
def XATS2PY_bool_gt(b1, b2):
  return (b1 > b2) ## HX: gt
def XATS2PY_bool_eq(b1, b2):
  return (b1 == b2) ## HX: eq
def XATS2PY_bool_lte(b1, b2):
  return (b1 <= b2) ## HX: lte
def XATS2PY_bool_gte(b1, b2):
  return (b1 >= b2) ## HX: gte
def XATS2PY_bool_neq(b1, b2):
  return (b1 != b2) ## HX: neq
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_bool000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:49:26 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_char_lt(c1, c2):
  return (c1 < c2) ## HX: lt
def XATS2PY_char_gt(c1, c2):
  return (c1 > c2) ## HX: gt
def XATS2PY_char_eq(c1, c2):
  return (c1 == c2) ## HX: eq
##
def XATS2PY_char_lte(c1, c2):
  return (c1 <= c2) ## HX: lte
def XATS2PY_char_gte(c1, c2):
  return (c1 >= c2) ## HX: gte
def XATS2PY_char_neq(c1, c2):
  return (c1 != c2) ## HX: noteq
##
########################################################################.
##
def XATS2PY_char_add_sint(c1, i2):
  c2 = c1+i2
  return (c2%256) ## HX: char=int8
##
def XATS2PY_char_sub_char(c1, c2):
  return (c1 - c2) ## HX: char=int8
##
########################################################################.
##
def XATS2PY_char_print(c0):
  XATS2PY_strn_print(chr(c0)); return
##
########################################################################.
########################################################################.
##
## HX-2026-01-17:
## Sat Jan 17 09:51:13 PM EST 2026
##
def \
XATS2PY_char_make_sint(i0): return i0
def \
XATS2PY_sint_make_char(ch): return ch
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_char000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:50:50 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_dflt_neg(df):
  return ( -df ) ## HX:neg
##
########################################################################.
##
def XATS2PY_dflt_abs(df):
  if df >= 0.0:
    return df
  else:
    return (-df) ## HX:abs
##
########################################################################.
##
def XATS2PY_dflt_sqrt(df):
  return math.sqrt(  df  )
##
def XATS2PY_dflt_cbrt(df):
  return math.cbrt(  df  )
##
########################################################################.
##
def XATS2PY_dflt_lt_dflt(f1, f2):
  return (f1 < f2) ## HX: lt
def XATS2PY_dflt_gt_dflt(f1, f2):
  return (f1 > f2) ## HX: gt
def XATS2PY_dflt_eq_dflt(f1, f2):
  return (f1 == f2) ## HX: equal
##
def XATS2PY_dflt_lte_dflt(f1, f2):
  return (f1 <= f2) ## HX: lte
def XATS2PY_dflt_gte_dflt(f1, f2):
  return (f1 >= f2) ## HX: gte
def XATS2PY_dflt_neq_dflt(f1, f2):
  return (f1 != f2) ## HX: noteq
##
########################################################################.
##
def XATS2PY_dflt_add_dflt(f1, f2):
  return (f1 + f2) ## HX: add
def XATS2PY_dflt_sub_dflt(f1, f2):
  return (f1 - f2) ## HX: sub
##
def XATS2PY_dflt_mul_dflt(f1, f2):
  return (f1 * f2) ## HX: mul
##
def XATS2PY_dflt_div_dflt(f1, f2):
  return (f1 / f2) ## HX: div
def XATS2PY_dflt_mod_dflt(f1, f2):
  return (f1 % f2) ## HX: mod
##
########################################################################.
########################################################################.
##
def XATS2PY_dflt_ceil(df):
  return math.ceil(df) ## (1.2) = 2
def XATS2PY_dflt_floor(df):
  return math.floor(df) ## (1.2) = 1
def XATS2PY_dflt_round(df):
  ## HX: (1.2) = 1 ## (1.5) = 2
  return math.round(df) ## (-1.5) = 1
def XATS2PY_dflt_trunc(df):
  ## HX: (1.2) = 1 ## (1.9) = 1
  return math.trunc(df) ## (-1.2) = -1
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_gflt000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:46:58 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_strn_cmp(x1, x2):
  df = 0
  i0 = 0
  n1 = len(x1)
  n2 = len(x2)
  n0 = n1 if (n1 <= n2) else n2
  while (i0 < n0):
    df = ord(x1[i0]) - ord(x2[i0])
    if (df != 0):
      return df
    else:
      i0 = i0 + 1
  return (n1 - n2)
##
########################################################################.
##
def XATS2PY_strn_length(cs):
  return len(cs) # PY special [len]
def XATS000_strn_length(cs):
  return len(cs) # PY special [len]
##
########################################################################.
##
def XATS2PY_strn_print(cs):
  sys.stdout.write(cs); return None
def XATS000_strn_print(cs):
  sys.stdout.write(cs); return None
##
########################################################################.
##
def XATS2PY_strn_get_at_raw(cs, i0):
  return ord(cs[i0]) # PY is charless
def XATS000_strn_get_at_raw(cs, i0):
  return XATS2PY_strn_get_at_raw(cs, i0)
##
########################################################################.
##
def XATS2PY_strn_make_fwork(fwork):
  res = []
  fwork(lambda ch: res.append(chr(ch)))
  return "".join(res)
def XATS000_strn_make_fwork(fwork):
  return XATS2PY_strn_make_fwork(fwork)
##
########################################################################.
##
def \
XATS2PY_strn_make_env_fwork(env, fwork):
  res = []
  fwork(env, lambda ch: res.append(chr(ch)))
  return "".join(res)
def \
XATS2PY_strn_make1_env_fwork(env, fwork):
  res = []
  fwork(env, lambda ch: res.append(chr(ch)))
  return "".join(res)
##
def XATS000_strn_make_env_fwork(env, fwork):
  return XATS2PY_strn_make_env_fwork(env, fwork)
def XATS000_strn_make1_env_fwork(env, fwork):
  return XATS2PY_strn_make1_env_fwork(env, fwork)
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_strn000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Sat Jan  3 05:24:14 PM EST 2026
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def \
XATS2PY_list_vt_foritm0_f1un \
  (xs, work):
  while (True):
    if XATS2PY_list_vt_nilq1(xs):
      break
    else:
      x1 = XATS2PY_list_vt_head_raw1(xs)
      work(x1)
      xs = XATS2PY_list_vt_tail_raw0(xs)
    ## end-of-(if(XATS2PY_list_vt_nilq1(xs)))
  return None ## XATS2PY_list_vt_foritm0_f1un(...)
##
########################################################################.
##
def \
XATS2PY_list_vt_forall0_f1un \
  (xs, test, free):
  while (True):
    if (XATS2PY_list_vt_nilq1(xs)):
      break
    else:
      x1 = XATS2PY_list_vt_head_raw1(xs)
      if (test(x1)):
        xs = XATS2PY_list_vt_tail_raw0(xs)
      else:
        xs = XATS2PY_list_vt_tail_raw0(xs)
        XATS2PY_list_vt_foritm0_f1un(xs, free)
        return False
    ## end-of-(if(XATS2PY_list_vt_nilq1(xs)))
  return True ## XATS2PY_list_vt_forall0_f1un(...)
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_list000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Sat Jan  3 05:24:14 PM EST 2026
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
## HX: It is yet to be populated!
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_optn000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Sat Jan  3 04:47:20 PM EST 2026
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def \
XATS2PY_strm_vt_forall0_f1un \
  (fxs, test):
  while (True):
    cxs = XATS2PY_lazy_vt_eval(fxs)
    if XATS2PY_strmcon_vt_nilq1(cxs):
      break
    else:
      x01 = XATS2PY_strmcon_vt_head_raw1(cxs)
      if (test(x01)):
        fxs = XATS2PY_strmcon_vt_tail_raw0(cxs)
      else:
        fxs = XATS2PY_strmcon_vt_tail_raw0(cxs)
        XATS2PY_lazy_vt_free(fxs)
        return False
      ## end-of-(if(test(x01))
    ## end-of-(if(XATS2PY_strmcon_vt_nilq1(cxs)))
  return True ## XATS2PY_strm_vt_forall0_f1un(...)
##
########################################################################.
##
def \
XATS2PY_strm_vt_filter0_f1un \
  (fxs, test, free):
  return XATS2PY_lazy_vt_make_f0un(
    lambda: XATS2PY_strmcon_vt_filter0_f1un(XATS2PY_lazy_vt_eval(fxs), test, free)
  )
##
def \
XATS2PY_strmcon_vt_filter0_f1un \
  (cxs, test, free):
  while (True):
    if XATS2PY_strmcon_vt_nilq1(cxs):
      return XATS2PY_strmcon_vt_nil()
    else:
      x01 = XATS2PY_strmcon_vt_head_raw1(cxs)
      fxs = XATS2PY_strmcon_vt_tail_raw0(cxs)
      if (test(x01)):
        return XATS2PY_strmcon_vt_cons(x01, XATS2PY_strm_vt_filter0_f1un(fxs, test, free))
      else:
        free(x01)
        cxs = XATS2PY_lazy_vt_eval(fxs)
        continue
      ## end-of-(if(test(x01))
    ## end-of-(if(XATS2PY_strmcon_vt_nilq1(cxs))
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_strm000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan 14 02:42:28 PM EST 2026
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def \
XATS2PY_strx_vt_forall0_f1un \
  (fxs, test):
  while (True):
    cxs = XATS2PY_lazy_vt_eval(fxs)
    x01 = XATS2PY_strxcon_vt_head_raw1(cxs)
    if (test(x01)):
      fxs = XATS2PY_strxcon_vt_tail_raw0(cxs)
    else:
      fxs = XATS2PY_strxcon_vt_tail_raw0(cxs)
      XATS2PY_lazy_vt_free(fxs)
      return False
    ## end-of-(if(test(x01)))
  return true ## XATS2PY_strx_vt_forall0_f1un(...)
##
########################################################################.
##
def \
XATS2PY_strx_vt_filter0_f1un \
  (fxs, test, free):
  return XATS2PY_lazy_vt_make_f0un(
    lambda: XATS2PY_strxcon_vt_filter0_f1un(XATS2PY_lazy_vt_eval(fxs), test, free)
  )
##
def \
XATS2PY_strxcon_vt_filter0_f1un \
  (cxs, test, free):
  while (True):
    x01 = XATS2PY_strxcon_vt_head_raw1(cxs)
    fxs = XATS2PY_strxcon_vt_tail_raw0(cxs)
    if (test(x01)):
      return XATS2PY_strxcon_vt_cons(x01, XATS2PY_strx_vt_filter0_f1un(fxs, test, free))
    else:
      free(x01)
      cxs = XATS2PY_lazy_vt_eval(fxs)
      continue
    ## end-of-(if(test(x01))
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_strx000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:46:14 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_a0rf_lget(A):
  return A[0]
def XATS2PY_a0rf_lset(A, x1):
  A[0] = x1; return
##
def XATS2PY_a0rf_make_1val(x0):
  return [x0] ## HX: singleton
##
########################################################################.
########################################################################.
##
def XATS2PY_a1rf_lget_at(A, i0):
  return A[i0]
def XATS2PY_a1rf_lset_at(A, i0, x1):
  A[i0] = x1; return
##
def XATS2PY_a1rf_make_ncpy(n0, x0):
  i0 = 0
  A0 = []
  while (i0 < n0):
    A0.append(x0); i0 = i0 + 1
  return A0 ## HX: A0 = [x0, x0, ..., x0]
##
def XATS2PY_a1rf_make_nfun(n0, fopr):
  i0 = 0
  A0 = []
  while (i0 < n0):
    A0.append(fopr(i0)); i0 = i0 + 1
  return A0 ## HX: A0 = [fopr(0),...,fopr(n)]
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_axrf000.cats]
########################################################################.
########################################################################.
########################################################################.
##                                                                    ##.
##                         Applied Type System                        ##.
##                                                                    ##.
########################################################################.

##
## ATS/Xanadu - Unleashing the Potential of Types!
## Copyright (C) 2025 Hongwei Xi, ATS Trustful Software, Inc.
## All rights reserved
##
## ATS is free software;  you can  redistribute it and/or modify it under
## the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
## Free Software Foundation; either version 3, or (at  your  option)  any
## later version.
## 
## ATS is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
## for more details.
## 
## You  should  have  received  a  copy of the GNU General Public License
## along  with  ATS;  see the  file COPYING.  If not, please write to the
## Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##

########################################################################.
########################################################################.
##
## Author: Hongwei Xi
## Wed Jan  8 02:46:14 AM EST 2025
## Authoremail: gmhwxiATgmailDOTcom
##
########################################################################.
########################################################################.
##
def XATS2PY_a1sz_length(A0):
  return len(A0)
##
########################################################################.
##
def XATS2PY_a1sz_lget_at(A0, i0):
  return A0[i0]
def XATS2PY_a1sz_lset_at(A0, i0, x1):
  A0[i0] = x1; return
##
########################################################################.
##
def XATS2PY_a1sz_make_ncpy(n0, x0):
  i0 = 0
  A0 = []
  while (i0 < n0):
    A0.append(x0); i0 = i0 + 1
  return A0 ## HX: A0 = [x0, ..., x0]
##
def XATS2PY_a1sz_make_nfun(n0, fopr):
  i0 = 0
  A0 = []
  while (i0 < n0):
    A0.append(fopr(i0)); i0 = i0 + 1
  return A0 ## HX: A0 = [fopr(0),...,fopr(n-1)]
##
########################################################################.
##
def XATS2PY_a1sz_make_fwork(fwork):
  A0 = []
  fwork(lambda x0: A0.append(x0)); return A0
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_axsz000.cats]
########################################################################.
########################################################################.
## LCSRCsome1(test01_a0rf000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## I1Dinclude(LCSRCsome1(test01_a0rf000.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(352(line=24,offs=1)--399(line=26,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(446(line=31,offs=1)--493(line=33,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(494(line=34,offs=1)--541(line=36,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(542(line=37,offs=1)--589(line=39,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(616(line=43,offs=1)--669(line=45,offs=34))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gbas000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(670(line=46,offs=1)--723(line=48,offs=34))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gbas001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(895(line=59,offs=1)--935(line=59,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gxyz000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gxyz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(982(line=64,offs=1)--1022(line=64,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/unsfx00.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1166(line=73,offs=1)--1206(line=73,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gnum000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gnum000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1207(line=74,offs=1)--1247(line=74,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gord000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gord000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1248(line=75,offs=1)--1288(line=75,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gfun000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1292(line=77,offs=1)--1332(line=77,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1333(line=78,offs=1)--1373(line=78,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1374(line=79,offs=1)--1414(line=79,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1418(line=81,offs=1)--1458(line=81,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1459(line=82,offs=1)--1499(line=82,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1500(line=83,offs=1)--1540(line=83,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1544(line=85,offs=1)--1584(line=85,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gmap000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gmap000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1585(line=86,offs=1)--1625(line=86,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gmap001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gmap001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1629(line=88,offs=1)--1669(line=88,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gcls000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1670(line=89,offs=1)--1710(line=89,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gsyn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1711(line=90,offs=1)--1751(line=90,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gsyn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1778(line=94,offs=1)--1818(line=94,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/bool000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/bool000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1819(line=95,offs=1)--1859(line=95,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/char000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1860(line=96,offs=1)--1900(line=96,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gint000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1901(line=97,offs=1)--1941(line=97,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gint001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1942(line=98,offs=1)--1982(line=98,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gflt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gflt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2009(line=102,offs=1)--2049(line=102,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2050(line=103,offs=1)--2090(line=103,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2117(line=107,offs=1)--2157(line=107,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axrf000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2158(line=108,offs=1)--2198(line=108,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axrf001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2199(line=109,offs=1)--2239(line=109,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axsz000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2240(line=110,offs=1)--2280(line=110,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axsz001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2281(line=111,offs=1)--2321(line=111,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/asrt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/asrt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2322(line=112,offs=1)--2362(line=112,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2363(line=113,offs=1)--2403(line=113,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2404(line=114,offs=1)--2444(line=114,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2445(line=115,offs=1)--2485(line=115,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2486(line=116,offs=1)--2526(line=116,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2527(line=117,offs=1)--2567(line=117,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2568(line=118,offs=1)--2608(line=118,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/lsrt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/lsrt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2609(line=119,offs=1)--2649(line=119,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/optn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2650(line=120,offs=1)--2690(line=120,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/optn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2691(line=121,offs=1)--2731(line=121,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strm000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strm000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2732(line=122,offs=1)--2772(line=122,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strm001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strm001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2773(line=123,offs=1)--2813(line=123,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strx000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strx000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2814(line=124,offs=1)--2854(line=124,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strx001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strx001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2901(line=129,offs=1)--2946(line=129,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gbas000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gbas000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2950(line=131,offs=1)--2995(line=131,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/bool000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/bool000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2996(line=132,offs=1)--3041(line=132,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/char000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/char000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3045(line=134,offs=1)--3090(line=134,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gint000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gint000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3091(line=135,offs=1)--3136(line=135,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gflt000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gflt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3140(line=137,offs=1)--3185(line=137,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/strn000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3189(line=139,offs=1)--3234(line=139,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/axrf000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/axrf000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3235(line=140,offs=1)--3280(line=140,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/axsz000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/axsz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3386(line=148,offs=1)--3432(line=148,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gnum000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3433(line=149,offs=1)--3479(line=149,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gord000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gord000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3480(line=150,offs=1)--3526(line=150,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gfun000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gfun000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3527(line=151,offs=1)--3573(line=151,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gcls000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gcls000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3574(line=152,offs=1)--3620(line=152,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3621(line=153,offs=1)--3667(line=153,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3668(line=154,offs=1)--3714(line=154,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq002_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq002_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3715(line=155,offs=1)--3761(line=155,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gasq000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gasq000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3762(line=156,offs=1)--3808(line=156,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gasq001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gasq001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3809(line=157,offs=1)--3855(line=157,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gsyn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3882(line=161,offs=1)--3928(line=161,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strn000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3955(line=165,offs=1)--4001(line=165,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/axrf000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/axrf000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4002(line=166,offs=1)--4048(line=166,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/axsz000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/axsz000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4049(line=167,offs=1)--4095(line=167,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/tupl000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/tupl000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4099(line=169,offs=1)--4145(line=169,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/list000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4146(line=170,offs=1)--4192(line=170,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/list001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4193(line=171,offs=1)--4239(line=171,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/lsrt000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/lsrt000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4240(line=172,offs=1)--4286(line=172,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/optn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/optn000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4287(line=173,offs=1)--4333(line=173,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/optn001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/optn001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4337(line=175,offs=1)--4383(line=175,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4384(line=176,offs=1)--4430(line=176,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4431(line=177,offs=1)--4477(line=177,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm002_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4478(line=178,offs=1)--4524(line=178,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strx000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strx000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4525(line=179,offs=1)--4571(line=179,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strx001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strx001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4742(line=190,offs=1)--4788(line=190,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gxyz000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(5117(line=198,offs=1)--5117(line=198,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(5117(line=198,offs=1)--5117(line=198,offs=1));D3Cnone0()))
## I1Dinclude(LCSRCsome1(test01_a0rf000.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(197(line=15,offs=1)--249(line=16,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/xtop000.dats";35));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/xtop000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(296(line=21,offs=1)--344(line=22,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/gbas000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gbas000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(345(line=23,offs=1)--393(line=24,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/gdbg000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gdbg000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(440(line=29,offs=1)--488(line=30,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/bool000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/bool000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(489(line=31,offs=1)--537(line=32,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/char000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(538(line=33,offs=1)--586(line=34,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/gint000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(587(line=35,offs=1)--635(line=36,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/gflt000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gflt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(682(line=41,offs=1)--730(line=42,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/strn000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(777(line=47,offs=1)--825(line=48,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/list000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(826(line=49,offs=1)--874(line=50,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/optn000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/optn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(901(line=54,offs=1)--949(line=55,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/strm000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strm000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(950(line=56,offs=1)--998(line=57,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/strx000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strx000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1045(line=62,offs=1)--1093(line=63,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/axrf000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1094(line=64,offs=1)--1142(line=65,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/axsz000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axsz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1398(line=73,offs=1)--1398(line=73,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1398(line=73,offs=1)--1398(line=73,offs=1));D3Cnone0()))
## LCSRCsome1(test01_a0rf000.dats)@(323(line=21,offs=1)--363(line=22,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csymload(T_SRP_SYMLOAD();ref;D2PTMsome(1000;D2ITMcst($list(a0rf_make_1val(1096))))))))
## I1Dvaldclist(LCSRCsome1(test01_a0rf000.dats)@(390(line=26,offs=1)--405(line=26,offs=16)))
## I1VALDCL
pyxtnm7 = None
## LCSRCsome1(test01_a0rf000.dats)@(399(line=26,offs=10)--402(line=26,offs=13))
## I0Etapq(I0Ecst(a0rf_make_1val(1096)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(2556(line=112,offs=1)--2570(line=112,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(a0rf_make_1val(1096), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2101(line=96,offs=1)--2262(line=108,offs=2)))
## T1IMPallx(a0rf_make_1val(1096)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8856],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_make_1val(1096);$list(@(a[2960],T2Pvar(a[8856])))))))
def pyxtnm5(arg1): ## timp: a0rf_make_1val(1096)
  pyxtnm1 = arg1
  ## I1CMP:start
  ## let
  pyxtnm4 = None
  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2189(line=104,offs=1)--2260(line=107,offs=37)))
  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a0rf_make_1val(2667));$list(I1FUNDCL(XATS2PY_a0rf_make_1val(5074);$list(FJARGdarg($list(I1BNDcons(I1TNM(2);I0Pvar(x1(5075));$list(@(x1(5075),I1Vtnm(I1TNM(2))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a0rf_make_1val);G1Nlist($list())))))))
  pyxtnm3 = XATSDAPP(XATS2PY_a0rf_make_1val(pyxtnm1))
  pyxtnm4 = pyxtnm3
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(4))
  return pyxtnm4
## endtimp(a0rf_make_1val(1096))
pyxtnm6 = XATSDAPP(pyxtnm5(XATSINT1(0)))
pyxtnm7 = pyxtnm6
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_a0rf000.dats)@(406(line=27,offs=1)--456(line=28,offs=42)))
## I1VALDCL
pyxtnm246 = None
## LCSRCsome1(test01_a0rf000.dats)@(415(line=28,offs=1)--421(line=28,offs=7))
## I0Etapq(I0Ecst(gs_print_a5(810)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(12006(line=769,offs=1)--12017(line=769,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a5(810), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21886(line=1350,offs=1)--22194(line=1368,offs=4)))
## T1IMPallx(gs_print_a5(810)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7027],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7028],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x2[7029],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7030],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x4[7031],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a5(810);$list(@(x0[2496],T2Pvar(x0[7027])),@(x1[2497],T2Pvar(x1[7028])),@(x2[2498],T2Pvar(x2[7029])),@(x3[2499],T2Pvar(x3[7030])),@(x4[2500],T2Pvar(x4[7031])))))))
def pyxtnm239(arg1, arg2, arg3, arg4, arg5): ## timp: gs_print_a5(810)
  pyxtnm8 = arg1
  pyxtnm9 = arg2
  pyxtnm10 = arg3
  pyxtnm11 = arg4
  pyxtnm12 = arg5
  ## I1CMP:start
  ## let
  pyxtnm238 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21986(line=1360,offs=1)--22009(line=1361,offs=15)))
  ## I1VALDCL
  pyxtnm16 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21995(line=1361,offs=1)--22007(line=1361,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm14(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm13 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(13))
    return pyxtnm13
  ## endtimp(gs_print$beg(802))
  pyxtnm15 = XATSDAPP(pyxtnm14())
  pyxtnm16 = pyxtnm15
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22022(line=1363,offs=3)--22029(line=1363,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7027])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm22 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm21(arg1): ## timp: strn_print(1040)
    pyxtnm17 = arg1
    ## I1CMP:start
    ## let
    pyxtnm20 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(18);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(18))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm19 = XATSDAPP(XATS2PY_strn_print(pyxtnm17))
    pyxtnm20 = pyxtnm19
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(20))
    return pyxtnm20
  ## endtimp(strn_print(1040))
  pyxtnm22 = pyxtnm21
  pyxtnm23 = XATSDAPP(pyxtnm22(pyxtnm8))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22039(line=1363,offs=20)--22051(line=1363,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm25(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm24 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(24))
    return pyxtnm24
  ## endtimp(gs_print$sep(803))
  pyxtnm26 = XATSDAPP(pyxtnm25())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22056(line=1364,offs=3)--22063(line=1364,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7028])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
  def pyxtnm64(arg1): ## timp: g_print(39)
    pyxtnm27 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
    ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
    ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1512(line=44,offs=1)--1614(line=51,offs=32)))
    ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(vt[7259],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(a0rf);$list(T2Pvar(vt[7259])))))))))
    def pyxtnm48(): ## timp: g_ptype(202)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1567(line=50,offs=1)--1572(line=50,offs=6))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm32(arg1): ## timp: strn_print(1040)
        pyxtnm28 = arg1
        ## I1CMP:start
        ## let
        pyxtnm31 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(29);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(29))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm30 = XATSDAPP(XATS2PY_strn_print(pyxtnm28))
        pyxtnm31 = pyxtnm30
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(31))
        return pyxtnm31
      ## endtimp(strn_print(1040))
      pyxtnm33 = XATSDAPP(pyxtnm32(XATSSTRN("a0rf(")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1583(line=51,offs=1)--1590(line=51,offs=8))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vt[7259])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
      def pyxtnm40(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm38(arg1): ## timp: strn_print(1040)
          pyxtnm34 = arg1
          ## I1CMP:start
          ## let
          pyxtnm37 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(35);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(35))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm36 = XATSDAPP(XATS2PY_strn_print(pyxtnm34))
          pyxtnm37 = pyxtnm36
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(37))
          return pyxtnm37
        ## endtimp(strn_print(1040))
        pyxtnm39 = XATSDAPP(pyxtnm38(XATSSTRN("sint")))
        ## I1CMP:return:I1Vtnm(I1TNM(39))
        return pyxtnm39
      ## endtimp(g_ptype(202))
      pyxtnm41 = XATSDAPP(pyxtnm40())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1603(line=51,offs=21)--1608(line=51,offs=26))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm46(arg1): ## timp: strn_print(1040)
        pyxtnm42 = arg1
        ## I1CMP:start
        ## let
        pyxtnm45 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(43);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(43))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm44 = XATSDAPP(XATS2PY_strn_print(pyxtnm42))
        pyxtnm45 = pyxtnm44
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(45))
        return pyxtnm45
      ## endtimp(strn_print(1040))
      pyxtnm47 = XATSDAPP(pyxtnm46(XATSSTRN(")")))
      ## I1CMP:return:I1Vtnm(I1TNM(47))
      return pyxtnm47
    ## endtimp(g_ptype(202))
    pyxtnm49 = XATSDAPP(pyxtnm48())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm54(arg1): ## timp: strn_print(1040)
      pyxtnm50 = arg1
      ## I1CMP:start
      ## let
      pyxtnm53 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(51);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(51))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm52 = XATSDAPP(XATS2PY_strn_print(pyxtnm50))
      pyxtnm53 = pyxtnm52
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(53))
      return pyxtnm53
    ## endtimp(strn_print(1040))
    pyxtnm55 = XATSDAPP(pyxtnm54(XATSSTRN(":")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
    ## I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
    ## T1IMPallx(g_psort(201), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1831(line=74,offs=1)--1885(line=78,offs=22)))
    ## T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(tx[5755],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(tx[5755])))))))
    def pyxtnm62(): ## timp: g_psort(201)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1866(line=78,offs=3)--1876(line=78,offs=13))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm60(arg1): ## timp: strn_print(1040)
        pyxtnm56 = arg1
        ## I1CMP:start
        ## let
        pyxtnm59 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(57);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(57))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm58 = XATSDAPP(XATS2PY_strn_print(pyxtnm56))
        pyxtnm59 = pyxtnm58
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(59))
        return pyxtnm59
      ## endtimp(strn_print(1040))
      pyxtnm61 = XATSDAPP(pyxtnm60(XATSSTRN("tbox")))
      ## I1CMP:return:I1Vtnm(I1TNM(61))
      return pyxtnm61
    ## endtimp(g_psort(201))
    pyxtnm63 = XATSDAPP(pyxtnm62())
    ## I1CMP:return:I1Vtnm(I1TNM(63))
    return pyxtnm63
  ## endtimp(g_print(39))
  pyxtnm65 = XATSDAPP(pyxtnm64(pyxtnm9))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22073(line=1364,offs=20)--22085(line=1364,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm67(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm66 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(66))
    return pyxtnm66
  ## endtimp(gs_print$sep(803))
  pyxtnm68 = XATSDAPP(pyxtnm67())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22090(line=1365,offs=3)--22097(line=1365,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7029])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm74 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm73(arg1): ## timp: strn_print(1040)
    pyxtnm69 = arg1
    ## I1CMP:start
    ## let
    pyxtnm72 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(70);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(70))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm71 = XATSDAPP(XATS2PY_strn_print(pyxtnm69))
    pyxtnm72 = pyxtnm71
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(72))
    return pyxtnm72
  ## endtimp(strn_print(1040))
  pyxtnm74 = pyxtnm73
  pyxtnm75 = XATSDAPP(pyxtnm74(pyxtnm10))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22107(line=1365,offs=20)--22119(line=1365,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm77(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm76 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(76))
    return pyxtnm76
  ## endtimp(gs_print$sep(803))
  pyxtnm78 = XATSDAPP(pyxtnm77())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22124(line=1366,offs=3)--22131(line=1366,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7030])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1873(line=74,offs=1)--2106(line=92,offs=4)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a0rf);$list(T2Pvar(x0[7262])))))))))
  def pyxtnm223(arg1): ## timp: g_print(39)
    pyxtnm79 = arg1
    ## I1CMP:start
    ## let
    pyxtnm222 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1931(line=81,offs=1)--1953(line=81,offs=23))
    ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(a0rf);$list(S2Evar(x0[7262])))))))
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1957(line=83,offs=1)--1990(line=84,offs=25)))
    ## I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7262]))))):timp
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1991(line=85,offs=1)--2024(line=86,offs=25)))
    ## I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7262]))))):timp
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2025(line=87,offs=1)--2062(line=88,offs=29)))
    ## I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7262]))))):timp
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2075(line=91,offs=3)--2086(line=91,offs=14))
    ## I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Pvar(x0[7262]))))),T2JAG($list(T2Pvar(x0[7262])))))
    ## T1IMPallx(gseq_print1(1687), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
    ## T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
    def pyxtnm220(arg1): ## timp: gseq_print1(1687)
      pyxtnm80 = arg1
      ## I1CMP:start
      ## let
      pyxtnm219 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
      ## I1VALDCL
      pyxtnm89 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm85(arg1): ## timp: strn_print(1040)
        pyxtnm81 = arg1
        ## I1CMP:start
        ## let
        pyxtnm84 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(82);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(82))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm83 = XATSDAPP(XATS2PY_strn_print(pyxtnm81))
        pyxtnm84 = pyxtnm83
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(84))
        return pyxtnm84
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2025(line=87,offs=1)--2062(line=88,offs=29)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a0rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
      def pyxtnm86(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("a0rf(")
      ## endtimp(gseq$beg(346))
      pyxtnm87 = XATSDAPP(pyxtnm86())
      pyxtnm88 = XATSDAPP(pyxtnm85(pyxtnm87))
      pyxtnm89 = pyxtnm88
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
      ## I1VALDCL
      pyxtnm209 = None
      ## let
      pyxtnm208 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq_iforitm1(1760), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
      def pyxtnm206(arg1): ## timp: gseq_iforitm1(1760)
        pyxtnm99 = arg1
        ## I1CMP:start
        ## let
        pyxtnm205 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
        ## let
        pyxtnm204 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
        ## I1VALDCL
        pyxtnm203 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
        ## T1IMPallx(gseq_iforall1(1736), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
        ## T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
        def pyxtnm201(arg1): ## timp: gseq_iforall1(1736)
          pyxtnm105 = arg1
          ## I1CMP:start
          ## let
          pyxtnm200 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm106 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
          ## I1VALDCL
          pyxtnm107 = None
          pyxtnm107 = XATSADDR(pyxtnm106)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
          ## I1VALDCL
          pyxtnm199 = None
          ## let
          pyxtnm198 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
          ## T1IMPallx(gseq_forall1(1720), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
          ## T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
          def pyxtnm196(arg1): ## timp: gseq_forall1(1720)
            pyxtnm116 = arg1
            ## I1CMP:start
            ## let
            pyxtnm195 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
            ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
            ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1473(line=43,offs=1)--1596(line=52,offs=27)))
            ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7278],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7278],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a0rf);$list(T2Pvar(x0[7278])))),@(x0[1168],T2Pvar(x0[7278])))))))
            def pyxtnm193(arg1): ## timp: gseq_forall(386)
              pyxtnm117 = arg1
              ## I1CMP:start
              ## let
              pyxtnm192 = None
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1538(line=49,offs=1)--1564(line=50,offs=18)))
              ## I1VALDCL
              pyxtnm131 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1547(line=50,offs=1)--1555(line=50,offs=9))
              ## I0Etapq(I0Ecst(a0rf_get(1097)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(2845(line=132,offs=1)--2853(line=132,offs=9))));$list(T2JAG($list(T2Pvar(x0[7278])))))
              ## T1IMPallx(a0rf_get(1097), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2613(line=128,offs=1)--2718(line=137,offs=28)))
              ## T1IMPallx(a0rf_get(1097)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7265],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_get(1097);$list(@(a[2961],T2Pvar(x0[7265])))))))
              def pyxtnm129(arg1): ## timp: a0rf_get(1097)
                pyxtnm118 = arg1
                ## I1CMP:start
                ## let
                pyxtnm128 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2650(line=132,offs=1)--2681(line=135,offs=17)))
                ## I1VALDCL
                pyxtnm125 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2665(line=135,offs=1)--2674(line=135,offs=10))
                ## I0Etapq(I0Ecst(a0rf_lget(1101)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3279(line=158,offs=1)--3288(line=158,offs=10))));$list(T2JAG($list(T2Pvar(x0[7265])))))
                ## T1IMPallx(a0rf_lget(1101), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1725(line=60,offs=1)--1882(line=75,offs=2)))
                ## T1IMPallx(a0rf_lget(1101)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8852],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_lget(1101);$list(@(a[2965],T2Pvar(a[8852])))))))
                def pyxtnm123(arg1): ## timp: a0rf_lget(1101)
                  pyxtnm119 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm122 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1801(line=68,offs=1)--1880(line=74,offs=28)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a0rf_lget(2665));$list(I1FUNDCL(XATS2PY_a0rf_lget(5064);$list(FJARGdarg($list(I1BNDcons(I1TNM(120);I0Pvar(A(5065));$list(@(A(5065),I1Vtnm(I1TNM(120))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a0rf_lget);G1Nlist($list())))))))
                  pyxtnm121 = XATSDAPP(XATS2PY_a0rf_lget(pyxtnm119))
                  pyxtnm122 = pyxtnm121
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(122))
                  return pyxtnm122
                ## endtimp(a0rf_lget(1101))
                pyxtnm124 = XATSDAPP(pyxtnm123(pyxtnm118))
                pyxtnm125 = pyxtnm124
                XATS000_patck(True)
                ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2682(line=136,offs=1)--2708(line=137,offs=18)))
                ## I1VALDCL
                ## I1BNDcons(I1TNM(127);I0Ptup0($list());$list())
                ## I1CMP:start
                ## I1LETnew1(I1TNM(126);I1INSdapp(I1Vcst(owed_t0_elim0(5));$list(I1Vnone0())))
                ## I1CMP(ival):I1Vtnm(I1TNM(126))## I1CMP:return
                pyxtnm128 = pyxtnm125
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(128))
                return pyxtnm128
              ## endtimp(a0rf_get(1097))
              pyxtnm130 = XATSDAPP(pyxtnm129(pyxtnm117))
              pyxtnm131 = pyxtnm130
              XATS000_patck(True)
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1572(line=52,offs=3)--1583(line=52,offs=14))
              ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7278])))))
              ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
              ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              pyxtnm190 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
              ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
              ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
              ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              def pyxtnm189(arg1): ## timp: forall$test1(1423)
                pyxtnm132 = arg1
                ## I1CMP:start
                ## let
                pyxtnm188 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                ## I1VALDCL
                pyxtnm137 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                def pyxtnm135(arg1): ## timp: p2tr_get(2309)
                  pyxtnm133 = arg1
                  ## I1CMP:start
                  pyxtnm134 = XATS000_dp2tr(pyxtnm133)
                  ## I1CMP:return:I1Vtnm(I1TNM(134))
                  return pyxtnm134
                ## endtimp(p2tr_get(2309))
                pyxtnm136 = XATSDAPP(pyxtnm135(pyxtnm107))
                pyxtnm137 = pyxtnm136
                XATS000_patck(True)
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                ## I1VALDCL
                pyxtnm175 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                ## I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                ## T1IMPallx(iforall$test1(1433), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                ## T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                def pyxtnm173(arg1, arg2): ## timp: iforall$test1(1433)
                  pyxtnm138 = arg1
                  pyxtnm139 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm172 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                  ## I1VALDCL
                  pyxtnm171 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                  ## I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                  ## T1IMPallx(iforitm$work1(1449), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                  ## T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm169(arg1, arg2): ## timp: iforitm$work1(1449)
                    pyxtnm140 = arg1
                    pyxtnm141 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm168 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                    ## I1VALDCL
                    pyxtnm159 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                    ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                    ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                    def pyxtnm148(arg1, arg2): ## timp: sint_gt$sint(928)
                      pyxtnm142 = arg1
                      pyxtnm143 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm147 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(144);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(144))))),I1BNDcons(I1TNM(145);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(145))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                      pyxtnm146 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm142, pyxtnm143))
                      pyxtnm147 = pyxtnm146
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(147))
                      return pyxtnm147
                    ## endtimp(sint_gt$sint(928))
                    pyxtnm149 = XATSDAPP(pyxtnm148(pyxtnm140, XATSINT1(0)))
                    pyxtnm158 = None
                    if (pyxtnm149):
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                      def pyxtnm154(arg1): ## timp: strn_print(1040)
                        pyxtnm150 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm153 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(151);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(151))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                        pyxtnm152 = XATSDAPP(XATS2PY_strn_print(pyxtnm150))
                        pyxtnm153 = pyxtnm152
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(153))
                        return pyxtnm153
                      ## endtimp(strn_print(1040))
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                      ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                      ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1957(line=83,offs=1)--1990(line=84,offs=25)))
                      ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a0rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm155(): ## timp: gseq$sep(348)
                        ## I1CMP:start
                        ## I1CMP:return:I1Vstr(...)
                        return XATSSTRN(",")
                      ## endtimp(gseq$sep(348))
                      pyxtnm156 = XATSDAPP(pyxtnm155())
                      pyxtnm157 = XATSDAPP(pyxtnm154(pyxtnm156))
                      pyxtnm158 = pyxtnm157
                    ## else: None
                    ## end-of(if)
                    pyxtnm159 = pyxtnm158
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                    ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                    ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                    ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                    pyxtnm166 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                    pyxtnm165 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                    ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                    ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                    def pyxtnm164(arg1): ## timp: sint_print(922)
                      pyxtnm160 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm163 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(161);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(161))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                      pyxtnm162 = XATSDAPP(XATS2PY_sint_print(pyxtnm160))
                      pyxtnm163 = pyxtnm162
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(163))
                      return pyxtnm163
                    ## endtimp(sint_print(922))
                    pyxtnm165 = pyxtnm164
                    pyxtnm166 = pyxtnm165
                    pyxtnm167 = XATSDAPP(pyxtnm166(pyxtnm141))
                    pyxtnm168 = pyxtnm167
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(168))
                    return pyxtnm168
                  ## endtimp(iforitm$work1(1449))
                  pyxtnm170 = XATSDAPP(pyxtnm169(pyxtnm138, pyxtnm139))
                  pyxtnm171 = pyxtnm170
                  XATS000_patck(True)
                  pyxtnm172 = XATSBOOL(True)
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(172))
                  return pyxtnm172
                ## endtimp(iforall$test1(1433))
                pyxtnm174 = XATSDAPP(pyxtnm173(pyxtnm137, pyxtnm132))
                pyxtnm175 = pyxtnm174
                XATS000_patck(True)
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                def pyxtnm178(arg1, arg2): ## timp: p2tr_set(2310)
                  pyxtnm176 = arg1
                  pyxtnm177 = arg2
                  ## I1CMP:start
                  XATS000_assgn(pyxtnm176, pyxtnm177)
                  ## I1CMP:return:I1V000()
                  return XATSVOID
                ## endtimp(p2tr_set(2310))
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                def pyxtnm185(arg1, arg2): ## timp: sint_add$sint(936)
                  pyxtnm179 = arg1
                  pyxtnm180 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm184 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(181);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(181))))),I1BNDcons(I1TNM(182);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(182))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                  pyxtnm183 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm179, pyxtnm180))
                  pyxtnm184 = pyxtnm183
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(184))
                  return pyxtnm184
                ## endtimp(sint_add$sint(936))
                pyxtnm186 = XATSDAPP(pyxtnm185(pyxtnm137, XATSINT1(1)))
                pyxtnm187 = XATSDAPP(pyxtnm178(pyxtnm107, pyxtnm186))
                pyxtnm188 = pyxtnm175
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(188))
                return pyxtnm188
              ## endtimp(forall$test1(1423))
              pyxtnm190 = pyxtnm189
              pyxtnm191 = XATSDAPP(pyxtnm190(pyxtnm131))
              pyxtnm192 = pyxtnm191
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(192))
              return pyxtnm192
            ## endtimp(gseq_forall(386))
            pyxtnm194 = XATSDAPP(pyxtnm193(pyxtnm116))
            pyxtnm195 = pyxtnm194
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(195))
            return pyxtnm195
          ## endtimp(gseq_forall1(1720))
          pyxtnm197 = XATSDAPP(pyxtnm196(pyxtnm105))
          pyxtnm198 = pyxtnm197
          ## end-of(let)
          pyxtnm199 = pyxtnm198
          XATS000_patck(True)
          pyxtnm200 = pyxtnm199
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(200))
          return pyxtnm200
        ## endtimp(gseq_iforall1(1736))
        pyxtnm202 = XATSDAPP(pyxtnm201(pyxtnm99))
        pyxtnm203 = pyxtnm202
        XATS000_patck(True)
        pyxtnm204 = XATSVOID
        ## end-of(let)
        pyxtnm205 = pyxtnm204
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(205))
        return pyxtnm205
      ## endtimp(gseq_iforitm1(1760))
      pyxtnm207 = XATSDAPP(pyxtnm206(pyxtnm80))
      pyxtnm208 = pyxtnm207
      ## end-of(let)
      pyxtnm209 = pyxtnm208
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
      ## I1VALDCL
      pyxtnm218 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm214(arg1): ## timp: strn_print(1040)
        pyxtnm210 = arg1
        ## I1CMP:start
        ## let
        pyxtnm213 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(211);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(211))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm212 = XATSDAPP(XATS2PY_strn_print(pyxtnm210))
        pyxtnm213 = pyxtnm212
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(213))
        return pyxtnm213
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1991(line=85,offs=1)--2024(line=86,offs=25)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a0rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
      def pyxtnm215(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm216 = XATSDAPP(pyxtnm215())
      pyxtnm217 = XATSDAPP(pyxtnm214(pyxtnm216))
      pyxtnm218 = pyxtnm217
      XATS000_patck(True)
      pyxtnm219 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(219))
      return pyxtnm219
    ## endtimp(gseq_print1(1687))
    pyxtnm221 = XATSDAPP(pyxtnm220(pyxtnm79))
    pyxtnm222 = pyxtnm221
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(222))
    return pyxtnm222
  ## endtimp(g_print(39))
  pyxtnm224 = XATSDAPP(pyxtnm223(pyxtnm11))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22141(line=1366,offs=20)--22153(line=1366,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm226(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm225 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(225))
    return pyxtnm225
  ## endtimp(gs_print$sep(803))
  pyxtnm227 = XATSDAPP(pyxtnm226())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22158(line=1367,offs=3)--22165(line=1367,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x4[7031])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm233 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm232(arg1): ## timp: strn_print(1040)
    pyxtnm228 = arg1
    ## I1CMP:start
    ## let
    pyxtnm231 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(229);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(229))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm230 = XATSDAPP(XATS2PY_strn_print(pyxtnm228))
    pyxtnm231 = pyxtnm230
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(231))
    return pyxtnm231
  ## endtimp(strn_print(1040))
  pyxtnm233 = pyxtnm232
  pyxtnm234 = XATSDAPP(pyxtnm233(pyxtnm12))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22175(line=1367,offs=20)--22187(line=1367,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm236(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm235 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(235))
    return pyxtnm235
  ## endtimp(gs_print$end(804))
  pyxtnm237 = XATSDAPP(pyxtnm236())
  pyxtnm238 = pyxtnm237
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(238))
  return pyxtnm238
## endtimp(gs_print_a5(810))
## LCSRCsome1(test01_a0rf000.dats)@(429(line=28,offs=15)--433(line=28,offs=19))
## I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
## T1IMPallx(g_type(196), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
## T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
def pyxtnm243(arg1): ## timp: g_type(196)
  pyxtnm240 = arg1
  ## I1CMP:start
  pyxtnm241 = XATSCAPP("unit", [0])
  pyxtnm242 = XATSCAST("castxy_1839", [pyxtnm241])
  ## I1CMP:return:I1Vtnm(I1TNM(242))
  return pyxtnm242
## endtimp(g_type(196))
pyxtnm244 = XATSDAPP(pyxtnm243(pyxtnm7))
pyxtnm245 = XATSDAPP(pyxtnm239(XATSSTRN("A0("), pyxtnm244, XATSSTRN(") = "), pyxtnm7, XATSSTRN("\n")))
pyxtnm246 = pyxtnm245
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_a0rf000.dats)@(483(line=32,offs=1)--499(line=32,offs=17)))
## I1VALDCL
pyxtnm260 = None
## LCSRCsome1(test01_a0rf000.dats)@(492(line=32,offs=10)--495(line=32,offs=13))
## I0Etapq(I0Ecst(a0rf_get(1097)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(2845(line=132,offs=1)--2853(line=132,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(a0rf_get(1097), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2613(line=128,offs=1)--2718(line=137,offs=28)))
## T1IMPallx(a0rf_get(1097)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7265],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_get(1097);$list(@(a[2961],T2Pvar(x0[7265])))))))
def pyxtnm258(arg1): ## timp: a0rf_get(1097)
  pyxtnm247 = arg1
  ## I1CMP:start
  ## let
  pyxtnm257 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2650(line=132,offs=1)--2681(line=135,offs=17)))
  ## I1VALDCL
  pyxtnm254 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2665(line=135,offs=1)--2674(line=135,offs=10))
  ## I0Etapq(I0Ecst(a0rf_lget(1101)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3279(line=158,offs=1)--3288(line=158,offs=10))));$list(T2JAG($list(T2Pvar(x0[7265])))))
  ## T1IMPallx(a0rf_lget(1101), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1725(line=60,offs=1)--1882(line=75,offs=2)))
  ## T1IMPallx(a0rf_lget(1101)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8852],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_lget(1101);$list(@(a[2965],T2Pvar(a[8852])))))))
  def pyxtnm252(arg1): ## timp: a0rf_lget(1101)
    pyxtnm248 = arg1
    ## I1CMP:start
    ## let
    pyxtnm251 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1801(line=68,offs=1)--1880(line=74,offs=28)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a0rf_lget(2665));$list(I1FUNDCL(XATS2PY_a0rf_lget(5064);$list(FJARGdarg($list(I1BNDcons(I1TNM(249);I0Pvar(A(5065));$list(@(A(5065),I1Vtnm(I1TNM(249))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a0rf_lget);G1Nlist($list())))))))
    pyxtnm250 = XATSDAPP(XATS2PY_a0rf_lget(pyxtnm248))
    pyxtnm251 = pyxtnm250
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(251))
    return pyxtnm251
  ## endtimp(a0rf_lget(1101))
  pyxtnm253 = XATSDAPP(pyxtnm252(pyxtnm247))
  pyxtnm254 = pyxtnm253
  XATS000_patck(True)
  ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2682(line=136,offs=1)--2708(line=137,offs=18)))
  ## I1VALDCL
  ## I1BNDcons(I1TNM(256);I0Ptup0($list());$list())
  ## I1CMP:start
  ## I1LETnew1(I1TNM(255);I1INSdapp(I1Vcst(owed_t0_elim0(5));$list(I1Vnone0())))
  ## I1CMP(ival):I1Vtnm(I1TNM(255))## I1CMP:return
  pyxtnm257 = pyxtnm254
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(257))
  return pyxtnm257
## endtimp(a0rf_get(1097))
pyxtnm259 = XATSDAPP(pyxtnm258(pyxtnm7))
pyxtnm260 = pyxtnm259
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_a0rf000.dats)@(500(line=33,offs=1)--550(line=34,offs=42)))
## I1VALDCL
pyxtnm346 = None
## LCSRCsome1(test01_a0rf000.dats)@(509(line=34,offs=1)--515(line=34,offs=7))
## I0Etapq(I0Ecst(gs_print_a5(810)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(12006(line=769,offs=1)--12017(line=769,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a5(810), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21886(line=1350,offs=1)--22194(line=1368,offs=4)))
## T1IMPallx(gs_print_a5(810)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7027],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7028],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x2[7029],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7030],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x4[7031],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a5(810);$list(@(x0[2496],T2Pvar(x0[7027])),@(x1[2497],T2Pvar(x1[7028])),@(x2[2498],T2Pvar(x2[7029])),@(x3[2499],T2Pvar(x3[7030])),@(x4[2500],T2Pvar(x4[7031])))))))
def pyxtnm339(arg1, arg2, arg3, arg4, arg5): ## timp: gs_print_a5(810)
  pyxtnm261 = arg1
  pyxtnm262 = arg2
  pyxtnm263 = arg3
  pyxtnm264 = arg4
  pyxtnm265 = arg5
  ## I1CMP:start
  ## let
  pyxtnm338 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21986(line=1360,offs=1)--22009(line=1361,offs=15)))
  ## I1VALDCL
  pyxtnm269 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21995(line=1361,offs=1)--22007(line=1361,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm267(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm266 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(266))
    return pyxtnm266
  ## endtimp(gs_print$beg(802))
  pyxtnm268 = XATSDAPP(pyxtnm267())
  pyxtnm269 = pyxtnm268
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22022(line=1363,offs=3)--22029(line=1363,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7027])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm275 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm274(arg1): ## timp: strn_print(1040)
    pyxtnm270 = arg1
    ## I1CMP:start
    ## let
    pyxtnm273 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(271);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(271))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm272 = XATSDAPP(XATS2PY_strn_print(pyxtnm270))
    pyxtnm273 = pyxtnm272
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(273))
    return pyxtnm273
  ## endtimp(strn_print(1040))
  pyxtnm275 = pyxtnm274
  pyxtnm276 = XATSDAPP(pyxtnm275(pyxtnm261))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22039(line=1363,offs=20)--22051(line=1363,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm278(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm277 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(277))
    return pyxtnm277
  ## endtimp(gs_print$sep(803))
  pyxtnm279 = XATSDAPP(pyxtnm278())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22056(line=1364,offs=3)--22063(line=1364,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7028])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
  def pyxtnm303(arg1): ## timp: g_print(39)
    pyxtnm280 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
    ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
    ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
    ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
    def pyxtnm287(): ## timp: g_ptype(202)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm285(arg1): ## timp: strn_print(1040)
        pyxtnm281 = arg1
        ## I1CMP:start
        ## let
        pyxtnm284 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(282);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(282))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm283 = XATSDAPP(XATS2PY_strn_print(pyxtnm281))
        pyxtnm284 = pyxtnm283
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(284))
        return pyxtnm284
      ## endtimp(strn_print(1040))
      pyxtnm286 = XATSDAPP(pyxtnm285(XATSSTRN("sint")))
      ## I1CMP:return:I1Vtnm(I1TNM(286))
      return pyxtnm286
    ## endtimp(g_ptype(202))
    pyxtnm288 = XATSDAPP(pyxtnm287())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm293(arg1): ## timp: strn_print(1040)
      pyxtnm289 = arg1
      ## I1CMP:start
      ## let
      pyxtnm292 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(290);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(290))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm291 = XATSDAPP(XATS2PY_strn_print(pyxtnm289))
      pyxtnm292 = pyxtnm291
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(292))
      return pyxtnm292
    ## endtimp(strn_print(1040))
    pyxtnm294 = XATSDAPP(pyxtnm293(XATSSTRN(":")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
    ## I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
    ## T1IMPallx(g_psort(201), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1776(line=69,offs=1)--1830(line=73,offs=22)))
    ## T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(t0[5754],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(t0[5754])))))))
    def pyxtnm301(): ## timp: g_psort(201)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1811(line=73,offs=3)--1821(line=73,offs=13))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm299(arg1): ## timp: strn_print(1040)
        pyxtnm295 = arg1
        ## I1CMP:start
        ## let
        pyxtnm298 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(296);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(296))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm297 = XATSDAPP(XATS2PY_strn_print(pyxtnm295))
        pyxtnm298 = pyxtnm297
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(298))
        return pyxtnm298
      ## endtimp(strn_print(1040))
      pyxtnm300 = XATSDAPP(pyxtnm299(XATSSTRN("type")))
      ## I1CMP:return:I1Vtnm(I1TNM(300))
      return pyxtnm300
    ## endtimp(g_psort(201))
    pyxtnm302 = XATSDAPP(pyxtnm301())
    ## I1CMP:return:I1Vtnm(I1TNM(302))
    return pyxtnm302
  ## endtimp(g_print(39))
  pyxtnm304 = XATSDAPP(pyxtnm303(pyxtnm262))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22073(line=1364,offs=20)--22085(line=1364,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm306(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm305 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(305))
    return pyxtnm305
  ## endtimp(gs_print$sep(803))
  pyxtnm307 = XATSDAPP(pyxtnm306())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22090(line=1365,offs=3)--22097(line=1365,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7029])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm313 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm312(arg1): ## timp: strn_print(1040)
    pyxtnm308 = arg1
    ## I1CMP:start
    ## let
    pyxtnm311 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(309);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(309))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm310 = XATSDAPP(XATS2PY_strn_print(pyxtnm308))
    pyxtnm311 = pyxtnm310
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(311))
    return pyxtnm311
  ## endtimp(strn_print(1040))
  pyxtnm313 = pyxtnm312
  pyxtnm314 = XATSDAPP(pyxtnm313(pyxtnm263))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22107(line=1365,offs=20)--22119(line=1365,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm316(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm315 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(315))
    return pyxtnm315
  ## endtimp(gs_print$sep(803))
  pyxtnm317 = XATSDAPP(pyxtnm316())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22124(line=1366,offs=3)--22131(line=1366,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7030])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
  pyxtnm323 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
  ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
  ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
  def pyxtnm322(arg1): ## timp: sint_print(922)
    pyxtnm318 = arg1
    ## I1CMP:start
    ## let
    pyxtnm321 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(319);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(319))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
    pyxtnm320 = XATSDAPP(XATS2PY_sint_print(pyxtnm318))
    pyxtnm321 = pyxtnm320
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(321))
    return pyxtnm321
  ## endtimp(sint_print(922))
  pyxtnm323 = pyxtnm322
  pyxtnm324 = XATSDAPP(pyxtnm323(pyxtnm264))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22141(line=1366,offs=20)--22153(line=1366,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm326(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm325 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(325))
    return pyxtnm325
  ## endtimp(gs_print$sep(803))
  pyxtnm327 = XATSDAPP(pyxtnm326())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22158(line=1367,offs=3)--22165(line=1367,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x4[7031])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm333 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm332(arg1): ## timp: strn_print(1040)
    pyxtnm328 = arg1
    ## I1CMP:start
    ## let
    pyxtnm331 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(329);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(329))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm330 = XATSDAPP(XATS2PY_strn_print(pyxtnm328))
    pyxtnm331 = pyxtnm330
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(331))
    return pyxtnm331
  ## endtimp(strn_print(1040))
  pyxtnm333 = pyxtnm332
  pyxtnm334 = XATSDAPP(pyxtnm333(pyxtnm265))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22175(line=1367,offs=20)--22187(line=1367,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm336(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm335 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(335))
    return pyxtnm335
  ## endtimp(gs_print$end(804))
  pyxtnm337 = XATSDAPP(pyxtnm336())
  pyxtnm338 = pyxtnm337
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(338))
  return pyxtnm338
## endtimp(gs_print_a5(810))
## LCSRCsome1(test01_a0rf000.dats)@(523(line=34,offs=15)--527(line=34,offs=19))
## I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
## T1IMPallx(g_type(196), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
## T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
def pyxtnm343(arg1): ## timp: g_type(196)
  pyxtnm340 = arg1
  ## I1CMP:start
  pyxtnm341 = XATSCAPP("unit", [0])
  pyxtnm342 = XATSCAST("castxy_1839", [pyxtnm341])
  ## I1CMP:return:I1Vtnm(I1TNM(342))
  return pyxtnm342
## endtimp(g_type(196))
pyxtnm344 = XATSDAPP(pyxtnm343(pyxtnm260))
pyxtnm345 = XATSDAPP(pyxtnm339(XATSSTRN("x0("), pyxtnm344, XATSSTRN(") = "), pyxtnm260, XATSSTRN("\n")))
pyxtnm346 = pyxtnm345
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_a0rf000.dats)@(554(line=36,offs=1)--574(line=36,offs=21)))
## I1VALDCL
pyxtnm362 = None
## LCSRCsome1(test01_a0rf000.dats)@(563(line=36,offs=10)--566(line=36,offs=13))
## I0Etapq(I0Ecst(a0rf_set(1098)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(2882(line=135,offs=1)--2890(line=135,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(a0rf_set(1098), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2719(line=138,offs=1)--2824(line=144,offs=29)))
## T1IMPallx(a0rf_set(1098)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7266],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_set(1098);$list(@(a[2962],T2Pvar(x0[7266])))))))
def pyxtnm360(arg1, arg2): ## timp: a0rf_set(1098)
  pyxtnm347 = arg1
  pyxtnm348 = arg2
  ## I1CMP:start
  ## let
  pyxtnm359 = None
  ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2759(line=142,offs=1)--2787(line=143,offs=20)))
  ## I1VALDCL
  ## I1BNDcons(I1TNM(350);I0Pvar(px(2276));$list(@(px(2276),I1Vtnm(I1TNM(350)))))
  ## I1CMP:start
  ## I1LETnew1(I1TNM(349);I1INSdapp(I1Vcst(owed_t0_make(4));$list()))
  ## I1CMP(ival):I1Vtnm(I1TNM(349))## I1CMP:return
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2796(line=144,offs=1)--2805(line=144,offs=10))
  ## I0Etapq(I0Ecst(a0rf_lset(1102)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3327(line=162,offs=1)--3336(line=162,offs=10))));$list(T2JAG($list(T2Pvar(x0[7266])))))
  ## T1IMPallx(a0rf_lset(1102), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1886(line=77,offs=1)--2054(line=91,offs=2)))
  ## T1IMPallx(a0rf_lset(1102)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8854],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_lset(1102);$list(@(a[2966],T2Pvar(a[8854])))))))
  def pyxtnm357(arg1, arg2): ## timp: a0rf_lset(1102)
    pyxtnm351 = arg1
    pyxtnm352 = arg2
    ## I1CMP:start
    ## let
    pyxtnm356 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1970(line=85,offs=1)--2052(line=90,offs=35)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a0rf_lset(2666));$list(I1FUNDCL(XATS2PY_a0rf_lset(5069);$list(FJARGdarg($list(I1BNDcons(I1TNM(353);I0Pvar(A(5071));$list(@(A(5071),I1Vtnm(I1TNM(353))))),I1BNDcons(I1TNM(354);I0Pvar(x(5072));$list(@(x(5072),I1Vtnm(I1TNM(354))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a0rf_lset);G1Nlist($list())))))))
    pyxtnm355 = XATSDAPP(XATS2PY_a0rf_lset(pyxtnm351, pyxtnm352))
    pyxtnm356 = pyxtnm355
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(356))
    return pyxtnm356
  ## endtimp(a0rf_lset(1102))
  pyxtnm358 = XATSDAPP(pyxtnm357(pyxtnm347, pyxtnm348))
  pyxtnm359 = pyxtnm358
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(359))
  return pyxtnm359
## endtimp(a0rf_set(1098))
pyxtnm361 = XATSDAPP(pyxtnm360(pyxtnm7, XATSINT1(10)))
pyxtnm362 = pyxtnm361
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_a0rf000.dats)@(575(line=37,offs=1)--625(line=38,offs=42)))
## I1VALDCL
pyxtnm601 = None
## LCSRCsome1(test01_a0rf000.dats)@(584(line=38,offs=1)--590(line=38,offs=7))
## I0Etapq(I0Ecst(gs_print_a5(810)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(12006(line=769,offs=1)--12017(line=769,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a5(810), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21886(line=1350,offs=1)--22194(line=1368,offs=4)))
## T1IMPallx(gs_print_a5(810)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7027],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7028],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x2[7029],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7030],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x4[7031],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a5(810);$list(@(x0[2496],T2Pvar(x0[7027])),@(x1[2497],T2Pvar(x1[7028])),@(x2[2498],T2Pvar(x2[7029])),@(x3[2499],T2Pvar(x3[7030])),@(x4[2500],T2Pvar(x4[7031])))))))
def pyxtnm594(arg1, arg2, arg3, arg4, arg5): ## timp: gs_print_a5(810)
  pyxtnm363 = arg1
  pyxtnm364 = arg2
  pyxtnm365 = arg3
  pyxtnm366 = arg4
  pyxtnm367 = arg5
  ## I1CMP:start
  ## let
  pyxtnm593 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21986(line=1360,offs=1)--22009(line=1361,offs=15)))
  ## I1VALDCL
  pyxtnm371 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21995(line=1361,offs=1)--22007(line=1361,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm369(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm368 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(368))
    return pyxtnm368
  ## endtimp(gs_print$beg(802))
  pyxtnm370 = XATSDAPP(pyxtnm369())
  pyxtnm371 = pyxtnm370
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22022(line=1363,offs=3)--22029(line=1363,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7027])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm377 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm376(arg1): ## timp: strn_print(1040)
    pyxtnm372 = arg1
    ## I1CMP:start
    ## let
    pyxtnm375 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(373);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(373))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm374 = XATSDAPP(XATS2PY_strn_print(pyxtnm372))
    pyxtnm375 = pyxtnm374
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(375))
    return pyxtnm375
  ## endtimp(strn_print(1040))
  pyxtnm377 = pyxtnm376
  pyxtnm378 = XATSDAPP(pyxtnm377(pyxtnm363))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22039(line=1363,offs=20)--22051(line=1363,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm380(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm379 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(379))
    return pyxtnm379
  ## endtimp(gs_print$sep(803))
  pyxtnm381 = XATSDAPP(pyxtnm380())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22056(line=1364,offs=3)--22063(line=1364,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7028])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
  def pyxtnm419(arg1): ## timp: g_print(39)
    pyxtnm382 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
    ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
    ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1512(line=44,offs=1)--1614(line=51,offs=32)))
    ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(vt[7259],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(a0rf);$list(T2Pvar(vt[7259])))))))))
    def pyxtnm403(): ## timp: g_ptype(202)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1567(line=50,offs=1)--1572(line=50,offs=6))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm387(arg1): ## timp: strn_print(1040)
        pyxtnm383 = arg1
        ## I1CMP:start
        ## let
        pyxtnm386 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(384);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(384))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm385 = XATSDAPP(XATS2PY_strn_print(pyxtnm383))
        pyxtnm386 = pyxtnm385
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(386))
        return pyxtnm386
      ## endtimp(strn_print(1040))
      pyxtnm388 = XATSDAPP(pyxtnm387(XATSSTRN("a0rf(")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1583(line=51,offs=1)--1590(line=51,offs=8))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vt[7259])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
      def pyxtnm395(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm393(arg1): ## timp: strn_print(1040)
          pyxtnm389 = arg1
          ## I1CMP:start
          ## let
          pyxtnm392 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(390);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(390))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm391 = XATSDAPP(XATS2PY_strn_print(pyxtnm389))
          pyxtnm392 = pyxtnm391
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(392))
          return pyxtnm392
        ## endtimp(strn_print(1040))
        pyxtnm394 = XATSDAPP(pyxtnm393(XATSSTRN("sint")))
        ## I1CMP:return:I1Vtnm(I1TNM(394))
        return pyxtnm394
      ## endtimp(g_ptype(202))
      pyxtnm396 = XATSDAPP(pyxtnm395())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1603(line=51,offs=21)--1608(line=51,offs=26))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm401(arg1): ## timp: strn_print(1040)
        pyxtnm397 = arg1
        ## I1CMP:start
        ## let
        pyxtnm400 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(398);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(398))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm399 = XATSDAPP(XATS2PY_strn_print(pyxtnm397))
        pyxtnm400 = pyxtnm399
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(400))
        return pyxtnm400
      ## endtimp(strn_print(1040))
      pyxtnm402 = XATSDAPP(pyxtnm401(XATSSTRN(")")))
      ## I1CMP:return:I1Vtnm(I1TNM(402))
      return pyxtnm402
    ## endtimp(g_ptype(202))
    pyxtnm404 = XATSDAPP(pyxtnm403())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm409(arg1): ## timp: strn_print(1040)
      pyxtnm405 = arg1
      ## I1CMP:start
      ## let
      pyxtnm408 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(406);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(406))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm407 = XATSDAPP(XATS2PY_strn_print(pyxtnm405))
      pyxtnm408 = pyxtnm407
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(408))
      return pyxtnm408
    ## endtimp(strn_print(1040))
    pyxtnm410 = XATSDAPP(pyxtnm409(XATSSTRN(":")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
    ## I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
    ## T1IMPallx(g_psort(201), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1831(line=74,offs=1)--1885(line=78,offs=22)))
    ## T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(tx[5755],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(tx[5755])))))))
    def pyxtnm417(): ## timp: g_psort(201)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1866(line=78,offs=3)--1876(line=78,offs=13))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm415(arg1): ## timp: strn_print(1040)
        pyxtnm411 = arg1
        ## I1CMP:start
        ## let
        pyxtnm414 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(412);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(412))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm413 = XATSDAPP(XATS2PY_strn_print(pyxtnm411))
        pyxtnm414 = pyxtnm413
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(414))
        return pyxtnm414
      ## endtimp(strn_print(1040))
      pyxtnm416 = XATSDAPP(pyxtnm415(XATSSTRN("tbox")))
      ## I1CMP:return:I1Vtnm(I1TNM(416))
      return pyxtnm416
    ## endtimp(g_psort(201))
    pyxtnm418 = XATSDAPP(pyxtnm417())
    ## I1CMP:return:I1Vtnm(I1TNM(418))
    return pyxtnm418
  ## endtimp(g_print(39))
  pyxtnm420 = XATSDAPP(pyxtnm419(pyxtnm364))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22073(line=1364,offs=20)--22085(line=1364,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm422(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm421 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(421))
    return pyxtnm421
  ## endtimp(gs_print$sep(803))
  pyxtnm423 = XATSDAPP(pyxtnm422())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22090(line=1365,offs=3)--22097(line=1365,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7029])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm429 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm428(arg1): ## timp: strn_print(1040)
    pyxtnm424 = arg1
    ## I1CMP:start
    ## let
    pyxtnm427 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(425);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(425))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm426 = XATSDAPP(XATS2PY_strn_print(pyxtnm424))
    pyxtnm427 = pyxtnm426
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(427))
    return pyxtnm427
  ## endtimp(strn_print(1040))
  pyxtnm429 = pyxtnm428
  pyxtnm430 = XATSDAPP(pyxtnm429(pyxtnm365))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22107(line=1365,offs=20)--22119(line=1365,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm432(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm431 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(431))
    return pyxtnm431
  ## endtimp(gs_print$sep(803))
  pyxtnm433 = XATSDAPP(pyxtnm432())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22124(line=1366,offs=3)--22131(line=1366,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7030])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1873(line=74,offs=1)--2106(line=92,offs=4)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a0rf);$list(T2Pvar(x0[7262])))))))))
  def pyxtnm578(arg1): ## timp: g_print(39)
    pyxtnm434 = arg1
    ## I1CMP:start
    ## let
    pyxtnm577 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1931(line=81,offs=1)--1953(line=81,offs=23))
    ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(a0rf);$list(S2Evar(x0[7262])))))))
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1957(line=83,offs=1)--1990(line=84,offs=25)))
    ## I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7262]))))):timp
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1991(line=85,offs=1)--2024(line=86,offs=25)))
    ## I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7262]))))):timp
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2025(line=87,offs=1)--2062(line=88,offs=29)))
    ## I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7262]))))):timp
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2075(line=91,offs=3)--2086(line=91,offs=14))
    ## I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Pvar(x0[7262]))))),T2JAG($list(T2Pvar(x0[7262])))))
    ## T1IMPallx(gseq_print1(1687), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
    ## T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
    def pyxtnm575(arg1): ## timp: gseq_print1(1687)
      pyxtnm435 = arg1
      ## I1CMP:start
      ## let
      pyxtnm574 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
      ## I1VALDCL
      pyxtnm444 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm440(arg1): ## timp: strn_print(1040)
        pyxtnm436 = arg1
        ## I1CMP:start
        ## let
        pyxtnm439 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(437);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(437))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm438 = XATSDAPP(XATS2PY_strn_print(pyxtnm436))
        pyxtnm439 = pyxtnm438
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(439))
        return pyxtnm439
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2025(line=87,offs=1)--2062(line=88,offs=29)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a0rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
      def pyxtnm441(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("a0rf(")
      ## endtimp(gseq$beg(346))
      pyxtnm442 = XATSDAPP(pyxtnm441())
      pyxtnm443 = XATSDAPP(pyxtnm440(pyxtnm442))
      pyxtnm444 = pyxtnm443
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
      ## I1VALDCL
      pyxtnm564 = None
      ## let
      pyxtnm563 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq_iforitm1(1760), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
      def pyxtnm561(arg1): ## timp: gseq_iforitm1(1760)
        pyxtnm454 = arg1
        ## I1CMP:start
        ## let
        pyxtnm560 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
        ## let
        pyxtnm559 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
        ## I1VALDCL
        pyxtnm558 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
        ## T1IMPallx(gseq_iforall1(1736), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
        ## T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
        def pyxtnm556(arg1): ## timp: gseq_iforall1(1736)
          pyxtnm460 = arg1
          ## I1CMP:start
          ## let
          pyxtnm555 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm461 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
          ## I1VALDCL
          pyxtnm462 = None
          pyxtnm462 = XATSADDR(pyxtnm461)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
          ## I1VALDCL
          pyxtnm554 = None
          ## let
          pyxtnm553 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
          ## T1IMPallx(gseq_forall1(1720), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
          ## T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
          def pyxtnm551(arg1): ## timp: gseq_forall1(1720)
            pyxtnm471 = arg1
            ## I1CMP:start
            ## let
            pyxtnm550 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
            ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
            ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1473(line=43,offs=1)--1596(line=52,offs=27)))
            ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7278],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7278],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a0rf);$list(T2Pvar(x0[7278])))),@(x0[1168],T2Pvar(x0[7278])))))))
            def pyxtnm548(arg1): ## timp: gseq_forall(386)
              pyxtnm472 = arg1
              ## I1CMP:start
              ## let
              pyxtnm547 = None
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1538(line=49,offs=1)--1564(line=50,offs=18)))
              ## I1VALDCL
              pyxtnm486 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1547(line=50,offs=1)--1555(line=50,offs=9))
              ## I0Etapq(I0Ecst(a0rf_get(1097)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(2845(line=132,offs=1)--2853(line=132,offs=9))));$list(T2JAG($list(T2Pvar(x0[7278])))))
              ## T1IMPallx(a0rf_get(1097), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2613(line=128,offs=1)--2718(line=137,offs=28)))
              ## T1IMPallx(a0rf_get(1097)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7265],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_get(1097);$list(@(a[2961],T2Pvar(x0[7265])))))))
              def pyxtnm484(arg1): ## timp: a0rf_get(1097)
                pyxtnm473 = arg1
                ## I1CMP:start
                ## let
                pyxtnm483 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2650(line=132,offs=1)--2681(line=135,offs=17)))
                ## I1VALDCL
                pyxtnm480 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2665(line=135,offs=1)--2674(line=135,offs=10))
                ## I0Etapq(I0Ecst(a0rf_lget(1101)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3279(line=158,offs=1)--3288(line=158,offs=10))));$list(T2JAG($list(T2Pvar(x0[7265])))))
                ## T1IMPallx(a0rf_lget(1101), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1725(line=60,offs=1)--1882(line=75,offs=2)))
                ## T1IMPallx(a0rf_lget(1101)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8852],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a0rf_lget(1101);$list(@(a[2965],T2Pvar(a[8852])))))))
                def pyxtnm478(arg1): ## timp: a0rf_lget(1101)
                  pyxtnm474 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm477 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(1801(line=68,offs=1)--1880(line=74,offs=28)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a0rf_lget(2665));$list(I1FUNDCL(XATS2PY_a0rf_lget(5064);$list(FJARGdarg($list(I1BNDcons(I1TNM(475);I0Pvar(A(5065));$list(@(A(5065),I1Vtnm(I1TNM(475))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a0rf_lget);G1Nlist($list())))))))
                  pyxtnm476 = XATSDAPP(XATS2PY_a0rf_lget(pyxtnm474))
                  pyxtnm477 = pyxtnm476
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(477))
                  return pyxtnm477
                ## endtimp(a0rf_lget(1101))
                pyxtnm479 = XATSDAPP(pyxtnm478(pyxtnm473))
                pyxtnm480 = pyxtnm479
                XATS000_patck(True)
                ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2682(line=136,offs=1)--2708(line=137,offs=18)))
                ## I1VALDCL
                ## I1BNDcons(I1TNM(482);I0Ptup0($list());$list())
                ## I1CMP:start
                ## I1LETnew1(I1TNM(481);I1INSdapp(I1Vcst(owed_t0_elim0(5));$list(I1Vnone0())))
                ## I1CMP(ival):I1Vtnm(I1TNM(481))## I1CMP:return
                pyxtnm483 = pyxtnm480
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(483))
                return pyxtnm483
              ## endtimp(a0rf_get(1097))
              pyxtnm485 = XATSDAPP(pyxtnm484(pyxtnm472))
              pyxtnm486 = pyxtnm485
              XATS000_patck(True)
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(1572(line=52,offs=3)--1583(line=52,offs=14))
              ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7278])))))
              ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
              ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              pyxtnm545 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
              ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
              ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
              ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              def pyxtnm544(arg1): ## timp: forall$test1(1423)
                pyxtnm487 = arg1
                ## I1CMP:start
                ## let
                pyxtnm543 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                ## I1VALDCL
                pyxtnm492 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                def pyxtnm490(arg1): ## timp: p2tr_get(2309)
                  pyxtnm488 = arg1
                  ## I1CMP:start
                  pyxtnm489 = XATS000_dp2tr(pyxtnm488)
                  ## I1CMP:return:I1Vtnm(I1TNM(489))
                  return pyxtnm489
                ## endtimp(p2tr_get(2309))
                pyxtnm491 = XATSDAPP(pyxtnm490(pyxtnm462))
                pyxtnm492 = pyxtnm491
                XATS000_patck(True)
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                ## I1VALDCL
                pyxtnm530 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                ## I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                ## T1IMPallx(iforall$test1(1433), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                ## T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                def pyxtnm528(arg1, arg2): ## timp: iforall$test1(1433)
                  pyxtnm493 = arg1
                  pyxtnm494 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm527 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                  ## I1VALDCL
                  pyxtnm526 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                  ## I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                  ## T1IMPallx(iforitm$work1(1449), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                  ## T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm524(arg1, arg2): ## timp: iforitm$work1(1449)
                    pyxtnm495 = arg1
                    pyxtnm496 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm523 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                    ## I1VALDCL
                    pyxtnm514 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                    ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                    ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                    def pyxtnm503(arg1, arg2): ## timp: sint_gt$sint(928)
                      pyxtnm497 = arg1
                      pyxtnm498 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm502 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(499);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(499))))),I1BNDcons(I1TNM(500);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(500))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                      pyxtnm501 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm497, pyxtnm498))
                      pyxtnm502 = pyxtnm501
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(502))
                      return pyxtnm502
                    ## endtimp(sint_gt$sint(928))
                    pyxtnm504 = XATSDAPP(pyxtnm503(pyxtnm495, XATSINT1(0)))
                    pyxtnm513 = None
                    if (pyxtnm504):
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                      def pyxtnm509(arg1): ## timp: strn_print(1040)
                        pyxtnm505 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm508 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(506);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(506))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                        pyxtnm507 = XATSDAPP(XATS2PY_strn_print(pyxtnm505))
                        pyxtnm508 = pyxtnm507
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(508))
                        return pyxtnm508
                      ## endtimp(strn_print(1040))
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                      ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                      ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1957(line=83,offs=1)--1990(line=84,offs=25)))
                      ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a0rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm510(): ## timp: gseq$sep(348)
                        ## I1CMP:start
                        ## I1CMP:return:I1Vstr(...)
                        return XATSSTRN(",")
                      ## endtimp(gseq$sep(348))
                      pyxtnm511 = XATSDAPP(pyxtnm510())
                      pyxtnm512 = XATSDAPP(pyxtnm509(pyxtnm511))
                      pyxtnm513 = pyxtnm512
                    ## else: None
                    ## end-of(if)
                    pyxtnm514 = pyxtnm513
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                    ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                    ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                    ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                    pyxtnm521 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                    pyxtnm520 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                    ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                    ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                    def pyxtnm519(arg1): ## timp: sint_print(922)
                      pyxtnm515 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm518 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(516);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(516))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                      pyxtnm517 = XATSDAPP(XATS2PY_sint_print(pyxtnm515))
                      pyxtnm518 = pyxtnm517
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(518))
                      return pyxtnm518
                    ## endtimp(sint_print(922))
                    pyxtnm520 = pyxtnm519
                    pyxtnm521 = pyxtnm520
                    pyxtnm522 = XATSDAPP(pyxtnm521(pyxtnm496))
                    pyxtnm523 = pyxtnm522
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(523))
                    return pyxtnm523
                  ## endtimp(iforitm$work1(1449))
                  pyxtnm525 = XATSDAPP(pyxtnm524(pyxtnm493, pyxtnm494))
                  pyxtnm526 = pyxtnm525
                  XATS000_patck(True)
                  pyxtnm527 = XATSBOOL(True)
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(527))
                  return pyxtnm527
                ## endtimp(iforall$test1(1433))
                pyxtnm529 = XATSDAPP(pyxtnm528(pyxtnm492, pyxtnm487))
                pyxtnm530 = pyxtnm529
                XATS000_patck(True)
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                def pyxtnm533(arg1, arg2): ## timp: p2tr_set(2310)
                  pyxtnm531 = arg1
                  pyxtnm532 = arg2
                  ## I1CMP:start
                  XATS000_assgn(pyxtnm531, pyxtnm532)
                  ## I1CMP:return:I1V000()
                  return XATSVOID
                ## endtimp(p2tr_set(2310))
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                def pyxtnm540(arg1, arg2): ## timp: sint_add$sint(936)
                  pyxtnm534 = arg1
                  pyxtnm535 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm539 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(536);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(536))))),I1BNDcons(I1TNM(537);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(537))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                  pyxtnm538 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm534, pyxtnm535))
                  pyxtnm539 = pyxtnm538
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(539))
                  return pyxtnm539
                ## endtimp(sint_add$sint(936))
                pyxtnm541 = XATSDAPP(pyxtnm540(pyxtnm492, XATSINT1(1)))
                pyxtnm542 = XATSDAPP(pyxtnm533(pyxtnm462, pyxtnm541))
                pyxtnm543 = pyxtnm530
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(543))
                return pyxtnm543
              ## endtimp(forall$test1(1423))
              pyxtnm545 = pyxtnm544
              pyxtnm546 = XATSDAPP(pyxtnm545(pyxtnm486))
              pyxtnm547 = pyxtnm546
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(547))
              return pyxtnm547
            ## endtimp(gseq_forall(386))
            pyxtnm549 = XATSDAPP(pyxtnm548(pyxtnm471))
            pyxtnm550 = pyxtnm549
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(550))
            return pyxtnm550
          ## endtimp(gseq_forall1(1720))
          pyxtnm552 = XATSDAPP(pyxtnm551(pyxtnm460))
          pyxtnm553 = pyxtnm552
          ## end-of(let)
          pyxtnm554 = pyxtnm553
          XATS000_patck(True)
          pyxtnm555 = pyxtnm554
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(555))
          return pyxtnm555
        ## endtimp(gseq_iforall1(1736))
        pyxtnm557 = XATSDAPP(pyxtnm556(pyxtnm454))
        pyxtnm558 = pyxtnm557
        XATS000_patck(True)
        pyxtnm559 = XATSVOID
        ## end-of(let)
        pyxtnm560 = pyxtnm559
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(560))
        return pyxtnm560
      ## endtimp(gseq_iforitm1(1760))
      pyxtnm562 = XATSDAPP(pyxtnm561(pyxtnm435))
      pyxtnm563 = pyxtnm562
      ## end-of(let)
      pyxtnm564 = pyxtnm563
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
      ## I1VALDCL
      pyxtnm573 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm569(arg1): ## timp: strn_print(1040)
        pyxtnm565 = arg1
        ## I1CMP:start
        ## let
        pyxtnm568 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(566);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(566))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm567 = XATSDAPP(XATS2PY_strn_print(pyxtnm565))
        pyxtnm568 = pyxtnm567
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(568))
        return pyxtnm568
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1991(line=85,offs=1)--2024(line=86,offs=25)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a0rf_vt_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7262],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a0rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
      def pyxtnm570(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm571 = XATSDAPP(pyxtnm570())
      pyxtnm572 = XATSDAPP(pyxtnm569(pyxtnm571))
      pyxtnm573 = pyxtnm572
      XATS000_patck(True)
      pyxtnm574 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(574))
      return pyxtnm574
    ## endtimp(gseq_print1(1687))
    pyxtnm576 = XATSDAPP(pyxtnm575(pyxtnm434))
    pyxtnm577 = pyxtnm576
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(577))
    return pyxtnm577
  ## endtimp(g_print(39))
  pyxtnm579 = XATSDAPP(pyxtnm578(pyxtnm366))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22141(line=1366,offs=20)--22153(line=1366,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm581(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm580 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(580))
    return pyxtnm580
  ## endtimp(gs_print$sep(803))
  pyxtnm582 = XATSDAPP(pyxtnm581())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22158(line=1367,offs=3)--22165(line=1367,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x4[7031])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm588 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm587(arg1): ## timp: strn_print(1040)
    pyxtnm583 = arg1
    ## I1CMP:start
    ## let
    pyxtnm586 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(584);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(584))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm585 = XATSDAPP(XATS2PY_strn_print(pyxtnm583))
    pyxtnm586 = pyxtnm585
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(586))
    return pyxtnm586
  ## endtimp(strn_print(1040))
  pyxtnm588 = pyxtnm587
  pyxtnm589 = XATSDAPP(pyxtnm588(pyxtnm367))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(22175(line=1367,offs=20)--22187(line=1367,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm591(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm590 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(590))
    return pyxtnm590
  ## endtimp(gs_print$end(804))
  pyxtnm592 = XATSDAPP(pyxtnm591())
  pyxtnm593 = pyxtnm592
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(593))
  return pyxtnm593
## endtimp(gs_print_a5(810))
## LCSRCsome1(test01_a0rf000.dats)@(598(line=38,offs=15)--602(line=38,offs=19))
## I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
## T1IMPallx(g_type(196), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
## T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
def pyxtnm598(arg1): ## timp: g_type(196)
  pyxtnm595 = arg1
  ## I1CMP:start
  pyxtnm596 = XATSCAPP("unit", [0])
  pyxtnm597 = XATSCAST("castxy_1839", [pyxtnm596])
  ## I1CMP:return:I1Vtnm(I1TNM(597))
  return pyxtnm597
## endtimp(g_type(196))
pyxtnm599 = XATSDAPP(pyxtnm598(pyxtnm7))
pyxtnm600 = XATSDAPP(pyxtnm594(XATSSTRN("A0("), pyxtnm599, XATSSTRN(") = "), pyxtnm7, XATSSTRN("\n")))
pyxtnm601 = pyxtnm600
XATS000_patck(True)
## LCSRCsome1(test01_a0rf000.dats)@(888(line=46,offs=1)--888(line=46,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test01_a0rf000.dats)@(888(line=46,offs=1)--888(line=46,offs=1));D3Cnone0()))
