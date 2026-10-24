## Sun Aug 16 12:19:08 PM EDT 2026
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
## LCSRCsome1(test02_a1rf000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## LCSRCsome1(test02_a1rf000.dats)@(187(line=12,offs=1)--221(line=13,offs=26))
## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csymload(T_SRP_SYMLOAD();array;D2PTMsome(0;D2ITMcst($list(a1rf_make_ncpy(1104))))))))
## LCSRCsome1(test02_a1rf000.dats)@(222(line=14,offs=1)--256(line=15,offs=26))
## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csymload(T_SRP_SYMLOAD();array;D2PTMsome(0;D2ITMcst($list(a1rf_make_nfun(1105))))))))
## I1Dinclude(LCSRCsome1(test02_a1rf000.dats)@(297(line=18,offs=1)--338(line=19,offs=33)))
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
## I1Dinclude(LCSRCsome1(test02_a1rf000.dats)@(339(line=20,offs=1)--383(line=21,offs=36)))
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
## I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(427(line=25,offs=1)--448(line=26,offs=13)))
## I1VALDCL
pyxtnm9 = None
## LCSRCsome1(test02_a1rf000.dats)@(436(line=26,offs=1)--441(line=26,offs=6))
## I0Etapq(I0Ecst(a1rf_make_ncpy(1104)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3640(line=183,offs=1)--3654(line=183,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(a1rf_make_ncpy(1104), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2728(line=149,offs=1)--2893(line=161,offs=2)))
## T1IMPallx(a1rf_make_ncpy(1104)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8862],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_make_ncpy(1104);$list(@(a[2969],T2Pvar(a[8862])))))))
def pyxtnm7(arg1, arg2): ## timp: a1rf_make_ncpy(1104)
  pyxtnm1 = arg1
  pyxtnm2 = arg2
  ## I1CMP:start
  ## let
  pyxtnm6 = None
  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2816(line=157,offs=1)--2891(line=160,offs=41)))
  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a1rf_make_ncpy(2670));$list(I1FUNDCL(XATS2PY_a1rf_make_ncpy(5092);$list(FJARGdarg($list(I1BNDcons(I1TNM(3);I0Pvar(n(5093));$list(@(n(5093),I1Vtnm(I1TNM(3))))),I1BNDcons(I1TNM(4);I0Pvar(x(5094));$list(@(x(5094),I1Vtnm(I1TNM(4))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a1rf_make_ncpy);G1Nlist($list())))))))
  pyxtnm5 = XATSDAPP(XATS2PY_a1rf_make_ncpy(pyxtnm1, pyxtnm2))
  pyxtnm6 = pyxtnm5
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(6))
  return pyxtnm6
## endtimp(a1rf_make_ncpy(1104))
pyxtnm8 = XATSDAPP(pyxtnm7(XATSINT1(10), XATSINT1(1)))
pyxtnm9 = pyxtnm8
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(449(line=27,offs=1)--552(line=35,offs=29)))
## I1VALDCL
pyxtnm246 = None
## let
pyxtnm245 = None
## I1Dimplmnt0(LCSRCsome1(test02_a1rf000.dats)@(493(line=32,offs=1)--550(line=35,offs=27)))
## I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8884])))),@(x0[1875],T2Pvar(x0[8884]))))):timp
## LCSRCsome1(test02_a1rf000.dats)@(462(line=29,offs=3)--470(line=29,offs=11))
## I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
## T1IMPallx(gs_println_a2(820), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
## T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
def pyxtnm243(arg1, arg2): ## timp: gs_println_a2(820)
  pyxtnm11 = arg1
  pyxtnm12 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  ## I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  ## T1IMPallx(gs_print_a2(807), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  ## T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  def pyxtnm234(arg1, arg2): ## timp: gs_print_a2(807)
    pyxtnm13 = arg1
    pyxtnm14 = arg2
    ## I1CMP:start
    ## let
    pyxtnm233 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
    ## I1VALDCL
    pyxtnm18 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
    ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    def pyxtnm16(): ## timp: gs_print$beg(802)
      ## I1CMP:start
      pyxtnm15 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(15))
      return pyxtnm15
    ## endtimp(gs_print$beg(802))
    pyxtnm17 = XATSDAPP(pyxtnm16())
    pyxtnm18 = pyxtnm17
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    pyxtnm24 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm23(arg1): ## timp: strn_print(1040)
      pyxtnm19 = arg1
      ## I1CMP:start
      ## let
      pyxtnm22 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(20);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(20))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm21 = XATSDAPP(XATS2PY_strn_print(pyxtnm19))
      pyxtnm22 = pyxtnm21
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(22))
      return pyxtnm22
    ## endtimp(strn_print(1040))
    pyxtnm24 = pyxtnm23
    pyxtnm25 = XATSDAPP(pyxtnm24(pyxtnm13))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
    ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    def pyxtnm27(): ## timp: gs_print$sep(803)
      ## I1CMP:start
      pyxtnm26 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(26))
      return pyxtnm26
    ## endtimp(gs_print$sep(803))
    pyxtnm28 = XATSDAPP(pyxtnm27())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2186(line=97,offs=1)--2419(line=115,offs=4)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7263])))))))))
    def pyxtnm228(arg1): ## timp: g_print(39)
      pyxtnm29 = arg1
      ## I1CMP:start
      ## let
      pyxtnm227 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2244(line=104,offs=1)--2266(line=104,offs=23))
      ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1rf);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7263])))))))
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
      ## I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7263]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
      ## I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7263]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
      ## I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7263]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2388(line=114,offs=3)--2399(line=114,offs=14))
      ## I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7263]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7263])))))
      ## T1IMPallx(gseq_print1(1687), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
      ## T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
      def pyxtnm225(arg1): ## timp: gseq_print1(1687)
        pyxtnm30 = arg1
        ## I1CMP:start
        ## let
        pyxtnm224 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
        ## I1VALDCL
        pyxtnm39 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm35(arg1): ## timp: strn_print(1040)
          pyxtnm31 = arg1
          ## I1CMP:start
          ## let
          pyxtnm34 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(32);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(32))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm33 = XATSDAPP(XATS2PY_strn_print(pyxtnm31))
          pyxtnm34 = pyxtnm33
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(34))
          return pyxtnm34
        ## endtimp(strn_print(1040))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
        ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
        ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
        ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
        def pyxtnm36(): ## timp: gseq$beg(346)
          ## I1CMP:start
          ## I1CMP:return:I1Vstr(...)
          return XATSSTRN("a1rf(")
        ## endtimp(gseq$beg(346))
        pyxtnm37 = XATSDAPP(pyxtnm36())
        pyxtnm38 = XATSDAPP(pyxtnm35(pyxtnm37))
        pyxtnm39 = pyxtnm38
        XATS000_patck(True)
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
        ## I1VALDCL
        pyxtnm214 = None
        ## let
        pyxtnm213 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
        ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
        ## T1IMPallx(gseq_iforitm1(1760), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
        ## T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
        def pyxtnm211(arg1): ## timp: gseq_iforitm1(1760)
          pyxtnm49 = arg1
          ## I1CMP:start
          ## let
          pyxtnm210 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
          ## let
          pyxtnm209 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
          ## I1VALDCL
          pyxtnm208 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
          ## T1IMPallx(gseq_iforall1(1736), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
          ## T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
          def pyxtnm206(arg1): ## timp: gseq_iforall1(1736)
            pyxtnm55 = arg1
            ## I1CMP:start
            ## let
            pyxtnm205 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm56 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
            ## I1VALDCL
            pyxtnm57 = None
            pyxtnm57 = XATSADDR(pyxtnm56)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
            ## I1VALDCL
            pyxtnm204 = None
            ## let
            pyxtnm203 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
            ## T1IMPallx(gseq_forall1(1720), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
            ## T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
            def pyxtnm201(arg1): ## timp: gseq_forall1(1720)
              pyxtnm66 = arg1
              ## I1CMP:start
              ## let
              pyxtnm200 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
              ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
              ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
              ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2740(line=141,offs=1)--2882(line=152,offs=2)))
              ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7287])))),@(x0[1168],T2Pvar(x0[7287])))))))
              def pyxtnm198(arg1): ## timp: gseq_forall(386)
                pyxtnm67 = arg1
                ## I1CMP:start
                ## let
                pyxtnm197 = None
                ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7287]))))):timp
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2798(line=147,offs=1)--2809(line=147,offs=12))
                ## I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7287]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7287])))))
                ## T1IMPallx(gasq_forall(609), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                ## T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                def pyxtnm195(arg1): ## timp: gasq_forall(609)
                  pyxtnm68 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm194 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                  ## I1VALDCL
                  pyxtnm72 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                  ## I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                  ## T1IMPallx(gasq_length(594), LCSRCsome1(test02_a1rf000.dats)@(493(line=32,offs=1)--550(line=35,offs=27)))
                  ## T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8884],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8884],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8884])))),@(x0[1875],T2Pvar(x0[8884])))))))
                  def pyxtnm70(arg1): ## timp: gasq_length(594)
                    pyxtnm69 = arg1
                    ## I1CMP:start
                    ## I1CMP:return:I1Vint(T_INT01(10))
                    return XATSINT1(10)
                  ## endtimp(gasq_length(594))
                  pyxtnm71 = XATSDAPP(pyxtnm70(pyxtnm68))
                  pyxtnm72 = pyxtnm71
                  XATS000_patck(True)
                  ## let
                  pyxtnm193 = None
                  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                  ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                  ## I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                  ## T1IMPallx(nint_forall(958), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                  ## T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                  def pyxtnm191(arg1): ## timp: nint_forall(958)
                    pyxtnm82 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm190 = None
                    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                    ## I1FUNDCL
                    def loop_2862(arg1, arg2): ## fun
                      pyxtnm83 = arg1
                      pyxtnm84 = arg2
                      ## I1CMP:start
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                      def pyxtnm91(arg1, arg2): ## timp: sint_gte$sint(931)
                        pyxtnm85 = arg1
                        pyxtnm86 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm90 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(87);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(87))))),I1BNDcons(I1TNM(88);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(88))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                        pyxtnm89 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm85, pyxtnm86))
                        pyxtnm90 = pyxtnm89
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(90))
                        return pyxtnm90
                      ## endtimp(sint_gte$sint(931))
                      pyxtnm92 = XATSDAPP(pyxtnm91(pyxtnm84, pyxtnm83))
                      pyxtnm188 = None
                      if (pyxtnm92):
                        pyxtnm188 = XATSBOOL(True)
                      else:
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                        ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                        ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                        ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                        def pyxtnm176(arg1): ## timp: forall$test(47)
                          pyxtnm93 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm175 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                          ## I1VALDCL
                          pyxtnm106 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                          ## I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                          ## T1IMPallx(gasq_lget$at$raw(2326), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4092(line=227,offs=1)--4187(line=231,offs=35)))
                          ## T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7276])))),@(x0[5735],T2Pvar(x0[7276])))))))
                          def pyxtnm104(arg1, arg2): ## timp: gasq_lget$at$raw(2326)
                            pyxtnm94 = arg1
                            pyxtnm95 = arg2
                            ## I1CMP:start
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4165(line=231,offs=13)--4177(line=231,offs=25))
                            ## I0Etapq(I0Ecst(a1rf_lget$at(1111)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(4779(line=262,offs=1)--4791(line=262,offs=13))));$list(T2JAG($list(T2Pvar(x0[7276])))))
                            ## T1IMPallx(a1rf_lget$at(1111), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2309(line=113,offs=1)--2486(line=128,offs=2)))
                            ## T1IMPallx(a1rf_lget$at(1111)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_lget$at(1111);$list(@(a[2983],T2Pvar(a[8858])))))))
                            def pyxtnm102(arg1, arg2): ## timp: a1rf_lget$at(1111)
                              pyxtnm96 = arg1
                              pyxtnm97 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm101 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2393(line=121,offs=1)--2484(line=127,offs=38)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a1rf_lget$at(2668));$list(I1FUNDCL(XATS2PY_a1rf_lget$at(5078);$list(FJARGdarg($list(I1BNDcons(I1TNM(98);I0Pvar(A(5079));$list(@(A(5079),I1Vtnm(I1TNM(98))))),I1BNDcons(I1TNM(99);I0Pvar(i(5080));$list(@(i(5080),I1Vtnm(I1TNM(99))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a1rf_lget$at);G1Nlist($list())))))))
                              pyxtnm100 = XATSDAPP(XATS2PY_a1rf_lget_at(pyxtnm96, pyxtnm97))
                              pyxtnm101 = pyxtnm100
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(101))
                              return pyxtnm101
                            ## endtimp(a1rf_lget$at(1111))
                            pyxtnm103 = XATSDAPP(pyxtnm102(pyxtnm94, pyxtnm95))
                            ## I1CMP:return:I1Vtnm(I1TNM(103))
                            return pyxtnm103
                          ## endtimp(gasq_lget$at$raw(2326))
                          pyxtnm105 = XATSDAPP(pyxtnm104(pyxtnm68, pyxtnm93))
                          pyxtnm106 = pyxtnm105
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                          ## I1VALDCL
                          pyxtnm168 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                          ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                          ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                          ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          pyxtnm166 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2865(line=151,offs=20)--2876(line=151,offs=31))
                          ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7287])))))
                          ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                          ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          pyxtnm165 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                          ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                          ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                          ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          def pyxtnm164(arg1): ## timp: forall$test1(1423)
                            pyxtnm107 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm163 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                            ## I1VALDCL
                            pyxtnm112 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                            ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                            ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                            def pyxtnm110(arg1): ## timp: p2tr_get(2309)
                              pyxtnm108 = arg1
                              ## I1CMP:start
                              pyxtnm109 = XATS000_dp2tr(pyxtnm108)
                              ## I1CMP:return:I1Vtnm(I1TNM(109))
                              return pyxtnm109
                            ## endtimp(p2tr_get(2309))
                            pyxtnm111 = XATSDAPP(pyxtnm110(pyxtnm57))
                            pyxtnm112 = pyxtnm111
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                            ## I1VALDCL
                            pyxtnm150 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                            ## I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                            ## T1IMPallx(iforall$test1(1433), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                            ## T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                            def pyxtnm148(arg1, arg2): ## timp: iforall$test1(1433)
                              pyxtnm113 = arg1
                              pyxtnm114 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm147 = None
                              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                              ## I1VALDCL
                              pyxtnm146 = None
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                              ## I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                              ## T1IMPallx(iforitm$work1(1449), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                              ## T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                              def pyxtnm144(arg1, arg2): ## timp: iforitm$work1(1449)
                                pyxtnm115 = arg1
                                pyxtnm116 = arg2
                                ## I1CMP:start
                                ## let
                                pyxtnm143 = None
                                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                ## I1VALDCL
                                pyxtnm134 = None
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                def pyxtnm123(arg1, arg2): ## timp: sint_gt$sint(928)
                                  pyxtnm117 = arg1
                                  pyxtnm118 = arg2
                                  ## I1CMP:start
                                  ## let
                                  pyxtnm122 = None
                                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(119);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(119))))),I1BNDcons(I1TNM(120);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(120))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                                  pyxtnm121 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm117, pyxtnm118))
                                  pyxtnm122 = pyxtnm121
                                  ## end-of(let)
                                  ## I1CMP:return:I1Vtnm(I1TNM(122))
                                  return pyxtnm122
                                ## endtimp(sint_gt$sint(928))
                                pyxtnm124 = XATSDAPP(pyxtnm123(pyxtnm115, XATSINT1(0)))
                                pyxtnm133 = None
                                if (pyxtnm124):
                                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                                  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                  def pyxtnm129(arg1): ## timp: strn_print(1040)
                                    pyxtnm125 = arg1
                                    ## I1CMP:start
                                    ## let
                                    pyxtnm128 = None
                                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(126);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(126))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                                    pyxtnm127 = XATSDAPP(XATS2PY_strn_print(pyxtnm125))
                                    pyxtnm128 = pyxtnm127
                                    ## end-of(let)
                                    ## I1CMP:return:I1Vtnm(I1TNM(128))
                                    return pyxtnm128
                                  ## endtimp(strn_print(1040))
                                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                  ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                  ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
                                  ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                  def pyxtnm130(): ## timp: gseq$sep(348)
                                    ## I1CMP:start
                                    ## I1CMP:return:I1Vstr(...)
                                    return XATSSTRN(",")
                                  ## endtimp(gseq$sep(348))
                                  pyxtnm131 = XATSDAPP(pyxtnm130())
                                  pyxtnm132 = XATSDAPP(pyxtnm129(pyxtnm131))
                                  pyxtnm133 = pyxtnm132
                                ## else: None
                                ## end-of(if)
                                pyxtnm134 = pyxtnm133
                                XATS000_patck(True)
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                pyxtnm141 = None
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                pyxtnm140 = None
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                                ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                def pyxtnm139(arg1): ## timp: sint_print(922)
                                  pyxtnm135 = arg1
                                  ## I1CMP:start
                                  ## let
                                  pyxtnm138 = None
                                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(136);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(136))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                                  pyxtnm137 = XATSDAPP(XATS2PY_sint_print(pyxtnm135))
                                  pyxtnm138 = pyxtnm137
                                  ## end-of(let)
                                  ## I1CMP:return:I1Vtnm(I1TNM(138))
                                  return pyxtnm138
                                ## endtimp(sint_print(922))
                                pyxtnm140 = pyxtnm139
                                pyxtnm141 = pyxtnm140
                                pyxtnm142 = XATSDAPP(pyxtnm141(pyxtnm116))
                                pyxtnm143 = pyxtnm142
                                ## end-of(let)
                                ## I1CMP:return:I1Vtnm(I1TNM(143))
                                return pyxtnm143
                              ## endtimp(iforitm$work1(1449))
                              pyxtnm145 = XATSDAPP(pyxtnm144(pyxtnm113, pyxtnm114))
                              pyxtnm146 = pyxtnm145
                              XATS000_patck(True)
                              pyxtnm147 = XATSBOOL(True)
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(147))
                              return pyxtnm147
                            ## endtimp(iforall$test1(1433))
                            pyxtnm149 = XATSDAPP(pyxtnm148(pyxtnm112, pyxtnm107))
                            pyxtnm150 = pyxtnm149
                            XATS000_patck(True)
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                            ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                            ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                            def pyxtnm153(arg1, arg2): ## timp: p2tr_set(2310)
                              pyxtnm151 = arg1
                              pyxtnm152 = arg2
                              ## I1CMP:start
                              XATS000_assgn(pyxtnm151, pyxtnm152)
                              ## I1CMP:return:I1V000()
                              return XATSVOID
                            ## endtimp(p2tr_set(2310))
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                            ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                            ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                            def pyxtnm160(arg1, arg2): ## timp: sint_add$sint(936)
                              pyxtnm154 = arg1
                              pyxtnm155 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm159 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(156);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(156))))),I1BNDcons(I1TNM(157);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(157))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                              pyxtnm158 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm154, pyxtnm155))
                              pyxtnm159 = pyxtnm158
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(159))
                              return pyxtnm159
                            ## endtimp(sint_add$sint(936))
                            pyxtnm161 = XATSDAPP(pyxtnm160(pyxtnm112, XATSINT1(1)))
                            pyxtnm162 = XATSDAPP(pyxtnm153(pyxtnm57, pyxtnm161))
                            pyxtnm163 = pyxtnm150
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(163))
                            return pyxtnm163
                          ## endtimp(forall$test1(1423))
                          pyxtnm165 = pyxtnm164
                          pyxtnm166 = pyxtnm165
                          pyxtnm167 = XATSDAPP(pyxtnm166(pyxtnm106))
                          pyxtnm168 = pyxtnm167
                          XATS000_patck(True)
                          ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                          ## I1VALDCL
                          ## I1BNDcons(I1TNM(170);I0Ptup0($list());$list())
                          ## I1CMP:start
                          ## I1LETnew1(I1TNM(169);I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(106)))))
                          ## I1CMP(ival):I1Vtnm(I1TNM(169))## I1CMP:return
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                          ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                          ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                          ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                          def pyxtnm173(arg1): ## timp: g_free(23)
                            pyxtnm171 = arg1
                            ## I1CMP:start
                            pyxtnm172 = XATSTUP0([])
                            ## I1CMP:return:I1Vtnm(I1TNM(172))
                            return pyxtnm172
                          ## endtimp(g_free(23))
                          pyxtnm174 = XATSDAPP(pyxtnm173(pyxtnm106))
                          pyxtnm175 = pyxtnm168
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(175))
                          return pyxtnm175
                        ## endtimp(forall$test(47))
                        pyxtnm177 = XATSDAPP(pyxtnm176(pyxtnm84))
                        pyxtnm187 = None
                        if (pyxtnm177):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                          ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                          ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                          def pyxtnm184(arg1, arg2): ## timp: sint_add$sint(936)
                            pyxtnm178 = arg1
                            pyxtnm179 = arg2
                            ## I1CMP:start
                            ## let
                            pyxtnm183 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(180);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(180))))),I1BNDcons(I1TNM(181);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(181))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                            pyxtnm182 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm178, pyxtnm179))
                            pyxtnm183 = pyxtnm182
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(183))
                            return pyxtnm183
                          ## endtimp(sint_add$sint(936))
                          pyxtnm185 = XATSDAPP(pyxtnm184(pyxtnm84, XATSINT1(1)))
                          pyxtnm186 = XATSDAPP(loop_2862(pyxtnm83, pyxtnm185))
                          pyxtnm187 = pyxtnm186
                        else:
                          pyxtnm187 = XATSBOOL(False)
                        ## end-of(if)
                        pyxtnm188 = pyxtnm187
                      ## end-of(if)
                      ## I1CMP:return:I1Vtnm(I1TNM(188))
                      return pyxtnm188
                    pyxtnm189 = XATSDAPP(loop_2862(pyxtnm82, XATSINT1(0)))
                    pyxtnm190 = pyxtnm189
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(190))
                    return pyxtnm190
                  ## endtimp(nint_forall(958))
                  pyxtnm192 = XATSDAPP(pyxtnm191(pyxtnm72))
                  pyxtnm193 = pyxtnm192
                  ## end-of(let)
                  pyxtnm194 = pyxtnm193
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(194))
                  return pyxtnm194
                ## endtimp(gasq_forall(609))
                pyxtnm196 = XATSDAPP(pyxtnm195(pyxtnm67))
                pyxtnm197 = pyxtnm196
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(197))
                return pyxtnm197
              ## endtimp(gseq_forall(386))
              pyxtnm199 = XATSDAPP(pyxtnm198(pyxtnm66))
              pyxtnm200 = pyxtnm199
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(200))
              return pyxtnm200
            ## endtimp(gseq_forall1(1720))
            pyxtnm202 = XATSDAPP(pyxtnm201(pyxtnm55))
            pyxtnm203 = pyxtnm202
            ## end-of(let)
            pyxtnm204 = pyxtnm203
            XATS000_patck(True)
            pyxtnm205 = pyxtnm204
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(205))
            return pyxtnm205
          ## endtimp(gseq_iforall1(1736))
          pyxtnm207 = XATSDAPP(pyxtnm206(pyxtnm49))
          pyxtnm208 = pyxtnm207
          XATS000_patck(True)
          pyxtnm209 = XATSVOID
          ## end-of(let)
          pyxtnm210 = pyxtnm209
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(210))
          return pyxtnm210
        ## endtimp(gseq_iforitm1(1760))
        pyxtnm212 = XATSDAPP(pyxtnm211(pyxtnm30))
        pyxtnm213 = pyxtnm212
        ## end-of(let)
        pyxtnm214 = pyxtnm213
        XATS000_patck(True)
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
        ## I1VALDCL
        pyxtnm223 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm219(arg1): ## timp: strn_print(1040)
          pyxtnm215 = arg1
          ## I1CMP:start
          ## let
          pyxtnm218 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(216);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(216))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm217 = XATSDAPP(XATS2PY_strn_print(pyxtnm215))
          pyxtnm218 = pyxtnm217
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(218))
          return pyxtnm218
        ## endtimp(strn_print(1040))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
        ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
        ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
        ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
        def pyxtnm220(): ## timp: gseq$end(347)
          ## I1CMP:start
          ## I1CMP:return:I1Vstr(...)
          return XATSSTRN(")")
        ## endtimp(gseq$end(347))
        pyxtnm221 = XATSDAPP(pyxtnm220())
        pyxtnm222 = XATSDAPP(pyxtnm219(pyxtnm221))
        pyxtnm223 = pyxtnm222
        XATS000_patck(True)
        pyxtnm224 = XATSVOID
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(224))
        return pyxtnm224
      ## endtimp(gseq_print1(1687))
      pyxtnm226 = XATSDAPP(pyxtnm225(pyxtnm29))
      pyxtnm227 = pyxtnm226
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(227))
      return pyxtnm227
    ## endtimp(g_print(39))
    pyxtnm229 = XATSDAPP(pyxtnm228(pyxtnm14))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
    ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    def pyxtnm231(): ## timp: gs_print$end(804)
      ## I1CMP:start
      pyxtnm230 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(230))
      return pyxtnm230
    ## endtimp(gs_print$end(804))
    pyxtnm232 = XATSDAPP(pyxtnm231())
    pyxtnm233 = pyxtnm232
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(233))
    return pyxtnm233
  ## endtimp(gs_print_a2(807))
  pyxtnm235 = XATSDAPP(pyxtnm234(pyxtnm11, pyxtnm12))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm241 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm240(arg1): ## timp: strn_print(1040)
    pyxtnm236 = arg1
    ## I1CMP:start
    ## let
    pyxtnm239 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(237);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(237))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm238 = XATSDAPP(XATS2PY_strn_print(pyxtnm236))
    pyxtnm239 = pyxtnm238
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(239))
    return pyxtnm239
  ## endtimp(strn_print(1040))
  pyxtnm241 = pyxtnm240
  pyxtnm242 = XATSDAPP(pyxtnm241(XATSSTRN("\n")))
  ## I1CMP:return:I1Vtnm(I1TNM(242))
  return pyxtnm242
## endtimp(gs_println_a2(820))
pyxtnm244 = XATSDAPP(pyxtnm243(XATSSTRN("A0 = "), pyxtnm9))
pyxtnm245 = pyxtnm244
## end-of(let)
pyxtnm246 = pyxtnm245
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(599(line=40,offs=1)--609(line=40,offs=11)))
## I1VALDCL
pyxtnm247 = None
pyxtnm247 = XATSINT1(10)
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(610(line=41,offs=1)--650(line=43,offs=26)))
## I1VALDCL
pyxtnm266 = None
## LCSRCsome1(test02_a1rf000.dats)@(619(line=42,offs=1)--624(line=42,offs=6))
## I0Etapq(I0Ecst(a1rf_make_nfun(1105)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3712(line=189,offs=1)--3726(line=189,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(a1rf_make_nfun(1105), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2920(line=165,offs=1)--3096(line=178,offs=2)))
## T1IMPallx(a1rf_make_nfun(1105)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8864],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_make_nfun(1105);$list(@(a[2971],T2Pvar(a[8864])))))))
def pyxtnm254(arg1, arg2): ## timp: a1rf_make_nfun(1105)
  pyxtnm248 = arg1
  pyxtnm249 = arg2
  ## I1CMP:start
  ## let
  pyxtnm253 = None
  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(3008(line=173,offs=1)--3094(line=177,offs=45)))
  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a1rf_make_nfun(2671));$list(I1FUNDCL(XATS2PY_a1rf_make_nfun(5097);$list(FJARGdarg($list(I1BNDcons(I1TNM(250);I0Pvar(n(5098));$list(@(n(5098),I1Vtnm(I1TNM(250))))),I1BNDcons(I1TNM(251);I0Pvar(f(5099));$list(@(f(5099),I1Vtnm(I1TNM(251))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a1rf_make_nfun);G1Nlist($list())))))))
  pyxtnm252 = XATSDAPP(XATS2PY_a1rf_make_nfun(pyxtnm248, pyxtnm249))
  pyxtnm253 = pyxtnm252
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(253))
  return pyxtnm253
## endtimp(a1rf_make_nfun(1105))
def pyxtnm264(arg1): ## { // lam0(T_LAM(0))
  pyxtnm255 = arg1
  ## I1CMP:start
  ## LCSRCsome1(test02_a1rf000.dats)@(646(line=43,offs=22)--647(line=43,offs=23))
  ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
  ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
  def pyxtnm262(arg1, arg2): ## timp: sint_add$sint(936)
    pyxtnm256 = arg1
    pyxtnm257 = arg2
    ## I1CMP:start
    ## let
    pyxtnm261 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(258);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(258))))),I1BNDcons(I1TNM(259);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(259))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
    pyxtnm260 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm256, pyxtnm257))
    pyxtnm261 = pyxtnm260
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(261))
    return pyxtnm261
  ## endtimp(sint_add$sint(936))
  pyxtnm263 = XATSDAPP(pyxtnm262(pyxtnm255, XATSINT1(1)))
  ## I1CMP:return:I1Vtnm(I1TNM(263))
  return pyxtnm263
## } // end(lam0)
pyxtnm265 = XATSDAPP(pyxtnm254(pyxtnm247, pyxtnm264))
pyxtnm266 = pyxtnm265
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(651(line=44,offs=1)--763(line=52,offs=2)))
## I1VALDCL
pyxtnm564 = None
## let
pyxtnm563 = None
## I1Dimplmnt0(LCSRCsome1(test02_a1rf000.dats)@(707(line=49,offs=1)--761(line=51,offs=36)))
## I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8885])))),@(x0[1875],T2Pvar(x0[8885]))))):timp
## LCSRCsome1(test02_a1rf000.dats)@(660(line=45,offs=1)--668(line=45,offs=9))
## I0Etapq(I0Ecst(gs_println_a4(822)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13918(line=908,offs=1)--13931(line=908,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
## T1IMPallx(gs_println_a4(822), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26458(line=1604,offs=1)--26602(line=1613,offs=59)))
## T1IMPallx(gs_println_a4(822)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7101],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7102],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7103],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7104],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a4(822);$list(@(x0[2570],T2Pvar(x0[7101])),@(x1[2571],T2Pvar(x1[7102])),@(x2[2572],T2Pvar(x2[7103])),@(x3[2573],T2Pvar(x3[7104])))))))
def pyxtnm556(arg1, arg2, arg3, arg4): ## timp: gs_println_a4(822)
  pyxtnm268 = arg1
  pyxtnm269 = arg2
  pyxtnm270 = arg3
  pyxtnm271 = arg4
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26546(line=1613,offs=3)--26557(line=1613,offs=14))
  ## I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Pvar(x0[7101]))),T2JAG($list(T2Pvar(x1[7102]))),T2JAG($list(T2Pvar(x2[7103]))),T2JAG($list(T2Pvar(x3[7104])))))
  ## T1IMPallx(gs_print_a4(809), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
  ## T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
  def pyxtnm547(arg1, arg2, arg3, arg4): ## timp: gs_print_a4(809)
    pyxtnm272 = arg1
    pyxtnm273 = arg2
    pyxtnm274 = arg3
    pyxtnm275 = arg4
    ## I1CMP:start
    ## let
    pyxtnm546 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
    ## I1VALDCL
    pyxtnm279 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
    ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    def pyxtnm277(): ## timp: gs_print$beg(802)
      ## I1CMP:start
      pyxtnm276 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(276))
      return pyxtnm276
    ## endtimp(gs_print$beg(802))
    pyxtnm278 = XATSDAPP(pyxtnm277())
    pyxtnm279 = pyxtnm278
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    pyxtnm285 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm284(arg1): ## timp: strn_print(1040)
      pyxtnm280 = arg1
      ## I1CMP:start
      ## let
      pyxtnm283 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(281);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(281))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm282 = XATSDAPP(XATS2PY_strn_print(pyxtnm280))
      pyxtnm283 = pyxtnm282
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(283))
      return pyxtnm283
    ## endtimp(strn_print(1040))
    pyxtnm285 = pyxtnm284
    pyxtnm286 = XATSDAPP(pyxtnm285(pyxtnm272))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
    ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    def pyxtnm288(): ## timp: gs_print$sep(803)
      ## I1CMP:start
      pyxtnm287 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(287))
      return pyxtnm287
    ## endtimp(gs_print$sep(803))
    pyxtnm289 = XATSDAPP(pyxtnm288())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
    def pyxtnm327(arg1): ## timp: g_print(39)
      pyxtnm290 = arg1
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1618(line=53,offs=1)--1720(line=60,offs=32)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(vt[7260],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(a1rf);$list(T2Pvar(vt[7260])))))))))
      def pyxtnm311(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1673(line=59,offs=1)--1678(line=59,offs=6))
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
        pyxtnm296 = XATSDAPP(pyxtnm295(XATSSTRN("a1rf(")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1689(line=60,offs=1)--1696(line=60,offs=8))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vt[7260])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
        def pyxtnm303(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm301(arg1): ## timp: strn_print(1040)
            pyxtnm297 = arg1
            ## I1CMP:start
            ## let
            pyxtnm300 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(298);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(298))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm299 = XATSDAPP(XATS2PY_strn_print(pyxtnm297))
            pyxtnm300 = pyxtnm299
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(300))
            return pyxtnm300
          ## endtimp(strn_print(1040))
          pyxtnm302 = XATSDAPP(pyxtnm301(XATSSTRN("sint")))
          ## I1CMP:return:I1Vtnm(I1TNM(302))
          return pyxtnm302
        ## endtimp(g_ptype(202))
        pyxtnm304 = XATSDAPP(pyxtnm303())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1709(line=60,offs=21)--1714(line=60,offs=26))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm309(arg1): ## timp: strn_print(1040)
          pyxtnm305 = arg1
          ## I1CMP:start
          ## let
          pyxtnm308 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(306);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(306))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm307 = XATSDAPP(XATS2PY_strn_print(pyxtnm305))
          pyxtnm308 = pyxtnm307
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(308))
          return pyxtnm308
        ## endtimp(strn_print(1040))
        pyxtnm310 = XATSDAPP(pyxtnm309(XATSSTRN(")")))
        ## I1CMP:return:I1Vtnm(I1TNM(310))
        return pyxtnm310
      ## endtimp(g_ptype(202))
      pyxtnm312 = XATSDAPP(pyxtnm311())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm317(arg1): ## timp: strn_print(1040)
        pyxtnm313 = arg1
        ## I1CMP:start
        ## let
        pyxtnm316 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(314);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(314))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm315 = XATSDAPP(XATS2PY_strn_print(pyxtnm313))
        pyxtnm316 = pyxtnm315
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(316))
        return pyxtnm316
      ## endtimp(strn_print(1040))
      pyxtnm318 = XATSDAPP(pyxtnm317(XATSSTRN(":")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
      ## I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
      ## T1IMPallx(g_psort(201), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1831(line=74,offs=1)--1885(line=78,offs=22)))
      ## T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(tx[5755],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(tx[5755])))))))
      def pyxtnm325(): ## timp: g_psort(201)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1866(line=78,offs=3)--1876(line=78,offs=13))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm323(arg1): ## timp: strn_print(1040)
          pyxtnm319 = arg1
          ## I1CMP:start
          ## let
          pyxtnm322 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(320);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(320))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm321 = XATSDAPP(XATS2PY_strn_print(pyxtnm319))
          pyxtnm322 = pyxtnm321
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(322))
          return pyxtnm322
        ## endtimp(strn_print(1040))
        pyxtnm324 = XATSDAPP(pyxtnm323(XATSSTRN("tbox")))
        ## I1CMP:return:I1Vtnm(I1TNM(324))
        return pyxtnm324
      ## endtimp(g_psort(201))
      pyxtnm326 = XATSDAPP(pyxtnm325())
      ## I1CMP:return:I1Vtnm(I1TNM(326))
      return pyxtnm326
    ## endtimp(g_print(39))
    pyxtnm328 = XATSDAPP(pyxtnm327(pyxtnm273))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
    ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    def pyxtnm330(): ## timp: gs_print$sep(803)
      ## I1CMP:start
      pyxtnm329 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(329))
      return pyxtnm329
    ## endtimp(gs_print$sep(803))
    pyxtnm331 = XATSDAPP(pyxtnm330())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    pyxtnm337 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm336(arg1): ## timp: strn_print(1040)
      pyxtnm332 = arg1
      ## I1CMP:start
      ## let
      pyxtnm335 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(333);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(333))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm334 = XATSDAPP(XATS2PY_strn_print(pyxtnm332))
      pyxtnm335 = pyxtnm334
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(335))
      return pyxtnm335
    ## endtimp(strn_print(1040))
    pyxtnm337 = pyxtnm336
    pyxtnm338 = XATSDAPP(pyxtnm337(pyxtnm274))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
    ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    def pyxtnm340(): ## timp: gs_print$sep(803)
      ## I1CMP:start
      pyxtnm339 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(339))
      return pyxtnm339
    ## endtimp(gs_print$sep(803))
    pyxtnm341 = XATSDAPP(pyxtnm340())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2186(line=97,offs=1)--2419(line=115,offs=4)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7263])))))))))
    def pyxtnm541(arg1): ## timp: g_print(39)
      pyxtnm342 = arg1
      ## I1CMP:start
      ## let
      pyxtnm540 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2244(line=104,offs=1)--2266(line=104,offs=23))
      ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1rf);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7263])))))))
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
      ## I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7263]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
      ## I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7263]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
      ## I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7263]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2388(line=114,offs=3)--2399(line=114,offs=14))
      ## I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7263]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7263])))))
      ## T1IMPallx(gseq_print1(1687), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
      ## T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
      def pyxtnm538(arg1): ## timp: gseq_print1(1687)
        pyxtnm343 = arg1
        ## I1CMP:start
        ## let
        pyxtnm537 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
        ## I1VALDCL
        pyxtnm352 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm348(arg1): ## timp: strn_print(1040)
          pyxtnm344 = arg1
          ## I1CMP:start
          ## let
          pyxtnm347 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(345);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(345))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm346 = XATSDAPP(XATS2PY_strn_print(pyxtnm344))
          pyxtnm347 = pyxtnm346
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(347))
          return pyxtnm347
        ## endtimp(strn_print(1040))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
        ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
        ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
        ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
        def pyxtnm349(): ## timp: gseq$beg(346)
          ## I1CMP:start
          ## I1CMP:return:I1Vstr(...)
          return XATSSTRN("a1rf(")
        ## endtimp(gseq$beg(346))
        pyxtnm350 = XATSDAPP(pyxtnm349())
        pyxtnm351 = XATSDAPP(pyxtnm348(pyxtnm350))
        pyxtnm352 = pyxtnm351
        XATS000_patck(True)
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
        ## I1VALDCL
        pyxtnm527 = None
        ## let
        pyxtnm526 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
        ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
        ## T1IMPallx(gseq_iforitm1(1760), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
        ## T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
        def pyxtnm524(arg1): ## timp: gseq_iforitm1(1760)
          pyxtnm362 = arg1
          ## I1CMP:start
          ## let
          pyxtnm523 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
          ## let
          pyxtnm522 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
          ## I1VALDCL
          pyxtnm521 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
          ## T1IMPallx(gseq_iforall1(1736), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
          ## T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
          def pyxtnm519(arg1): ## timp: gseq_iforall1(1736)
            pyxtnm368 = arg1
            ## I1CMP:start
            ## let
            pyxtnm518 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm369 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
            ## I1VALDCL
            pyxtnm370 = None
            pyxtnm370 = XATSADDR(pyxtnm369)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
            ## I1VALDCL
            pyxtnm517 = None
            ## let
            pyxtnm516 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
            ## T1IMPallx(gseq_forall1(1720), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
            ## T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
            def pyxtnm514(arg1): ## timp: gseq_forall1(1720)
              pyxtnm379 = arg1
              ## I1CMP:start
              ## let
              pyxtnm513 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
              ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
              ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
              ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2740(line=141,offs=1)--2882(line=152,offs=2)))
              ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7287])))),@(x0[1168],T2Pvar(x0[7287])))))))
              def pyxtnm511(arg1): ## timp: gseq_forall(386)
                pyxtnm380 = arg1
                ## I1CMP:start
                ## let
                pyxtnm510 = None
                ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7287]))))):timp
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2798(line=147,offs=1)--2809(line=147,offs=12))
                ## I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7287]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7287])))))
                ## T1IMPallx(gasq_forall(609), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                ## T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                def pyxtnm508(arg1): ## timp: gasq_forall(609)
                  pyxtnm381 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm507 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                  ## I1VALDCL
                  pyxtnm385 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                  ## I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                  ## T1IMPallx(gasq_length(594), LCSRCsome1(test02_a1rf000.dats)@(707(line=49,offs=1)--761(line=51,offs=36)))
                  ## T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8885],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8885],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8885])))),@(x0[1875],T2Pvar(x0[8885])))))))
                  def pyxtnm383(arg1): ## timp: gasq_length(594)
                    pyxtnm382 = arg1
                    ## I1CMP:start
                    ## I1CMP:return:I1Vtnm(I1TNM(247))
                    return pyxtnm247
                  ## endtimp(gasq_length(594))
                  pyxtnm384 = XATSDAPP(pyxtnm383(pyxtnm381))
                  pyxtnm385 = pyxtnm384
                  XATS000_patck(True)
                  ## let
                  pyxtnm506 = None
                  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                  ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                  ## I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                  ## T1IMPallx(nint_forall(958), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                  ## T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                  def pyxtnm504(arg1): ## timp: nint_forall(958)
                    pyxtnm395 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm503 = None
                    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                    ## I1FUNDCL
                    def loop_2862(arg1, arg2): ## fun
                      pyxtnm396 = arg1
                      pyxtnm397 = arg2
                      ## I1CMP:start
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                      def pyxtnm404(arg1, arg2): ## timp: sint_gte$sint(931)
                        pyxtnm398 = arg1
                        pyxtnm399 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm403 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(400);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(400))))),I1BNDcons(I1TNM(401);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(401))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                        pyxtnm402 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm398, pyxtnm399))
                        pyxtnm403 = pyxtnm402
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(403))
                        return pyxtnm403
                      ## endtimp(sint_gte$sint(931))
                      pyxtnm405 = XATSDAPP(pyxtnm404(pyxtnm397, pyxtnm396))
                      pyxtnm501 = None
                      if (pyxtnm405):
                        pyxtnm501 = XATSBOOL(True)
                      else:
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                        ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                        ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                        ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                        def pyxtnm489(arg1): ## timp: forall$test(47)
                          pyxtnm406 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm488 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                          ## I1VALDCL
                          pyxtnm419 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                          ## I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                          ## T1IMPallx(gasq_lget$at$raw(2326), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4092(line=227,offs=1)--4187(line=231,offs=35)))
                          ## T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7276])))),@(x0[5735],T2Pvar(x0[7276])))))))
                          def pyxtnm417(arg1, arg2): ## timp: gasq_lget$at$raw(2326)
                            pyxtnm407 = arg1
                            pyxtnm408 = arg2
                            ## I1CMP:start
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4165(line=231,offs=13)--4177(line=231,offs=25))
                            ## I0Etapq(I0Ecst(a1rf_lget$at(1111)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(4779(line=262,offs=1)--4791(line=262,offs=13))));$list(T2JAG($list(T2Pvar(x0[7276])))))
                            ## T1IMPallx(a1rf_lget$at(1111), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2309(line=113,offs=1)--2486(line=128,offs=2)))
                            ## T1IMPallx(a1rf_lget$at(1111)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_lget$at(1111);$list(@(a[2983],T2Pvar(a[8858])))))))
                            def pyxtnm415(arg1, arg2): ## timp: a1rf_lget$at(1111)
                              pyxtnm409 = arg1
                              pyxtnm410 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm414 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2393(line=121,offs=1)--2484(line=127,offs=38)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a1rf_lget$at(2668));$list(I1FUNDCL(XATS2PY_a1rf_lget$at(5078);$list(FJARGdarg($list(I1BNDcons(I1TNM(411);I0Pvar(A(5079));$list(@(A(5079),I1Vtnm(I1TNM(411))))),I1BNDcons(I1TNM(412);I0Pvar(i(5080));$list(@(i(5080),I1Vtnm(I1TNM(412))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a1rf_lget$at);G1Nlist($list())))))))
                              pyxtnm413 = XATSDAPP(XATS2PY_a1rf_lget_at(pyxtnm409, pyxtnm410))
                              pyxtnm414 = pyxtnm413
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(414))
                              return pyxtnm414
                            ## endtimp(a1rf_lget$at(1111))
                            pyxtnm416 = XATSDAPP(pyxtnm415(pyxtnm407, pyxtnm408))
                            ## I1CMP:return:I1Vtnm(I1TNM(416))
                            return pyxtnm416
                          ## endtimp(gasq_lget$at$raw(2326))
                          pyxtnm418 = XATSDAPP(pyxtnm417(pyxtnm381, pyxtnm406))
                          pyxtnm419 = pyxtnm418
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                          ## I1VALDCL
                          pyxtnm481 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                          ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                          ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                          ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          pyxtnm479 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2865(line=151,offs=20)--2876(line=151,offs=31))
                          ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7287])))))
                          ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                          ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          pyxtnm478 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                          ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                          ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                          ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          def pyxtnm477(arg1): ## timp: forall$test1(1423)
                            pyxtnm420 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm476 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                            ## I1VALDCL
                            pyxtnm425 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                            ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                            ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                            def pyxtnm423(arg1): ## timp: p2tr_get(2309)
                              pyxtnm421 = arg1
                              ## I1CMP:start
                              pyxtnm422 = XATS000_dp2tr(pyxtnm421)
                              ## I1CMP:return:I1Vtnm(I1TNM(422))
                              return pyxtnm422
                            ## endtimp(p2tr_get(2309))
                            pyxtnm424 = XATSDAPP(pyxtnm423(pyxtnm370))
                            pyxtnm425 = pyxtnm424
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                            ## I1VALDCL
                            pyxtnm463 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                            ## I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                            ## T1IMPallx(iforall$test1(1433), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                            ## T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                            def pyxtnm461(arg1, arg2): ## timp: iforall$test1(1433)
                              pyxtnm426 = arg1
                              pyxtnm427 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm460 = None
                              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                              ## I1VALDCL
                              pyxtnm459 = None
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                              ## I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                              ## T1IMPallx(iforitm$work1(1449), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                              ## T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                              def pyxtnm457(arg1, arg2): ## timp: iforitm$work1(1449)
                                pyxtnm428 = arg1
                                pyxtnm429 = arg2
                                ## I1CMP:start
                                ## let
                                pyxtnm456 = None
                                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                ## I1VALDCL
                                pyxtnm447 = None
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                def pyxtnm436(arg1, arg2): ## timp: sint_gt$sint(928)
                                  pyxtnm430 = arg1
                                  pyxtnm431 = arg2
                                  ## I1CMP:start
                                  ## let
                                  pyxtnm435 = None
                                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(432);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(432))))),I1BNDcons(I1TNM(433);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(433))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                                  pyxtnm434 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm430, pyxtnm431))
                                  pyxtnm435 = pyxtnm434
                                  ## end-of(let)
                                  ## I1CMP:return:I1Vtnm(I1TNM(435))
                                  return pyxtnm435
                                ## endtimp(sint_gt$sint(928))
                                pyxtnm437 = XATSDAPP(pyxtnm436(pyxtnm428, XATSINT1(0)))
                                pyxtnm446 = None
                                if (pyxtnm437):
                                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                                  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                  def pyxtnm442(arg1): ## timp: strn_print(1040)
                                    pyxtnm438 = arg1
                                    ## I1CMP:start
                                    ## let
                                    pyxtnm441 = None
                                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(439);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(439))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                                    pyxtnm440 = XATSDAPP(XATS2PY_strn_print(pyxtnm438))
                                    pyxtnm441 = pyxtnm440
                                    ## end-of(let)
                                    ## I1CMP:return:I1Vtnm(I1TNM(441))
                                    return pyxtnm441
                                  ## endtimp(strn_print(1040))
                                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                  ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                  ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
                                  ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                  def pyxtnm443(): ## timp: gseq$sep(348)
                                    ## I1CMP:start
                                    ## I1CMP:return:I1Vstr(...)
                                    return XATSSTRN(",")
                                  ## endtimp(gseq$sep(348))
                                  pyxtnm444 = XATSDAPP(pyxtnm443())
                                  pyxtnm445 = XATSDAPP(pyxtnm442(pyxtnm444))
                                  pyxtnm446 = pyxtnm445
                                ## else: None
                                ## end-of(if)
                                pyxtnm447 = pyxtnm446
                                XATS000_patck(True)
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                pyxtnm454 = None
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                pyxtnm453 = None
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                                ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                def pyxtnm452(arg1): ## timp: sint_print(922)
                                  pyxtnm448 = arg1
                                  ## I1CMP:start
                                  ## let
                                  pyxtnm451 = None
                                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(449);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(449))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                                  pyxtnm450 = XATSDAPP(XATS2PY_sint_print(pyxtnm448))
                                  pyxtnm451 = pyxtnm450
                                  ## end-of(let)
                                  ## I1CMP:return:I1Vtnm(I1TNM(451))
                                  return pyxtnm451
                                ## endtimp(sint_print(922))
                                pyxtnm453 = pyxtnm452
                                pyxtnm454 = pyxtnm453
                                pyxtnm455 = XATSDAPP(pyxtnm454(pyxtnm429))
                                pyxtnm456 = pyxtnm455
                                ## end-of(let)
                                ## I1CMP:return:I1Vtnm(I1TNM(456))
                                return pyxtnm456
                              ## endtimp(iforitm$work1(1449))
                              pyxtnm458 = XATSDAPP(pyxtnm457(pyxtnm426, pyxtnm427))
                              pyxtnm459 = pyxtnm458
                              XATS000_patck(True)
                              pyxtnm460 = XATSBOOL(True)
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(460))
                              return pyxtnm460
                            ## endtimp(iforall$test1(1433))
                            pyxtnm462 = XATSDAPP(pyxtnm461(pyxtnm425, pyxtnm420))
                            pyxtnm463 = pyxtnm462
                            XATS000_patck(True)
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                            ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                            ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                            def pyxtnm466(arg1, arg2): ## timp: p2tr_set(2310)
                              pyxtnm464 = arg1
                              pyxtnm465 = arg2
                              ## I1CMP:start
                              XATS000_assgn(pyxtnm464, pyxtnm465)
                              ## I1CMP:return:I1V000()
                              return XATSVOID
                            ## endtimp(p2tr_set(2310))
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                            ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                            ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                            def pyxtnm473(arg1, arg2): ## timp: sint_add$sint(936)
                              pyxtnm467 = arg1
                              pyxtnm468 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm472 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(469);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(469))))),I1BNDcons(I1TNM(470);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(470))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                              pyxtnm471 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm467, pyxtnm468))
                              pyxtnm472 = pyxtnm471
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(472))
                              return pyxtnm472
                            ## endtimp(sint_add$sint(936))
                            pyxtnm474 = XATSDAPP(pyxtnm473(pyxtnm425, XATSINT1(1)))
                            pyxtnm475 = XATSDAPP(pyxtnm466(pyxtnm370, pyxtnm474))
                            pyxtnm476 = pyxtnm463
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(476))
                            return pyxtnm476
                          ## endtimp(forall$test1(1423))
                          pyxtnm478 = pyxtnm477
                          pyxtnm479 = pyxtnm478
                          pyxtnm480 = XATSDAPP(pyxtnm479(pyxtnm419))
                          pyxtnm481 = pyxtnm480
                          XATS000_patck(True)
                          ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                          ## I1VALDCL
                          ## I1BNDcons(I1TNM(483);I0Ptup0($list());$list())
                          ## I1CMP:start
                          ## I1LETnew1(I1TNM(482);I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(419)))))
                          ## I1CMP(ival):I1Vtnm(I1TNM(482))## I1CMP:return
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                          ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                          ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                          ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                          def pyxtnm486(arg1): ## timp: g_free(23)
                            pyxtnm484 = arg1
                            ## I1CMP:start
                            pyxtnm485 = XATSTUP0([])
                            ## I1CMP:return:I1Vtnm(I1TNM(485))
                            return pyxtnm485
                          ## endtimp(g_free(23))
                          pyxtnm487 = XATSDAPP(pyxtnm486(pyxtnm419))
                          pyxtnm488 = pyxtnm481
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(488))
                          return pyxtnm488
                        ## endtimp(forall$test(47))
                        pyxtnm490 = XATSDAPP(pyxtnm489(pyxtnm397))
                        pyxtnm500 = None
                        if (pyxtnm490):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                          ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                          ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                          def pyxtnm497(arg1, arg2): ## timp: sint_add$sint(936)
                            pyxtnm491 = arg1
                            pyxtnm492 = arg2
                            ## I1CMP:start
                            ## let
                            pyxtnm496 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(493);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(493))))),I1BNDcons(I1TNM(494);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(494))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                            pyxtnm495 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm491, pyxtnm492))
                            pyxtnm496 = pyxtnm495
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(496))
                            return pyxtnm496
                          ## endtimp(sint_add$sint(936))
                          pyxtnm498 = XATSDAPP(pyxtnm497(pyxtnm397, XATSINT1(1)))
                          pyxtnm499 = XATSDAPP(loop_2862(pyxtnm396, pyxtnm498))
                          pyxtnm500 = pyxtnm499
                        else:
                          pyxtnm500 = XATSBOOL(False)
                        ## end-of(if)
                        pyxtnm501 = pyxtnm500
                      ## end-of(if)
                      ## I1CMP:return:I1Vtnm(I1TNM(501))
                      return pyxtnm501
                    pyxtnm502 = XATSDAPP(loop_2862(pyxtnm395, XATSINT1(0)))
                    pyxtnm503 = pyxtnm502
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(503))
                    return pyxtnm503
                  ## endtimp(nint_forall(958))
                  pyxtnm505 = XATSDAPP(pyxtnm504(pyxtnm385))
                  pyxtnm506 = pyxtnm505
                  ## end-of(let)
                  pyxtnm507 = pyxtnm506
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(507))
                  return pyxtnm507
                ## endtimp(gasq_forall(609))
                pyxtnm509 = XATSDAPP(pyxtnm508(pyxtnm380))
                pyxtnm510 = pyxtnm509
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(510))
                return pyxtnm510
              ## endtimp(gseq_forall(386))
              pyxtnm512 = XATSDAPP(pyxtnm511(pyxtnm379))
              pyxtnm513 = pyxtnm512
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(513))
              return pyxtnm513
            ## endtimp(gseq_forall1(1720))
            pyxtnm515 = XATSDAPP(pyxtnm514(pyxtnm368))
            pyxtnm516 = pyxtnm515
            ## end-of(let)
            pyxtnm517 = pyxtnm516
            XATS000_patck(True)
            pyxtnm518 = pyxtnm517
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(518))
            return pyxtnm518
          ## endtimp(gseq_iforall1(1736))
          pyxtnm520 = XATSDAPP(pyxtnm519(pyxtnm362))
          pyxtnm521 = pyxtnm520
          XATS000_patck(True)
          pyxtnm522 = XATSVOID
          ## end-of(let)
          pyxtnm523 = pyxtnm522
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(523))
          return pyxtnm523
        ## endtimp(gseq_iforitm1(1760))
        pyxtnm525 = XATSDAPP(pyxtnm524(pyxtnm343))
        pyxtnm526 = pyxtnm525
        ## end-of(let)
        pyxtnm527 = pyxtnm526
        XATS000_patck(True)
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
        ## I1VALDCL
        pyxtnm536 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm532(arg1): ## timp: strn_print(1040)
          pyxtnm528 = arg1
          ## I1CMP:start
          ## let
          pyxtnm531 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(529);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(529))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm530 = XATSDAPP(XATS2PY_strn_print(pyxtnm528))
          pyxtnm531 = pyxtnm530
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(531))
          return pyxtnm531
        ## endtimp(strn_print(1040))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
        ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
        ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
        ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
        def pyxtnm533(): ## timp: gseq$end(347)
          ## I1CMP:start
          ## I1CMP:return:I1Vstr(...)
          return XATSSTRN(")")
        ## endtimp(gseq$end(347))
        pyxtnm534 = XATSDAPP(pyxtnm533())
        pyxtnm535 = XATSDAPP(pyxtnm532(pyxtnm534))
        pyxtnm536 = pyxtnm535
        XATS000_patck(True)
        pyxtnm537 = XATSVOID
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(537))
        return pyxtnm537
      ## endtimp(gseq_print1(1687))
      pyxtnm539 = XATSDAPP(pyxtnm538(pyxtnm342))
      pyxtnm540 = pyxtnm539
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(540))
      return pyxtnm540
    ## endtimp(g_print(39))
    pyxtnm542 = XATSDAPP(pyxtnm541(pyxtnm275))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
    ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    def pyxtnm544(): ## timp: gs_print$end(804)
      ## I1CMP:start
      pyxtnm543 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(543))
      return pyxtnm543
    ## endtimp(gs_print$end(804))
    pyxtnm545 = XATSDAPP(pyxtnm544())
    pyxtnm546 = pyxtnm545
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(546))
    return pyxtnm546
  ## endtimp(gs_print_a4(809))
  pyxtnm548 = XATSDAPP(pyxtnm547(pyxtnm268, pyxtnm269, pyxtnm270, pyxtnm271))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26588(line=1613,offs=45)--26595(line=1613,offs=52))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm554 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm553(arg1): ## timp: strn_print(1040)
    pyxtnm549 = arg1
    ## I1CMP:start
    ## let
    pyxtnm552 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(550);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(550))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm551 = XATSDAPP(XATS2PY_strn_print(pyxtnm549))
    pyxtnm552 = pyxtnm551
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(552))
    return pyxtnm552
  ## endtimp(strn_print(1040))
  pyxtnm554 = pyxtnm553
  pyxtnm555 = XATSDAPP(pyxtnm554(XATSSTRN("\n")))
  ## I1CMP:return:I1Vtnm(I1TNM(555))
  return pyxtnm555
## endtimp(gs_println_a4(822))
## LCSRCsome1(test02_a1rf000.dats)@(677(line=46,offs=9)--681(line=46,offs=13))
## I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
## T1IMPallx(g_type(196), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
## T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
def pyxtnm560(arg1): ## timp: g_type(196)
  pyxtnm557 = arg1
  ## I1CMP:start
  pyxtnm558 = XATSCAPP("unit", [0])
  pyxtnm559 = XATSCAST("castxy_1839", [pyxtnm558])
  ## I1CMP:return:I1Vtnm(I1TNM(559))
  return pyxtnm559
## endtimp(g_type(196))
pyxtnm561 = XATSDAPP(pyxtnm560(pyxtnm266))
pyxtnm562 = XATSDAPP(pyxtnm556(XATSSTRN("A1("), pyxtnm561, XATSSTRN(") = "), pyxtnm266))
pyxtnm563 = pyxtnm562
## end-of(let)
pyxtnm564 = pyxtnm563
XATS000_patck(True)
## I1Dfundclist(LCSRCsome1(test02_a1rf000.dats)@(790(line=56,offs=1)--916(line=66,offs=35)))
## I1FUNDCL
def fact_793(arg1): ## fun
  pyxtnm565 = arg1
  ## I1CMP:start
  ## let
  pyxtnm742 = None
  ## I1Dimplmnt0(LCSRCsome1(test02_a1rf000.dats)@(863(line=64,offs=1)--914(line=66,offs=33)))
  ## I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8886])))),@(x0[1875],T2Pvar(x0[8886]))))):timp
  ## LCSRCsome1(test02_a1rf000.dats)@(847(line=61,offs=25)--854(line=61,offs=32))
  ## I0Etapq(I0Ecst(GSEQ_prod(249)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2953(line=150,offs=1)--2962(line=150,offs=10))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  ## T1IMPallx(GSEQ_prod(249), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2187(line=101,offs=1)--2283(line=108,offs=35)))
  ## T1IMPallx(GSEQ_prod(249)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6659],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6660],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_prod(249);$list(@(xs[825],T2Pvar(xs[6659])),@(x0[826],T2Pvar(x0[6660])))))))
  def pyxtnm721(arg1): ## timp: GSEQ_prod(249)
    pyxtnm567 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2239(line=107,offs=1)--2248(line=107,offs=10))
    ## I0Etapq(I0Ecst(gseq_prod(345)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2064(line=105,offs=1)--2073(line=105,offs=10))));$list(T2JAG($list(T2Pvar(xs[6659]))),T2JAG($list(T2Pvar(x0[6660])))))
    ## T1IMPallx(gseq_prod(345), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2634(line=144,offs=1)--2693(line=147,offs=31)))
    ## T1IMPallx(gseq_prod(345)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6050],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6051],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_prod(345);$list(@(xs[1065],T2Pvar(xs[6050])),@(x0[1066],T2Pvar(x0[6051])))))))
    pyxtnm715 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2675(line=147,offs=13)--2685(line=147,offs=23))
    ## I0Etapq(I0Ecst(gseq_prod0(1667)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(2132(line=108,offs=1)--2142(line=108,offs=11))));$list(T2JAG($list(T2Pvar(xs[6050]))),T2JAG($list(T2Pvar(x0[6051])))))
    ## T1IMPallx(gseq_prod0(1667), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(1943(line=75,offs=1)--2120(line=87,offs=4)))
    ## T1IMPallx(gseq_prod0(1667)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7891],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_prod0(1667);$list(@(xs[4181],T2Pvar(xs[7891])),@(x0[4182],T2Pvar(x0[7892])))))))
    def pyxtnm714(arg1): ## timp: gseq_prod0(1667)
      pyxtnm568 = arg1
      ## I1CMP:start
      ## let
      pyxtnm713 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(1993(line=80,offs=1)--2011(line=80,offs=19)))
      ## I1VALDCL
      pyxtnm571 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2002(line=80,offs=10)--2005(line=80,offs=13))
      ## I0Etapq(I0Ecst(g_1(211)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gnum000.sats)@(1457(line=46,offs=1)--1460(line=46,offs=4))));$list(T2JAG($list(T2Pvar(x0[7892])))))
      ## T1IMPallx(g_1(211), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(1619(line=51,offs=1)--1645(line=52,offs=18)))
      ## T1IMPallx(g_1(211)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_1(211);$list(@(a[779],T2Pcst(si)))))))
      def pyxtnm569(): ## timp: g_1(211)
        ## I1CMP:start
        ## I1CMP:return:I1Vint(T_INT01(1))
        return XATSINT1(1)
      ## endtimp(g_1(211))
      pyxtnm570 = XATSDAPP(pyxtnm569())
      pyxtnm571 = pyxtnm570
      XATS000_patck(True)
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2012(line=81,offs=1)--2074(line=84,offs=31)))
      ## I1Dimplmnt0(DIMPLone2(folditm$fopr0(1454);$list(@(x0[3797],T2Pvar(x0[7892])),@(r0[3798],T2Pvar(x0[7892]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2083(line=86,offs=1)--2096(line=86,offs=14))
      ## I0Etapq(I0Ecst(gseq_folditm0(1767)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(12340(line=666,offs=1)--12353(line=666,offs=14))));$list(T2JAG($list(T2Pvar(xs[7891]))),T2JAG($list(T2Pvar(x0[7892]))),T2JAG($list(T2Pvar(x0[7892])))))
      ## T1IMPallx(gseq_folditm0(1767), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11599(line=792,offs=1)--11911(line=818,offs=2)))
      ## T1IMPallx(gseq_folditm0(1767)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8054],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8055],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[8056],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_folditm0(1767);$list(@(xs[4418],T2Pvar(xs[8054])),@(x0[4419],T2Pvar(x0[8055])),@(r0[4420],T2Pvar(r0[8056])))))))
      def pyxtnm711(arg1, arg2): ## timp: gseq_folditm0(1767)
        pyxtnm575 = arg1
        pyxtnm576 = arg2
        ## I1CMP:start
        ## let
        pyxtnm710 = None
        ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11679(line=800,offs=1)--11694(line=800,offs=16)))
        ## I1VARDCL
        ## I1CMP:start
        ## I1CMP:return:I1Vtnm(I1TNM(576))
        pyxtnm577 = XATSVAR1(pyxtnm576)
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11698(line=802,offs=1)--11716(line=802,offs=19)))
        ## I1VALDCL
        pyxtnm578 = None
        pyxtnm578 = XATSADDR(pyxtnm577)
        XATS000_patck(True)
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11720(line=804,offs=1)--11906(line=816,offs=41)))
        ## I1VALDCL
        pyxtnm708 = None
        ## let
        pyxtnm707 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11766(line=809,offs=1)--11905(line=816,offs=40)))
        ## I1Dimplmnt0(DIMPLone2(foritm$work0(1442);$list(@(x0[3785],T2Pvar(x0[8055]))))):timp
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11731(line=806,offs=1)--11743(line=806,offs=13))
        ## I0Etapq(I0Ecst(gseq_foritm0(1751)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(9424(line=503,offs=1)--9436(line=503,offs=13))));$list(T2JAG($list(T2Pvar(xs[8054]))),T2JAG($list(T2Pvar(x0[8055])))))
        ## T1IMPallx(gseq_foritm0(1751), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8019(line=527,offs=1)--8210(line=544,offs=2)))
        ## T1IMPallx(gseq_foritm0(1751)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8022],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8023],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm0(1751);$list(@(xs[4386],T2Pvar(xs[8022])),@(x0[4387],T2Pvar(x0[8023])))))))
        def pyxtnm705(arg1): ## timp: gseq_foritm0(1751)
          pyxtnm586 = arg1
          ## I1CMP:start
          ## let
          pyxtnm704 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8131(line=539,offs=1)--8208(line=543,offs=33)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8023]))))):timp
          ## let
          pyxtnm703 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8078(line=534,offs=1)--8111(line=536,offs=13)))
          ## I1VALDCL
          pyxtnm702 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8086(line=535,offs=1)--8098(line=535,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8022]))),T2JAG($list(T2Pvar(x0[8023])))))
          ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
          ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
          def pyxtnm700(arg1): ## timp: gseq_forall0(1719)
            pyxtnm591 = arg1
            ## I1CMP:start
            ## let
            pyxtnm699 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
            ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
            ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2740(line=141,offs=1)--2882(line=152,offs=2)))
            ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7287])))),@(x0[1168],T2Pvar(x0[7287])))))))
            def pyxtnm697(arg1): ## timp: gseq_forall(386)
              pyxtnm592 = arg1
              ## I1CMP:start
              ## let
              pyxtnm696 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
              ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7287]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2798(line=147,offs=1)--2809(line=147,offs=12))
              ## I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7287]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7287])))))
              ## T1IMPallx(gasq_forall(609), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
              ## T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
              def pyxtnm694(arg1): ## timp: gasq_forall(609)
                pyxtnm593 = arg1
                ## I1CMP:start
                ## let
                pyxtnm693 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                ## I1VALDCL
                pyxtnm597 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                ## I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                ## T1IMPallx(gasq_length(594), LCSRCsome1(test02_a1rf000.dats)@(863(line=64,offs=1)--914(line=66,offs=33)))
                ## T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8886],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8886],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8886])))),@(x0[1875],T2Pvar(x0[8886])))))))
                def pyxtnm595(arg1): ## timp: gasq_length(594)
                  pyxtnm594 = arg1
                  ## I1CMP:start
                  ## I1CMP:return:I1Vtnm(I1TNM(565))
                  return pyxtnm565
                ## endtimp(gasq_length(594))
                pyxtnm596 = XATSDAPP(pyxtnm595(pyxtnm593))
                pyxtnm597 = pyxtnm596
                XATS000_patck(True)
                ## let
                pyxtnm692 = None
                ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                ## I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                ## T1IMPallx(nint_forall(958), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                ## T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                def pyxtnm690(arg1): ## timp: nint_forall(958)
                  pyxtnm607 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm689 = None
                  ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                  ## I1FUNDCL
                  def loop_2862(arg1, arg2): ## fun
                    pyxtnm608 = arg1
                    pyxtnm609 = arg2
                    ## I1CMP:start
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                    ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                    ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                    def pyxtnm616(arg1, arg2): ## timp: sint_gte$sint(931)
                      pyxtnm610 = arg1
                      pyxtnm611 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm615 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(612);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(612))))),I1BNDcons(I1TNM(613);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(613))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                      pyxtnm614 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm610, pyxtnm611))
                      pyxtnm615 = pyxtnm614
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(615))
                      return pyxtnm615
                    ## endtimp(sint_gte$sint(931))
                    pyxtnm617 = XATSDAPP(pyxtnm616(pyxtnm609, pyxtnm608))
                    pyxtnm687 = None
                    if (pyxtnm617):
                      pyxtnm687 = XATSBOOL(True)
                    else:
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                      ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                      ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                      def pyxtnm675(arg1): ## timp: forall$test(47)
                        pyxtnm618 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm674 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                        ## I1VALDCL
                        pyxtnm631 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                        ## I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                        ## T1IMPallx(gasq_lget$at$raw(2326), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4092(line=227,offs=1)--4187(line=231,offs=35)))
                        ## T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7276])))),@(x0[5735],T2Pvar(x0[7276])))))))
                        def pyxtnm629(arg1, arg2): ## timp: gasq_lget$at$raw(2326)
                          pyxtnm619 = arg1
                          pyxtnm620 = arg2
                          ## I1CMP:start
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4165(line=231,offs=13)--4177(line=231,offs=25))
                          ## I0Etapq(I0Ecst(a1rf_lget$at(1111)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(4779(line=262,offs=1)--4791(line=262,offs=13))));$list(T2JAG($list(T2Pvar(x0[7276])))))
                          ## T1IMPallx(a1rf_lget$at(1111), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2309(line=113,offs=1)--2486(line=128,offs=2)))
                          ## T1IMPallx(a1rf_lget$at(1111)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_lget$at(1111);$list(@(a[2983],T2Pvar(a[8858])))))))
                          def pyxtnm627(arg1, arg2): ## timp: a1rf_lget$at(1111)
                            pyxtnm621 = arg1
                            pyxtnm622 = arg2
                            ## I1CMP:start
                            ## let
                            pyxtnm626 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2393(line=121,offs=1)--2484(line=127,offs=38)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a1rf_lget$at(2668));$list(I1FUNDCL(XATS2PY_a1rf_lget$at(5078);$list(FJARGdarg($list(I1BNDcons(I1TNM(623);I0Pvar(A(5079));$list(@(A(5079),I1Vtnm(I1TNM(623))))),I1BNDcons(I1TNM(624);I0Pvar(i(5080));$list(@(i(5080),I1Vtnm(I1TNM(624))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a1rf_lget$at);G1Nlist($list())))))))
                            pyxtnm625 = XATSDAPP(XATS2PY_a1rf_lget_at(pyxtnm621, pyxtnm622))
                            pyxtnm626 = pyxtnm625
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(626))
                            return pyxtnm626
                          ## endtimp(a1rf_lget$at(1111))
                          pyxtnm628 = XATSDAPP(pyxtnm627(pyxtnm619, pyxtnm620))
                          ## I1CMP:return:I1Vtnm(I1TNM(628))
                          return pyxtnm628
                        ## endtimp(gasq_lget$at$raw(2326))
                        pyxtnm630 = XATSDAPP(pyxtnm629(pyxtnm593, pyxtnm618))
                        pyxtnm631 = pyxtnm630
                        XATS000_patck(True)
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                        ## I1VALDCL
                        pyxtnm667 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                        ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                        ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                        ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        pyxtnm665 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2865(line=151,offs=20)--2876(line=151,offs=31))
                        ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7287])))))
                        ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                        ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        pyxtnm664 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                        ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                        ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8131(line=539,offs=1)--8208(line=543,offs=33)))
                        ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8022],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8023],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        def pyxtnm663(arg1): ## timp: forall$test0(1422)
                          pyxtnm632 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm662 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8167(line=542,offs=1)--8196(line=543,offs=21)))
                          ## I1VALDCL
                          pyxtnm661 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8176(line=543,offs=1)--8188(line=543,offs=13))
                          ## I0Etapq(I0Ecst(foritm$work0(1442)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3042(line=183,offs=1)--3054(line=183,offs=13))));$list(T2JAG($list(T2Pvar(x0[8023])))))
                          ## T1IMPallx(foritm$work0(1442), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11766(line=809,offs=1)--11905(line=816,offs=40)))
                          ## T1IMPallx(foritm$work0(1442)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8054],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8055],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[8056],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work0(1442);$list(@(x0[3785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          def pyxtnm659(arg1): ## timp: foritm$work0(1442)
                            pyxtnm633 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm658 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11836(line=815,offs=1)--11865(line=815,offs=30)))
                            ## I1VALDCL
                            pyxtnm638 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11849(line=815,offs=14)--11857(line=815,offs=22))
                            ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Pvar(r0[8056])))))
                            ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                            ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                            def pyxtnm636(arg1): ## timp: p2tr_get(2309)
                              pyxtnm634 = arg1
                              ## I1CMP:start
                              pyxtnm635 = XATS000_dp2tr(pyxtnm634)
                              ## I1CMP:return:I1Vtnm(I1TNM(635))
                              return pyxtnm635
                            ## endtimp(p2tr_get(2309))
                            pyxtnm637 = XATSDAPP(pyxtnm636(pyxtnm578))
                            pyxtnm638 = pyxtnm637
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11866(line=816,offs=1)--11904(line=816,offs=39)))
                            ## I1VALDCL
                            pyxtnm653 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11875(line=816,offs=10)--11888(line=816,offs=23))
                            ## I0Etapq(I0Ecst(folditm$fopr0(1454)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3581(line=226,offs=1)--3594(line=226,offs=14))));$list(T2JAG($list(T2Pvar(x0[8055]))),T2JAG($list(T2Pvar(r0[8056])))))
                            ## T1IMPallx(folditm$fopr0(1454), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2012(line=81,offs=1)--2074(line=84,offs=31)))
                            ## T1IMPallx(folditm$fopr0(1454)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7891],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(folditm$fopr0(1454);$list(@(x0[3797],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[3798],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                            def pyxtnm651(arg1, arg2): ## timp: folditm$fopr0(1454)
                              pyxtnm639 = arg1
                              pyxtnm640 = arg2
                              ## I1CMP:start
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2055(line=84,offs=12)--2062(line=84,offs=19))
                              ## I0Etapq(I0Ecst(g_mul00(1586)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gnum000_vt.sats)@(2005(line=95,offs=1)--2012(line=95,offs=8))));$list(T2JAG($list(T2Pvar(x0[7892])))))
                              ## T1IMPallx(g_mul00(1586), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats)@(1874(line=76,offs=1)--1916(line=78,offs=24)))
                              ## T1IMPallx(g_mul00(1586)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7800],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_mul00(1586);$list(@(x0[4047],T2Pvar(x0[7800])))))))
                              pyxtnm649 = None
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats)@(1907(line=78,offs=15)--1912(line=78,offs=20))
                              ## I0Etapq(I0Ecst(g_mul(223)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gnum000.sats)@(2025(line=99,offs=1)--2030(line=99,offs=6))));$list(T2JAG($list(T2Pvar(x0[7800])))))
                              ## T1IMPallx(g_mul(223), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2166(line=88,offs=1)--2202(line=89,offs=28)))
                              ## T1IMPallx(g_mul(223)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_mul(223);$list(@(x0[791],T2Pcst(si)))))))
                              pyxtnm648 = None
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2187(line=89,offs=13)--2200(line=89,offs=26))
                              ## I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
                              ## T1IMPallx(sint_mul$sint(938), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
                              ## T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
                              def pyxtnm647(arg1, arg2): ## timp: sint_mul$sint(938)
                                pyxtnm641 = arg1
                                pyxtnm642 = arg2
                                ## I1CMP:start
                                ## let
                                pyxtnm646 = None
                                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
                                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mul$sint(2621));$list(I1FUNDCL(XATS2PY_sint_mul$sint(4901);$list(FJARGdarg($list(I1BNDcons(I1TNM(643);I0Pvar(i1(4902));$list(@(i1(4902),I1Vtnm(I1TNM(643))))),I1BNDcons(I1TNM(644);I0Pvar(i2(4903));$list(@(i2(4903),I1Vtnm(I1TNM(644))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mul$sint);G1Nlist($list())))))))
                                pyxtnm645 = XATSDAPP(XATS2PY_sint_mul_sint(pyxtnm641, pyxtnm642))
                                pyxtnm646 = pyxtnm645
                                ## end-of(let)
                                ## I1CMP:return:I1Vtnm(I1TNM(646))
                                return pyxtnm646
                              ## endtimp(sint_mul$sint(938))
                              pyxtnm648 = pyxtnm647
                              pyxtnm649 = pyxtnm648
                              pyxtnm650 = XATSDAPP(pyxtnm649(pyxtnm639, pyxtnm640))
                              ## I1CMP:return:I1Vtnm(I1TNM(650))
                              return pyxtnm650
                            ## endtimp(folditm$fopr0(1454))
                            pyxtnm652 = XATSDAPP(pyxtnm651(pyxtnm638, pyxtnm633))
                            pyxtnm653 = pyxtnm652
                            XATS000_patck(True)
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11806(line=812,offs=7)--11814(line=812,offs=15))
                            ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Pvar(r0[8056])))))
                            ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                            ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                            def pyxtnm656(arg1, arg2): ## timp: p2tr_set(2310)
                              pyxtnm654 = arg1
                              pyxtnm655 = arg2
                              ## I1CMP:start
                              XATS000_assgn(pyxtnm654, pyxtnm655)
                              ## I1CMP:return:I1V000()
                              return XATSVOID
                            ## endtimp(p2tr_set(2310))
                            pyxtnm657 = XATSDAPP(pyxtnm656(pyxtnm578, pyxtnm653))
                            pyxtnm658 = pyxtnm657
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(658))
                            return pyxtnm658
                          ## endtimp(foritm$work0(1442))
                          pyxtnm660 = XATSDAPP(pyxtnm659(pyxtnm632))
                          pyxtnm661 = pyxtnm660
                          XATS000_patck(True)
                          pyxtnm662 = XATSBOOL(True)
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(662))
                          return pyxtnm662
                        ## endtimp(forall$test0(1422))
                        pyxtnm664 = pyxtnm663
                        pyxtnm665 = pyxtnm664
                        pyxtnm666 = XATSDAPP(pyxtnm665(pyxtnm631))
                        pyxtnm667 = pyxtnm666
                        XATS000_patck(True)
                        ## I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                        ## I1VALDCL
                        ## I1BNDcons(I1TNM(669);I0Ptup0($list());$list())
                        ## I1CMP:start
                        ## I1LETnew1(I1TNM(668);I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(631)))))
                        ## I1CMP(ival):I1Vtnm(I1TNM(668))## I1CMP:return
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                        ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                        ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                        ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                        def pyxtnm672(arg1): ## timp: g_free(23)
                          pyxtnm670 = arg1
                          ## I1CMP:start
                          pyxtnm671 = XATSTUP0([])
                          ## I1CMP:return:I1Vtnm(I1TNM(671))
                          return pyxtnm671
                        ## endtimp(g_free(23))
                        pyxtnm673 = XATSDAPP(pyxtnm672(pyxtnm631))
                        pyxtnm674 = pyxtnm667
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(674))
                        return pyxtnm674
                      ## endtimp(forall$test(47))
                      pyxtnm676 = XATSDAPP(pyxtnm675(pyxtnm609))
                      pyxtnm686 = None
                      if (pyxtnm676):
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                        ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                        ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                        def pyxtnm683(arg1, arg2): ## timp: sint_add$sint(936)
                          pyxtnm677 = arg1
                          pyxtnm678 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm682 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(679);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(679))))),I1BNDcons(I1TNM(680);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(680))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                          pyxtnm681 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm677, pyxtnm678))
                          pyxtnm682 = pyxtnm681
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(682))
                          return pyxtnm682
                        ## endtimp(sint_add$sint(936))
                        pyxtnm684 = XATSDAPP(pyxtnm683(pyxtnm609, XATSINT1(1)))
                        pyxtnm685 = XATSDAPP(loop_2862(pyxtnm608, pyxtnm684))
                        pyxtnm686 = pyxtnm685
                      else:
                        pyxtnm686 = XATSBOOL(False)
                      ## end-of(if)
                      pyxtnm687 = pyxtnm686
                    ## end-of(if)
                    ## I1CMP:return:I1Vtnm(I1TNM(687))
                    return pyxtnm687
                  pyxtnm688 = XATSDAPP(loop_2862(pyxtnm607, XATSINT1(0)))
                  pyxtnm689 = pyxtnm688
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(689))
                  return pyxtnm689
                ## endtimp(nint_forall(958))
                pyxtnm691 = XATSDAPP(pyxtnm690(pyxtnm597))
                pyxtnm692 = pyxtnm691
                ## end-of(let)
                pyxtnm693 = pyxtnm692
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(693))
                return pyxtnm693
              ## endtimp(gasq_forall(609))
              pyxtnm695 = XATSDAPP(pyxtnm694(pyxtnm592))
              pyxtnm696 = pyxtnm695
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(696))
              return pyxtnm696
            ## endtimp(gseq_forall(386))
            pyxtnm698 = XATSDAPP(pyxtnm697(pyxtnm591))
            pyxtnm699 = pyxtnm698
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(699))
            return pyxtnm699
          ## endtimp(gseq_forall0(1719))
          pyxtnm701 = XATSDAPP(pyxtnm700(pyxtnm586))
          pyxtnm702 = pyxtnm701
          XATS000_patck(True)
          pyxtnm703 = XATSVOID
          ## end-of(let)
          pyxtnm704 = pyxtnm703
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(704))
          return pyxtnm704
        ## endtimp(gseq_foritm0(1751))
        pyxtnm706 = XATSDAPP(pyxtnm705(pyxtnm575))
        pyxtnm707 = pyxtnm706
        ## end-of(let)
        pyxtnm708 = pyxtnm707
        XATS000_patck(True)
        pyxtnm709 = XATSFLAT(pyxtnm577)
        pyxtnm710 = pyxtnm709
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(710))
        return pyxtnm710
      ## endtimp(gseq_folditm0(1767))
      pyxtnm712 = XATSDAPP(pyxtnm711(pyxtnm568, pyxtnm571))
      pyxtnm713 = pyxtnm712
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(713))
      return pyxtnm713
    ## endtimp(gseq_prod0(1667))
    pyxtnm715 = pyxtnm714
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2258(line=108,offs=10)--2267(line=108,offs=19))
    ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6659]))),T2JAG($list(T2Pvar(x0[6660])))))
    ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
    ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
    def pyxtnm718(arg1): ## timp: GSEQ_unmk(245)
      pyxtnm716 = arg1
      ## I1CMP:start
      pyxtnm717 = XATSCAST("castxy_1839", [pyxtnm716])
      ## I1CMP:return:I1Vtnm(I1TNM(717))
      return pyxtnm717
    ## endtimp(GSEQ_unmk(245))
    pyxtnm719 = XATSDAPP(pyxtnm718(pyxtnm567))
    pyxtnm720 = XATSDAPP(pyxtnm715(pyxtnm719))
    ## I1CMP:return:I1Vtnm(I1TNM(720))
    return pyxtnm720
  ## endtimp(GSEQ_prod(249))
  ## LCSRCsome1(test02_a1rf000.dats)@(817(line=60,offs=1)--822(line=60,offs=6))
  ## I0Etapq(I0Ecst(a1rf_make_nfun(1105)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3712(line=189,offs=1)--3726(line=189,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  ## T1IMPallx(a1rf_make_nfun(1105), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(2920(line=165,offs=1)--3096(line=178,offs=2)))
  ## T1IMPallx(a1rf_make_nfun(1105)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8864],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_make_nfun(1105);$list(@(a[2971],T2Pvar(a[8864])))))))
  def pyxtnm728(arg1, arg2): ## timp: a1rf_make_nfun(1105)
    pyxtnm722 = arg1
    pyxtnm723 = arg2
    ## I1CMP:start
    ## let
    pyxtnm727 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats)@(3008(line=173,offs=1)--3094(line=177,offs=45)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_a1rf_make_nfun(2671));$list(I1FUNDCL(XATS2PY_a1rf_make_nfun(5097);$list(FJARGdarg($list(I1BNDcons(I1TNM(724);I0Pvar(n(5098));$list(@(n(5098),I1Vtnm(I1TNM(724))))),I1BNDcons(I1TNM(725);I0Pvar(f(5099));$list(@(f(5099),I1Vtnm(I1TNM(725))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_a1rf_make_nfun);G1Nlist($list())))))))
    pyxtnm726 = XATSDAPP(XATS2PY_a1rf_make_nfun(pyxtnm722, pyxtnm723))
    pyxtnm727 = pyxtnm726
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(727))
    return pyxtnm727
  ## endtimp(a1rf_make_nfun(1105))
  def pyxtnm738(arg1): ## { // lam0(T_LAM(0))
    pyxtnm729 = arg1
    ## I1CMP:start
    ## LCSRCsome1(test02_a1rf000.dats)@(843(line=61,offs=21)--844(line=61,offs=22))
    ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
    ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
    ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
    def pyxtnm736(arg1, arg2): ## timp: sint_add$sint(936)
      pyxtnm730 = arg1
      pyxtnm731 = arg2
      ## I1CMP:start
      ## let
      pyxtnm735 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(732);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(732))))),I1BNDcons(I1TNM(733);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(733))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
      pyxtnm734 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm730, pyxtnm731))
      pyxtnm735 = pyxtnm734
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(735))
      return pyxtnm735
    ## endtimp(sint_add$sint(936))
    pyxtnm737 = XATSDAPP(pyxtnm736(pyxtnm729, XATSINT1(1)))
    ## I1CMP:return:I1Vtnm(I1TNM(737))
    return pyxtnm737
  ## } // end(lam0)
  pyxtnm739 = XATSDAPP(pyxtnm728(pyxtnm565, pyxtnm738))
  pyxtnm740 = XATSCAST("GSEQ_make_a1rf_5120", [pyxtnm739])
  pyxtnm741 = XATSDAPP(pyxtnm721(pyxtnm740))
  pyxtnm742 = pyxtnm741
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(742))
  return pyxtnm742
## I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(920(line=68,offs=1)--967(line=70,offs=37)))
## I1VALDCL
pyxtnm784 = None
## LCSRCsome1(test02_a1rf000.dats)@(933(line=70,offs=3)--941(line=70,offs=11))
## I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(gs_println_a2(820), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
## T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
def pyxtnm781(arg1, arg2): ## timp: gs_println_a2(820)
  pyxtnm743 = arg1
  pyxtnm744 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  ## I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  ## T1IMPallx(gs_print_a2(807), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  ## T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  def pyxtnm772(arg1, arg2): ## timp: gs_print_a2(807)
    pyxtnm745 = arg1
    pyxtnm746 = arg2
    ## I1CMP:start
    ## let
    pyxtnm771 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
    ## I1VALDCL
    pyxtnm750 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
    ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    def pyxtnm748(): ## timp: gs_print$beg(802)
      ## I1CMP:start
      pyxtnm747 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(747))
      return pyxtnm747
    ## endtimp(gs_print$beg(802))
    pyxtnm749 = XATSDAPP(pyxtnm748())
    pyxtnm750 = pyxtnm749
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    pyxtnm756 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm755(arg1): ## timp: strn_print(1040)
      pyxtnm751 = arg1
      ## I1CMP:start
      ## let
      pyxtnm754 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(752);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(752))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm753 = XATSDAPP(XATS2PY_strn_print(pyxtnm751))
      pyxtnm754 = pyxtnm753
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(754))
      return pyxtnm754
    ## endtimp(strn_print(1040))
    pyxtnm756 = pyxtnm755
    pyxtnm757 = XATSDAPP(pyxtnm756(pyxtnm745))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
    ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    def pyxtnm759(): ## timp: gs_print$sep(803)
      ## I1CMP:start
      pyxtnm758 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(758))
      return pyxtnm758
    ## endtimp(gs_print$sep(803))
    pyxtnm760 = XATSDAPP(pyxtnm759())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
    pyxtnm766 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
    ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
    ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
    def pyxtnm765(arg1): ## timp: sint_print(922)
      pyxtnm761 = arg1
      ## I1CMP:start
      ## let
      pyxtnm764 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(762);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(762))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
      pyxtnm763 = XATSDAPP(XATS2PY_sint_print(pyxtnm761))
      pyxtnm764 = pyxtnm763
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(764))
      return pyxtnm764
    ## endtimp(sint_print(922))
    pyxtnm766 = pyxtnm765
    pyxtnm767 = XATSDAPP(pyxtnm766(pyxtnm746))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
    ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    def pyxtnm769(): ## timp: gs_print$end(804)
      ## I1CMP:start
      pyxtnm768 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(768))
      return pyxtnm768
    ## endtimp(gs_print$end(804))
    pyxtnm770 = XATSDAPP(pyxtnm769())
    pyxtnm771 = pyxtnm770
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(771))
    return pyxtnm771
  ## endtimp(gs_print_a2(807))
  pyxtnm773 = XATSDAPP(pyxtnm772(pyxtnm743, pyxtnm744))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm779 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm778(arg1): ## timp: strn_print(1040)
    pyxtnm774 = arg1
    ## I1CMP:start
    ## let
    pyxtnm777 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(775);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(775))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm776 = XATSDAPP(XATS2PY_strn_print(pyxtnm774))
    pyxtnm777 = pyxtnm776
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(777))
    return pyxtnm777
  ## endtimp(strn_print(1040))
  pyxtnm779 = pyxtnm778
  pyxtnm780 = XATSDAPP(pyxtnm779(XATSSTRN("\n")))
  ## I1CMP:return:I1Vtnm(I1TNM(780))
  return pyxtnm780
## endtimp(gs_println_a2(820))
pyxtnm782 = XATSDAPP(fact_793(XATSINT1(10)))
pyxtnm783 = XATSDAPP(pyxtnm781(XATSSTRN("fact(10) = "), pyxtnm782))
pyxtnm784 = pyxtnm783
XATS000_patck(True)
## LCSRCsome1(test02_a1rf000.dats)@(1230(line=78,offs=1)--1230(line=78,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test02_a1rf000.dats)@(1230(line=78,offs=1)--1230(line=78,offs=1));D3Cnone0()))
