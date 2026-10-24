## Sun Aug 16 12:19:36 PM EDT 2026
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
    return ds ## ascii code of [ch]
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
## Mon Aug 10 01:05:55 PM EDT 2026
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
## LCSRCsome1(test05_gdbg000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## I1Dinclude(LCSRCsome1(test05_gdbg000.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
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
## I1Dinclude(LCSRCsome1(test05_gdbg000.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
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
## I1Dfundclist(LCSRCsome1(test05_gdbg000.dats)@(323(line=21,offs=1)--385(line=25,offs=26)))
## I1FUNDCL
def fact_326(arg1): ## fun
  pyxtnm1 = arg1
  ## I1CMP:start
  ## LCSRCsome1(test05_gdbg000.dats)@(355(line=24,offs=4)--356(line=24,offs=5))
  ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
  ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
  def pyxtnm8(arg1, arg2): ## timp: sint_gt$sint(928)
    pyxtnm2 = arg1
    pyxtnm3 = arg2
    ## I1CMP:start
    ## let
    pyxtnm7 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(4);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(4))))),I1BNDcons(I1TNM(5);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(5))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
    pyxtnm6 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm2, pyxtnm3))
    pyxtnm7 = pyxtnm6
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(7))
    return pyxtnm7
  ## endtimp(sint_gt$sint(928))
  pyxtnm9 = XATSDAPP(pyxtnm8(pyxtnm1, XATSINT1(0)))
  pyxtnm27 = None
  if (pyxtnm9):
    ## LCSRCsome1(test05_gdbg000.dats)@(367(line=25,offs=8)--368(line=25,offs=9))
    ## I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
    ## T1IMPallx(sint_mul$sint(938), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
    ## T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
    def pyxtnm16(arg1, arg2): ## timp: sint_mul$sint(938)
      pyxtnm10 = arg1
      pyxtnm11 = arg2
      ## I1CMP:start
      ## let
      pyxtnm15 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mul$sint(2621));$list(I1FUNDCL(XATS2PY_sint_mul$sint(4901);$list(FJARGdarg($list(I1BNDcons(I1TNM(12);I0Pvar(i1(4902));$list(@(i1(4902),I1Vtnm(I1TNM(12))))),I1BNDcons(I1TNM(13);I0Pvar(i2(4903));$list(@(i2(4903),I1Vtnm(I1TNM(13))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mul$sint);G1Nlist($list())))))))
      pyxtnm14 = XATSDAPP(XATS2PY_sint_mul_sint(pyxtnm10, pyxtnm11))
      pyxtnm15 = pyxtnm14
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(15))
      return pyxtnm15
    ## endtimp(sint_mul$sint(938))
    ## LCSRCsome1(test05_gdbg000.dats)@(375(line=25,offs=16)--376(line=25,offs=17))
    ## I0Etapq(I0Ecst(sint_sub$sint(937)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3146(line=146,offs=1)--3159(line=146,offs=14))));$list(T2JAG($list())))
    ## T1IMPallx(sint_sub$sint(937), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2845(line=159,offs=1)--3009(line=171,offs=2)))
    ## T1IMPallx(sint_sub$sint(937)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_sub$sint(937);$list()))))
    def pyxtnm23(arg1, arg2): ## timp: sint_sub$sint(937)
      pyxtnm17 = arg1
      pyxtnm18 = arg2
      ## I1CMP:start
      ## let
      pyxtnm22 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2935(line=167,offs=1)--3007(line=170,offs=39)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_sub$sint(2620));$list(I1FUNDCL(XATS2PY_sint_sub$sint(4896);$list(FJARGdarg($list(I1BNDcons(I1TNM(19);I0Pvar(i1(4897));$list(@(i1(4897),I1Vtnm(I1TNM(19))))),I1BNDcons(I1TNM(20);I0Pvar(i2(4898));$list(@(i2(4898),I1Vtnm(I1TNM(20))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_sub$sint);G1Nlist($list())))))))
      pyxtnm21 = XATSDAPP(XATS2PY_sint_sub_sint(pyxtnm17, pyxtnm18))
      pyxtnm22 = pyxtnm21
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(22))
      return pyxtnm22
    ## endtimp(sint_sub$sint(937))
    pyxtnm24 = XATSDAPP(pyxtnm23(pyxtnm1, XATSINT1(1)))
    pyxtnm25 = XATSDAPP(fact_326(pyxtnm24))
    pyxtnm26 = XATSDAPP(pyxtnm16(pyxtnm1, pyxtnm25))
    pyxtnm27 = pyxtnm26
  else:
    pyxtnm27 = XATSINT1(1)
  ## end-of(if)
  ## I1CMP:return:I1Vtnm(I1TNM(27))
  return pyxtnm27
## I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(432(line=30,offs=1)--462(line=31,offs=27)))
## I1VALDCL
pyxtnm134 = None
## LCSRCsome1(test05_gdbg000.dats)@(443(line=31,offs=8)--448(line=31,offs=13))
## I0Etapq(I0Ecst(f1un_trace(316)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gfun000.sats)@(3453(line=188,offs=1)--3463(line=188,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(f1un_trace(316), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2559(line=124,offs=1)--2769(line=137,offs=39)))
## T1IMPallx(f1un_trace(316)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a1[5966],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[5967],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(f1un_trace(316);$list(@(a1[986],T2Pvar(a1[5966])),@(r0[987],T2Pvar(r0[5967])))))))
def pyxtnm132(arg1, arg2): ## timp: f1un_trace(316)
  pyxtnm28 = arg1
  pyxtnm29 = arg2
  ## I1CMP:start
  def pyxtnm131(arg1): ## { // lam0(T_LAM(0))
    pyxtnm30 = arg1
    ## I1CMP:start
    ## let
    pyxtnm130 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2634(line=131,offs=1)--2678(line=132,offs=29)))
    ## I1VALDCL
    pyxtnm82 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2643(line=131,offs=10)--2649(line=131,offs=16))
    ## I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(a1[5966]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    ## T1IMPallx(gs_print_a4(809), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
    ## T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[7025],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
    def pyxtnm80(arg1, arg2, arg3, arg4): ## timp: gs_print_a4(809)
      pyxtnm31 = arg1
      pyxtnm32 = arg2
      pyxtnm33 = arg3
      pyxtnm34 = arg4
      ## I1CMP:start
      ## let
      pyxtnm79 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
      ## I1VALDCL
      pyxtnm38 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
      ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      def pyxtnm36(): ## timp: gs_print$beg(802)
        ## I1CMP:start
        pyxtnm35 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(35))
        return pyxtnm35
      ## endtimp(gs_print$beg(802))
      pyxtnm37 = XATSDAPP(pyxtnm36())
      pyxtnm38 = pyxtnm37
      XATS000_patck(True)
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm44 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm43(arg1): ## timp: strn_print(1040)
        pyxtnm39 = arg1
        ## I1CMP:start
        ## let
        pyxtnm42 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(40);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(40))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm41 = XATSDAPP(XATS2PY_strn_print(pyxtnm39))
        pyxtnm42 = pyxtnm41
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(42))
        return pyxtnm42
      ## endtimp(strn_print(1040))
      pyxtnm44 = pyxtnm43
      pyxtnm45 = XATSDAPP(pyxtnm44(pyxtnm31))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm47(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm46 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(46))
        return pyxtnm46
      ## endtimp(gs_print$sep(803))
      pyxtnm48 = XATSDAPP(pyxtnm47())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm54 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm53(arg1): ## timp: strn_print(1040)
        pyxtnm49 = arg1
        ## I1CMP:start
        ## let
        pyxtnm52 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(50);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(50))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm51 = XATSDAPP(XATS2PY_strn_print(pyxtnm49))
        pyxtnm52 = pyxtnm51
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(52))
        return pyxtnm52
      ## endtimp(strn_print(1040))
      pyxtnm54 = pyxtnm53
      pyxtnm55 = XATSDAPP(pyxtnm54(pyxtnm32))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm57(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm56 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(56))
        return pyxtnm56
      ## endtimp(gs_print$sep(803))
      pyxtnm58 = XATSDAPP(pyxtnm57())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
      pyxtnm64 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
      ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
      ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
      def pyxtnm63(arg1): ## timp: sint_print(922)
        pyxtnm59 = arg1
        ## I1CMP:start
        ## let
        pyxtnm62 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(60);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(60))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
        pyxtnm61 = XATSDAPP(XATS2PY_sint_print(pyxtnm59))
        pyxtnm62 = pyxtnm61
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(62))
        return pyxtnm62
      ## endtimp(sint_print(922))
      pyxtnm64 = pyxtnm63
      pyxtnm65 = XATSDAPP(pyxtnm64(pyxtnm33))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
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
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
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
      pyxtnm75 = XATSDAPP(pyxtnm74(pyxtnm34))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
      ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      def pyxtnm77(): ## timp: gs_print$end(804)
        ## I1CMP:start
        pyxtnm76 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(76))
        return pyxtnm76
      ## endtimp(gs_print$end(804))
      pyxtnm78 = XATSDAPP(pyxtnm77())
      pyxtnm79 = pyxtnm78
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(79))
      return pyxtnm79
    ## endtimp(gs_print_a4(809))
    pyxtnm81 = XATSDAPP(pyxtnm80(pyxtnm29, XATSSTRN(": arg1 = "), pyxtnm30, XATSSTRN("\n")))
    pyxtnm82 = pyxtnm81
    XATS000_patck(True)
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2682(line=134,offs=1)--2710(line=134,offs=29)))
    ## I1VALDCL
    pyxtnm84 = None
    pyxtnm83 = XATSDAPP(pyxtnm28(pyxtnm30))
    pyxtnm84 = pyxtnm83
    XATS000_patck(True)
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2714(line=136,offs=1)--2759(line=137,offs=29)))
    ## I1VALDCL
    pyxtnm129 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2723(line=136,offs=10)--2730(line=136,offs=17))
    ## I0Etapq(I0Ecst(gs_print1_a4(1989)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3688(line=226,offs=1)--3700(line=226,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(r0[5967]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    ## T1IMPallx(gs_print1_a4(1989), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5678(line=285,offs=1)--5877(line=295,offs=21)))
    ## T1IMPallx(gs_print1_a4(1989)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8384],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8385],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[8386],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x3[8387],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a4(1989);$list(@(x0[5122],T2Pvar(x0[8384])),@(x1[5123],T2Pvar(x1[8385])),@(x2[5124],T2Pvar(x2[8386])),@(x3[5125],T2Pvar(x3[8387])))))))
    def pyxtnm127(arg1, arg2, arg3, arg4): ## timp: gs_print1_a4(1989)
      pyxtnm85 = arg1
      pyxtnm86 = arg2
      pyxtnm87 = arg3
      pyxtnm88 = arg4
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5763(line=292,offs=3)--5776(line=292,offs=16))
      ## I0Etapq(I0Ecst(gs_print1$beg(1972)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print1$beg(1972), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
      ## T1IMPallx(gs_print1$beg(1972)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$beg(1972);$list()))))
      def pyxtnm90(): ## timp: gs_print1$beg(1972)
        ## I1CMP:start
        pyxtnm89 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(89))
        return pyxtnm89
      ## endtimp(gs_print1$beg(1972))
      pyxtnm91 = XATSDAPP(pyxtnm90())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5784(line=293,offs=3)--5792(line=293,offs=11))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[8384])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm98 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm97 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm96(arg1): ## timp: strn_print(1040)
        pyxtnm92 = arg1
        ## I1CMP:start
        ## let
        pyxtnm95 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(93);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(93))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm94 = XATSDAPP(XATS2PY_strn_print(pyxtnm92))
        pyxtnm95 = pyxtnm94
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(95))
        return pyxtnm95
      ## endtimp(strn_print(1040))
      pyxtnm97 = pyxtnm96
      pyxtnm98 = pyxtnm97
      pyxtnm99 = XATSDAPP(pyxtnm98(pyxtnm85))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5802(line=293,offs=21)--5810(line=293,offs=29))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[8385])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm106 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm105 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm104(arg1): ## timp: strn_print(1040)
        pyxtnm100 = arg1
        ## I1CMP:start
        ## let
        pyxtnm103 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(101);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(101))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm102 = XATSDAPP(XATS2PY_strn_print(pyxtnm100))
        pyxtnm103 = pyxtnm102
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(103))
        return pyxtnm103
      ## endtimp(strn_print(1040))
      pyxtnm105 = pyxtnm104
      pyxtnm106 = pyxtnm105
      pyxtnm107 = XATSDAPP(pyxtnm106(pyxtnm86))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5821(line=294,offs=3)--5829(line=294,offs=11))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[8386])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm114 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
      pyxtnm113 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
      ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
      ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
      def pyxtnm112(arg1): ## timp: sint_print(922)
        pyxtnm108 = arg1
        ## I1CMP:start
        ## let
        pyxtnm111 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(109);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(109))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
        pyxtnm110 = XATSDAPP(XATS2PY_sint_print(pyxtnm108))
        pyxtnm111 = pyxtnm110
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(111))
        return pyxtnm111
      ## endtimp(sint_print(922))
      pyxtnm113 = pyxtnm112
      pyxtnm114 = pyxtnm113
      pyxtnm115 = XATSDAPP(pyxtnm114(pyxtnm87))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5839(line=294,offs=21)--5847(line=294,offs=29))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x3[8387])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm122 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm121 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm120(arg1): ## timp: strn_print(1040)
        pyxtnm116 = arg1
        ## I1CMP:start
        ## let
        pyxtnm119 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(117);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(117))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm118 = XATSDAPP(XATS2PY_strn_print(pyxtnm116))
        pyxtnm119 = pyxtnm118
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(119))
        return pyxtnm119
      ## endtimp(strn_print(1040))
      pyxtnm121 = pyxtnm120
      pyxtnm122 = pyxtnm121
      pyxtnm123 = XATSDAPP(pyxtnm122(pyxtnm88))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5859(line=295,offs=3)--5872(line=295,offs=16))
      ## I0Etapq(I0Ecst(gs_print1$end(1973)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print1$end(1973), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
      ## T1IMPallx(gs_print1$end(1973)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$end(1973);$list()))))
      def pyxtnm125(): ## timp: gs_print1$end(1973)
        ## I1CMP:start
        pyxtnm124 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(124))
        return pyxtnm124
      ## endtimp(gs_print1$end(1973))
      pyxtnm126 = XATSDAPP(pyxtnm125())
      ## I1CMP:return:I1Vtnm(I1TNM(126))
      return pyxtnm126
    ## endtimp(gs_print1_a4(1989))
    pyxtnm128 = XATSDAPP(pyxtnm127(pyxtnm29, XATSSTRN(": res0 = "), pyxtnm84, XATSSTRN("\n")))
    pyxtnm129 = pyxtnm128
    XATS000_patck(True)
    pyxtnm130 = pyxtnm84
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(130))
    return pyxtnm130
  ## } // end(lam0)
  ## I1CMP:return:I1Vtnm(I1TNM(131))
  return pyxtnm131
## endtimp(f1un_trace(316))
pyxtnm133 = XATSDAPP(pyxtnm132(fact_326, XATSSTRN("fact")))
pyxtnm134 = pyxtnm133
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(466(line=33,offs=1)--519(line=35,offs=31)))
## I1VALDCL
pyxtnm196 = None
## LCSRCsome1(test05_gdbg000.dats)@(481(line=34,offs=5)--519(line=35,offs=31))
## I0Etapq(I0Ecst(nint_foritm$f1un(964)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3054(line=146,offs=1)--3070(line=146,offs=17))));$list(T2JAG($list())))
## T1IMPallx(nint_foritm$f1un(964), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4008(line=237,offs=1)--4137(line=246,offs=2)))
## T1IMPallx(nint_foritm$f1un(964)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_foritm$f1un(964);$list()))))
def pyxtnm187(arg1, arg2): ## timp: nint_foritm$f1un(964)
  pyxtnm135 = arg1
  pyxtnm136 = arg2
  ## I1CMP:start
  ## let
  pyxtnm186 = None
  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4090(line=244,offs=1)--4135(line=245,offs=37)))
  ## I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(ni))))):timp
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4063(line=242,offs=3)--4074(line=242,offs=14))
  ## I0Etapq(I0Ecst(nint_foritm(962)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(2701(line=122,offs=1)--2712(line=122,offs=12))));$list(T2JAG($list())))
  ## T1IMPallx(nint_foritm(962), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3945(line=233,offs=1)--3999(line=236,offs=22)))
  ## T1IMPallx(nint_foritm(962)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_foritm(962);$list()))))
  pyxtnm184 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3978(line=236,offs=1)--3989(line=236,offs=12))
  ## I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  ## T1IMPallx(gseq_foritm(402), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
  ## T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
  def pyxtnm183(arg1): ## timp: gseq_foritm(402)
    pyxtnm139 = arg1
    ## I1CMP:start
    ## let
    pyxtnm182 = None
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
    ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
    ## let
    pyxtnm181 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
    ## I1VALDCL
    pyxtnm180 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
    ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
    ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3103(line=172,offs=1)--3149(line=173,offs=38)))
    ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(nint)),@(x0[1168],T2Pcst(ni)))))))
    pyxtnm178 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3136(line=173,offs=25)--3147(line=173,offs=36))
    ## I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
    ## T1IMPallx(nint_forall(958), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
    ## T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
    def pyxtnm177(arg1): ## timp: nint_forall(958)
      pyxtnm144 = arg1
      ## I1CMP:start
      ## let
      pyxtnm176 = None
      ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
      ## I1FUNDCL
      def loop_2862(arg1, arg2): ## fun
        pyxtnm145 = arg1
        pyxtnm146 = arg2
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
        ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
        ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
        ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
        def pyxtnm153(arg1, arg2): ## timp: sint_gte$sint(931)
          pyxtnm147 = arg1
          pyxtnm148 = arg2
          ## I1CMP:start
          ## let
          pyxtnm152 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(149);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(149))))),I1BNDcons(I1TNM(150);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(150))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
          pyxtnm151 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm147, pyxtnm148))
          pyxtnm152 = pyxtnm151
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(152))
          return pyxtnm152
        ## endtimp(sint_gte$sint(931))
        pyxtnm154 = XATSDAPP(pyxtnm153(pyxtnm146, pyxtnm145))
        pyxtnm174 = None
        if (pyxtnm154):
          pyxtnm174 = XATSBOOL(True)
        else:
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
          ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
          ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
          ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
          def pyxtnm162(arg1): ## timp: forall$test(47)
            pyxtnm155 = arg1
            ## I1CMP:start
            ## let
            pyxtnm161 = None
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
            ## I1VALDCL
            pyxtnm160 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
            ## I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
            ## T1IMPallx(foritm$work(51), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4090(line=244,offs=1)--4135(line=245,offs=37)))
            ## T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(ni)))))))
            def pyxtnm158(arg1): ## timp: foritm$work(51)
              pyxtnm156 = arg1
              ## I1CMP:start
              pyxtnm157 = XATSDAPP(pyxtnm136(pyxtnm156))
              ## I1CMP:return:I1Vtnm(I1TNM(157))
              return pyxtnm157
            ## endtimp(foritm$work(51))
            pyxtnm159 = XATSDAPP(pyxtnm158(pyxtnm155))
            pyxtnm160 = pyxtnm159
            XATS000_patck(True)
            pyxtnm161 = XATSBOOL(True)
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(161))
            return pyxtnm161
          ## endtimp(forall$test(47))
          pyxtnm163 = XATSDAPP(pyxtnm162(pyxtnm146))
          pyxtnm173 = None
          if (pyxtnm163):
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
            ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
            ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
            ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
            def pyxtnm170(arg1, arg2): ## timp: sint_add$sint(936)
              pyxtnm164 = arg1
              pyxtnm165 = arg2
              ## I1CMP:start
              ## let
              pyxtnm169 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(166);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(166))))),I1BNDcons(I1TNM(167);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(167))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
              pyxtnm168 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm164, pyxtnm165))
              pyxtnm169 = pyxtnm168
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(169))
              return pyxtnm169
            ## endtimp(sint_add$sint(936))
            pyxtnm171 = XATSDAPP(pyxtnm170(pyxtnm146, XATSINT1(1)))
            pyxtnm172 = XATSDAPP(loop_2862(pyxtnm145, pyxtnm171))
            pyxtnm173 = pyxtnm172
          else:
            pyxtnm173 = XATSBOOL(False)
          ## end-of(if)
          pyxtnm174 = pyxtnm173
        ## end-of(if)
        ## I1CMP:return:I1Vtnm(I1TNM(174))
        return pyxtnm174
      pyxtnm175 = XATSDAPP(loop_2862(pyxtnm144, XATSINT1(0)))
      pyxtnm176 = pyxtnm175
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(176))
      return pyxtnm176
    ## endtimp(nint_forall(958))
    pyxtnm178 = pyxtnm177
    pyxtnm179 = XATSDAPP(pyxtnm178(pyxtnm139))
    pyxtnm180 = pyxtnm179
    XATS000_patck(True)
    pyxtnm181 = XATSVOID
    ## end-of(let)
    pyxtnm182 = pyxtnm181
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(182))
    return pyxtnm182
  ## endtimp(gseq_foritm(402))
  pyxtnm184 = pyxtnm183
  pyxtnm185 = XATSDAPP(pyxtnm184(pyxtnm135))
  pyxtnm186 = pyxtnm185
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(186))
  return pyxtnm186
## endtimp(nint_foritm$f1un(964))
def pyxtnm194(arg1): ## { // lam0(T_LAM(0))
  pyxtnm188 = arg1
  ## I1CMP:start
  ## LCSRCsome1(test05_gdbg000.dats)@(503(line=35,offs=15)--509(line=35,offs=21))
  ## I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  ## T1IMPallx(g_void(22), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
  ## T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
  def pyxtnm191(arg1): ## timp: g_void(22)
    pyxtnm189 = arg1
    ## I1CMP:start
    pyxtnm190 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(190))
    return pyxtnm190
  ## endtimp(g_void(22))
  pyxtnm192 = XATSDAPP(pyxtnm134(pyxtnm188))
  pyxtnm193 = XATSDAPP(pyxtnm191(pyxtnm192))
  ## I1CMP:return:I1Vtnm(I1TNM(193))
  return pyxtnm193
## } // end(lam0)
pyxtnm195 = XATSDAPP(pyxtnm187(XATSINT1(20), pyxtnm194))
pyxtnm196 = pyxtnm195
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(566(line=40,offs=1)--619(line=42,offs=36)))
## I1VALDCL
pyxtnm533 = None
## LCSRCsome1(test05_gdbg000.dats)@(584(line=42,offs=1)--589(line=42,offs=6))
## I0Etapq(I0Ecst(f2un_trace(317)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gfun000.sats)@(3536(line=196,offs=1)--3546(line=196,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(f2un_trace(317), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2796(line=141,offs=1)--3068(line=158,offs=39)))
## T1IMPallx(f2un_trace(317)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(a1[5968],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(a2[5969],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(r0[5970],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(f2un_trace(317);$list(@(a1[988],T2Pvar(a1[5968])),@(a2[989],T2Pvar(a2[5969])),@(r0[990],T2Pvar(r0[5970])))))))
def pyxtnm354(arg1, arg2): ## timp: f2un_trace(317)
  pyxtnm197 = arg1
  pyxtnm198 = arg2
  ## I1CMP:start
  def pyxtnm353(arg1, arg2): ## { // lam0(T_LAM(0))
    pyxtnm199 = arg1
    pyxtnm200 = arg2
    ## I1CMP:start
    ## let
    pyxtnm352 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2888(line=150,offs=1)--2932(line=151,offs=29)))
    ## I1VALDCL
    pyxtnm252 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2897(line=150,offs=10)--2903(line=150,offs=16))
    ## I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(a1[5968]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    ## T1IMPallx(gs_print_a4(809), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
    ## T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
    def pyxtnm250(arg1, arg2, arg3, arg4): ## timp: gs_print_a4(809)
      pyxtnm201 = arg1
      pyxtnm202 = arg2
      pyxtnm203 = arg3
      pyxtnm204 = arg4
      ## I1CMP:start
      ## let
      pyxtnm249 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
      ## I1VALDCL
      pyxtnm208 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
      ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      def pyxtnm206(): ## timp: gs_print$beg(802)
        ## I1CMP:start
        pyxtnm205 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(205))
        return pyxtnm205
      ## endtimp(gs_print$beg(802))
      pyxtnm207 = XATSDAPP(pyxtnm206())
      pyxtnm208 = pyxtnm207
      XATS000_patck(True)
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm214 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm213(arg1): ## timp: strn_print(1040)
        pyxtnm209 = arg1
        ## I1CMP:start
        ## let
        pyxtnm212 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(210);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(210))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm211 = XATSDAPP(XATS2PY_strn_print(pyxtnm209))
        pyxtnm212 = pyxtnm211
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(212))
        return pyxtnm212
      ## endtimp(strn_print(1040))
      pyxtnm214 = pyxtnm213
      pyxtnm215 = XATSDAPP(pyxtnm214(pyxtnm201))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm217(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm216 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(216))
        return pyxtnm216
      ## endtimp(gs_print$sep(803))
      pyxtnm218 = XATSDAPP(pyxtnm217())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm224 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm223(arg1): ## timp: strn_print(1040)
        pyxtnm219 = arg1
        ## I1CMP:start
        ## let
        pyxtnm222 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(220);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(220))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm221 = XATSDAPP(XATS2PY_strn_print(pyxtnm219))
        pyxtnm222 = pyxtnm221
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(222))
        return pyxtnm222
      ## endtimp(strn_print(1040))
      pyxtnm224 = pyxtnm223
      pyxtnm225 = XATSDAPP(pyxtnm224(pyxtnm202))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm227(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm226 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(226))
        return pyxtnm226
      ## endtimp(gs_print$sep(803))
      pyxtnm228 = XATSDAPP(pyxtnm227())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm234 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm233(arg1): ## timp: strn_print(1040)
        pyxtnm229 = arg1
        ## I1CMP:start
        ## let
        pyxtnm232 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(230);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(230))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm231 = XATSDAPP(XATS2PY_strn_print(pyxtnm229))
        pyxtnm232 = pyxtnm231
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(232))
        return pyxtnm232
      ## endtimp(strn_print(1040))
      pyxtnm234 = pyxtnm233
      pyxtnm235 = XATSDAPP(pyxtnm234(pyxtnm203))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm237(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm236 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(236))
        return pyxtnm236
      ## endtimp(gs_print$sep(803))
      pyxtnm238 = XATSDAPP(pyxtnm237())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm244 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm243(arg1): ## timp: strn_print(1040)
        pyxtnm239 = arg1
        ## I1CMP:start
        ## let
        pyxtnm242 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(240);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(240))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm241 = XATSDAPP(XATS2PY_strn_print(pyxtnm239))
        pyxtnm242 = pyxtnm241
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(242))
        return pyxtnm242
      ## endtimp(strn_print(1040))
      pyxtnm244 = pyxtnm243
      pyxtnm245 = XATSDAPP(pyxtnm244(pyxtnm204))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
      ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      def pyxtnm247(): ## timp: gs_print$end(804)
        ## I1CMP:start
        pyxtnm246 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(246))
        return pyxtnm246
      ## endtimp(gs_print$end(804))
      pyxtnm248 = XATSDAPP(pyxtnm247())
      pyxtnm249 = pyxtnm248
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(249))
      return pyxtnm249
    ## endtimp(gs_print_a4(809))
    pyxtnm251 = XATSDAPP(pyxtnm250(pyxtnm198, XATSSTRN(": arg1 = "), pyxtnm199, XATSSTRN("\n")))
    pyxtnm252 = pyxtnm251
    XATS000_patck(True)
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2933(line=152,offs=1)--2977(line=153,offs=29)))
    ## I1VALDCL
    pyxtnm304 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2942(line=152,offs=10)--2948(line=152,offs=16))
    ## I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(a2[5969]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    ## T1IMPallx(gs_print_a4(809), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
    ## T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
    def pyxtnm302(arg1, arg2, arg3, arg4): ## timp: gs_print_a4(809)
      pyxtnm253 = arg1
      pyxtnm254 = arg2
      pyxtnm255 = arg3
      pyxtnm256 = arg4
      ## I1CMP:start
      ## let
      pyxtnm301 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
      ## I1VALDCL
      pyxtnm260 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
      ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      def pyxtnm258(): ## timp: gs_print$beg(802)
        ## I1CMP:start
        pyxtnm257 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(257))
        return pyxtnm257
      ## endtimp(gs_print$beg(802))
      pyxtnm259 = XATSDAPP(pyxtnm258())
      pyxtnm260 = pyxtnm259
      XATS000_patck(True)
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm266 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm265(arg1): ## timp: strn_print(1040)
        pyxtnm261 = arg1
        ## I1CMP:start
        ## let
        pyxtnm264 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(262);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(262))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm263 = XATSDAPP(XATS2PY_strn_print(pyxtnm261))
        pyxtnm264 = pyxtnm263
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(264))
        return pyxtnm264
      ## endtimp(strn_print(1040))
      pyxtnm266 = pyxtnm265
      pyxtnm267 = XATSDAPP(pyxtnm266(pyxtnm253))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm269(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm268 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(268))
        return pyxtnm268
      ## endtimp(gs_print$sep(803))
      pyxtnm270 = XATSDAPP(pyxtnm269())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm276 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm275(arg1): ## timp: strn_print(1040)
        pyxtnm271 = arg1
        ## I1CMP:start
        ## let
        pyxtnm274 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(272);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(272))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm273 = XATSDAPP(XATS2PY_strn_print(pyxtnm271))
        pyxtnm274 = pyxtnm273
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(274))
        return pyxtnm274
      ## endtimp(strn_print(1040))
      pyxtnm276 = pyxtnm275
      pyxtnm277 = XATSDAPP(pyxtnm276(pyxtnm254))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm279(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm278 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(278))
        return pyxtnm278
      ## endtimp(gs_print$sep(803))
      pyxtnm280 = XATSDAPP(pyxtnm279())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm286 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
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
      pyxtnm286 = pyxtnm285
      pyxtnm287 = XATSDAPP(pyxtnm286(pyxtnm255))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
      ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      def pyxtnm289(): ## timp: gs_print$sep(803)
        ## I1CMP:start
        pyxtnm288 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(288))
        return pyxtnm288
      ## endtimp(gs_print$sep(803))
      pyxtnm290 = XATSDAPP(pyxtnm289())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm296 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm295(arg1): ## timp: strn_print(1040)
        pyxtnm291 = arg1
        ## I1CMP:start
        ## let
        pyxtnm294 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(292);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(292))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm293 = XATSDAPP(XATS2PY_strn_print(pyxtnm291))
        pyxtnm294 = pyxtnm293
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(294))
        return pyxtnm294
      ## endtimp(strn_print(1040))
      pyxtnm296 = pyxtnm295
      pyxtnm297 = XATSDAPP(pyxtnm296(pyxtnm256))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
      ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      def pyxtnm299(): ## timp: gs_print$end(804)
        ## I1CMP:start
        pyxtnm298 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(298))
        return pyxtnm298
      ## endtimp(gs_print$end(804))
      pyxtnm300 = XATSDAPP(pyxtnm299())
      pyxtnm301 = pyxtnm300
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(301))
      return pyxtnm301
    ## endtimp(gs_print_a4(809))
    pyxtnm303 = XATSDAPP(pyxtnm302(pyxtnm198, XATSSTRN(": arg2 = "), pyxtnm200, XATSSTRN("\n")))
    pyxtnm304 = pyxtnm303
    XATS000_patck(True)
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2981(line=155,offs=1)--3009(line=155,offs=29)))
    ## I1VALDCL
    pyxtnm306 = None
    pyxtnm305 = XATSDAPP(pyxtnm197(pyxtnm199, pyxtnm200))
    pyxtnm306 = pyxtnm305
    XATS000_patck(True)
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(3013(line=157,offs=1)--3058(line=158,offs=29)))
    ## I1VALDCL
    pyxtnm351 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(3022(line=157,offs=10)--3029(line=157,offs=17))
    ## I0Etapq(I0Ecst(gs_print1_a4(1989)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3688(line=226,offs=1)--3700(line=226,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(r0[5970]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    ## T1IMPallx(gs_print1_a4(1989), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5678(line=285,offs=1)--5877(line=295,offs=21)))
    ## T1IMPallx(gs_print1_a4(1989)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8384],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8385],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[8386],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[8387],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a4(1989);$list(@(x0[5122],T2Pvar(x0[8384])),@(x1[5123],T2Pvar(x1[8385])),@(x2[5124],T2Pvar(x2[8386])),@(x3[5125],T2Pvar(x3[8387])))))))
    def pyxtnm349(arg1, arg2, arg3, arg4): ## timp: gs_print1_a4(1989)
      pyxtnm307 = arg1
      pyxtnm308 = arg2
      pyxtnm309 = arg3
      pyxtnm310 = arg4
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5763(line=292,offs=3)--5776(line=292,offs=16))
      ## I0Etapq(I0Ecst(gs_print1$beg(1972)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print1$beg(1972), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
      ## T1IMPallx(gs_print1$beg(1972)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$beg(1972);$list()))))
      def pyxtnm312(): ## timp: gs_print1$beg(1972)
        ## I1CMP:start
        pyxtnm311 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(311))
        return pyxtnm311
      ## endtimp(gs_print1$beg(1972))
      pyxtnm313 = XATSDAPP(pyxtnm312())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5784(line=293,offs=3)--5792(line=293,offs=11))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[8384])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm320 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm319 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm318(arg1): ## timp: strn_print(1040)
        pyxtnm314 = arg1
        ## I1CMP:start
        ## let
        pyxtnm317 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(315);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(315))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm316 = XATSDAPP(XATS2PY_strn_print(pyxtnm314))
        pyxtnm317 = pyxtnm316
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(317))
        return pyxtnm317
      ## endtimp(strn_print(1040))
      pyxtnm319 = pyxtnm318
      pyxtnm320 = pyxtnm319
      pyxtnm321 = XATSDAPP(pyxtnm320(pyxtnm307))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5802(line=293,offs=21)--5810(line=293,offs=29))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[8385])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm328 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm327 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm326(arg1): ## timp: strn_print(1040)
        pyxtnm322 = arg1
        ## I1CMP:start
        ## let
        pyxtnm325 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(323);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(323))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm324 = XATSDAPP(XATS2PY_strn_print(pyxtnm322))
        pyxtnm325 = pyxtnm324
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(325))
        return pyxtnm325
      ## endtimp(strn_print(1040))
      pyxtnm327 = pyxtnm326
      pyxtnm328 = pyxtnm327
      pyxtnm329 = XATSDAPP(pyxtnm328(pyxtnm308))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5821(line=294,offs=3)--5829(line=294,offs=11))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[8386])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm336 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm335 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm334(arg1): ## timp: strn_print(1040)
        pyxtnm330 = arg1
        ## I1CMP:start
        ## let
        pyxtnm333 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(331);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(331))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm332 = XATSDAPP(XATS2PY_strn_print(pyxtnm330))
        pyxtnm333 = pyxtnm332
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(333))
        return pyxtnm333
      ## endtimp(strn_print(1040))
      pyxtnm335 = pyxtnm334
      pyxtnm336 = pyxtnm335
      pyxtnm337 = XATSDAPP(pyxtnm336(pyxtnm309))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5839(line=294,offs=21)--5847(line=294,offs=29))
      ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x3[8387])))))
      ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
      ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
      pyxtnm344 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      pyxtnm343 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm342(arg1): ## timp: strn_print(1040)
        pyxtnm338 = arg1
        ## I1CMP:start
        ## let
        pyxtnm341 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(339);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(339))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm340 = XATSDAPP(XATS2PY_strn_print(pyxtnm338))
        pyxtnm341 = pyxtnm340
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(341))
        return pyxtnm341
      ## endtimp(strn_print(1040))
      pyxtnm343 = pyxtnm342
      pyxtnm344 = pyxtnm343
      pyxtnm345 = XATSDAPP(pyxtnm344(pyxtnm310))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5859(line=295,offs=3)--5872(line=295,offs=16))
      ## I0Etapq(I0Ecst(gs_print1$end(1973)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(gs_print1$end(1973), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
      ## T1IMPallx(gs_print1$end(1973)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$end(1973);$list()))))
      def pyxtnm347(): ## timp: gs_print1$end(1973)
        ## I1CMP:start
        pyxtnm346 = XATSTUP0([])
        ## I1CMP:return:I1Vtnm(I1TNM(346))
        return pyxtnm346
      ## endtimp(gs_print1$end(1973))
      pyxtnm348 = XATSDAPP(pyxtnm347())
      ## I1CMP:return:I1Vtnm(I1TNM(348))
      return pyxtnm348
    ## endtimp(gs_print1_a4(1989))
    pyxtnm350 = XATSDAPP(pyxtnm349(pyxtnm198, XATSSTRN(": res0 = "), pyxtnm306, XATSSTRN("\n")))
    pyxtnm351 = pyxtnm350
    XATS000_patck(True)
    pyxtnm352 = pyxtnm306
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(352))
    return pyxtnm352
  ## } // end(lam0)
  ## I1CMP:return:I1Vtnm(I1TNM(353))
  return pyxtnm353
## endtimp(f2un_trace(317))
## LCSRCsome1(test05_gdbg000.dats)@(590(line=42,offs=7)--601(line=42,offs=18))
## I0Etapq(I0Ecst(strn_append(1063)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(5650(line=339,offs=1)--5661(line=339,offs=12))));$list(T2JAG($list())))
## T1IMPallx(strn_append(1063), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3415(line=190,offs=1)--3529(line=197,offs=38)))
## T1IMPallx(strn_append(1063)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_append(1063);$list()))))
def pyxtnm531(arg1, arg2): ## timp: strn_append(1063)
  pyxtnm355 = arg1
  pyxtnm356 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3459(line=194,offs=1)--3474(line=194,offs=16))
  ## I0Etapq(I0Ecst(strn_make_fwork(1090)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(4102(line=185,offs=1)--4117(line=185,offs=16))));$list(T2JAG($list())))
  ## T1IMPallx(strn_make_fwork(1090), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2479(line=126,offs=1)--2658(line=139,offs=2)))
  ## T1IMPallx(strn_make_fwork(1090)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_make_fwork(1090);$list()))))
  def pyxtnm361(arg1): ## timp: strn_make_fwork(1090)
    pyxtnm357 = arg1
    ## I1CMP:start
    ## let
    pyxtnm360 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2571(line=134,offs=1)--2656(line=138,offs=42)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS000_strn_make_fwork(2527));$list(I1FUNDCL(XATS000_strn_make_fwork(3302);$list(FJARGdarg($list(I1BNDcons(I1TNM(358);I0Pvar(fwork(3303));$list(@(fwork(3303),I1Vtnm(I1TNM(358))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS000_strn_make_fwork);G1Nlist($list())))))))
    pyxtnm359 = XATSDAPP(XATS000_strn_make_fwork(pyxtnm357))
    pyxtnm360 = pyxtnm359
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(360))
    return pyxtnm360
  ## endtimp(strn_make_fwork(1090))
  def pyxtnm529(arg1): ## { // lam0(T_LAM(0))
    pyxtnm362 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3493(line=197,offs=2)--3499(line=197,offs=8))
    ## I0Etapq(I0Ecst(strn_foritm$f1un(1086)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3510(line=153,offs=1)--3526(line=153,offs=17))));$list(T2JAG($list())))
    ## T1IMPallx(strn_foritm$f1un(1086), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3971(line=237,offs=1)--4096(line=246,offs=2)))
    ## T1IMPallx(strn_foritm$f1un(1086)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm$f1un(1086);$list()))))
    def pyxtnm444(arg1, arg2): ## timp: strn_foritm$f1un(1086)
      pyxtnm363 = arg1
      pyxtnm364 = arg2
      ## I1CMP:start
      ## let
      pyxtnm443 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
      ## I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4026(line=242,offs=3)--4037(line=242,offs=14))
      ## I0Etapq(I0Ecst(strn_foritm(1082)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3113(line=132,offs=1)--3124(line=132,offs=12))));$list(T2JAG($list())))
      ## T1IMPallx(strn_foritm(1082), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3914(line=233,offs=1)--3970(line=236,offs=24)))
      ## T1IMPallx(strn_foritm(1082)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm(1082);$list()))))
      pyxtnm441 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3947(line=236,offs=1)--3958(line=236,offs=12))
      ## I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
      ## T1IMPallx(gseq_foritm(402), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
      ## T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
      def pyxtnm440(arg1): ## timp: gseq_foritm(402)
        pyxtnm367 = arg1
        ## I1CMP:start
        ## let
        pyxtnm439 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
        ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
        ## let
        pyxtnm438 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
        ## I1VALDCL
        pyxtnm437 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
        ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
        ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1976(line=85,offs=1)--2025(line=87,offs=29)))
        ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(strn)),@(x0[1168],T2Pcst(cgtz)))))))
        pyxtnm435 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(2012(line=87,offs=16)--2023(line=87,offs=27))
        ## I0Etapq(I0Ecst(strn_forall(1074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(2101(line=80,offs=1)--2112(line=80,offs=12))));$list(T2JAG($list())))
        ## T1IMPallx(strn_forall(1074), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1556(line=51,offs=1)--1772(line=72,offs=2)))
        ## T1IMPallx(strn_forall(1074)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_forall(1074);$list()))))
        def pyxtnm434(arg1): ## timp: strn_forall(1074)
          pyxtnm372 = arg1
          ## I1CMP:start
          ## let
          pyxtnm433 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1627(line=59,offs=1)--1658(line=61,offs=21)))
          ## I1VALDCL
          pyxtnm379 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1640(line=61,offs=3)--1651(line=61,offs=14))
          ## I0Etapq(I0Ecst(strn_length(1041)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2709(line=131,offs=1)--2720(line=131,offs=12))));$list(T2JAG($list())))
          ## T1IMPallx(strn_length(1041), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1430(line=40,offs=1)--1576(line=52,offs=2)))
          ## T1IMPallx(strn_length(1041)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_length(1041);$list()))))
          def pyxtnm377(arg1): ## timp: strn_length(1041)
            pyxtnm373 = arg1
            ## I1CMP:start
            ## let
            pyxtnm376 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1512(line=48,offs=1)--1574(line=51,offs=31)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_length(2646));$list(I1FUNDCL(XATS2PY_strn_length(5003);$list(FJARGdarg($list(I1BNDcons(I1TNM(374);I0Pvar(cs(5004));$list(@(cs(5004),I1Vtnm(I1TNM(374))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_length);G1Nlist($list())))))))
            pyxtnm375 = XATSDAPP(XATS2PY_strn_length(pyxtnm373))
            pyxtnm376 = pyxtnm375
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(376))
            return pyxtnm376
          ## endtimp(strn_length(1041))
          pyxtnm378 = XATSDAPP(pyxtnm377(pyxtnm372))
          pyxtnm379 = pyxtnm378
          XATS000_patck(True)
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
          ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1597(line=55,offs=3)--1608(line=55,offs=14))
          ## I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
          ## T1IMPallx(nint_forall(958), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
          ## T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
          def pyxtnm431(arg1): ## timp: nint_forall(958)
            pyxtnm385 = arg1
            ## I1CMP:start
            ## let
            pyxtnm430 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
            ## I1FUNDCL
            def loop_2862(arg1, arg2): ## fun
              pyxtnm386 = arg1
              pyxtnm387 = arg2
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
              ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
              ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
              ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
              def pyxtnm394(arg1, arg2): ## timp: sint_gte$sint(931)
                pyxtnm388 = arg1
                pyxtnm389 = arg2
                ## I1CMP:start
                ## let
                pyxtnm393 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(390);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(390))))),I1BNDcons(I1TNM(391);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(391))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                pyxtnm392 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm388, pyxtnm389))
                pyxtnm393 = pyxtnm392
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(393))
                return pyxtnm393
              ## endtimp(sint_gte$sint(931))
              pyxtnm395 = XATSDAPP(pyxtnm394(pyxtnm387, pyxtnm386))
              pyxtnm428 = None
              if (pyxtnm395):
                pyxtnm428 = XATSBOOL(True)
              else:
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
                ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                def pyxtnm416(arg1): ## timp: forall$test(47)
                  pyxtnm396 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm415 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1728(line=69,offs=1)--1768(line=70,offs=32)))
                  ## I1VALDCL
                  pyxtnm405 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1743(line=70,offs=7)--1758(line=70,offs=22))
                  ## I0Etapq(I0Ecst(strn_get$at$raw(2330)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4484(line=273,offs=1)--4499(line=273,offs=16))));$list(T2JAG($list())))
                  ## T1IMPallx(strn_get$at$raw(2330), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2200(line=104,offs=1)--2376(line=116,offs=2)))
                  ## T1IMPallx(strn_get$at$raw(2330)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_get$at$raw(2330);$list()))))
                  def pyxtnm403(arg1, arg2): ## timp: strn_get$at$raw(2330)
                    pyxtnm397 = arg1
                    pyxtnm398 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm402 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2298(line=112,offs=1)--2374(line=115,offs=41)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS000_strn_get$at$raw(2526));$list(I1FUNDCL(XATS000_strn_get$at$raw(3298);$list(FJARGdarg($list(I1BNDcons(I1TNM(399);I0Pvar(cs(3299));$list(@(cs(3299),I1Vtnm(I1TNM(399))))),I1BNDcons(I1TNM(400);I0Pvar(i0(3300));$list(@(i0(3300),I1Vtnm(I1TNM(400))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS000_strn_get$at$raw);G1Nlist($list())))))))
                    pyxtnm401 = XATSDAPP(XATS000_strn_get_at_raw(pyxtnm397, pyxtnm398))
                    pyxtnm402 = pyxtnm401
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(402))
                    return pyxtnm402
                  ## endtimp(strn_get$at$raw(2330))
                  pyxtnm404 = XATSDAPP(pyxtnm403(pyxtnm372, pyxtnm396))
                  pyxtnm405 = pyxtnm404
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1697(line=66,offs=3)--1708(line=66,offs=14))
                  ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
                  ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                  ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))))
                  def pyxtnm413(arg1): ## timp: forall$test(47)
                    pyxtnm406 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm412 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                    ## I1VALDCL
                    pyxtnm411 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                    ## I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                    ## T1IMPallx(foritm$work(51), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
                    ## T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz)))))))
                    def pyxtnm409(arg1): ## timp: foritm$work(51)
                      pyxtnm407 = arg1
                      ## I1CMP:start
                      pyxtnm408 = XATSDAPP(pyxtnm364(pyxtnm407))
                      ## I1CMP:return:I1Vtnm(I1TNM(408))
                      return pyxtnm408
                    ## endtimp(foritm$work(51))
                    pyxtnm410 = XATSDAPP(pyxtnm409(pyxtnm406))
                    pyxtnm411 = pyxtnm410
                    XATS000_patck(True)
                    pyxtnm412 = XATSBOOL(True)
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(412))
                    return pyxtnm412
                  ## endtimp(forall$test(47))
                  pyxtnm414 = XATSDAPP(pyxtnm413(pyxtnm405))
                  pyxtnm415 = pyxtnm414
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(415))
                  return pyxtnm415
                ## endtimp(forall$test(47))
                pyxtnm417 = XATSDAPP(pyxtnm416(pyxtnm387))
                pyxtnm427 = None
                if (pyxtnm417):
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                  ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                  ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                  def pyxtnm424(arg1, arg2): ## timp: sint_add$sint(936)
                    pyxtnm418 = arg1
                    pyxtnm419 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm423 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(420);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(420))))),I1BNDcons(I1TNM(421);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(421))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                    pyxtnm422 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm418, pyxtnm419))
                    pyxtnm423 = pyxtnm422
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(423))
                    return pyxtnm423
                  ## endtimp(sint_add$sint(936))
                  pyxtnm425 = XATSDAPP(pyxtnm424(pyxtnm387, XATSINT1(1)))
                  pyxtnm426 = XATSDAPP(loop_2862(pyxtnm386, pyxtnm425))
                  pyxtnm427 = pyxtnm426
                else:
                  pyxtnm427 = XATSBOOL(False)
                ## end-of(if)
                pyxtnm428 = pyxtnm427
              ## end-of(if)
              ## I1CMP:return:I1Vtnm(I1TNM(428))
              return pyxtnm428
            pyxtnm429 = XATSDAPP(loop_2862(pyxtnm385, XATSINT1(0)))
            pyxtnm430 = pyxtnm429
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(430))
            return pyxtnm430
          ## endtimp(nint_forall(958))
          pyxtnm432 = XATSDAPP(pyxtnm431(pyxtnm379))
          pyxtnm433 = pyxtnm432
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(433))
          return pyxtnm433
        ## endtimp(strn_forall(1074))
        pyxtnm435 = pyxtnm434
        pyxtnm436 = XATSDAPP(pyxtnm435(pyxtnm367))
        pyxtnm437 = pyxtnm436
        XATS000_patck(True)
        pyxtnm438 = XATSVOID
        ## end-of(let)
        pyxtnm439 = pyxtnm438
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(439))
        return pyxtnm439
      ## endtimp(gseq_foritm(402))
      pyxtnm441 = pyxtnm440
      pyxtnm442 = XATSDAPP(pyxtnm441(pyxtnm363))
      pyxtnm443 = pyxtnm442
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(443))
      return pyxtnm443
    ## endtimp(strn_foritm$f1un(1086))
    pyxtnm445 = XATSDAPP(pyxtnm444(pyxtnm355, pyxtnm362))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3511(line=197,offs=20)--3517(line=197,offs=26))
    ## I0Etapq(I0Ecst(strn_foritm$f1un(1086)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3510(line=153,offs=1)--3526(line=153,offs=17))));$list(T2JAG($list())))
    ## T1IMPallx(strn_foritm$f1un(1086), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3971(line=237,offs=1)--4096(line=246,offs=2)))
    ## T1IMPallx(strn_foritm$f1un(1086)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm$f1un(1086);$list()))))
    def pyxtnm527(arg1, arg2): ## timp: strn_foritm$f1un(1086)
      pyxtnm446 = arg1
      pyxtnm447 = arg2
      ## I1CMP:start
      ## let
      pyxtnm526 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
      ## I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4026(line=242,offs=3)--4037(line=242,offs=14))
      ## I0Etapq(I0Ecst(strn_foritm(1082)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3113(line=132,offs=1)--3124(line=132,offs=12))));$list(T2JAG($list())))
      ## T1IMPallx(strn_foritm(1082), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3914(line=233,offs=1)--3970(line=236,offs=24)))
      ## T1IMPallx(strn_foritm(1082)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm(1082);$list()))))
      pyxtnm524 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3947(line=236,offs=1)--3958(line=236,offs=12))
      ## I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
      ## T1IMPallx(gseq_foritm(402), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
      ## T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
      def pyxtnm523(arg1): ## timp: gseq_foritm(402)
        pyxtnm450 = arg1
        ## I1CMP:start
        ## let
        pyxtnm522 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
        ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
        ## let
        pyxtnm521 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
        ## I1VALDCL
        pyxtnm520 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
        ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
        ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1976(line=85,offs=1)--2025(line=87,offs=29)))
        ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(strn)),@(x0[1168],T2Pcst(cgtz)))))))
        pyxtnm518 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(2012(line=87,offs=16)--2023(line=87,offs=27))
        ## I0Etapq(I0Ecst(strn_forall(1074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(2101(line=80,offs=1)--2112(line=80,offs=12))));$list(T2JAG($list())))
        ## T1IMPallx(strn_forall(1074), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1556(line=51,offs=1)--1772(line=72,offs=2)))
        ## T1IMPallx(strn_forall(1074)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_forall(1074);$list()))))
        def pyxtnm517(arg1): ## timp: strn_forall(1074)
          pyxtnm455 = arg1
          ## I1CMP:start
          ## let
          pyxtnm516 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1627(line=59,offs=1)--1658(line=61,offs=21)))
          ## I1VALDCL
          pyxtnm462 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1640(line=61,offs=3)--1651(line=61,offs=14))
          ## I0Etapq(I0Ecst(strn_length(1041)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2709(line=131,offs=1)--2720(line=131,offs=12))));$list(T2JAG($list())))
          ## T1IMPallx(strn_length(1041), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1430(line=40,offs=1)--1576(line=52,offs=2)))
          ## T1IMPallx(strn_length(1041)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_length(1041);$list()))))
          def pyxtnm460(arg1): ## timp: strn_length(1041)
            pyxtnm456 = arg1
            ## I1CMP:start
            ## let
            pyxtnm459 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1512(line=48,offs=1)--1574(line=51,offs=31)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_length(2646));$list(I1FUNDCL(XATS2PY_strn_length(5003);$list(FJARGdarg($list(I1BNDcons(I1TNM(457);I0Pvar(cs(5004));$list(@(cs(5004),I1Vtnm(I1TNM(457))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_length);G1Nlist($list())))))))
            pyxtnm458 = XATSDAPP(XATS2PY_strn_length(pyxtnm456))
            pyxtnm459 = pyxtnm458
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(459))
            return pyxtnm459
          ## endtimp(strn_length(1041))
          pyxtnm461 = XATSDAPP(pyxtnm460(pyxtnm455))
          pyxtnm462 = pyxtnm461
          XATS000_patck(True)
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
          ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1597(line=55,offs=3)--1608(line=55,offs=14))
          ## I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
          ## T1IMPallx(nint_forall(958), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
          ## T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
          def pyxtnm514(arg1): ## timp: nint_forall(958)
            pyxtnm468 = arg1
            ## I1CMP:start
            ## let
            pyxtnm513 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
            ## I1FUNDCL
            def loop_2862(arg1, arg2): ## fun
              pyxtnm469 = arg1
              pyxtnm470 = arg2
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
              ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
              ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
              ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
              def pyxtnm477(arg1, arg2): ## timp: sint_gte$sint(931)
                pyxtnm471 = arg1
                pyxtnm472 = arg2
                ## I1CMP:start
                ## let
                pyxtnm476 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(473);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(473))))),I1BNDcons(I1TNM(474);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(474))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                pyxtnm475 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm471, pyxtnm472))
                pyxtnm476 = pyxtnm475
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(476))
                return pyxtnm476
              ## endtimp(sint_gte$sint(931))
              pyxtnm478 = XATSDAPP(pyxtnm477(pyxtnm470, pyxtnm469))
              pyxtnm511 = None
              if (pyxtnm478):
                pyxtnm511 = XATSBOOL(True)
              else:
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
                ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                def pyxtnm499(arg1): ## timp: forall$test(47)
                  pyxtnm479 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm498 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1728(line=69,offs=1)--1768(line=70,offs=32)))
                  ## I1VALDCL
                  pyxtnm488 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1743(line=70,offs=7)--1758(line=70,offs=22))
                  ## I0Etapq(I0Ecst(strn_get$at$raw(2330)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4484(line=273,offs=1)--4499(line=273,offs=16))));$list(T2JAG($list())))
                  ## T1IMPallx(strn_get$at$raw(2330), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2200(line=104,offs=1)--2376(line=116,offs=2)))
                  ## T1IMPallx(strn_get$at$raw(2330)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_get$at$raw(2330);$list()))))
                  def pyxtnm486(arg1, arg2): ## timp: strn_get$at$raw(2330)
                    pyxtnm480 = arg1
                    pyxtnm481 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm485 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2298(line=112,offs=1)--2374(line=115,offs=41)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS000_strn_get$at$raw(2526));$list(I1FUNDCL(XATS000_strn_get$at$raw(3298);$list(FJARGdarg($list(I1BNDcons(I1TNM(482);I0Pvar(cs(3299));$list(@(cs(3299),I1Vtnm(I1TNM(482))))),I1BNDcons(I1TNM(483);I0Pvar(i0(3300));$list(@(i0(3300),I1Vtnm(I1TNM(483))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS000_strn_get$at$raw);G1Nlist($list())))))))
                    pyxtnm484 = XATSDAPP(XATS000_strn_get_at_raw(pyxtnm480, pyxtnm481))
                    pyxtnm485 = pyxtnm484
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(485))
                    return pyxtnm485
                  ## endtimp(strn_get$at$raw(2330))
                  pyxtnm487 = XATSDAPP(pyxtnm486(pyxtnm455, pyxtnm479))
                  pyxtnm488 = pyxtnm487
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1697(line=66,offs=3)--1708(line=66,offs=14))
                  ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
                  ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                  ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))))
                  def pyxtnm496(arg1): ## timp: forall$test(47)
                    pyxtnm489 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm495 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                    ## I1VALDCL
                    pyxtnm494 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                    ## I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                    ## T1IMPallx(foritm$work(51), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
                    ## T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz)))))))
                    def pyxtnm492(arg1): ## timp: foritm$work(51)
                      pyxtnm490 = arg1
                      ## I1CMP:start
                      pyxtnm491 = XATSDAPP(pyxtnm447(pyxtnm490))
                      ## I1CMP:return:I1Vtnm(I1TNM(491))
                      return pyxtnm491
                    ## endtimp(foritm$work(51))
                    pyxtnm493 = XATSDAPP(pyxtnm492(pyxtnm489))
                    pyxtnm494 = pyxtnm493
                    XATS000_patck(True)
                    pyxtnm495 = XATSBOOL(True)
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(495))
                    return pyxtnm495
                  ## endtimp(forall$test(47))
                  pyxtnm497 = XATSDAPP(pyxtnm496(pyxtnm488))
                  pyxtnm498 = pyxtnm497
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(498))
                  return pyxtnm498
                ## endtimp(forall$test(47))
                pyxtnm500 = XATSDAPP(pyxtnm499(pyxtnm470))
                pyxtnm510 = None
                if (pyxtnm500):
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                  ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                  ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                  def pyxtnm507(arg1, arg2): ## timp: sint_add$sint(936)
                    pyxtnm501 = arg1
                    pyxtnm502 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm506 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(503);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(503))))),I1BNDcons(I1TNM(504);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(504))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                    pyxtnm505 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm501, pyxtnm502))
                    pyxtnm506 = pyxtnm505
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(506))
                    return pyxtnm506
                  ## endtimp(sint_add$sint(936))
                  pyxtnm508 = XATSDAPP(pyxtnm507(pyxtnm470, XATSINT1(1)))
                  pyxtnm509 = XATSDAPP(loop_2862(pyxtnm469, pyxtnm508))
                  pyxtnm510 = pyxtnm509
                else:
                  pyxtnm510 = XATSBOOL(False)
                ## end-of(if)
                pyxtnm511 = pyxtnm510
              ## end-of(if)
              ## I1CMP:return:I1Vtnm(I1TNM(511))
              return pyxtnm511
            pyxtnm512 = XATSDAPP(loop_2862(pyxtnm468, XATSINT1(0)))
            pyxtnm513 = pyxtnm512
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(513))
            return pyxtnm513
          ## endtimp(nint_forall(958))
          pyxtnm515 = XATSDAPP(pyxtnm514(pyxtnm462))
          pyxtnm516 = pyxtnm515
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(516))
          return pyxtnm516
        ## endtimp(strn_forall(1074))
        pyxtnm518 = pyxtnm517
        pyxtnm519 = XATSDAPP(pyxtnm518(pyxtnm450))
        pyxtnm520 = pyxtnm519
        XATS000_patck(True)
        pyxtnm521 = XATSVOID
        ## end-of(let)
        pyxtnm522 = pyxtnm521
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(522))
        return pyxtnm522
      ## endtimp(gseq_foritm(402))
      pyxtnm524 = pyxtnm523
      pyxtnm525 = XATSDAPP(pyxtnm524(pyxtnm446))
      pyxtnm526 = pyxtnm525
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(526))
      return pyxtnm526
    ## endtimp(strn_foritm$f1un(1086))
    pyxtnm528 = XATSDAPP(pyxtnm527(pyxtnm356, pyxtnm362))
    ## I1CMP:return:I1Vtnm(I1TNM(528))
    return pyxtnm528
  ## } // end(lam0)
  pyxtnm530 = XATSDAPP(pyxtnm361(pyxtnm529))
  ## I1CMP:return:I1Vtnm(I1TNM(530))
  return pyxtnm530
## endtimp(strn_append(1063))
pyxtnm532 = XATSDAPP(pyxtnm354(pyxtnm531, XATSSTRN("strn_append")))
pyxtnm533 = pyxtnm532
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(620(line=43,offs=1)--657(line=43,offs=38)))
## I1VALDCL
pyxtnm535 = None
pyxtnm534 = XATSDAPP(pyxtnm533(XATSSTRN("a"), XATSSTRN("bc")))
pyxtnm535 = pyxtnm534
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(658(line=44,offs=1)--695(line=44,offs=38)))
## I1VALDCL
pyxtnm537 = None
pyxtnm536 = XATSDAPP(pyxtnm533(XATSSTRN("x"), XATSSTRN("yz")))
pyxtnm537 = pyxtnm536
XATS000_patck(True)
## LCSRCsome1(test05_gdbg000.dats)@(958(line=52,offs=1)--958(line=52,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test05_gdbg000.dats)@(958(line=52,offs=1)--958(line=52,offs=1));D3Cnone0()))
