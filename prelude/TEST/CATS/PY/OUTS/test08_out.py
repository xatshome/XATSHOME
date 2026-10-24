## Sun Aug 16 12:20:01 PM EDT 2026
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
## LCSRCsome1(test08_optn000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## I1Dinclude(LCSRCsome1(test08_optn000.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
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
## I1Dinclude(LCSRCsome1(test08_optn000.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
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
## I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(323(line=21,offs=1)--345(line=21,offs=23)))
## I1VALDCL
pyxtnm2 = None
pyxtnm1 = XATSCAPP("optn_cons", [1, XATSINT1(10)])
pyxtnm2 = pyxtnm1
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(349(line=23,offs=1)--383(line=24,offs=26)))
## I1VALDCL
pyxtnm315 = None
## LCSRCsome1(test08_optn000.dats)@(358(line=24,offs=1)--364(line=24,offs=7))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm313(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm3 = arg1
  pyxtnm4 = arg2
  pyxtnm5 = arg3
  ## I1CMP:start
  ## let
  pyxtnm312 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm9 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm7(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm6 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(6))
    return pyxtnm6
  ## endtimp(gs_print$beg(802))
  pyxtnm8 = XATSDAPP(pyxtnm7())
  pyxtnm9 = pyxtnm8
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm15 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm14(arg1): ## timp: strn_print(1040)
    pyxtnm10 = arg1
    ## I1CMP:start
    ## let
    pyxtnm13 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(11);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(11))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm12 = XATSDAPP(XATS2PY_strn_print(pyxtnm10))
    pyxtnm13 = pyxtnm12
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(13))
    return pyxtnm13
  ## endtimp(strn_print(1040))
  pyxtnm15 = pyxtnm14
  pyxtnm16 = XATSDAPP(pyxtnm15(pyxtnm3))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm18(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm17 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(17))
    return pyxtnm17
  ## endtimp(gs_print$sep(803))
  pyxtnm19 = XATSDAPP(pyxtnm18())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3076(line=178,offs=1)--3151(line=183,offs=30)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7649],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7649])))))))))
  def pyxtnm297(arg1): ## timp: g_print(39)
    pyxtnm20 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3122(line=183,offs=1)--3132(line=183,offs=11))
    ## I0Etapq(I0Ecst(gseq_print(353)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2942(line=185,offs=1)--2952(line=185,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Pvar(x0[7649]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7649])))))
    ## T1IMPallx(gseq_print(353), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2867(line=161,offs=1)--2928(line=164,offs=33)))
    ## T1IMPallx(gseq_print(353)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6056],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6057],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print(353);$list(@(xs[1081],T2Pvar(xs[6056])),@(x0[1082],T2Pvar(x0[6057])))))))
    pyxtnm295 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2909(line=164,offs=14)--2920(line=164,offs=25))
    ## I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Pvar(xs[6056]))),T2JAG($list(T2Pvar(x0[6057])))))
    ## T1IMPallx(gseq_print0(1686), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    ## T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    def pyxtnm294(arg1): ## timp: gseq_print0(1686)
      pyxtnm21 = arg1
      ## I1CMP:start
      ## let
      pyxtnm293 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
      ## I1VALDCL
      pyxtnm30 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm26(arg1): ## timp: strn_print(1040)
        pyxtnm22 = arg1
        ## I1CMP:start
        ## let
        pyxtnm25 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(23);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(23))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm24 = XATSDAPP(XATS2PY_strn_print(pyxtnm22))
        pyxtnm25 = pyxtnm24
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(25))
        return pyxtnm25
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3018(line=173,offs=1)--3072(line=176,offs=27)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7648],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7648],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7648])))),@(x0[1068],T2Pvar(x0[7648])))))))
      def pyxtnm27(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("optn(")
      ## endtimp(gseq$beg(346))
      pyxtnm28 = XATSDAPP(pyxtnm27())
      pyxtnm29 = XATSDAPP(pyxtnm26(pyxtnm28))
      pyxtnm30 = pyxtnm29
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
      ## I1VALDCL
      pyxtnm283 = None
      ## let
      pyxtnm282 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
      ## I1VALDCL
      pyxtnm39 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
      ## I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$prlen(350), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
      ## T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
      def pyxtnm37(): ## timp: gseq$prlen(350)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
        ## I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
        ## T1IMPallx(sint_neg(923), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
        ## T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
        def pyxtnm35(arg1): ## timp: sint_neg(923)
          pyxtnm31 = arg1
          ## I1CMP:start
          ## let
          pyxtnm34 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_neg(2612));$list(I1FUNDCL(XATS2PY_sint_neg(4857);$list(FJARGdarg($list(I1BNDcons(I1TNM(32);I0Pvar(i1(4858));$list(@(i1(4858),I1Vtnm(I1TNM(32))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_neg);G1Nlist($list())))))))
          pyxtnm33 = XATSDAPP(XATS2PY_sint_neg(pyxtnm31))
          pyxtnm34 = pyxtnm33
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(34))
          return pyxtnm34
        ## endtimp(sint_neg(923))
        pyxtnm36 = XATSDAPP(pyxtnm35(XATSINT1(1)))
        ## I1CMP:return:I1Vtnm(I1TNM(36))
        return pyxtnm36
      ## endtimp(gseq$prlen(350))
      pyxtnm38 = XATSDAPP(pyxtnm37())
      pyxtnm39 = pyxtnm38
      XATS000_patck(True)
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm72(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm66 = arg1
        pyxtnm67 = arg2
        ## I1CMP:start
        ## let
        pyxtnm71 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(68);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(68))))),I1BNDcons(I1TNM(69);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(69))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm70 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm66, pyxtnm67))
        pyxtnm71 = pyxtnm70
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(71))
        return pyxtnm71
      ## endtimp(sint_gte$sint(931))
      pyxtnm73 = XATSDAPP(pyxtnm72(pyxtnm39, XATSINT1(0)))
      pyxtnm281 = None
      if (pyxtnm73):
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
        ## I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
        ## T1IMPallx(g_void(22), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
        ## T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
        def pyxtnm76(arg1): ## timp: g_void(22)
          pyxtnm74 = arg1
          ## I1CMP:start
          pyxtnm75 = XATSTUP0([])
          ## I1CMP:return:I1Vtnm(I1TNM(75))
          return pyxtnm75
        ## endtimp(g_void(22))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
        ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
        def pyxtnm180(arg1): ## timp: gseq_iforall0(1735)
          pyxtnm77 = arg1
          ## I1CMP:start
          ## let
          pyxtnm179 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm78 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
          ## I1VALDCL
          pyxtnm79 = None
          pyxtnm79 = XATSADDR(pyxtnm78)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
          ## I1VALDCL
          pyxtnm178 = None
          ## let
          pyxtnm177 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
          ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
          ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
          def pyxtnm175(arg1): ## timp: gseq_forall0(1719)
            pyxtnm88 = arg1
            ## I1CMP:start
            ## let
            pyxtnm174 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
            ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
            ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1618(line=55,offs=1)--1681(line=58,offs=33)))
            ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7655])))),@(x0[1168],T2Pvar(x0[7655])))))))
            pyxtnm172 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1666(line=58,offs=18)--1677(line=58,offs=29))
            ## I0Etapq(I0Ecst(optn_forall(1314)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn001.sats)@(1428(line=43,offs=1)--1439(line=43,offs=12))));$list(T2JAG($list(T2Pvar(x0[7655])))))
            ## T1IMPallx(optn_forall(1314), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1498(line=45,offs=1)--1614(line=53,offs=2)))
            ## T1IMPallx(optn_forall(1314)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7654],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_forall(1314);$list(@(x0[3580],T2Pvar(x0[7654])))))))
            def pyxtnm171(arg1): ## timp: optn_forall(1314)
              pyxtnm89 = arg1
              ## I1CMP:start
              pyxtnm170 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(90);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
                if (XATS000_ctgeq(pyxtnm89, XATSCTAG("optn_nil",0))): ## { // gpt
                  pyxtnm90 = pyxtnm89
                  pyxtnm170 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(91);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(2852))));$list(@(x0(2852),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(91));0)))))
                if (XATS000_ctgeq(pyxtnm89, XATSCTAG("optn_cons",1))): ## { // gpt
                  pyxtnm91 = pyxtnm89
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1593(line=52,offs=19)--1604(line=52,offs=30))
                  ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7654])))))
                  ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                  ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  pyxtnm168 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                  ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                  ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                  ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm167(arg1): ## timp: forall$test0(1422)
                    pyxtnm92 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm166 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                    ## I1VALDCL
                    pyxtnm97 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                    def pyxtnm95(arg1): ## timp: p2tr_get(2309)
                      pyxtnm93 = arg1
                      ## I1CMP:start
                      pyxtnm94 = XATS000_dp2tr(pyxtnm93)
                      ## I1CMP:return:I1Vtnm(I1TNM(94))
                      return pyxtnm94
                    ## endtimp(p2tr_get(2309))
                    pyxtnm96 = XATSDAPP(pyxtnm95(pyxtnm79))
                    pyxtnm97 = pyxtnm96
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                    ## I1VALDCL
                    pyxtnm153 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                    ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                    ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm151(arg1, arg2): ## timp: iforall$test0(1432)
                      pyxtnm98 = arg1
                      pyxtnm99 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm150 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                      ## I1VALDCL
                      pyxtnm117 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                      ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                      ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                      def pyxtnm106(arg1, arg2): ## timp: sint_gt$sint(928)
                        pyxtnm100 = arg1
                        pyxtnm101 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm105 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(102);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(102))))),I1BNDcons(I1TNM(103);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(103))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                        pyxtnm104 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm100, pyxtnm101))
                        pyxtnm105 = pyxtnm104
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(105))
                        return pyxtnm105
                      ## endtimp(sint_gt$sint(928))
                      pyxtnm107 = XATSDAPP(pyxtnm106(pyxtnm98, XATSINT1(0)))
                      pyxtnm116 = None
                      if (pyxtnm107):
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                        def pyxtnm112(arg1): ## timp: strn_print(1040)
                          pyxtnm108 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm111 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(109);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(109))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                          pyxtnm110 = XATSDAPP(XATS2PY_strn_print(pyxtnm108))
                          pyxtnm111 = pyxtnm110
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(111))
                          return pyxtnm111
                        ## endtimp(strn_print(1040))
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                        ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                        ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2916(line=165,offs=1)--2966(line=168,offs=23)))
                        ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7646])))),@(x0[1072],T2Pvar(x0[7646])))))))
                        def pyxtnm113(): ## timp: gseq$sep(348)
                          ## I1CMP:start
                          ## I1CMP:return:I1Vstr(...)
                          return XATSSTRN(",")
                        ## endtimp(gseq$sep(348))
                        pyxtnm114 = XATSDAPP(pyxtnm113())
                        pyxtnm115 = XATSDAPP(pyxtnm112(pyxtnm114))
                        pyxtnm116 = pyxtnm115
                      ## else: None
                      ## end-of(if)
                      pyxtnm117 = pyxtnm116
                      XATS000_patck(True)
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                      def pyxtnm124(arg1, arg2): ## timp: sint_gte$sint(931)
                        pyxtnm118 = arg1
                        pyxtnm119 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm123 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(120);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(120))))),I1BNDcons(I1TNM(121);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(121))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                        pyxtnm122 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm118, pyxtnm119))
                        pyxtnm123 = pyxtnm122
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(123))
                        return pyxtnm123
                      ## endtimp(sint_gte$sint(931))
                      pyxtnm125 = XATSDAPP(pyxtnm124(pyxtnm98, pyxtnm39))
                      pyxtnm149 = None
                      if (pyxtnm125):
                        ## let
                        pyxtnm140 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                        ## I1VALDCL
                        pyxtnm130 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                        ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                        ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                        ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                        def pyxtnm128(arg1): ## timp: g_free(23)
                          pyxtnm126 = arg1
                          ## I1CMP:start
                          pyxtnm127 = XATSTUP0([])
                          ## I1CMP:return:I1Vtnm(I1TNM(127))
                          return pyxtnm127
                        ## endtimp(g_free(23))
                        pyxtnm129 = XATSDAPP(pyxtnm128(pyxtnm99))
                        pyxtnm130 = pyxtnm129
                        XATS000_patck(True)
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                        ## I1VALDCL
                        pyxtnm139 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                        def pyxtnm135(arg1): ## timp: strn_print(1040)
                          pyxtnm131 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm134 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(132);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(132))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                          pyxtnm133 = XATSDAPP(XATS2PY_strn_print(pyxtnm131))
                          pyxtnm134 = pyxtnm133
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(134))
                          return pyxtnm134
                        ## endtimp(strn_print(1040))
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                        ## I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                        ## T1IMPallx(gseq$rst(349), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                        ## T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                        def pyxtnm136(): ## timp: gseq$rst(349)
                          ## I1CMP:start
                          ## I1CMP:return:I1Vstr(...)
                          return XATSSTRN("...")
                        ## endtimp(gseq$rst(349))
                        pyxtnm137 = XATSDAPP(pyxtnm136())
                        pyxtnm138 = XATSDAPP(pyxtnm135(pyxtnm137))
                        pyxtnm139 = pyxtnm138
                        XATS000_patck(True)
                        pyxtnm140 = XATSBOOL(False)
                        ## end-of(let)
                        pyxtnm149 = pyxtnm140
                      else:
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                        ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                        ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                        ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                        pyxtnm147 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                        ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                        ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                        ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                        pyxtnm146 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                        ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                        ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                        def pyxtnm145(arg1): ## timp: sint_print(922)
                          pyxtnm141 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm144 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(142);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(142))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                          pyxtnm143 = XATSDAPP(XATS2PY_sint_print(pyxtnm141))
                          pyxtnm144 = pyxtnm143
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(144))
                          return pyxtnm144
                        ## endtimp(sint_print(922))
                        pyxtnm146 = pyxtnm145
                        pyxtnm147 = pyxtnm146
                        pyxtnm148 = XATSDAPP(pyxtnm147(pyxtnm99))
                        pyxtnm149 = XATSBOOL(True)
                      ## end-of(if)
                      pyxtnm150 = pyxtnm149
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(150))
                      return pyxtnm150
                    ## endtimp(iforall$test0(1432))
                    pyxtnm152 = XATSDAPP(pyxtnm151(pyxtnm97, pyxtnm92))
                    pyxtnm153 = pyxtnm152
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                    def pyxtnm156(arg1, arg2): ## timp: p2tr_set(2310)
                      pyxtnm154 = arg1
                      pyxtnm155 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm154, pyxtnm155)
                      ## I1CMP:return:I1V000()
                      return XATSVOID
                    ## endtimp(p2tr_set(2310))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                    def pyxtnm163(arg1, arg2): ## timp: sint_add$sint(936)
                      pyxtnm157 = arg1
                      pyxtnm158 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm162 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(159);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(159))))),I1BNDcons(I1TNM(160);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(160))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm161 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm157, pyxtnm158))
                      pyxtnm162 = pyxtnm161
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(162))
                      return pyxtnm162
                    ## endtimp(sint_add$sint(936))
                    pyxtnm164 = XATSDAPP(pyxtnm163(pyxtnm97, XATSINT1(1)))
                    pyxtnm165 = XATSDAPP(pyxtnm156(pyxtnm79, pyxtnm164))
                    pyxtnm166 = pyxtnm153
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(166))
                    return pyxtnm166
                  ## endtimp(forall$test0(1422))
                  pyxtnm168 = pyxtnm167
                  pyxtnm169 = XATSDAPP(pyxtnm168(XATSP1CN("optn_cons", pyxtnm91[0+1])))
                  pyxtnm170 = pyxtnm169
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:I1Vtnm(I1TNM(170))
              return pyxtnm170
            ## endtimp(optn_forall(1314))
            pyxtnm172 = pyxtnm171
            pyxtnm173 = XATSDAPP(pyxtnm172(pyxtnm88))
            pyxtnm174 = pyxtnm173
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(174))
            return pyxtnm174
          ## endtimp(gseq_forall0(1719))
          pyxtnm176 = XATSDAPP(pyxtnm175(pyxtnm77))
          pyxtnm177 = pyxtnm176
          ## end-of(let)
          pyxtnm178 = pyxtnm177
          XATS000_patck(True)
          pyxtnm179 = pyxtnm178
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(179))
          return pyxtnm179
        ## endtimp(gseq_iforall0(1735))
        pyxtnm181 = XATSDAPP(pyxtnm180(pyxtnm21))
        pyxtnm182 = XATSDAPP(pyxtnm76(pyxtnm181))
        pyxtnm281 = pyxtnm182
      else:
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforitm0(1759), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
        ## T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
        def pyxtnm279(arg1): ## timp: gseq_iforitm0(1759)
          pyxtnm183 = arg1
          ## I1CMP:start
          ## let
          pyxtnm278 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
          ## let
          pyxtnm277 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
          ## I1VALDCL
          pyxtnm276 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
          ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
          ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
          def pyxtnm274(arg1): ## timp: gseq_iforall0(1735)
            pyxtnm189 = arg1
            ## I1CMP:start
            ## let
            pyxtnm273 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm190 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
            ## I1VALDCL
            pyxtnm191 = None
            pyxtnm191 = XATSADDR(pyxtnm190)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
            ## I1VALDCL
            pyxtnm272 = None
            ## let
            pyxtnm271 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
            ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
            ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
            def pyxtnm269(arg1): ## timp: gseq_forall0(1719)
              pyxtnm200 = arg1
              ## I1CMP:start
              ## let
              pyxtnm268 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
              ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
              ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
              ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1618(line=55,offs=1)--1681(line=58,offs=33)))
              ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7655])))),@(x0[1168],T2Pvar(x0[7655])))))))
              pyxtnm266 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1666(line=58,offs=18)--1677(line=58,offs=29))
              ## I0Etapq(I0Ecst(optn_forall(1314)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn001.sats)@(1428(line=43,offs=1)--1439(line=43,offs=12))));$list(T2JAG($list(T2Pvar(x0[7655])))))
              ## T1IMPallx(optn_forall(1314), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1498(line=45,offs=1)--1614(line=53,offs=2)))
              ## T1IMPallx(optn_forall(1314)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7654],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_forall(1314);$list(@(x0[3580],T2Pvar(x0[7654])))))))
              def pyxtnm265(arg1): ## timp: optn_forall(1314)
                pyxtnm201 = arg1
                ## I1CMP:start
                pyxtnm264 = None
                while True: ## do {
                  ## { // cls
                  ## I1GPTpat(I1BNDcons(I1TNM(202);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
                  if (XATS000_ctgeq(pyxtnm201, XATSCTAG("optn_nil",0))): ## { // gpt
                    pyxtnm202 = pyxtnm201
                    pyxtnm264 = XATSBOOL(True)
                    break ## cls
                  ## } // gpt
                  ## } // cls
                  ## { // cls
                  ## I1GPTpat(I1BNDcons(I1TNM(203);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(2852))));$list(@(x0(2852),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(203));0)))))
                  if (XATS000_ctgeq(pyxtnm201, XATSCTAG("optn_cons",1))): ## { // gpt
                    pyxtnm203 = pyxtnm201
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1593(line=52,offs=19)--1604(line=52,offs=30))
                    ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7654])))))
                    ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                    ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    pyxtnm262 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                    ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                    ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                    ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm261(arg1): ## timp: forall$test0(1422)
                      pyxtnm204 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm260 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                      ## I1VALDCL
                      pyxtnm209 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                      ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                      ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                      def pyxtnm207(arg1): ## timp: p2tr_get(2309)
                        pyxtnm205 = arg1
                        ## I1CMP:start
                        pyxtnm206 = XATS000_dp2tr(pyxtnm205)
                        ## I1CMP:return:I1Vtnm(I1TNM(206))
                        return pyxtnm206
                      ## endtimp(p2tr_get(2309))
                      pyxtnm208 = XATSDAPP(pyxtnm207(pyxtnm191))
                      pyxtnm209 = pyxtnm208
                      XATS000_patck(True)
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                      ## I1VALDCL
                      pyxtnm247 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                      ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                      ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                      ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm245(arg1, arg2): ## timp: iforall$test0(1432)
                        pyxtnm210 = arg1
                        pyxtnm211 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm244 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                        ## I1VALDCL
                        pyxtnm243 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                        ## I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                        ## T1IMPallx(iforitm$work0(1448), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                        ## T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        def pyxtnm241(arg1, arg2): ## timp: iforitm$work0(1448)
                          pyxtnm212 = arg1
                          pyxtnm213 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm240 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                          ## I1VALDCL
                          pyxtnm231 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                          ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                          ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                          def pyxtnm220(arg1, arg2): ## timp: sint_gt$sint(928)
                            pyxtnm214 = arg1
                            pyxtnm215 = arg2
                            ## I1CMP:start
                            ## let
                            pyxtnm219 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(216);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(216))))),I1BNDcons(I1TNM(217);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(217))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                            pyxtnm218 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm214, pyxtnm215))
                            pyxtnm219 = pyxtnm218
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(219))
                            return pyxtnm219
                          ## endtimp(sint_gt$sint(928))
                          pyxtnm221 = XATSDAPP(pyxtnm220(pyxtnm212, XATSINT1(0)))
                          pyxtnm230 = None
                          if (pyxtnm221):
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                            def pyxtnm226(arg1): ## timp: strn_print(1040)
                              pyxtnm222 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm225 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(223);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(223))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                              pyxtnm224 = XATSDAPP(XATS2PY_strn_print(pyxtnm222))
                              pyxtnm225 = pyxtnm224
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(225))
                              return pyxtnm225
                            ## endtimp(strn_print(1040))
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                            ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                            ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2916(line=165,offs=1)--2966(line=168,offs=23)))
                            ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7646])))),@(x0[1072],T2Pvar(x0[7646])))))))
                            def pyxtnm227(): ## timp: gseq$sep(348)
                              ## I1CMP:start
                              ## I1CMP:return:I1Vstr(...)
                              return XATSSTRN(",")
                            ## endtimp(gseq$sep(348))
                            pyxtnm228 = XATSDAPP(pyxtnm227())
                            pyxtnm229 = XATSDAPP(pyxtnm226(pyxtnm228))
                            pyxtnm230 = pyxtnm229
                          ## else: None
                          ## end-of(if)
                          pyxtnm231 = pyxtnm230
                          XATS000_patck(True)
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                          ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                          ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                          pyxtnm238 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                          pyxtnm237 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                          ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                          ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                          def pyxtnm236(arg1): ## timp: sint_print(922)
                            pyxtnm232 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm235 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(233);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(233))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                            pyxtnm234 = XATSDAPP(XATS2PY_sint_print(pyxtnm232))
                            pyxtnm235 = pyxtnm234
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(235))
                            return pyxtnm235
                          ## endtimp(sint_print(922))
                          pyxtnm237 = pyxtnm236
                          pyxtnm238 = pyxtnm237
                          pyxtnm239 = XATSDAPP(pyxtnm238(pyxtnm213))
                          pyxtnm240 = pyxtnm239
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(240))
                          return pyxtnm240
                        ## endtimp(iforitm$work0(1448))
                        pyxtnm242 = XATSDAPP(pyxtnm241(pyxtnm210, pyxtnm211))
                        pyxtnm243 = pyxtnm242
                        XATS000_patck(True)
                        pyxtnm244 = XATSBOOL(True)
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(244))
                        return pyxtnm244
                      ## endtimp(iforall$test0(1432))
                      pyxtnm246 = XATSDAPP(pyxtnm245(pyxtnm209, pyxtnm204))
                      pyxtnm247 = pyxtnm246
                      XATS000_patck(True)
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                      ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                      ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                      def pyxtnm250(arg1, arg2): ## timp: p2tr_set(2310)
                        pyxtnm248 = arg1
                        pyxtnm249 = arg2
                        ## I1CMP:start
                        XATS000_assgn(pyxtnm248, pyxtnm249)
                        ## I1CMP:return:I1V000()
                        return XATSVOID
                      ## endtimp(p2tr_set(2310))
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                      ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                      ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                      def pyxtnm257(arg1, arg2): ## timp: sint_add$sint(936)
                        pyxtnm251 = arg1
                        pyxtnm252 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm256 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(253);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(253))))),I1BNDcons(I1TNM(254);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(254))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                        pyxtnm255 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm251, pyxtnm252))
                        pyxtnm256 = pyxtnm255
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(256))
                        return pyxtnm256
                      ## endtimp(sint_add$sint(936))
                      pyxtnm258 = XATSDAPP(pyxtnm257(pyxtnm209, XATSINT1(1)))
                      pyxtnm259 = XATSDAPP(pyxtnm250(pyxtnm191, pyxtnm258))
                      pyxtnm260 = pyxtnm247
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(260))
                      return pyxtnm260
                    ## endtimp(forall$test0(1422))
                    pyxtnm262 = pyxtnm261
                    pyxtnm263 = XATSDAPP(pyxtnm262(XATSP1CN("optn_cons", pyxtnm203[0+1])))
                    pyxtnm264 = pyxtnm263
                    break ## cls
                  ## } // gpt
                  ## } // cls
                  XATS000_cfail()
                ## } while True // end-of(do-cls)
                ## I1CMP:return:I1Vtnm(I1TNM(264))
                return pyxtnm264
              ## endtimp(optn_forall(1314))
              pyxtnm266 = pyxtnm265
              pyxtnm267 = XATSDAPP(pyxtnm266(pyxtnm200))
              pyxtnm268 = pyxtnm267
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(268))
              return pyxtnm268
            ## endtimp(gseq_forall0(1719))
            pyxtnm270 = XATSDAPP(pyxtnm269(pyxtnm189))
            pyxtnm271 = pyxtnm270
            ## end-of(let)
            pyxtnm272 = pyxtnm271
            XATS000_patck(True)
            pyxtnm273 = pyxtnm272
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(273))
            return pyxtnm273
          ## endtimp(gseq_iforall0(1735))
          pyxtnm275 = XATSDAPP(pyxtnm274(pyxtnm183))
          pyxtnm276 = pyxtnm275
          XATS000_patck(True)
          pyxtnm277 = XATSVOID
          ## end-of(let)
          pyxtnm278 = pyxtnm277
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(278))
          return pyxtnm278
        ## endtimp(gseq_iforitm0(1759))
        pyxtnm280 = XATSDAPP(pyxtnm279(pyxtnm21))
        pyxtnm281 = pyxtnm280
      ## end-of(if)
      pyxtnm282 = pyxtnm281
      ## end-of(let)
      pyxtnm283 = pyxtnm282
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
      ## I1VALDCL
      pyxtnm292 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm288(arg1): ## timp: strn_print(1040)
        pyxtnm284 = arg1
        ## I1CMP:start
        ## let
        pyxtnm287 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(285);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(285))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm286 = XATSDAPP(XATS2PY_strn_print(pyxtnm284))
        pyxtnm287 = pyxtnm286
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(287))
        return pyxtnm287
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2967(line=169,offs=1)--3017(line=172,offs=23)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7647],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7647],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7647])))),@(x0[1070],T2Pvar(x0[7647])))))))
      def pyxtnm289(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm290 = XATSDAPP(pyxtnm289())
      pyxtnm291 = XATSDAPP(pyxtnm288(pyxtnm290))
      pyxtnm292 = pyxtnm291
      XATS000_patck(True)
      pyxtnm293 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(293))
      return pyxtnm293
    ## endtimp(gseq_print0(1686))
    pyxtnm295 = pyxtnm294
    pyxtnm296 = XATSDAPP(pyxtnm295(pyxtnm20))
    ## I1CMP:return:I1Vtnm(I1TNM(296))
    return pyxtnm296
  ## endtimp(g_print(39))
  pyxtnm298 = XATSDAPP(pyxtnm297(pyxtnm4))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm300(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm299 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(299))
    return pyxtnm299
  ## endtimp(gs_print$sep(803))
  pyxtnm301 = XATSDAPP(pyxtnm300())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm307 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm306(arg1): ## timp: strn_print(1040)
    pyxtnm302 = arg1
    ## I1CMP:start
    ## let
    pyxtnm305 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(303);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(303))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm304 = XATSDAPP(XATS2PY_strn_print(pyxtnm302))
    pyxtnm305 = pyxtnm304
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(305))
    return pyxtnm305
  ## endtimp(strn_print(1040))
  pyxtnm307 = pyxtnm306
  pyxtnm308 = XATSDAPP(pyxtnm307(pyxtnm5))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm310(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm309 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(309))
    return pyxtnm309
  ## endtimp(gs_print$end(804))
  pyxtnm311 = XATSDAPP(pyxtnm310())
  pyxtnm312 = pyxtnm311
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(312))
  return pyxtnm312
## endtimp(gs_print_a3(808))
pyxtnm314 = XATSDAPP(pyxtnm313(XATSSTRN("ns = "), pyxtnm2, XATSSTRN("\n")))
pyxtnm315 = pyxtnm314
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(384(line=25,offs=1)--429(line=26,offs=30)))
## I1VALDCL
pyxtnm362 = None
## LCSRCsome1(test08_optn000.dats)@(393(line=25,offs=10)--399(line=25,offs=16))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm354(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm316 = arg1
  pyxtnm317 = arg2
  pyxtnm318 = arg3
  ## I1CMP:start
  ## let
  pyxtnm353 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm322 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm320(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm319 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(319))
    return pyxtnm319
  ## endtimp(gs_print$beg(802))
  pyxtnm321 = XATSDAPP(pyxtnm320())
  pyxtnm322 = pyxtnm321
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm328 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm327(arg1): ## timp: strn_print(1040)
    pyxtnm323 = arg1
    ## I1CMP:start
    ## let
    pyxtnm326 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(324);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(324))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm325 = XATSDAPP(XATS2PY_strn_print(pyxtnm323))
    pyxtnm326 = pyxtnm325
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(326))
    return pyxtnm326
  ## endtimp(strn_print(1040))
  pyxtnm328 = pyxtnm327
  pyxtnm329 = XATSDAPP(pyxtnm328(pyxtnm316))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm331(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm330 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(330))
    return pyxtnm330
  ## endtimp(gs_print$sep(803))
  pyxtnm332 = XATSDAPP(pyxtnm331())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
  pyxtnm338 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
  ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
  ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
  def pyxtnm337(arg1): ## timp: sint_print(922)
    pyxtnm333 = arg1
    ## I1CMP:start
    ## let
    pyxtnm336 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(334);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(334))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
    pyxtnm335 = XATSDAPP(XATS2PY_sint_print(pyxtnm333))
    pyxtnm336 = pyxtnm335
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(336))
    return pyxtnm336
  ## endtimp(sint_print(922))
  pyxtnm338 = pyxtnm337
  pyxtnm339 = XATSDAPP(pyxtnm338(pyxtnm317))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm341(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm340 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(340))
    return pyxtnm340
  ## endtimp(gs_print$sep(803))
  pyxtnm342 = XATSDAPP(pyxtnm341())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm348 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm347(arg1): ## timp: strn_print(1040)
    pyxtnm343 = arg1
    ## I1CMP:start
    ## let
    pyxtnm346 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(344);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(344))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm345 = XATSDAPP(XATS2PY_strn_print(pyxtnm343))
    pyxtnm346 = pyxtnm345
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(346))
    return pyxtnm346
  ## endtimp(strn_print(1040))
  pyxtnm348 = pyxtnm347
  pyxtnm349 = XATSDAPP(pyxtnm348(pyxtnm318))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm351(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm350 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(350))
    return pyxtnm350
  ## endtimp(gs_print$end(804))
  pyxtnm352 = XATSDAPP(pyxtnm351())
  pyxtnm353 = pyxtnm352
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(353))
  return pyxtnm353
## endtimp(gs_print_a3(808))
## LCSRCsome1(test08_optn000.dats)@(412(line=26,offs=13)--418(line=26,offs=19))
## I0Etapq(I0Ecst(optn_length(1313)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn000.sats)@(2061(line=90,offs=1)--2072(line=90,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(optn_length(1313), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3294(line=195,offs=1)--3387(line=202,offs=21)))
## T1IMPallx(optn_length(1313)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7651],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_length(1313);$list(@(a[3578],T2Pvar(x0[7651])))))))
def pyxtnm359(arg1): ## timp: optn_length(1313)
  pyxtnm355 = arg1
  ## I1CMP:start
  pyxtnm358 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(356);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
    if (XATS000_ctgeq(pyxtnm355, XATSCTAG("optn_nil",0))): ## { // gpt
      pyxtnm356 = pyxtnm355
      pyxtnm358 = XATSINT1(0)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(357);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pany()));$list()))
    if (XATS000_ctgeq(pyxtnm355, XATSCTAG("optn_cons",1))): ## { // gpt
      pyxtnm357 = pyxtnm355
      pyxtnm358 = XATSINT1(1)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:I1Vtnm(I1TNM(358))
  return pyxtnm358
## endtimp(optn_length(1313))
pyxtnm360 = XATSDAPP(pyxtnm359(pyxtnm2))
pyxtnm361 = XATSDAPP(pyxtnm354(XATSSTRN("|ns| = "), pyxtnm360, XATSSTRN("\n")))
pyxtnm362 = pyxtnm361
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(430(line=27,offs=1)--477(line=28,offs=32)))
## I1VALDCL
pyxtnm408 = None
## LCSRCsome1(test08_optn000.dats)@(439(line=27,offs=10)--445(line=27,offs=16))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm401(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm363 = arg1
  pyxtnm364 = arg2
  pyxtnm365 = arg3
  ## I1CMP:start
  ## let
  pyxtnm400 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm369 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm367(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm366 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(366))
    return pyxtnm366
  ## endtimp(gs_print$beg(802))
  pyxtnm368 = XATSDAPP(pyxtnm367())
  pyxtnm369 = pyxtnm368
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm375 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm374(arg1): ## timp: strn_print(1040)
    pyxtnm370 = arg1
    ## I1CMP:start
    ## let
    pyxtnm373 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(371);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(371))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm372 = XATSDAPP(XATS2PY_strn_print(pyxtnm370))
    pyxtnm373 = pyxtnm372
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(373))
    return pyxtnm373
  ## endtimp(strn_print(1040))
  pyxtnm375 = pyxtnm374
  pyxtnm376 = XATSDAPP(pyxtnm375(pyxtnm363))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm378(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm377 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(377))
    return pyxtnm377
  ## endtimp(gs_print$sep(803))
  pyxtnm379 = XATSDAPP(pyxtnm378())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
  pyxtnm385 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
  ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
  ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
  def pyxtnm384(arg1): ## timp: sint_print(922)
    pyxtnm380 = arg1
    ## I1CMP:start
    ## let
    pyxtnm383 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(381);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(381))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
    pyxtnm382 = XATSDAPP(XATS2PY_sint_print(pyxtnm380))
    pyxtnm383 = pyxtnm382
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(383))
    return pyxtnm383
  ## endtimp(sint_print(922))
  pyxtnm385 = pyxtnm384
  pyxtnm386 = XATSDAPP(pyxtnm385(pyxtnm364))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm388(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm387 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(387))
    return pyxtnm387
  ## endtimp(gs_print$sep(803))
  pyxtnm389 = XATSDAPP(pyxtnm388())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm395 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm394(arg1): ## timp: strn_print(1040)
    pyxtnm390 = arg1
    ## I1CMP:start
    ## let
    pyxtnm393 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(391);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(391))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm392 = XATSDAPP(XATS2PY_strn_print(pyxtnm390))
    pyxtnm393 = pyxtnm392
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(393))
    return pyxtnm393
  ## endtimp(strn_print(1040))
  pyxtnm395 = pyxtnm394
  pyxtnm396 = XATSDAPP(pyxtnm395(pyxtnm365))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm398(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm397 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(397))
    return pyxtnm397
  ## endtimp(gs_print$end(804))
  pyxtnm399 = XATSDAPP(pyxtnm398())
  pyxtnm400 = pyxtnm399
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(400))
  return pyxtnm400
## endtimp(gs_print_a3(808))
## LCSRCsome1(test08_optn000.dats)@(462(line=28,offs=17)--466(line=28,offs=21))
## I0Etapq(I0Ecst(optn_head(1311)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn000.sats)@(1695(line=64,offs=1)--1704(line=64,offs=10))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(optn_head(1311), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2478(line=129,offs=1)--2556(line=135,offs=25)))
## T1IMPallx(optn_head(1311)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[7642],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_head(1311);$list(@(a[3576],T2Pvar(a[7642])))))))
def pyxtnm405(arg1): ## timp: optn_head(1311)
  pyxtnm402 = arg1
  ## I1CMP:start
  pyxtnm404 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(403);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(2844))));$list(@(x0(2844),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(403));0)))))
    if (XATS000_ctgeq(pyxtnm402, XATSCTAG("optn_cons",1))): ## { // gpt
      pyxtnm403 = pyxtnm402
      pyxtnm404 = XATSP1CN("optn_cons", pyxtnm403[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:I1Vtnm(I1TNM(404))
  return pyxtnm404
## endtimp(optn_head(1311))
pyxtnm406 = XATSDAPP(pyxtnm405(pyxtnm2))
pyxtnm407 = XATSDAPP(pyxtnm401(XATSSTRN("head(ns) = "), pyxtnm406, XATSSTRN("\n")))
pyxtnm408 = pyxtnm407
XATS000_patck(True)
## LCSRCsome1(test08_optn000.dats)@(740(line=36,offs=1)--740(line=36,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test08_optn000.dats)@(740(line=36,offs=1)--740(line=36,offs=1));D3Cnone0()))
