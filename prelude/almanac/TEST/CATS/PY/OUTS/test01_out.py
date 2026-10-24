## Wed Jan  7 08:14:35 PM EST 2026
########################################################################.
########################################################################.
##
## HX-2025-01-02:
## ATS3-XANADU/srcgen2/xats2py/srcgen1
##
########################################################################.
########################################################################.
##
XATSTOP0 = None
##
########################################################################.
##
def XATSINT0(i0): return i0
##
def XATSINT1(i0): return i0
def XATSBOOL(b0): return b0
def XATSFLT1(f0): return i0
def XATSSTRN(cs): return cs
##
def XATSCNUL(  ): return (0)
def XATSCHR1(  ): return (0)
##
def XATSCHR2(ch):
  return ord(ch[0]) ## acsii
##
def XATSCHR3(ch):
  c1 = ord(ch[1])
  ## ord('0') = 48
  ## ord('7') = 55
  if (c1 < 48 or c1 > 55):
    ## for example: '\(', '\)'
    return ord(ch[1]) ## acsii
  else:
    i1 = 2
    d1 = c1 - 48
    while (i1 < len(ch)):
      c1 = ch[i1]
      if (c1 == "'"):
        return d1
      else:
        d1 = 8*d1 + ord(c1)-48
    return d1 ## ascii code of [ch]
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
## Wed Jan  7 03:41:32 PM EST 2026
########################################################################
########################################################################
##
## the beg of
## [ATS3-XANADU
## /srcgen2/xats2py/srcgen1/xshared/runtime/xats2py_prelude.py]
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
def XATS2PY_strn_fmake_fwork(fwork):
  res = []
  fwork(lambda ch: res.append(chr(ch)))
  return "".join(res)
def XATS000_strn_fmake_fwork(fwork):
  return XATS2PY_strn_fmake_fwork(fwork)
##
########################################################################.
##
def \
XATS2PY_strn_fmake_env_fwork(env, fwork):
  res = []
  fwork(env, lambda ch: res.append(chr(ch)))
  return "".join(res)
def \
XATS2PY_strn_fmake1_env_fwork(env, fwork):
  res = []
  fwork(env, lambda ch: res.append(chr(ch)))
  return "".join(res)
##
def XATS000_strn_fmake_env_fwork(env, fwork):
  return XATS2PY_strn_fmake_env_fwork(env, fwork)
def XATS000_strn_fmake1_env_fwork(env, fwork):
  return XATS2PY_strn_fmake1_env_fwork(env, fwork)
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
  return true ## XATS2PY_strm_vt_forall0_f1un(...)
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
def XATS2PY_a1sz_fmake_fwork(fwork):
  A0 = []
  fwork(lambda x0: A0.append(x0)); return A0
##
########################################################################.
########################################################################.
## end of [ATS3/XANADU_prelude_DATS_CATS_PY_axsz000.cats]
########################################################################.
########################################################################.
## Sat Jan  3 04:36:35 PM EST 2026
## LCSRCsome1(precats.dats)@(1291(line=30,offs=1)--1332(line=31,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(0;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(UN);G1Estr(T_STRN1_clsd("prelude/SATS/unsfx00.sats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats));...)))
## I1Dextern(LCSRCsome1(precats.dats)@(1978(line=81,offs=1)--2048(line=86,offs=29)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_nilq(2163));$list(I1FUNDCL(XATS2PY_optn_nilq(2);$list(FJARGdarg($list(I1BNDcons(I1TNM(1);I0Pvar(xs(3));$list(@(xs(3),I1Vtnm(I1TNM(1))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_nilq);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(2049(line=87,offs=1)--2138(line=91,offs=43)))
def XATS2PY_optn_nilq(arg1): ## impl
  pyxtnm2 = arg1
  ## I1CMP:start
  pyxtnm5 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(3);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
    if (XATS000_ctgeq(pyxtnm2, XATSCTAG("optn_nil",0))): ## { // gpt
      pyxtnm3 = pyxtnm2
      pyxtnm5 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(4);I0Pdap1(I0Pcon(optn_cons(5)));$list()))
    if (XATS000_ctgeq(pyxtnm2, XATSCTAG("optn_cons",1))): ## { // gpt
      pyxtnm4 = pyxtnm2
      pyxtnm5 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm5
  return pyxtnm5
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(2142(line=93,offs=1)--2213(line=98,offs=29)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_consq(2164));$list(I1FUNDCL(XATS2PY_optn_consq(5);$list(FJARGdarg($list(I1BNDcons(I1TNM(6);I0Pvar(xs(6));$list(@(xs(6),I1Vtnm(I1TNM(6))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_consq);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(2214(line=99,offs=1)--2306(line=103,offs=45)))
def XATS2PY_optn_consq(arg1): ## impl
  pyxtnm7 = arg1
  ## I1CMP:start
  pyxtnm10 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(8);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
    if (XATS000_ctgeq(pyxtnm7, XATSCTAG("optn_nil",0))): ## { // gpt
      pyxtnm8 = pyxtnm7
      pyxtnm10 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(9);I0Pdap1(I0Pcon(optn_cons(5)));$list()))
    if (XATS000_ctgeq(pyxtnm7, XATSCTAG("optn_cons",1))): ## { // gpt
      pyxtnm9 = pyxtnm7
      pyxtnm10 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm10
  return pyxtnm10
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(2333(line=107,offs=1)--2406(line=112,offs=28)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_head$raw(2165));$list(I1FUNDCL(XATS2PY_optn_head$raw(8);$list(FJARGdarg($list(I1BNDcons(I1TNM(11);I0Pvar(xs(9));$list(@(xs(9),I1Vtnm(I1TNM(11))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_head$raw);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(2407(line=113,offs=1)--2480(line=116,offs=35)))
def XATS2PY_optn_head_raw(arg1): ## impl
  pyxtnm12 = arg1
  ## I1CMP:start
  pyxtnm14 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(13);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(11))));$list(@(x0(11),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(13));0)))))
    if (XATS000_ctgeq(pyxtnm12, XATSCTAG("optn_cons",1))): ## { // gpt
      pyxtnm13 = pyxtnm12
      pyxtnm14 = XATSP1CN("optn_cons", pyxtnm13[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm14
  return pyxtnm14
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(2484(line=118,offs=1)--2559(line=123,offs=28)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_uncons$raw(2166));$list(I1FUNDCL(XATS2PY_optn_uncons$raw(12);$list(FJARGdarg($list(I1BNDcons(I1TNM(15);I0Pvar(xs(13));$list(@(xs(13),I1Vtnm(I1TNM(15))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_uncons$raw);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(2560(line=124,offs=1)--2635(line=127,offs=35)))
def XATS2PY_optn_uncons_raw(arg1): ## impl
  pyxtnm16 = arg1
  ## I1CMP:start
  pyxtnm18 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(17);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(15))));$list(@(x0(15),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(17));0)))))
    if (XATS000_ctgeq(pyxtnm16, XATSCTAG("optn_cons",1))): ## { // gpt
      pyxtnm17 = pyxtnm16
      pyxtnm18 = XATSP1CN("optn_cons", pyxtnm17[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm18
  return pyxtnm18
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3050(line=162,offs=1)--3120(line=167,offs=29)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_nilq(2167));$list(I1FUNDCL(XATS2PY_list_nilq(16);$list(FJARGdarg($list(I1BNDcons(I1TNM(19);I0Pvar(xs(17));$list(@(xs(17),I1Vtnm(I1TNM(19))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_nilq);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3121(line=168,offs=1)--3210(line=172,offs=43)))
def XATS2PY_list_nilq(arg1): ## impl
  pyxtnm20 = arg1
  ## I1CMP:start
  pyxtnm23 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(21);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
    if (XATS000_ctgeq(pyxtnm20, XATSCTAG("list_nil",0))): ## { // gpt
      pyxtnm21 = pyxtnm20
      pyxtnm23 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(22);I0Pdap1(I0Pcon(list_cons(9)));$list()))
    if (XATS000_ctgeq(pyxtnm20, XATSCTAG("list_cons",1))): ## { // gpt
      pyxtnm22 = pyxtnm20
      pyxtnm23 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm23
  return pyxtnm23
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3214(line=174,offs=1)--3285(line=179,offs=29)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_consq(2168));$list(I1FUNDCL(XATS2PY_list_consq(19);$list(FJARGdarg($list(I1BNDcons(I1TNM(24);I0Pvar(xs(20));$list(@(xs(20),I1Vtnm(I1TNM(24))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_consq);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3286(line=180,offs=1)--3378(line=184,offs=45)))
def XATS2PY_list_consq(arg1): ## impl
  pyxtnm25 = arg1
  ## I1CMP:start
  pyxtnm28 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(26);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
    if (XATS000_ctgeq(pyxtnm25, XATSCTAG("list_nil",0))): ## { // gpt
      pyxtnm26 = pyxtnm25
      pyxtnm28 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(27);I0Pdap1(I0Pcon(list_cons(9)));$list()))
    if (XATS000_ctgeq(pyxtnm25, XATSCTAG("list_cons",1))): ## { // gpt
      pyxtnm27 = pyxtnm25
      pyxtnm28 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm28
  return pyxtnm28
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3405(line=188,offs=1)--3478(line=193,offs=28)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_head$raw(2169));$list(I1FUNDCL(XATS2PY_list_head$raw(22);$list(FJARGdarg($list(I1BNDcons(I1TNM(29);I0Pvar(xs(23));$list(@(xs(23),I1Vtnm(I1TNM(29))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_head$raw);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3479(line=194,offs=1)--3556(line=197,offs=39)))
def XATS2PY_list_head_raw(arg1): ## impl
  pyxtnm30 = arg1
  ## I1CMP:start
  pyxtnm32 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(31);I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(25)),I0Pvar(xs(26))));$list(@(x1(25),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(31));0)),@(xs(26),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(31));1)))))
    if (XATS000_ctgeq(pyxtnm30, XATSCTAG("list_cons",1))): ## { // gpt
      pyxtnm31 = pyxtnm30
      pyxtnm32 = XATSP1CN("list_cons", pyxtnm31[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm32
  return pyxtnm32
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3603(line=202,offs=1)--3681(line=207,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_make_f0un(2170));$list(I1FUNDCL(XATS2PY_lazy_make_f0un(27);$list(FJARGdarg($list(I1BNDcons(I1TNM(33);I0Pvar(f0(28));$list(@(f0(28),I1Vtnm(I1TNM(33))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_make_f0un);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3682(line=208,offs=1)--3731(line=209,offs=41)))
def XATS2PY_lazy_make_f0un(arg1): ## impl
  pyxtnm34 = arg1
  ## I1CMP:start
  def pyxtnm36_(): ## { // l0azy
    ## I1CMP:start
    pyxtnm35 = XATSDAPP(pyxtnm34())
    ## I1CMP:return:pyxtnm35
    return pyxtnm35
  ## } // end(l0azy)
  pyxtnm36 = XATS000_l0azy(pyxtnm36_)
  ## I1CMP:return:pyxtnm36
  return pyxtnm36
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3778(line=214,offs=1)--3848(line=218,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_nil(2171));$list(I1FUNDCL(XATS2PY_strmcon_nil(30);$list(FJARGdarg($list()));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_nil);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3849(line=219,offs=1)--3895(line=220,offs=38)))
def XATS2PY_strmcon_nil(): ## impl
  ## I1CMP:start
  pyxtnm37 = XATSCAPP("strmcon_nil", [0])
  ## I1CMP:return:pyxtnm37
  return pyxtnm37
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3899(line=222,offs=1)--3989(line=227,offs=38)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_cons(2172));$list(I1FUNDCL(XATS2PY_strmcon_cons(31);$list(FJARGdarg($list(I1BNDcons(I1TNM(38);I0Pvar(x1(32));$list(@(x1(32),I1Vtnm(I1TNM(38))))),I1BNDcons(I1TNM(39);I0Pvar(xs(33));$list(@(xs(33),I1Vtnm(I1TNM(39))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_cons);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3990(line=228,offs=1)--4048(line=229,offs=50)))
def XATS2PY_strmcon_cons(arg1, arg2): ## impl
  pyxtnm40 = arg1
  pyxtnm41 = arg2
  ## I1CMP:start
  pyxtnm42 = XATSCAPP("strmcon_cons", [1, pyxtnm40, pyxtnm41])
  ## I1CMP:return:pyxtnm42
  return pyxtnm42
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(4075(line=233,offs=1)--4151(line=238,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_nilq(2173));$list(I1FUNDCL(XATS2PY_strmcon_nilq(36);$list(FJARGdarg($list(I1BNDcons(I1TNM(43);I0Pvar(xs(37));$list(@(xs(37),I1Vtnm(I1TNM(43))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_nilq);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(4152(line=239,offs=1)--4250(line=243,offs=49)))
def XATS2PY_strmcon_nilq(arg1): ## impl
  pyxtnm44 = arg1
  ## I1CMP:start
  pyxtnm47 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(45);I0Pdapp(I0Pcon(strmcon_nil(12));$list());$list()))
    if (XATS000_ctgeq(pyxtnm44, XATSCTAG("strmcon_nil",0))): ## { // gpt
      pyxtnm45 = pyxtnm44
      pyxtnm47 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(46);I0Pdap1(I0Pcon(strmcon_cons(13)));$list()))
    if (XATS000_ctgeq(pyxtnm44, XATSCTAG("strmcon_cons",1))): ## { // gpt
      pyxtnm46 = pyxtnm44
      pyxtnm47 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm47
  return pyxtnm47
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(4254(line=245,offs=1)--4331(line=250,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_consq(2174));$list(I1FUNDCL(XATS2PY_strmcon_consq(39);$list(FJARGdarg($list(I1BNDcons(I1TNM(48);I0Pvar(xs(40));$list(@(xs(40),I1Vtnm(I1TNM(48))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_consq);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(4332(line=251,offs=1)--4433(line=255,offs=51)))
def XATS2PY_strmcon_consq(arg1): ## impl
  pyxtnm49 = arg1
  ## I1CMP:start
  pyxtnm52 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(50);I0Pdapp(I0Pcon(strmcon_nil(12));$list());$list()))
    if (XATS000_ctgeq(pyxtnm49, XATSCTAG("strmcon_nil",0))): ## { // gpt
      pyxtnm50 = pyxtnm49
      pyxtnm52 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(51);I0Pdap1(I0Pcon(strmcon_cons(13)));$list()))
    if (XATS000_ctgeq(pyxtnm49, XATSCTAG("strmcon_cons",1))): ## { // gpt
      pyxtnm51 = pyxtnm49
      pyxtnm52 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm52
  return pyxtnm52
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(4460(line=259,offs=1)--4539(line=264,offs=31)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_head$raw(2175));$list(I1FUNDCL(XATS2PY_strmcon_head$raw(42);$list(FJARGdarg($list(I1BNDcons(I1TNM(53);I0Pvar(xs(43));$list(@(xs(43),I1Vtnm(I1TNM(53))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_head$raw);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(4540(line=265,offs=1)--4623(line=268,offs=42)))
def XATS2PY_strmcon_head_raw(arg1): ## impl
  pyxtnm54 = arg1
  ## I1CMP:start
  pyxtnm56 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(55);I0Pdapp(I0Pcon(strmcon_cons(13));$list(I0Pvar(x1(45)),I0Pvar(xs(46))));$list(@(x1(45),I1Vp1cn(I0Pcon(strmcon_cons(13));I1Vtnm(I1TNM(55));0)),@(xs(46),I1Vp1cn(I0Pcon(strmcon_cons(13));I1Vtnm(I1TNM(55));1)))))
    if (XATS000_ctgeq(pyxtnm54, XATSCTAG("strmcon_cons",1))): ## { // gpt
      pyxtnm55 = pyxtnm54
      pyxtnm56 = XATSP1CN("strmcon_cons", pyxtnm55[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm56
  return pyxtnm56
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(5084(line=306,offs=1)--5162(line=311,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_nilq1(2176));$list(I1FUNDCL(XATS2PY_optn_vt_nilq1(47);$list(FJARGdarg($list(I1BNDcons(I1TNM(57);I0Pvar(xs(48));$list(@(xs(48),I1Vtnm(I1TNM(57))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_nilq1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(5163(line=312,offs=1)--5259(line=316,offs=46)))
def XATS2PY_optn_vt_nilq1(arg1): ## impl
  pyxtnm58 = arg1
  ## I1CMP:start
  pyxtnm61 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(59);I0Pdapp(I0Pcon(optn_vt_nil(6));$list());$list()))
    if (XATS000_ctgeq(pyxtnm58, XATSCTAG("optn_vt_nil",0))): ## { // gpt
      pyxtnm59 = pyxtnm58
      pyxtnm61 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(60);I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(50))));$list(@(x0(50),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(60));0)))))
    if (XATS000_ctgeq(pyxtnm58, XATSCTAG("optn_vt_cons",1))): ## { // gpt
      pyxtnm60 = pyxtnm58
      pyxtnm61 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm61
  return pyxtnm61
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(5263(line=318,offs=1)--5342(line=323,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_consq1(2177));$list(I1FUNDCL(XATS2PY_optn_vt_consq1(51);$list(FJARGdarg($list(I1BNDcons(I1TNM(62);I0Pvar(xs(52));$list(@(xs(52),I1Vtnm(I1TNM(62))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_consq1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(5343(line=324,offs=1)--5442(line=328,offs=48)))
def XATS2PY_optn_vt_consq1(arg1): ## impl
  pyxtnm63 = arg1
  ## I1CMP:start
  pyxtnm66 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(64);I0Pdapp(I0Pcon(optn_vt_nil(6));$list());$list()))
    if (XATS000_ctgeq(pyxtnm63, XATSCTAG("optn_vt_nil",0))): ## { // gpt
      pyxtnm64 = pyxtnm63
      pyxtnm66 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(65);I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(54))));$list(@(x0(54),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(65));0)))))
    if (XATS000_ctgeq(pyxtnm63, XATSCTAG("optn_vt_cons",1))): ## { // gpt
      pyxtnm65 = pyxtnm63
      pyxtnm66 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm66
  return pyxtnm66
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(5469(line=332,offs=1)--5549(line=337,offs=31)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_head$raw0(2178));$list(I1FUNDCL(XATS2PY_optn_vt_head$raw0(55);$list(FJARGdarg($list(I1BNDcons(I1TNM(67);I0Pvar(xs(56));$list(@(xs(56),I1Vtnm(I1TNM(67))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_head$raw0);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(5550(line=338,offs=1)--5631(line=341,offs=39)))
def XATS2PY_optn_vt_head_raw0(arg1): ## impl
  pyxtnm68 = arg1
  ## I1CMP:start
  pyxtnm70 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(69);I0Pfree(I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(58)))));$list(@(x0(58),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(69));0)))))
    if (XATS000_ctgeq(pyxtnm68, XATSCTAG("optn_vt_cons",1))): ## { // gpt
      pyxtnm69 = pyxtnm68
      pyxtnm70 = XATSP1CN("optn_vt_cons", pyxtnm69[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm70
  return pyxtnm70
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(5635(line=343,offs=1)--5717(line=348,offs=31)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_uncons$raw0(2179));$list(I1FUNDCL(XATS2PY_optn_vt_uncons$raw0(59);$list(FJARGdarg($list(I1BNDcons(I1TNM(71);I0Pvar(xs(60));$list(@(xs(60),I1Vtnm(I1TNM(71))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_uncons$raw0);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(5718(line=349,offs=1)--5801(line=352,offs=39)))
def XATS2PY_optn_vt_uncons_raw0(arg1): ## impl
  pyxtnm72 = arg1
  ## I1CMP:start
  pyxtnm74 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(73);I0Pfree(I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(62)))));$list(@(x0(62),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(73));0)))))
    if (XATS000_ctgeq(pyxtnm72, XATSCTAG("optn_vt_cons",1))): ## { // gpt
      pyxtnm73 = pyxtnm72
      pyxtnm74 = XATSP1CN("optn_vt_cons", pyxtnm73[0+1])
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm74
  return pyxtnm74
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(6220(line=385,offs=1)--6298(line=390,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_nilq1(2180));$list(I1FUNDCL(XATS2PY_list_vt_nilq1(63);$list(FJARGdarg($list(I1BNDcons(I1TNM(75);I0Pvar(xs(64));$list(@(xs(64),I1Vtnm(I1TNM(75))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_nilq1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(6299(line=391,offs=1)--6395(line=395,offs=46)))
def XATS2PY_list_vt_nilq1(arg1): ## impl
  pyxtnm76 = arg1
  ## I1CMP:start
  pyxtnm79 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(77);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
    if (XATS000_ctgeq(pyxtnm76, XATSCTAG("list_vt_nil",0))): ## { // gpt
      pyxtnm77 = pyxtnm76
      pyxtnm79 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(78);I0Pdap1(I0Pcon(list_vt_cons(11)));$list()))
    if (XATS000_ctgeq(pyxtnm76, XATSCTAG("list_vt_cons",1))): ## { // gpt
      pyxtnm78 = pyxtnm76
      pyxtnm79 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm79
  return pyxtnm79
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(6399(line=397,offs=1)--6478(line=402,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_consq1(2181));$list(I1FUNDCL(XATS2PY_list_vt_consq1(66);$list(FJARGdarg($list(I1BNDcons(I1TNM(80);I0Pvar(xs(67));$list(@(xs(67),I1Vtnm(I1TNM(80))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_consq1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(6479(line=403,offs=1)--6578(line=407,offs=48)))
def XATS2PY_list_vt_consq1(arg1): ## impl
  pyxtnm81 = arg1
  ## I1CMP:start
  pyxtnm84 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(82);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
    if (XATS000_ctgeq(pyxtnm81, XATSCTAG("list_vt_nil",0))): ## { // gpt
      pyxtnm82 = pyxtnm81
      pyxtnm84 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(83);I0Pdap1(I0Pcon(list_vt_cons(11)));$list()))
    if (XATS000_ctgeq(pyxtnm81, XATSCTAG("list_vt_cons",1))): ## { // gpt
      pyxtnm83 = pyxtnm81
      pyxtnm84 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm84
  return pyxtnm84
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(6605(line=411,offs=1)--6685(line=416,offs=31)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_head$raw1(2182));$list(I1FUNDCL(XATS2PY_list_vt_head$raw1(69);$list(FJARGdarg($list(I1BNDcons(I1TNM(85);I0Pvar(xs(70));$list(@(xs(70),I1Vtnm(I1TNM(85))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_head$raw1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(6686(line=417,offs=1)--6826(line=426,offs=42)))
def XATS2PY_list_vt_head_raw1(arg1): ## impl
  pyxtnm86 = arg1
  ## I1CMP:start
  pyxtnm92 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(87);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(72)),I0Pvar(xs(73))));$list(@(x1(72),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(87));0)),@(xs(73),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(87));1)))))
    if (XATS000_ctgeq(pyxtnm86, XATSCTAG("list_vt_cons",1))): ## { // gpt
      pyxtnm87 = pyxtnm86
      ## let
      pyxtnm91 = None
      ## I1Dvaldclist(LCSRCsome1(precats.dats)@(6776(line=425,offs=1)--6801(line=426,offs=17)))
      ## I1VALDCL
      pyxtnm89 = None
      pyxtnm88 = XATSCAST("datacopy_1720", [XATSP1CN("list_vt_cons", pyxtnm87[0+1])])
      pyxtnm89 = pyxtnm88
      XATS000_patck(True)
      pyxtnm90 = XATSCAST("enlinear_1756", [pyxtnm89])
      pyxtnm91 = pyxtnm90
      ## end-of(let)
      pyxtnm92 = pyxtnm91
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm92
  return pyxtnm92
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(6830(line=428,offs=1)--6918(line=433,offs=38)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_tail$raw0(2183));$list(I1FUNDCL(XATS2PY_list_vt_tail$raw0(75);$list(FJARGdarg($list(I1BNDcons(I1TNM(93);I0Pvar(xs(76));$list(@(xs(76),I1Vtnm(I1TNM(93))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_tail$raw0);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(6919(line=434,offs=1)--7049(line=441,offs=43)))
def XATS2PY_list_vt_tail_raw0(arg1): ## impl
  pyxtnm94 = arg1
  ## I1CMP:start
  pyxtnm99 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(95);I0Pfree(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(78)),I0Pvar(xs(79)))));$list(@(x1(78),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(95));0)),@(xs(79),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(95));1)))))
    if (XATS000_ctgeq(pyxtnm94, XATSCTAG("list_vt_cons",1))): ## { // gpt
      pyxtnm95 = pyxtnm94
      ## let
      pyxtnm98 = None
      ## I1Dvaldclist(LCSRCsome1(precats.dats)@(7013(line=441,offs=7)--7038(line=441,offs=32)))
      ## I1VALDCL
      pyxtnm97 = None
      pyxtnm96 = XATSCAST("delinear_1667", [XATSP1CN("list_vt_cons", pyxtnm95[0+1])])
      pyxtnm97 = pyxtnm96
      XATS000_patck(True)
      pyxtnm98 = XATSP1CN("list_vt_cons", pyxtnm95[1+1])
      ## end-of(let)
      pyxtnm99 = pyxtnm98
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm99
  return pyxtnm99
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7096(line=446,offs=1)--7172(line=451,offs=31)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_vt_eval(2184));$list(I1FUNDCL(XATS2PY_lazy_vt_eval(81);$list(FJARGdarg($list(I1BNDcons(I1TNM(100);I0Pvar(lz(82));$list(@(lz(82),I1Vtnm(I1TNM(100))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_vt_eval);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7173(line=452,offs=1)--7218(line=453,offs=37)))
def XATS2PY_lazy_vt_eval(arg1): ## impl
  pyxtnm101 = arg1
  ## I1CMP:start
  pyxtnm102 = XATS000_dl1az(pyxtnm101)
  ## I1CMP:return:pyxtnm102
  return pyxtnm102
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7222(line=455,offs=1)--7299(line=460,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_vt_free(2185));$list(I1FUNDCL(XATS2PY_lazy_vt_free(84);$list(FJARGdarg($list(I1BNDcons(I1TNM(103);I0Pvar(lz(85));$list(@(lz(85),I1Vtnm(I1TNM(103))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_vt_free);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7300(line=461,offs=1)--7345(line=462,offs=37)))
def XATS2PY_lazy_vt_free(arg1): ## impl
  pyxtnm104 = arg1
  ## I1CMP:start
  XATS000_free(pyxtnm104)
  ## I1CMP:return:[]
  return []
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7372(line=466,offs=1)--7456(line=471,offs=35)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_vt_make_f0un(2186));$list(I1FUNDCL(XATS2PY_lazy_vt_make_f0un(87);$list(FJARGdarg($list(I1BNDcons(I1TNM(105);I0Pvar(f0(88));$list(@(f0(88),I1Vtnm(I1TNM(105))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_vt_make_f0un);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7457(line=472,offs=1)--7510(line=473,offs=45)))
def XATS2PY_lazy_vt_make_f0un(arg1): ## impl
  pyxtnm106 = arg1
  ## I1CMP:start
  def pyxtnm108(tlaz): ## { // l1azy
    ## I1CMP:start
    pyxtnm107 = XATSDAPP(pyxtnm106())
    ## I1CMP:return:pyxtnm107
    return pyxtnm107
  ## } // end(l1azy)
  ## I1CMP:return:pyxtnm108
  return pyxtnm108
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7557(line=478,offs=1)--7633(line=482,offs=35)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_nil(2187));$list(I1FUNDCL(XATS2PY_strmcon_vt_nil(90);$list(FJARGdarg($list()));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_nil);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7634(line=483,offs=1)--7686(line=484,offs=44)))
def XATS2PY_strmcon_vt_nil(): ## impl
  ## I1CMP:start
  pyxtnm109 = XATSCAPP("strmcon_vt_nil", [0])
  ## I1CMP:return:pyxtnm109
  return pyxtnm109
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7690(line=486,offs=1)--7789(line=491,offs=44)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_cons(2188));$list(I1FUNDCL(XATS2PY_strmcon_vt_cons(91);$list(FJARGdarg($list(I1BNDcons(I1TNM(110);I0Pvar(x1(92));$list(@(x1(92),I1Vtnm(I1TNM(110))))),I1BNDcons(I1TNM(111);I0Pvar(xs(93));$list(@(xs(93),I1Vtnm(I1TNM(111))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_cons);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7790(line=492,offs=1)--7854(line=493,offs=56)))
def XATS2PY_strmcon_vt_cons(arg1, arg2): ## impl
  pyxtnm112 = arg1
  pyxtnm113 = arg2
  ## I1CMP:start
  pyxtnm114 = XATSCAPP("strmcon_vt_cons", [1, pyxtnm112, pyxtnm113])
  ## I1CMP:return:pyxtnm114
  return pyxtnm114
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7881(line=497,offs=1)--7965(line=502,offs=35)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_nilq1(2189));$list(I1FUNDCL(XATS2PY_strmcon_vt_nilq1(96);$list(FJARGdarg($list(I1BNDcons(I1TNM(115);I0Pvar(xs(97));$list(@(xs(97),I1Vtnm(I1TNM(115))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_nilq1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7966(line=503,offs=1)--8070(line=507,offs=51)))
def XATS2PY_strmcon_vt_nilq1(arg1): ## impl
  pyxtnm116 = arg1
  ## I1CMP:start
  pyxtnm119 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(117);I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list());$list()))
    if (XATS000_ctgeq(pyxtnm116, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
      pyxtnm117 = pyxtnm116
      pyxtnm119 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(118);I0Pdap1(I0Pcon(strmcon_vt_cons(16)));$list()))
    if (XATS000_ctgeq(pyxtnm116, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
      pyxtnm118 = pyxtnm116
      pyxtnm119 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm119
  return pyxtnm119
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(8074(line=509,offs=1)--8159(line=514,offs=35)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_consq1(2190));$list(I1FUNDCL(XATS2PY_strmcon_vt_consq1(99);$list(FJARGdarg($list(I1BNDcons(I1TNM(120);I0Pvar(xs(100));$list(@(xs(100),I1Vtnm(I1TNM(120))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_consq1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(8160(line=515,offs=1)--8267(line=519,offs=53)))
def XATS2PY_strmcon_vt_consq1(arg1): ## impl
  pyxtnm121 = arg1
  ## I1CMP:start
  pyxtnm124 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(122);I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list());$list()))
    if (XATS000_ctgeq(pyxtnm121, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
      pyxtnm122 = pyxtnm121
      pyxtnm124 = XATSBOOL(False)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(123);I0Pdap1(I0Pcon(strmcon_vt_cons(16)));$list()))
    if (XATS000_ctgeq(pyxtnm121, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
      pyxtnm123 = pyxtnm121
      pyxtnm124 = XATSBOOL(True)
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm124
  return pyxtnm124
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(8294(line=523,offs=1)--8381(line=528,offs=34)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_head$raw1(2191));$list(I1FUNDCL(XATS2PY_strmcon_vt_head$raw1(102);$list(FJARGdarg($list(I1BNDcons(I1TNM(125);I0Pvar(xs(103));$list(@(xs(103),I1Vtnm(I1TNM(125))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_head$raw1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(8382(line=529,offs=1)--8531(line=538,offs=42)))
def XATS2PY_strmcon_vt_head_raw1(arg1): ## impl
  pyxtnm126 = arg1
  ## I1CMP:start
  pyxtnm132 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(127);I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(105)),I0Pvar(xs(106))));$list(@(x1(105),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(127));0)),@(xs(106),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(127));1)))))
    if (XATS000_ctgeq(pyxtnm126, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
      pyxtnm127 = pyxtnm126
      ## let
      pyxtnm131 = None
      ## I1Dvaldclist(LCSRCsome1(precats.dats)@(8481(line=537,offs=1)--8506(line=538,offs=17)))
      ## I1VALDCL
      pyxtnm129 = None
      pyxtnm128 = XATSCAST("datacopy_1720", [XATSP1CN("strmcon_vt_cons", pyxtnm127[0+1])])
      pyxtnm129 = pyxtnm128
      XATS000_patck(True)
      pyxtnm130 = XATSCAST("enlinear_1756", [pyxtnm129])
      pyxtnm131 = pyxtnm130
      ## end-of(let)
      pyxtnm132 = pyxtnm131
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm132
  return pyxtnm132
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(8535(line=540,offs=1)--8629(line=545,offs=41)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_tail$raw0(2192));$list(I1FUNDCL(XATS2PY_strmcon_vt_tail$raw0(108);$list(FJARGdarg($list(I1BNDcons(I1TNM(133);I0Pvar(xs(109));$list(@(xs(109),I1Vtnm(I1TNM(133))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_tail$raw0);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(8630(line=546,offs=1)--8769(line=553,offs=43)))
def XATS2PY_strmcon_vt_tail_raw0(arg1): ## impl
  pyxtnm134 = arg1
  ## I1CMP:start
  pyxtnm139 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(135);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(111)),I0Pvar(xs(112)))));$list(@(x1(111),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(135));0)),@(xs(112),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(135));1)))))
    if (XATS000_ctgeq(pyxtnm134, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
      pyxtnm135 = pyxtnm134
      ## let
      pyxtnm138 = None
      ## I1Dvaldclist(LCSRCsome1(precats.dats)@(8733(line=553,offs=7)--8758(line=553,offs=32)))
      ## I1VALDCL
      pyxtnm137 = None
      pyxtnm136 = XATSCAST("delinear_1667", [XATSP1CN("strmcon_vt_cons", pyxtnm135[0+1])])
      pyxtnm137 = pyxtnm136
      XATS000_patck(True)
      pyxtnm138 = XATSP1CN("strmcon_vt_cons", pyxtnm135[1+1])
      ## end-of(let)
      pyxtnm139 = pyxtnm138
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm139
  return pyxtnm139
## endfun(impl)
## LCSRCsome1(precats.dats)@(9025(line=561,offs=1)--9025(line=561,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(precats.dats)@(9025(line=561,offs=1)--9025(line=561,offs=1));D3Cnone0()))
## I1Dinclude(LCSRCsome1(test01_pre2026.dats)@(103(line=8,offs=1)--154(line=10,offs=33)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_sats.hats)@(1436(line=42,offs=1)--1482(line=44,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(0;T_SRP_STALOAD();G1Estr(T_STRN1_clsd("prelude/almanac/SATS/pre2026.sats";37));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_sats.hats)@(1483(line=45,offs=1)--1535(line=47,offs=34))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(0;T_SRP_STALOAD();G1Estr(T_STRN1_clsd("prelude/almanac/SATS/VT/pre2026_vt.sats";43));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/VT/pre2026_vt.sats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_sats.hats)@(1796(line=55,offs=1)--1796(line=55,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_sats.hats)@(1796(line=55,offs=1)--1796(line=55,offs=1));D3Cnone0()))
## I1Dinclude(LCSRCsome1(test01_pre2026.dats)@(195(line=13,offs=1)--236(line=14,offs=33)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(244(line=17,offs=1)--291(line=19,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(292(line=20,offs=1)--339(line=22,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(340(line=23,offs=1)--387(line=25,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(414(line=29,offs=1)--461(line=31,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(488(line=35,offs=1)--541(line=37,offs=34))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gbas000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(542(line=38,offs=1)--595(line=40,offs=34))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gbas001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(767(line=51,offs=1)--807(line=51,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gxyz000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gxyz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(854(line=56,offs=1)--894(line=56,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/unsfx00.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1038(line=65,offs=1)--1078(line=65,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gnum000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gnum000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1079(line=66,offs=1)--1119(line=66,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gord000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gord000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1120(line=67,offs=1)--1160(line=67,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gfun000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1164(line=69,offs=1)--1204(line=69,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1205(line=70,offs=1)--1245(line=70,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1246(line=71,offs=1)--1286(line=71,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1290(line=73,offs=1)--1330(line=73,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1331(line=74,offs=1)--1371(line=74,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1372(line=75,offs=1)--1412(line=75,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1416(line=77,offs=1)--1456(line=77,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gmap000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gmap000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1457(line=78,offs=1)--1497(line=78,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gmap001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gmap001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1501(line=80,offs=1)--1541(line=80,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gcls000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1542(line=81,offs=1)--1582(line=81,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gsyn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1583(line=82,offs=1)--1623(line=82,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gsyn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1650(line=86,offs=1)--1690(line=86,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/bool000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/bool000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1691(line=87,offs=1)--1731(line=87,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/char000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1732(line=88,offs=1)--1772(line=88,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gint000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1773(line=89,offs=1)--1813(line=89,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gint001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1814(line=90,offs=1)--1854(line=90,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gflt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gflt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1881(line=94,offs=1)--1921(line=94,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1922(line=95,offs=1)--1962(line=95,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1989(line=99,offs=1)--2029(line=99,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axrf000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2030(line=100,offs=1)--2070(line=100,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axrf001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2071(line=101,offs=1)--2111(line=101,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axsz000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2112(line=102,offs=1)--2152(line=102,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axsz001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2153(line=103,offs=1)--2193(line=103,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/asrt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/asrt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2194(line=104,offs=1)--2234(line=104,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2235(line=105,offs=1)--2275(line=105,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2276(line=106,offs=1)--2316(line=106,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2317(line=107,offs=1)--2357(line=107,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2358(line=108,offs=1)--2398(line=108,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2399(line=109,offs=1)--2439(line=109,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2440(line=110,offs=1)--2480(line=110,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/lsrt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/lsrt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2481(line=111,offs=1)--2521(line=111,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/optn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2522(line=112,offs=1)--2562(line=112,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/optn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2563(line=113,offs=1)--2603(line=113,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strm000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strm000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2604(line=114,offs=1)--2644(line=114,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strm001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strm001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2645(line=115,offs=1)--2685(line=115,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strx000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strx000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2686(line=116,offs=1)--2726(line=116,offs=41))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strx001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strx001.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2773(line=121,offs=1)--2818(line=121,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gbas000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gbas000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2822(line=123,offs=1)--2867(line=123,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/bool000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/bool000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2868(line=124,offs=1)--2913(line=124,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/char000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/char000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2917(line=126,offs=1)--2962(line=126,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gint000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gint000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2963(line=127,offs=1)--3008(line=127,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gflt000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gflt000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3012(line=129,offs=1)--3057(line=129,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/strn000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3061(line=131,offs=1)--3106(line=131,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/axrf000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/axrf000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3107(line=132,offs=1)--3152(line=132,offs=46))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/axsz000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/axsz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3196(line=136,offs=1)--3242(line=136,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gnum000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3243(line=137,offs=1)--3289(line=137,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gord000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gord000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3290(line=138,offs=1)--3336(line=138,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gfun000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gfun000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3337(line=139,offs=1)--3383(line=139,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gcls000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gcls000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3384(line=140,offs=1)--3430(line=140,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3431(line=141,offs=1)--3477(line=141,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3478(line=142,offs=1)--3524(line=142,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq002_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq002_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3525(line=143,offs=1)--3571(line=143,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gasq000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gasq000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3572(line=144,offs=1)--3618(line=144,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gasq001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gasq001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3619(line=145,offs=1)--3665(line=145,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gsyn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3686(line=147,offs=1)--3732(line=147,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strn000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3756(line=150,offs=1)--3802(line=150,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/axrf000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/axrf000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3803(line=151,offs=1)--3849(line=151,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/axsz000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/axsz000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3850(line=152,offs=1)--3896(line=152,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/tupl000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/tupl000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3900(line=154,offs=1)--3946(line=154,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/list000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3947(line=155,offs=1)--3993(line=155,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/list001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3994(line=156,offs=1)--4040(line=156,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/lsrt000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/lsrt000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4041(line=157,offs=1)--4087(line=157,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/optn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/optn000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4088(line=158,offs=1)--4134(line=158,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/optn001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/optn001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4138(line=160,offs=1)--4184(line=160,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4185(line=161,offs=1)--4231(line=161,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4232(line=162,offs=1)--4278(line=162,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm002_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4279(line=163,offs=1)--4325(line=163,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strx000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strx000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4326(line=164,offs=1)--4372(line=164,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strx001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strx001_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4543(line=175,offs=1)--4589(line=175,offs=47))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gxyz000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4913(line=183,offs=1)--4913(line=183,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4913(line=183,offs=1)--4913(line=183,offs=1));D3Cnone0()))
## I1Dinclude(LCSRCsome1(test01_pre2026.dats)@(237(line=15,offs=1)--288(line=17,offs=33)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_dats.hats)@(1436(line=42,offs=1)--1482(line=44,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Estr(T_STRN1_clsd("prelude/almanac/DATS/pre2026.dats";37));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_dats.hats)@(1483(line=45,offs=1)--1535(line=47,offs=34))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Estr(T_STRN1_clsd("prelude/almanac/DATS/VT/pre2026_vt.dats";43));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/VT/pre2026_vt.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_dats.hats)@(1796(line=55,offs=1)--1796(line=55,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/HATS/pre2026_dats.hats)@(1796(line=55,offs=1)--1796(line=55,offs=1));D3Cnone0()))
## I1Dinclude(LCSRCsome1(test01_pre2026.dats)@(309(line=19,offs=1)--353(line=20,offs=36)))
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
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(996(line=60,offs=1)--1044(line=61,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/axrf000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axrf000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1045(line=62,offs=1)--1093(line=63,offs=36))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/PY/axsz000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/axsz000.dats));...)))
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1349(line=71,offs=1)--1349(line=71,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_PY_dats.hats)@(1349(line=71,offs=1)--1349(line=71,offs=1));D3Cnone0()))
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(397(line=24,offs=1)--446(line=25,offs=41)))
## I1VALDCL
pyxtnm29 = None
## LCSRCsome1(test01_pre2026.dats)@(406(line=25,offs=1)--414(line=25,offs=9))
## I0Etapq(I0Ecst(gs_println_a1(755)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13747(line=892,offs=1)--13760(line=892,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_println_a1(755), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26148(line=1579,offs=1)--26234(line=1584,offs=40)))
## T1IMPallx(gs_println_a1(755)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[6598],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a1(755);$list(@(x0[2339],T2Pvar(x0[6598])))))))
def pyxtnm27(arg1): ## timp: gs_println_a1(755)
  pyxtnm1 = arg1
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26197(line=1584,offs=3)--26208(line=1584,offs=14))
  ## I0Etapq(I0Ecst(gs_print_a1(742)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11760(line=745,offs=1)--11771(line=745,offs=12))));$list(T2JAG($list(T2Pvar(x0[6598])))))
  ## T1IMPallx(gs_print_a1(742), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21002(line=1292,offs=1)--21119(line=1301,offs=4)))
  ## T1IMPallx(gs_print_a1(742)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[6520],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a1(742);$list(@(x0[2261],T2Pvar(x0[6520])))))))
  def pyxtnm18(arg1): ## timp: gs_print_a1(742)
    pyxtnm2 = arg1
    ## I1CMP:start
    ## let
    pyxtnm17 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21049(line=1297,offs=1)--21072(line=1298,offs=15)))
    ## I1VALDCL
    pyxtnm6 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21058(line=1298,offs=1)--21070(line=1298,offs=13))
    ## I0Etapq(I0Ecst(gs_print$beg(738)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$beg(738), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20721(line=1268,offs=1)--20759(line=1270,offs=20)))
    ## T1IMPallx(gs_print$beg(738)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(738);$list()))))
    def pyxtnm4(): ## timp: gs_print$beg(738)
      ## I1CMP:start
      pyxtnm3 = XATSTUP0([])
      ## I1CMP:return:pyxtnm3
      return pyxtnm3
    ## endtimp(gs_print$beg(738))
    pyxtnm5 = XATSDAPP(pyxtnm4())
    pyxtnm6 = pyxtnm5
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21083(line=1300,offs=1)--21090(line=1300,offs=8))
    ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[6520])))))
    ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(strn)))))))
    pyxtnm12 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
    def pyxtnm11(arg1): ## timp: strn_print(974)
      pyxtnm7 = arg1
      ## I1CMP:start
      ## let
      pyxtnm10 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(8);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(8))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm9 = XATSDAPP(XATS2PY_strn_print(pyxtnm7))
      pyxtnm10 = pyxtnm9
      ## end-of(let)
      ## I1CMP:return:pyxtnm10
      return pyxtnm10
    ## endtimp(strn_print(974))
    pyxtnm12 = pyxtnm11
    pyxtnm13 = XATSDAPP(pyxtnm12(pyxtnm2))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21100(line=1300,offs=18)--21112(line=1300,offs=30))
    ## I0Etapq(I0Ecst(gs_print$end(740)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$end(740), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20799(line=1274,offs=1)--20837(line=1276,offs=20)))
    ## T1IMPallx(gs_print$end(740)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(740);$list()))))
    def pyxtnm15(): ## timp: gs_print$end(740)
      ## I1CMP:start
      pyxtnm14 = XATSTUP0([])
      ## I1CMP:return:pyxtnm14
      return pyxtnm14
    ## endtimp(gs_print$end(740))
    pyxtnm16 = XATSDAPP(pyxtnm15())
    pyxtnm17 = pyxtnm16
    ## end-of(let)
    ## I1CMP:return:pyxtnm17
    return pyxtnm17
  ## endtimp(gs_print_a1(742))
  pyxtnm19 = XATSDAPP(pyxtnm18(pyxtnm1))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26220(line=1584,offs=26)--26227(line=1584,offs=33))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(strn)))))))
  pyxtnm25 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
  def pyxtnm24(arg1): ## timp: strn_print(974)
    pyxtnm20 = arg1
    ## I1CMP:start
    ## let
    pyxtnm23 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(21);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(21))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm22 = XATSDAPP(XATS2PY_strn_print(pyxtnm20))
    pyxtnm23 = pyxtnm22
    ## end-of(let)
    ## I1CMP:return:pyxtnm23
    return pyxtnm23
  ## endtimp(strn_print(974))
  pyxtnm25 = pyxtnm24
  pyxtnm26 = XATSDAPP(pyxtnm25(XATSSTRN("\n")))
  ## I1CMP:return:pyxtnm26
  return pyxtnm26
## endtimp(gs_println_a1(755))
pyxtnm28 = XATSDAPP(pyxtnm27(XATSSTRN("Hello from [test01_pre2026]!")))
pyxtnm29 = pyxtnm28
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(493(line=30,offs=1)--581(line=35,offs=36)))
## I1VALDCL
pyxtnm253 = None
## let
pyxtnm252 = None
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(506(line=32,offs=1)--531(line=33,offs=17)))
## I1VALDCL
pyxtnm88 = None
## LCSRCsome1(test01_pre2026.dats)@(515(line=33,offs=1)--528(line=33,offs=14))
## I0Etapq(I0Ecst(nint_digitize(2127)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(1914(line=77,offs=1)--1927(line=77,offs=14))));$list(T2JAG($list())))
## T1IMPallx(nint_digitize(2127), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2412(line=106,offs=1)--2486(line=110,offs=29)))
## T1IMPallx(nint_digitize(2127)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_digitize(2127);$list()))))
def pyxtnm86(arg1): ## timp: nint_digitize(2127)
  pyxtnm30 = arg1
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2458(line=110,offs=1)--2476(line=110,offs=19))
  ## I0Etapq(I0Ecst(nint_base$digitize(2129)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2000(line=82,offs=1)--2018(line=82,offs=19))));$list(T2JAG($list())))
  ## T1IMPallx(nint_base$digitize(2129), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2567(line=117,offs=1)--2672(line=123,offs=31)))
  ## T1IMPallx(nint_base$digitize(2129)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$digitize(2129);$list()))))
  def pyxtnm84(arg1, arg2): ## timp: nint_base$digitize(2129)
    pyxtnm31 = arg1
    pyxtnm32 = arg2
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2618(line=121,offs=1)--2635(line=121,offs=18))
    ## I0Etapq(I0Ecst(strm_vt_rlistize0(2074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm001_vt.sats)@(8509(line=433,offs=1)--8526(line=433,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
    ## T1IMPallx(strm_vt_rlistize0(2074), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7032(line=445,offs=1)--7325(line=468,offs=2)))
    ## T1IMPallx(strm_vt_rlistize0(2074)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8065],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_rlistize0(2074);$list(@(x0[5158],T2Pvar(x0[8065])))))))
    def pyxtnm46(arg1): ## timp: strm_vt_rlistize0(2074)
      pyxtnm33 = arg1
      ## I1CMP:start
      ## let
      pyxtnm45 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7109(line=453,offs=1)--7131(line=453,offs=23)))
      ## I1VALDCL
      pyxtnm35 = None
      pyxtnm34 = XATSCAPP("list_vt_nil", [0])
      pyxtnm35 = pyxtnm34
      XATS000_patck(True)
      ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7135(line=455,offs=1)--7323(line=467,offs=35)))
      ## I1FUNDCL
      def loop_7138(arg1, arg2): ## fun
        pyxtnm36 = arg1
        pyxtnm37 = arg2
        ## I1CMP:start
        pyxtnm38 = XATS000_dl1az(pyxtnm36)
        pyxtnm43 = None
        while True: ## do {
          ## { // cls
          ## I1GPTpat(I1BNDcons(I1TNM(39);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
          if (XATS000_ctgeq(pyxtnm38, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
            pyxtnm39 = pyxtnm38
            pyxtnm43 = pyxtnm37
            break ## cls
          ## } // gpt
          ## } // cls
          ## { // cls
          ## I1GPTpat(I1BNDcons(I1TNM(40);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(4259)),I0Pvar(xs(4260)))));$list(@(x1(4259),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(40));0)),@(xs(4260),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(40));1)))))
          if (XATS000_ctgeq(pyxtnm38, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
            pyxtnm40 = pyxtnm38
            pyxtnm41 = XATSCAPP("list_vt_cons", [1, XATSP1CN("strmcon_vt_cons", pyxtnm40[0+1]), pyxtnm37])
            pyxtnm42 = XATSDAPP(loop_7138(XATSP1CN("strmcon_vt_cons", pyxtnm40[1+1]), pyxtnm41))
            pyxtnm43 = pyxtnm42
            break ## cls
          ## } // gpt
          ## } // cls
          XATS000_cfail()
        ## } while True // end-of(do-cls)
        ## I1CMP:return:pyxtnm43
        return pyxtnm43
      pyxtnm44 = XATSDAPP(loop_7138(pyxtnm33, pyxtnm35))
      pyxtnm45 = pyxtnm44
      ## end-of(let)
      ## I1CMP:return:pyxtnm45
      return pyxtnm45
    ## endtimp(strm_vt_rlistize0(2074))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2642(line=123,offs=1)--2661(line=123,offs=20))
    ## I0Etapq(I0Ecst(nint_base$rdigitize(2130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2067(line=85,offs=1)--2086(line=85,offs=20))));$list(T2JAG($list())))
    ## T1IMPallx(nint_base$rdigitize(2130), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2676(line=125,offs=1)--2903(line=144,offs=2)))
    ## T1IMPallx(nint_base$rdigitize(2130)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$rdigitize(2130);$list()))))
    def pyxtnm81(arg1, arg2): ## timp: nint_base$rdigitize(2130)
      pyxtnm47 = arg1
      pyxtnm48 = arg2
      ## I1CMP:start
      ## let
      pyxtnm80 = None
      ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2756(line=133,offs=1)--2898(line=142,offs=43)))
      ## I1FUNDCL
      def auxmain_2759(arg1): ## fun
        pyxtnm49 = arg1
        ## I1CMP:start
        def pyxtnm78(tlaz): ## { // l1azy
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2818(line=139,offs=5)--2820(line=139,offs=7))
          ## I0Etapq(I0Ecst(sint_lte$sint(866)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2344(line=100,offs=1)--2357(line=100,offs=14))));$list(T2JAG($list())))
          ## T1IMPallx(sint_lte$sint(866), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2130(line=100,offs=1)--2294(line=112,offs=2)))
          ## T1IMPallx(sint_lte$sint(866)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_lte$sint(866);$list()))))
          def pyxtnm56(arg1, arg2): ## timp: sint_lte$sint(866)
            pyxtnm50 = arg1
            pyxtnm51 = arg2
            ## I1CMP:start
            ## let
            pyxtnm55 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2220(line=108,offs=1)--2292(line=111,offs=39)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_lte$sint(2442));$list(I1FUNDCL(XATS2PY_sint_lte$sint(4642);$list(FJARGdarg($list(I1BNDcons(I1TNM(52);I0Pvar(i1(4643));$list(@(i1(4643),I1Vtnm(I1TNM(52))))),I1BNDcons(I1TNM(53);I0Pvar(i2(4644));$list(@(i2(4644),I1Vtnm(I1TNM(53))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_lte$sint);G1Nlist($list())))))))
            pyxtnm54 = XATSDAPP(XATS2PY_sint_lte_sint(pyxtnm50, pyxtnm51))
            pyxtnm55 = pyxtnm54
            ## end-of(let)
            ## I1CMP:return:pyxtnm55
            return pyxtnm55
          ## endtimp(sint_lte$sint(866))
          pyxtnm57 = XATSDAPP(pyxtnm56(pyxtnm49, XATSINT1(0)))
          pyxtnm77 = None
          if (pyxtnm57):
            pyxtnm58 = XATSCAPP("strmcon_vt_nil", [0])
            pyxtnm77 = pyxtnm58
          else:
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2876(line=142,offs=21)--2877(line=142,offs=22))
            ## I0Etapq(I0Ecst(sint_mod$sint(874)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3076(line=143,offs=1)--3089(line=143,offs=14))));$list(T2JAG($list())))
            ## T1IMPallx(sint_mod$sint(874), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3349(line=201,offs=1)--3513(line=213,offs=2)))
            ## T1IMPallx(sint_mod$sint(874)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mod$sint(874);$list()))))
            def pyxtnm65(arg1, arg2): ## timp: sint_mod$sint(874)
              pyxtnm59 = arg1
              pyxtnm60 = arg2
              ## I1CMP:start
              ## let
              pyxtnm64 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3439(line=209,offs=1)--3511(line=212,offs=39)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mod$sint(2449));$list(I1FUNDCL(XATS2PY_sint_mod$sint(4677);$list(FJARGdarg($list(I1BNDcons(I1TNM(61);I0Pvar(i1(4678));$list(@(i1(4678),I1Vtnm(I1TNM(61))))),I1BNDcons(I1TNM(62);I0Pvar(i2(4679));$list(@(i2(4679),I1Vtnm(I1TNM(62))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mod$sint);G1Nlist($list())))))))
              pyxtnm63 = XATSDAPP(XATS2PY_sint_mod_sint(pyxtnm59, pyxtnm60))
              pyxtnm64 = pyxtnm63
              ## end-of(let)
              ## I1CMP:return:pyxtnm64
              return pyxtnm64
            ## endtimp(sint_mod$sint(874))
            pyxtnm66 = XATSDAPP(pyxtnm65(pyxtnm49, pyxtnm48))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2891(line=142,offs=36)--2892(line=142,offs=37))
            ## I0Etapq(I0Ecst(sint_div$sint(873)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3011(line=139,offs=1)--3024(line=139,offs=14))));$list(T2JAG($list())))
            ## T1IMPallx(sint_div$sint(873), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3181(line=187,offs=1)--3345(line=199,offs=2)))
            ## T1IMPallx(sint_div$sint(873)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_div$sint(873);$list()))))
            def pyxtnm73(arg1, arg2): ## timp: sint_div$sint(873)
              pyxtnm67 = arg1
              pyxtnm68 = arg2
              ## I1CMP:start
              ## let
              pyxtnm72 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3271(line=195,offs=1)--3343(line=198,offs=39)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_div$sint(2448));$list(I1FUNDCL(XATS2PY_sint_div$sint(4672);$list(FJARGdarg($list(I1BNDcons(I1TNM(69);I0Pvar(i1(4673));$list(@(i1(4673),I1Vtnm(I1TNM(69))))),I1BNDcons(I1TNM(70);I0Pvar(i2(4674));$list(@(i2(4674),I1Vtnm(I1TNM(70))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_div$sint);G1Nlist($list())))))))
              pyxtnm71 = XATSDAPP(XATS2PY_sint_div_sint(pyxtnm67, pyxtnm68))
              pyxtnm72 = pyxtnm71
              ## end-of(let)
              ## I1CMP:return:pyxtnm72
              return pyxtnm72
            ## endtimp(sint_div$sint(873))
            pyxtnm74 = XATSDAPP(pyxtnm73(pyxtnm49, pyxtnm48))
            pyxtnm75 = XATSDAPP(auxmain_2759(pyxtnm74))
            pyxtnm76 = XATSCAPP("strmcon_vt_cons", [1, pyxtnm66, pyxtnm75])
            pyxtnm77 = pyxtnm76
          ## end-of(if)
          ## I1CMP:return:pyxtnm77
          return pyxtnm77
        ## } // end(l1azy)
        ## I1CMP:return:pyxtnm78
        return pyxtnm78
      pyxtnm79 = XATSDAPP(auxmain_2759(pyxtnm47))
      pyxtnm80 = pyxtnm79
      ## end-of(let)
      ## I1CMP:return:pyxtnm80
      return pyxtnm80
    ## endtimp(nint_base$rdigitize(2130))
    pyxtnm82 = XATSDAPP(pyxtnm81(pyxtnm31, pyxtnm32))
    pyxtnm83 = XATSDAPP(pyxtnm46(pyxtnm82))
    ## I1CMP:return:pyxtnm83
    return pyxtnm83
  ## endtimp(nint_base$digitize(2129))
  pyxtnm85 = XATSDAPP(pyxtnm84(pyxtnm30, XATSINT1(10)))
  ## I1CMP:return:pyxtnm85
  return pyxtnm85
## endtimp(nint_digitize(2127))
pyxtnm87 = XATSDAPP(pyxtnm86(XATSINT1(0)))
pyxtnm88 = pyxtnm87
XATS000_patck(True)
## LCSRCsome1(test01_pre2026.dats)@(535(line=34,offs=1)--542(line=34,offs=8))
## I0Etapq(I0Ecst(gs_print1_a3(1857)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3614(line=218,offs=1)--3626(line=218,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
## T1IMPallx(gs_print1_a3(1857), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5507(line=274,offs=1)--5674(line=283,offs=21)))
## T1IMPallx(gs_print1_a3(1857)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7768],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7769],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7770],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a3(1857);$list(@(x0[4737],T2Pvar(x0[7768])),@(x1[4738],T2Pvar(x1[7769])),@(x2[4739],T2Pvar(x2[7770])))))))
def pyxtnm250(arg1, arg2, arg3): ## timp: gs_print1_a3(1857)
  pyxtnm89 = arg1
  pyxtnm90 = arg2
  pyxtnm91 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5578(line=280,offs=3)--5591(line=280,offs=16))
  ## I0Etapq(I0Ecst(gs_print$beg1(1841)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg1(1841), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
  ## T1IMPallx(gs_print$beg1(1841)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg1(1841);$list()))))
  def pyxtnm93(): ## timp: gs_print$beg1(1841)
    ## I1CMP:start
    pyxtnm92 = XATSTUP0([])
    ## I1CMP:return:pyxtnm92
    return pyxtnm92
  ## endtimp(gs_print$beg1(1841))
  pyxtnm94 = XATSDAPP(pyxtnm93())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5599(line=281,offs=3)--5607(line=281,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7768])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm101 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(strn)))))))
  pyxtnm100 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
  def pyxtnm99(arg1): ## timp: strn_print(974)
    pyxtnm95 = arg1
    ## I1CMP:start
    ## let
    pyxtnm98 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(96);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(96))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm97 = XATSDAPP(XATS2PY_strn_print(pyxtnm95))
    pyxtnm98 = pyxtnm97
    ## end-of(let)
    ## I1CMP:return:pyxtnm98
    return pyxtnm98
  ## endtimp(strn_print(974))
  pyxtnm100 = pyxtnm99
  pyxtnm101 = pyxtnm100
  pyxtnm102 = XATSDAPP(pyxtnm101(pyxtnm89))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5618(line=282,offs=3)--5626(line=282,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[7769])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2935(line=156,offs=1)--3019(line=162,offs=2)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7873],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7873])))))))))
  def pyxtnm237(arg1): ## timp: g_print1(1329)
    pyxtnm103 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2985(line=161,offs=1)--2996(line=161,offs=12))
    ## I0Etapq(I0Ecst(gseq_print1(1561)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3970(line=243,offs=1)--3981(line=243,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[7873]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7873])))))
    ## T1IMPallx(gseq_print1(1561), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4437(line=281,offs=1)--4754(line=306,offs=7)))
    ## T1IMPallx(gseq_print1(1561)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1561);$list(@(xs[3852],T2Pvar(xs[7298])),@(x0[3853],T2Pvar(x0[7299])))))))
    def pyxtnm235(arg1): ## timp: gseq_print1(1561)
      pyxtnm104 = arg1
      ## I1CMP:start
      ## let
      pyxtnm234 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4488(line=286,offs=1)--4530(line=288,offs=21)))
      ## I1VALDCL
      pyxtnm113 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4497(line=287,offs=1)--4507(line=287,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm109(arg1): ## timp: strn_print(974)
        pyxtnm105 = arg1
        ## I1CMP:start
        ## let
        pyxtnm108 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(106);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(106))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm107 = XATSDAPP(XATS2PY_strn_print(pyxtnm105))
        pyxtnm108 = pyxtnm107
        ## end-of(let)
        ## I1CMP:return:pyxtnm108
        return pyxtnm108
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4511(line=288,offs=2)--4519(line=288,offs=10))
      ## I0Etapq(I0Ecst(gseq_beg(319)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2370(line=129,offs=1)--2378(line=129,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_beg(319), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq_beg(319)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_beg(319);$list(@(xs[949],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7871])))),@(x0[950],T2Pvar(x0[7871])))))))
      def pyxtnm110(): ## timp: gseq_beg(319)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN("list_vt(")
        return XATSSTRN("list_vt(")
      ## endtimp(gseq_beg(319))
      pyxtnm111 = XATSDAPP(pyxtnm110())
      pyxtnm112 = XATSDAPP(pyxtnm109(pyxtnm111))
      pyxtnm113 = pyxtnm112
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4531(line=289,offs=1)--4705(line=303,offs=2)))
      ## I1VALDCL
      pyxtnm224 = None
      ## let
      pyxtnm223 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Pvar(x0[7299]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4542(line=291,offs=1)--4555(line=291,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1635)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10879(line=588,offs=1)--10892(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_iforitm1(1635), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9859(line=671,offs=1)--10064(line=688,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1635)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1635);$list(@(xs[4038],T2Pvar(xs[7435])),@(x0[4039],T2Pvar(x0[7436])))))))
      def pyxtnm221(arg1): ## timp: gseq_iforitm1(1635)
        pyxtnm123 = arg1
        ## I1CMP:start
        ## let
        pyxtnm220 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Pvar(x0[7436]))))):timp
        ## let
        pyxtnm219 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9919(line=678,offs=1)--9955(line=680,offs=15)))
        ## I1VALDCL
        pyxtnm218 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9927(line=679,offs=1)--9940(line=679,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1611)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6521(line=346,offs=1)--6534(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[7435]))),T2JAG($list(T2Pvar(x0[7436])))))
        ## T1IMPallx(gseq_iforall1(1611), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5881(line=370,offs=1)--6184(line=396,offs=2)))
        ## T1IMPallx(gseq_iforall1(1611)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1611);$list(@(xs[3990],T2Pvar(xs[7403])),@(x0[3991],T2Pvar(x0[7404])))))))
        def pyxtnm216(arg1): ## timp: gseq_iforall1(1611)
          pyxtnm129 = arg1
          ## I1CMP:start
          ## let
          pyxtnm215 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5949(line=377,offs=1)--5965(line=377,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:XATSINT1(0)
          pyxtnm130 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5969(line=379,offs=1)--5987(line=379,offs=19)))
          ## I1VALDCL
          pyxtnm131 = None
          pyxtnm131 = XATSADDR(pyxtnm130)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5991(line=381,offs=1)--6179(line=394,offs=2)))
          ## I1VALDCL
          pyxtnm214 = None
          ## let
          pyxtnm213 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Pvar(x0[7404]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6002(line=383,offs=1)--6014(line=383,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1595)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[7403]))),T2JAG($list(T2Pvar(x0[7404])))))
          ## T1IMPallx(gseq_forall1(1595), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2042(line=92,offs=1)--2113(line=95,offs=40)))
          ## T1IMPallx(gseq_forall1(1595)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1595);$list(@(xs[3958],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7912])))),@(x0[3959],T2Pvar(x0[7912])))))))
          pyxtnm211 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2094(line=95,offs=21)--2109(line=95,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall1(1908)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1481(line=47,offs=1)--1496(line=47,offs=16))));$list(T2JAG($list(T2Pvar(x0[7912])))))
          ## T1IMPallx(list_vt_forall1(1908), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1701(line=65,offs=1)--1958(line=86,offs=2)))
          ## T1IMPallx(list_vt_forall1(1908)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7910],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall1(1908);$list(@(x0[4880],T2Pvar(x0[7910])))))))
          def pyxtnm210(arg1): ## timp: list_vt_forall1(1908)
            pyxtnm140 = arg1
            ## I1CMP:start
            ## let
            pyxtnm209 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1771(line=72,offs=1)--1956(line=85,offs=38)))
            ## I1FUNDCL
            def loop_1774(arg1): ## fun
              pyxtnm141 = arg1
              ## I1CMP:start
              pyxtnm207 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(142);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
                if (XATS000_ctgeq(pyxtnm141, XATSCTAG("list_vt_nil",0))): ## { // gpt
                  pyxtnm142 = pyxtnm141
                  pyxtnm207 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(143);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(4054)),I0Pvar(xs(4055))));$list(@(x1(4054),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(143));0)),@(xs(4055),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(143));1)))))
                if (XATS000_ctgeq(pyxtnm141, XATSCTAG("list_vt_cons",1))): ## { // gpt
                  pyxtnm143 = pyxtnm141
                  ## let
                  pyxtnm206 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1884(line=83,offs=1)--1915(line=84,offs=21)))
                  ## I1VALDCL
                  pyxtnm203 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1895(line=84,offs=1)--1907(line=84,offs=13))
                  ## I0Etapq(I0Ecst(forall$test1(1340)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[7910])))))
                  ## T1IMPallx(forall$test1(1340), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
                  ## T1IMPallx(forall$test1(1340)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm201(arg1): ## timp: forall$test1(1340)
                    pyxtnm144 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm200 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6111(line=392,offs=1)--6140(line=392,offs=30)))
                    ## I1VALDCL
                    pyxtnm149 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6124(line=392,offs=14)--6132(line=392,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2151)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2151), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2151)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5486],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2151);$list(@(a[5302],T2Pvar(a[5486])))))))
                    def pyxtnm147(arg1): ## timp: p2tr_get(2151)
                      pyxtnm145 = arg1
                      ## I1CMP:start
                      pyxtnm146 = XATS000_dp2tr(pyxtnm145)
                      ## I1CMP:return:pyxtnm146
                      return pyxtnm146
                    ## endtimp(p2tr_get(2151))
                    pyxtnm148 = XATSDAPP(pyxtnm147(pyxtnm131))
                    pyxtnm149 = pyxtnm148
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6141(line=393,offs=1)--6175(line=393,offs=35)))
                    ## I1VALDCL
                    pyxtnm187 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6150(line=393,offs=10)--6163(line=393,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test1(1352)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2693(line=154,offs=1)--2706(line=154,offs=14))));$list(T2JAG($list(T2Pvar(x0[7404])))))
                    ## T1IMPallx(iforall$test1(1352), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
                    ## T1IMPallx(iforall$test1(1352)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm185(arg1, arg2): ## timp: iforall$test1(1352)
                      pyxtnm150 = arg1
                      pyxtnm151 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm184 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10016(line=686,offs=1)--10050(line=687,offs=26)))
                      ## I1VALDCL
                      pyxtnm183 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10025(line=687,offs=1)--10038(line=687,offs=14))
                      ## I0Etapq(I0Ecst(iforitm$work1(1366)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[7436])))))
                      ## T1IMPallx(iforitm$work1(1366), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
                      ## T1IMPallx(iforitm$work1(1366)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm181(arg1, arg2): ## timp: iforitm$work1(1366)
                        pyxtnm152 = arg1
                        pyxtnm153 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm180 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4645(line=299,offs=1)--4701(line=301,offs=33)))
                        ## I1VALDCL
                        pyxtnm171 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4660(line=300,offs=7)--4661(line=300,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(864)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(864), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(864)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(864);$list()))))
                        def pyxtnm160(arg1, arg2): ## timp: sint_gt$sint(864)
                          pyxtnm154 = arg1
                          pyxtnm155 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm159 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2440));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4632);$list(FJARGdarg($list(I1BNDcons(I1TNM(156);I0Pvar(i1(4633));$list(@(i1(4633),I1Vtnm(I1TNM(156))))),I1BNDcons(I1TNM(157);I0Pvar(i2(4634));$list(@(i2(4634),I1Vtnm(I1TNM(157))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm158 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm154, pyxtnm155))
                          pyxtnm159 = pyxtnm158
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm159
                          return pyxtnm159
                        ## endtimp(sint_gt$sint(864))
                        pyxtnm161 = XATSDAPP(pyxtnm160(pyxtnm152, XATSINT1(0)))
                        pyxtnm170 = None
                        if (pyxtnm161):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4669(line=301,offs=1)--4679(line=301,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
                          def pyxtnm166(arg1): ## timp: strn_print(974)
                            pyxtnm162 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm165 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(163);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(163))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm164 = XATSDAPP(XATS2PY_strn_print(pyxtnm162))
                            pyxtnm165 = pyxtnm164
                            ## end-of(let)
                            ## I1CMP:return:pyxtnm165
                            return pyxtnm165
                          ## endtimp(strn_print(974))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4682(line=301,offs=14)--4690(line=301,offs=22))
                          ## I0Etapq(I0Ecst(gseq_sep(321)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2454(line=137,offs=1)--2462(line=137,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
                          ## T1IMPallx(gseq_sep(321), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                          ## T1IMPallx(gseq_sep(321)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_sep(321);$list(@(xs[953],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7869])))),@(x0[954],T2Pvar(x0[7869])))))))
                          def pyxtnm167(): ## timp: gseq_sep(321)
                            ## I1CMP:start
                            ## I1CMP:return:XATSSTRN(",")
                            return XATSSTRN(",")
                          ## endtimp(gseq_sep(321))
                          pyxtnm168 = XATSDAPP(pyxtnm167())
                          pyxtnm169 = XATSDAPP(pyxtnm166(pyxtnm168))
                          pyxtnm170 = pyxtnm169
                        ## else: None
                        ## end-of(if)
                        pyxtnm171 = pyxtnm170
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4619(line=297,offs=3)--4627(line=297,offs=11))
                        ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7299])))))
                        ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                        ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
                        pyxtnm178 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                        ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
                        ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                        ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(si)))))))
                        pyxtnm177 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                        ## I0Etapq(I0Ecst(sint_print(858)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_print(858), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                        ## T1IMPallx(sint_print(858)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(858);$list()))))
                        def pyxtnm176(arg1): ## timp: sint_print(858)
                          pyxtnm172 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm175 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2450));$list(I1FUNDCL(XATS2PY_sint_print(4681);$list(FJARGdarg($list(I1BNDcons(I1TNM(173);I0Pvar(i0(4682));$list(@(i0(4682),I1Vtnm(I1TNM(173))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                          pyxtnm174 = XATSDAPP(XATS2PY_sint_print(pyxtnm172))
                          pyxtnm175 = pyxtnm174
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm175
                          return pyxtnm175
                        ## endtimp(sint_print(858))
                        pyxtnm177 = pyxtnm176
                        pyxtnm178 = pyxtnm177
                        pyxtnm179 = XATSDAPP(pyxtnm178(pyxtnm153))
                        pyxtnm180 = pyxtnm179
                        ## end-of(let)
                        ## I1CMP:return:pyxtnm180
                        return pyxtnm180
                      ## endtimp(iforitm$work1(1366))
                      pyxtnm182 = XATSDAPP(pyxtnm181(pyxtnm150, pyxtnm151))
                      pyxtnm183 = pyxtnm182
                      XATS000_patck(True)
                      pyxtnm184 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm184
                      return pyxtnm184
                    ## endtimp(iforall$test1(1352))
                    pyxtnm186 = XATSDAPP(pyxtnm185(pyxtnm149, pyxtnm144))
                    pyxtnm187 = pyxtnm186
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6075(line=389,offs=5)--6083(line=389,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2152)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2152), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2152)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5487],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2152);$list(@(a[5303],T2Pvar(a[5487])))))))
                    def pyxtnm190(arg1, arg2): ## timp: p2tr_set(2152)
                      pyxtnm188 = arg1
                      pyxtnm189 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm188, pyxtnm189)
                      ## I1CMP:return:[]
                      return []
                    ## endtimp(p2tr_set(2152))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6094(line=389,offs=24)--6095(line=389,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(870)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2816(line=127,offs=1)--2829(line=127,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(870), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(870)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(870);$list()))))
                    def pyxtnm197(arg1, arg2): ## timp: sint_add$sint(870)
                      pyxtnm191 = arg1
                      pyxtnm192 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm196 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2445));$list(I1FUNDCL(XATS2PY_sint_add$sint(4657);$list(FJARGdarg($list(I1BNDcons(I1TNM(193);I0Pvar(i1(4658));$list(@(i1(4658),I1Vtnm(I1TNM(193))))),I1BNDcons(I1TNM(194);I0Pvar(i2(4659));$list(@(i2(4659),I1Vtnm(I1TNM(194))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm195 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm191, pyxtnm192))
                      pyxtnm196 = pyxtnm195
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm196
                      return pyxtnm196
                    ## endtimp(sint_add$sint(870))
                    pyxtnm198 = XATSDAPP(pyxtnm197(pyxtnm149, XATSINT1(1)))
                    pyxtnm199 = XATSDAPP(pyxtnm190(pyxtnm131, pyxtnm198))
                    pyxtnm200 = pyxtnm187
                    ## end-of(let)
                    ## I1CMP:return:pyxtnm200
                    return pyxtnm200
                  ## endtimp(forall$test1(1340))
                  pyxtnm202 = XATSDAPP(pyxtnm201(XATSP1CN("list_vt_cons", pyxtnm143[0+1])))
                  pyxtnm203 = pyxtnm202
                  XATS000_patck(True)
                  pyxtnm205 = None
                  if (pyxtnm203):
                    pyxtnm204 = XATSDAPP(loop_1774(XATSP1CN("list_vt_cons", pyxtnm143[1+1])))
                    pyxtnm205 = pyxtnm204
                  else:
                    pyxtnm205 = XATSBOOL(False)
                  ## end-of(if)
                  pyxtnm206 = pyxtnm205
                  ## end-of(let)
                  pyxtnm207 = pyxtnm206
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:pyxtnm207
              return pyxtnm207
            pyxtnm208 = XATSDAPP(loop_1774(pyxtnm140))
            pyxtnm209 = pyxtnm208
            ## end-of(let)
            ## I1CMP:return:pyxtnm209
            return pyxtnm209
          ## endtimp(list_vt_forall1(1908))
          pyxtnm211 = pyxtnm210
          pyxtnm212 = XATSDAPP(pyxtnm211(pyxtnm129))
          pyxtnm213 = pyxtnm212
          ## end-of(let)
          pyxtnm214 = pyxtnm213
          XATS000_patck(True)
          pyxtnm215 = pyxtnm214
          ## end-of(let)
          ## I1CMP:return:pyxtnm215
          return pyxtnm215
        ## endtimp(gseq_iforall1(1611))
        pyxtnm217 = XATSDAPP(pyxtnm216(pyxtnm123))
        pyxtnm218 = pyxtnm217
        XATS000_patck(True)
        pyxtnm219 = []
        ## end-of(let)
        pyxtnm220 = pyxtnm219
        ## end-of(let)
        ## I1CMP:return:pyxtnm220
        return pyxtnm220
      ## endtimp(gseq_iforitm1(1635))
      pyxtnm222 = XATSDAPP(pyxtnm221(pyxtnm104))
      pyxtnm223 = pyxtnm222
      ## end-of(let)
      pyxtnm224 = pyxtnm223
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=304,offs=1)--4747(line=305,offs=33)))
      ## I1VALDCL
      pyxtnm233 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=305,offs=1)--4725(line=305,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm229(arg1): ## timp: strn_print(974)
        pyxtnm225 = arg1
        ## I1CMP:start
        ## let
        pyxtnm228 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(226);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(226))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm227 = XATSDAPP(XATS2PY_strn_print(pyxtnm225))
        pyxtnm228 = pyxtnm227
        ## end-of(let)
        ## I1CMP:return:pyxtnm228
        return pyxtnm228
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=305,offs=14)--4736(line=305,offs=22))
      ## I0Etapq(I0Ecst(gseq_end(320)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2412(line=133,offs=1)--2420(line=133,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_end(320), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq_end(320)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_end(320);$list(@(xs[951],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7870])))),@(x0[952],T2Pvar(x0[7870])))))))
      def pyxtnm230(): ## timp: gseq_end(320)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN(")")
        return XATSSTRN(")")
      ## endtimp(gseq_end(320))
      pyxtnm231 = XATSDAPP(pyxtnm230())
      pyxtnm232 = XATSDAPP(pyxtnm229(pyxtnm231))
      pyxtnm233 = pyxtnm232
      XATS000_patck(True)
      pyxtnm234 = []
      ## end-of(let)
      ## I1CMP:return:pyxtnm234
      return pyxtnm234
    ## endtimp(gseq_print1(1561))
    pyxtnm236 = XATSDAPP(pyxtnm235(pyxtnm103))
    ## I1CMP:return:pyxtnm236
    return pyxtnm236
  ## endtimp(g_print1(1329))
  pyxtnm238 = XATSDAPP(pyxtnm237(pyxtnm90))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5636(line=282,offs=21)--5644(line=282,offs=29))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[7770])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm245 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2611(line=136,offs=1)--2648(line=137,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(char)))))))
  pyxtnm244 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2636(line=137,offs=17)--2646(line=137,offs=27))
  ## I0Etapq(I0Ecst(char_print(826)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/char000.sats)@(2501(line=119,offs=1)--2511(line=119,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(char_print(826), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2887(line=170,offs=1)--3027(line=181,offs=2)))
  ## T1IMPallx(char_print(826)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(char_print(826);$list()))))
  def pyxtnm243(arg1): ## timp: char_print(826)
    pyxtnm239 = arg1
    ## I1CMP:start
    ## let
    pyxtnm242 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2967(line=178,offs=1)--3025(line=180,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_char_print(2437));$list(I1FUNDCL(XATS2PY_char_print(4620);$list(FJARGdarg($list(I1BNDcons(I1TNM(240);I0Pvar(c0(4621));$list(@(c0(4621),I1Vtnm(I1TNM(240))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_char_print);G1Nlist($list())))))))
    pyxtnm241 = XATSDAPP(XATS2PY_char_print(pyxtnm239))
    pyxtnm242 = pyxtnm241
    ## end-of(let)
    ## I1CMP:return:pyxtnm242
    return pyxtnm242
  ## endtimp(char_print(826))
  pyxtnm244 = pyxtnm243
  pyxtnm245 = pyxtnm244
  pyxtnm246 = XATSDAPP(pyxtnm245(pyxtnm91))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5656(line=283,offs=3)--5669(line=283,offs=16))
  ## I0Etapq(I0Ecst(gs_print$end1(1842)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end1(1842), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
  ## T1IMPallx(gs_print$end1(1842)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end1(1842);$list()))))
  def pyxtnm248(): ## timp: gs_print$end1(1842)
    ## I1CMP:start
    pyxtnm247 = XATSTUP0([])
    ## I1CMP:return:pyxtnm247
    return pyxtnm247
  ## endtimp(gs_print$end1(1842))
  pyxtnm249 = XATSDAPP(pyxtnm248())
  ## I1CMP:return:pyxtnm249
  return pyxtnm249
## endtimp(gs_print1_a3(1857))
pyxtnm251 = XATSDAPP(pyxtnm250(XATSSTRN("nint_digitize(0) = "), pyxtnm88, XATSCHR2('\n')))
pyxtnm252 = pyxtnm251
## end-of(let)
pyxtnm253 = pyxtnm252
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(582(line=36,offs=1)--686(line=41,offs=44)))
## I1VALDCL
pyxtnm477 = None
## let
pyxtnm476 = None
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(595(line=38,offs=1)--628(line=39,offs=25)))
## I1VALDCL
pyxtnm312 = None
## LCSRCsome1(test01_pre2026.dats)@(604(line=39,offs=1)--617(line=39,offs=14))
## I0Etapq(I0Ecst(nint_digitize(2127)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(1914(line=77,offs=1)--1927(line=77,offs=14))));$list(T2JAG($list())))
## T1IMPallx(nint_digitize(2127), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2412(line=106,offs=1)--2486(line=110,offs=29)))
## T1IMPallx(nint_digitize(2127)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_digitize(2127);$list()))))
def pyxtnm310(arg1): ## timp: nint_digitize(2127)
  pyxtnm254 = arg1
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2458(line=110,offs=1)--2476(line=110,offs=19))
  ## I0Etapq(I0Ecst(nint_base$digitize(2129)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2000(line=82,offs=1)--2018(line=82,offs=19))));$list(T2JAG($list())))
  ## T1IMPallx(nint_base$digitize(2129), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2567(line=117,offs=1)--2672(line=123,offs=31)))
  ## T1IMPallx(nint_base$digitize(2129)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$digitize(2129);$list()))))
  def pyxtnm308(arg1, arg2): ## timp: nint_base$digitize(2129)
    pyxtnm255 = arg1
    pyxtnm256 = arg2
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2618(line=121,offs=1)--2635(line=121,offs=18))
    ## I0Etapq(I0Ecst(strm_vt_rlistize0(2074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm001_vt.sats)@(8509(line=433,offs=1)--8526(line=433,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
    ## T1IMPallx(strm_vt_rlistize0(2074), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7032(line=445,offs=1)--7325(line=468,offs=2)))
    ## T1IMPallx(strm_vt_rlistize0(2074)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8065],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_rlistize0(2074);$list(@(x0[5158],T2Pvar(x0[8065])))))))
    def pyxtnm270(arg1): ## timp: strm_vt_rlistize0(2074)
      pyxtnm257 = arg1
      ## I1CMP:start
      ## let
      pyxtnm269 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7109(line=453,offs=1)--7131(line=453,offs=23)))
      ## I1VALDCL
      pyxtnm259 = None
      pyxtnm258 = XATSCAPP("list_vt_nil", [0])
      pyxtnm259 = pyxtnm258
      XATS000_patck(True)
      ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7135(line=455,offs=1)--7323(line=467,offs=35)))
      ## I1FUNDCL
      def loop_7138(arg1, arg2): ## fun
        pyxtnm260 = arg1
        pyxtnm261 = arg2
        ## I1CMP:start
        pyxtnm262 = XATS000_dl1az(pyxtnm260)
        pyxtnm267 = None
        while True: ## do {
          ## { // cls
          ## I1GPTpat(I1BNDcons(I1TNM(263);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
          if (XATS000_ctgeq(pyxtnm262, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
            pyxtnm263 = pyxtnm262
            pyxtnm267 = pyxtnm261
            break ## cls
          ## } // gpt
          ## } // cls
          ## { // cls
          ## I1GPTpat(I1BNDcons(I1TNM(264);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(4259)),I0Pvar(xs(4260)))));$list(@(x1(4259),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(264));0)),@(xs(4260),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(264));1)))))
          if (XATS000_ctgeq(pyxtnm262, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
            pyxtnm264 = pyxtnm262
            pyxtnm265 = XATSCAPP("list_vt_cons", [1, XATSP1CN("strmcon_vt_cons", pyxtnm264[0+1]), pyxtnm261])
            pyxtnm266 = XATSDAPP(loop_7138(XATSP1CN("strmcon_vt_cons", pyxtnm264[1+1]), pyxtnm265))
            pyxtnm267 = pyxtnm266
            break ## cls
          ## } // gpt
          ## } // cls
          XATS000_cfail()
        ## } while True // end-of(do-cls)
        ## I1CMP:return:pyxtnm267
        return pyxtnm267
      pyxtnm268 = XATSDAPP(loop_7138(pyxtnm257, pyxtnm259))
      pyxtnm269 = pyxtnm268
      ## end-of(let)
      ## I1CMP:return:pyxtnm269
      return pyxtnm269
    ## endtimp(strm_vt_rlistize0(2074))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2642(line=123,offs=1)--2661(line=123,offs=20))
    ## I0Etapq(I0Ecst(nint_base$rdigitize(2130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2067(line=85,offs=1)--2086(line=85,offs=20))));$list(T2JAG($list())))
    ## T1IMPallx(nint_base$rdigitize(2130), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2676(line=125,offs=1)--2903(line=144,offs=2)))
    ## T1IMPallx(nint_base$rdigitize(2130)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$rdigitize(2130);$list()))))
    def pyxtnm305(arg1, arg2): ## timp: nint_base$rdigitize(2130)
      pyxtnm271 = arg1
      pyxtnm272 = arg2
      ## I1CMP:start
      ## let
      pyxtnm304 = None
      ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2756(line=133,offs=1)--2898(line=142,offs=43)))
      ## I1FUNDCL
      def auxmain_2759(arg1): ## fun
        pyxtnm273 = arg1
        ## I1CMP:start
        def pyxtnm302(tlaz): ## { // l1azy
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2818(line=139,offs=5)--2820(line=139,offs=7))
          ## I0Etapq(I0Ecst(sint_lte$sint(866)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2344(line=100,offs=1)--2357(line=100,offs=14))));$list(T2JAG($list())))
          ## T1IMPallx(sint_lte$sint(866), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2130(line=100,offs=1)--2294(line=112,offs=2)))
          ## T1IMPallx(sint_lte$sint(866)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_lte$sint(866);$list()))))
          def pyxtnm280(arg1, arg2): ## timp: sint_lte$sint(866)
            pyxtnm274 = arg1
            pyxtnm275 = arg2
            ## I1CMP:start
            ## let
            pyxtnm279 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2220(line=108,offs=1)--2292(line=111,offs=39)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_lte$sint(2442));$list(I1FUNDCL(XATS2PY_sint_lte$sint(4642);$list(FJARGdarg($list(I1BNDcons(I1TNM(276);I0Pvar(i1(4643));$list(@(i1(4643),I1Vtnm(I1TNM(276))))),I1BNDcons(I1TNM(277);I0Pvar(i2(4644));$list(@(i2(4644),I1Vtnm(I1TNM(277))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_lte$sint);G1Nlist($list())))))))
            pyxtnm278 = XATSDAPP(XATS2PY_sint_lte_sint(pyxtnm274, pyxtnm275))
            pyxtnm279 = pyxtnm278
            ## end-of(let)
            ## I1CMP:return:pyxtnm279
            return pyxtnm279
          ## endtimp(sint_lte$sint(866))
          pyxtnm281 = XATSDAPP(pyxtnm280(pyxtnm273, XATSINT1(0)))
          pyxtnm301 = None
          if (pyxtnm281):
            pyxtnm282 = XATSCAPP("strmcon_vt_nil", [0])
            pyxtnm301 = pyxtnm282
          else:
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2876(line=142,offs=21)--2877(line=142,offs=22))
            ## I0Etapq(I0Ecst(sint_mod$sint(874)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3076(line=143,offs=1)--3089(line=143,offs=14))));$list(T2JAG($list())))
            ## T1IMPallx(sint_mod$sint(874), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3349(line=201,offs=1)--3513(line=213,offs=2)))
            ## T1IMPallx(sint_mod$sint(874)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mod$sint(874);$list()))))
            def pyxtnm289(arg1, arg2): ## timp: sint_mod$sint(874)
              pyxtnm283 = arg1
              pyxtnm284 = arg2
              ## I1CMP:start
              ## let
              pyxtnm288 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3439(line=209,offs=1)--3511(line=212,offs=39)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mod$sint(2449));$list(I1FUNDCL(XATS2PY_sint_mod$sint(4677);$list(FJARGdarg($list(I1BNDcons(I1TNM(285);I0Pvar(i1(4678));$list(@(i1(4678),I1Vtnm(I1TNM(285))))),I1BNDcons(I1TNM(286);I0Pvar(i2(4679));$list(@(i2(4679),I1Vtnm(I1TNM(286))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mod$sint);G1Nlist($list())))))))
              pyxtnm287 = XATSDAPP(XATS2PY_sint_mod_sint(pyxtnm283, pyxtnm284))
              pyxtnm288 = pyxtnm287
              ## end-of(let)
              ## I1CMP:return:pyxtnm288
              return pyxtnm288
            ## endtimp(sint_mod$sint(874))
            pyxtnm290 = XATSDAPP(pyxtnm289(pyxtnm273, pyxtnm272))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2891(line=142,offs=36)--2892(line=142,offs=37))
            ## I0Etapq(I0Ecst(sint_div$sint(873)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3011(line=139,offs=1)--3024(line=139,offs=14))));$list(T2JAG($list())))
            ## T1IMPallx(sint_div$sint(873), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3181(line=187,offs=1)--3345(line=199,offs=2)))
            ## T1IMPallx(sint_div$sint(873)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_div$sint(873);$list()))))
            def pyxtnm297(arg1, arg2): ## timp: sint_div$sint(873)
              pyxtnm291 = arg1
              pyxtnm292 = arg2
              ## I1CMP:start
              ## let
              pyxtnm296 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3271(line=195,offs=1)--3343(line=198,offs=39)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_div$sint(2448));$list(I1FUNDCL(XATS2PY_sint_div$sint(4672);$list(FJARGdarg($list(I1BNDcons(I1TNM(293);I0Pvar(i1(4673));$list(@(i1(4673),I1Vtnm(I1TNM(293))))),I1BNDcons(I1TNM(294);I0Pvar(i2(4674));$list(@(i2(4674),I1Vtnm(I1TNM(294))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_div$sint);G1Nlist($list())))))))
              pyxtnm295 = XATSDAPP(XATS2PY_sint_div_sint(pyxtnm291, pyxtnm292))
              pyxtnm296 = pyxtnm295
              ## end-of(let)
              ## I1CMP:return:pyxtnm296
              return pyxtnm296
            ## endtimp(sint_div$sint(873))
            pyxtnm298 = XATSDAPP(pyxtnm297(pyxtnm273, pyxtnm272))
            pyxtnm299 = XATSDAPP(auxmain_2759(pyxtnm298))
            pyxtnm300 = XATSCAPP("strmcon_vt_cons", [1, pyxtnm290, pyxtnm299])
            pyxtnm301 = pyxtnm300
          ## end-of(if)
          ## I1CMP:return:pyxtnm301
          return pyxtnm301
        ## } // end(l1azy)
        ## I1CMP:return:pyxtnm302
        return pyxtnm302
      pyxtnm303 = XATSDAPP(auxmain_2759(pyxtnm271))
      pyxtnm304 = pyxtnm303
      ## end-of(let)
      ## I1CMP:return:pyxtnm304
      return pyxtnm304
    ## endtimp(nint_base$rdigitize(2130))
    pyxtnm306 = XATSDAPP(pyxtnm305(pyxtnm255, pyxtnm256))
    pyxtnm307 = XATSDAPP(pyxtnm270(pyxtnm306))
    ## I1CMP:return:pyxtnm307
    return pyxtnm307
  ## endtimp(nint_base$digitize(2129))
  pyxtnm309 = XATSDAPP(pyxtnm308(pyxtnm254, XATSINT1(10)))
  ## I1CMP:return:pyxtnm309
  return pyxtnm309
## endtimp(nint_digitize(2127))
pyxtnm311 = XATSDAPP(pyxtnm310(XATSINT1(123456789)))
pyxtnm312 = pyxtnm311
XATS000_patck(True)
## LCSRCsome1(test01_pre2026.dats)@(632(line=40,offs=1)--639(line=40,offs=8))
## I0Etapq(I0Ecst(gs_print1_a3(1857)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3614(line=218,offs=1)--3626(line=218,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
## T1IMPallx(gs_print1_a3(1857), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5507(line=274,offs=1)--5674(line=283,offs=21)))
## T1IMPallx(gs_print1_a3(1857)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7768],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7769],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7770],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a3(1857);$list(@(x0[4737],T2Pvar(x0[7768])),@(x1[4738],T2Pvar(x1[7769])),@(x2[4739],T2Pvar(x2[7770])))))))
def pyxtnm474(arg1, arg2, arg3): ## timp: gs_print1_a3(1857)
  pyxtnm313 = arg1
  pyxtnm314 = arg2
  pyxtnm315 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5578(line=280,offs=3)--5591(line=280,offs=16))
  ## I0Etapq(I0Ecst(gs_print$beg1(1841)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg1(1841), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
  ## T1IMPallx(gs_print$beg1(1841)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg1(1841);$list()))))
  def pyxtnm317(): ## timp: gs_print$beg1(1841)
    ## I1CMP:start
    pyxtnm316 = XATSTUP0([])
    ## I1CMP:return:pyxtnm316
    return pyxtnm316
  ## endtimp(gs_print$beg1(1841))
  pyxtnm318 = XATSDAPP(pyxtnm317())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5599(line=281,offs=3)--5607(line=281,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7768])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm325 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(strn)))))))
  pyxtnm324 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
  def pyxtnm323(arg1): ## timp: strn_print(974)
    pyxtnm319 = arg1
    ## I1CMP:start
    ## let
    pyxtnm322 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(320);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(320))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm321 = XATSDAPP(XATS2PY_strn_print(pyxtnm319))
    pyxtnm322 = pyxtnm321
    ## end-of(let)
    ## I1CMP:return:pyxtnm322
    return pyxtnm322
  ## endtimp(strn_print(974))
  pyxtnm324 = pyxtnm323
  pyxtnm325 = pyxtnm324
  pyxtnm326 = XATSDAPP(pyxtnm325(pyxtnm313))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5618(line=282,offs=3)--5626(line=282,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[7769])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2935(line=156,offs=1)--3019(line=162,offs=2)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7873],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7873])))))))))
  def pyxtnm461(arg1): ## timp: g_print1(1329)
    pyxtnm327 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2985(line=161,offs=1)--2996(line=161,offs=12))
    ## I0Etapq(I0Ecst(gseq_print1(1561)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3970(line=243,offs=1)--3981(line=243,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[7873]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7873])))))
    ## T1IMPallx(gseq_print1(1561), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4437(line=281,offs=1)--4754(line=306,offs=7)))
    ## T1IMPallx(gseq_print1(1561)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1561);$list(@(xs[3852],T2Pvar(xs[7298])),@(x0[3853],T2Pvar(x0[7299])))))))
    def pyxtnm459(arg1): ## timp: gseq_print1(1561)
      pyxtnm328 = arg1
      ## I1CMP:start
      ## let
      pyxtnm458 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4488(line=286,offs=1)--4530(line=288,offs=21)))
      ## I1VALDCL
      pyxtnm337 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4497(line=287,offs=1)--4507(line=287,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm333(arg1): ## timp: strn_print(974)
        pyxtnm329 = arg1
        ## I1CMP:start
        ## let
        pyxtnm332 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(330);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(330))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm331 = XATSDAPP(XATS2PY_strn_print(pyxtnm329))
        pyxtnm332 = pyxtnm331
        ## end-of(let)
        ## I1CMP:return:pyxtnm332
        return pyxtnm332
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4511(line=288,offs=2)--4519(line=288,offs=10))
      ## I0Etapq(I0Ecst(gseq_beg(319)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2370(line=129,offs=1)--2378(line=129,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_beg(319), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq_beg(319)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_beg(319);$list(@(xs[949],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7871])))),@(x0[950],T2Pvar(x0[7871])))))))
      def pyxtnm334(): ## timp: gseq_beg(319)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN("list_vt(")
        return XATSSTRN("list_vt(")
      ## endtimp(gseq_beg(319))
      pyxtnm335 = XATSDAPP(pyxtnm334())
      pyxtnm336 = XATSDAPP(pyxtnm333(pyxtnm335))
      pyxtnm337 = pyxtnm336
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4531(line=289,offs=1)--4705(line=303,offs=2)))
      ## I1VALDCL
      pyxtnm448 = None
      ## let
      pyxtnm447 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Pvar(x0[7299]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4542(line=291,offs=1)--4555(line=291,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1635)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10879(line=588,offs=1)--10892(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_iforitm1(1635), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9859(line=671,offs=1)--10064(line=688,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1635)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1635);$list(@(xs[4038],T2Pvar(xs[7435])),@(x0[4039],T2Pvar(x0[7436])))))))
      def pyxtnm445(arg1): ## timp: gseq_iforitm1(1635)
        pyxtnm347 = arg1
        ## I1CMP:start
        ## let
        pyxtnm444 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Pvar(x0[7436]))))):timp
        ## let
        pyxtnm443 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9919(line=678,offs=1)--9955(line=680,offs=15)))
        ## I1VALDCL
        pyxtnm442 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9927(line=679,offs=1)--9940(line=679,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1611)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6521(line=346,offs=1)--6534(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[7435]))),T2JAG($list(T2Pvar(x0[7436])))))
        ## T1IMPallx(gseq_iforall1(1611), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5881(line=370,offs=1)--6184(line=396,offs=2)))
        ## T1IMPallx(gseq_iforall1(1611)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1611);$list(@(xs[3990],T2Pvar(xs[7403])),@(x0[3991],T2Pvar(x0[7404])))))))
        def pyxtnm440(arg1): ## timp: gseq_iforall1(1611)
          pyxtnm353 = arg1
          ## I1CMP:start
          ## let
          pyxtnm439 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5949(line=377,offs=1)--5965(line=377,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:XATSINT1(0)
          pyxtnm354 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5969(line=379,offs=1)--5987(line=379,offs=19)))
          ## I1VALDCL
          pyxtnm355 = None
          pyxtnm355 = XATSADDR(pyxtnm354)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5991(line=381,offs=1)--6179(line=394,offs=2)))
          ## I1VALDCL
          pyxtnm438 = None
          ## let
          pyxtnm437 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Pvar(x0[7404]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6002(line=383,offs=1)--6014(line=383,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1595)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[7403]))),T2JAG($list(T2Pvar(x0[7404])))))
          ## T1IMPallx(gseq_forall1(1595), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2042(line=92,offs=1)--2113(line=95,offs=40)))
          ## T1IMPallx(gseq_forall1(1595)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1595);$list(@(xs[3958],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7912])))),@(x0[3959],T2Pvar(x0[7912])))))))
          pyxtnm435 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2094(line=95,offs=21)--2109(line=95,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall1(1908)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1481(line=47,offs=1)--1496(line=47,offs=16))));$list(T2JAG($list(T2Pvar(x0[7912])))))
          ## T1IMPallx(list_vt_forall1(1908), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1701(line=65,offs=1)--1958(line=86,offs=2)))
          ## T1IMPallx(list_vt_forall1(1908)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7910],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall1(1908);$list(@(x0[4880],T2Pvar(x0[7910])))))))
          def pyxtnm434(arg1): ## timp: list_vt_forall1(1908)
            pyxtnm364 = arg1
            ## I1CMP:start
            ## let
            pyxtnm433 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1771(line=72,offs=1)--1956(line=85,offs=38)))
            ## I1FUNDCL
            def loop_1774(arg1): ## fun
              pyxtnm365 = arg1
              ## I1CMP:start
              pyxtnm431 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(366);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
                if (XATS000_ctgeq(pyxtnm365, XATSCTAG("list_vt_nil",0))): ## { // gpt
                  pyxtnm366 = pyxtnm365
                  pyxtnm431 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(367);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(4054)),I0Pvar(xs(4055))));$list(@(x1(4054),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(367));0)),@(xs(4055),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(367));1)))))
                if (XATS000_ctgeq(pyxtnm365, XATSCTAG("list_vt_cons",1))): ## { // gpt
                  pyxtnm367 = pyxtnm365
                  ## let
                  pyxtnm430 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1884(line=83,offs=1)--1915(line=84,offs=21)))
                  ## I1VALDCL
                  pyxtnm427 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1895(line=84,offs=1)--1907(line=84,offs=13))
                  ## I0Etapq(I0Ecst(forall$test1(1340)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[7910])))))
                  ## T1IMPallx(forall$test1(1340), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
                  ## T1IMPallx(forall$test1(1340)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm425(arg1): ## timp: forall$test1(1340)
                    pyxtnm368 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm424 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6111(line=392,offs=1)--6140(line=392,offs=30)))
                    ## I1VALDCL
                    pyxtnm373 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6124(line=392,offs=14)--6132(line=392,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2151)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2151), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2151)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5486],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2151);$list(@(a[5302],T2Pvar(a[5486])))))))
                    def pyxtnm371(arg1): ## timp: p2tr_get(2151)
                      pyxtnm369 = arg1
                      ## I1CMP:start
                      pyxtnm370 = XATS000_dp2tr(pyxtnm369)
                      ## I1CMP:return:pyxtnm370
                      return pyxtnm370
                    ## endtimp(p2tr_get(2151))
                    pyxtnm372 = XATSDAPP(pyxtnm371(pyxtnm355))
                    pyxtnm373 = pyxtnm372
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6141(line=393,offs=1)--6175(line=393,offs=35)))
                    ## I1VALDCL
                    pyxtnm411 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6150(line=393,offs=10)--6163(line=393,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test1(1352)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2693(line=154,offs=1)--2706(line=154,offs=14))));$list(T2JAG($list(T2Pvar(x0[7404])))))
                    ## T1IMPallx(iforall$test1(1352), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
                    ## T1IMPallx(iforall$test1(1352)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm409(arg1, arg2): ## timp: iforall$test1(1352)
                      pyxtnm374 = arg1
                      pyxtnm375 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm408 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10016(line=686,offs=1)--10050(line=687,offs=26)))
                      ## I1VALDCL
                      pyxtnm407 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10025(line=687,offs=1)--10038(line=687,offs=14))
                      ## I0Etapq(I0Ecst(iforitm$work1(1366)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[7436])))))
                      ## T1IMPallx(iforitm$work1(1366), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
                      ## T1IMPallx(iforitm$work1(1366)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm405(arg1, arg2): ## timp: iforitm$work1(1366)
                        pyxtnm376 = arg1
                        pyxtnm377 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm404 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4645(line=299,offs=1)--4701(line=301,offs=33)))
                        ## I1VALDCL
                        pyxtnm395 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4660(line=300,offs=7)--4661(line=300,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(864)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(864), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(864)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(864);$list()))))
                        def pyxtnm384(arg1, arg2): ## timp: sint_gt$sint(864)
                          pyxtnm378 = arg1
                          pyxtnm379 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm383 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2440));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4632);$list(FJARGdarg($list(I1BNDcons(I1TNM(380);I0Pvar(i1(4633));$list(@(i1(4633),I1Vtnm(I1TNM(380))))),I1BNDcons(I1TNM(381);I0Pvar(i2(4634));$list(@(i2(4634),I1Vtnm(I1TNM(381))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm382 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm378, pyxtnm379))
                          pyxtnm383 = pyxtnm382
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm383
                          return pyxtnm383
                        ## endtimp(sint_gt$sint(864))
                        pyxtnm385 = XATSDAPP(pyxtnm384(pyxtnm376, XATSINT1(0)))
                        pyxtnm394 = None
                        if (pyxtnm385):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4669(line=301,offs=1)--4679(line=301,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
                          def pyxtnm390(arg1): ## timp: strn_print(974)
                            pyxtnm386 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm389 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(387);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(387))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm388 = XATSDAPP(XATS2PY_strn_print(pyxtnm386))
                            pyxtnm389 = pyxtnm388
                            ## end-of(let)
                            ## I1CMP:return:pyxtnm389
                            return pyxtnm389
                          ## endtimp(strn_print(974))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4682(line=301,offs=14)--4690(line=301,offs=22))
                          ## I0Etapq(I0Ecst(gseq_sep(321)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2454(line=137,offs=1)--2462(line=137,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
                          ## T1IMPallx(gseq_sep(321), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                          ## T1IMPallx(gseq_sep(321)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_sep(321);$list(@(xs[953],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7869])))),@(x0[954],T2Pvar(x0[7869])))))))
                          def pyxtnm391(): ## timp: gseq_sep(321)
                            ## I1CMP:start
                            ## I1CMP:return:XATSSTRN(",")
                            return XATSSTRN(",")
                          ## endtimp(gseq_sep(321))
                          pyxtnm392 = XATSDAPP(pyxtnm391())
                          pyxtnm393 = XATSDAPP(pyxtnm390(pyxtnm392))
                          pyxtnm394 = pyxtnm393
                        ## else: None
                        ## end-of(if)
                        pyxtnm395 = pyxtnm394
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4619(line=297,offs=3)--4627(line=297,offs=11))
                        ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7299])))))
                        ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                        ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
                        pyxtnm402 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                        ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
                        ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                        ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(si)))))))
                        pyxtnm401 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                        ## I0Etapq(I0Ecst(sint_print(858)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_print(858), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                        ## T1IMPallx(sint_print(858)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(858);$list()))))
                        def pyxtnm400(arg1): ## timp: sint_print(858)
                          pyxtnm396 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm399 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2450));$list(I1FUNDCL(XATS2PY_sint_print(4681);$list(FJARGdarg($list(I1BNDcons(I1TNM(397);I0Pvar(i0(4682));$list(@(i0(4682),I1Vtnm(I1TNM(397))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                          pyxtnm398 = XATSDAPP(XATS2PY_sint_print(pyxtnm396))
                          pyxtnm399 = pyxtnm398
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm399
                          return pyxtnm399
                        ## endtimp(sint_print(858))
                        pyxtnm401 = pyxtnm400
                        pyxtnm402 = pyxtnm401
                        pyxtnm403 = XATSDAPP(pyxtnm402(pyxtnm377))
                        pyxtnm404 = pyxtnm403
                        ## end-of(let)
                        ## I1CMP:return:pyxtnm404
                        return pyxtnm404
                      ## endtimp(iforitm$work1(1366))
                      pyxtnm406 = XATSDAPP(pyxtnm405(pyxtnm374, pyxtnm375))
                      pyxtnm407 = pyxtnm406
                      XATS000_patck(True)
                      pyxtnm408 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm408
                      return pyxtnm408
                    ## endtimp(iforall$test1(1352))
                    pyxtnm410 = XATSDAPP(pyxtnm409(pyxtnm373, pyxtnm368))
                    pyxtnm411 = pyxtnm410
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6075(line=389,offs=5)--6083(line=389,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2152)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2152), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2152)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5487],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2152);$list(@(a[5303],T2Pvar(a[5487])))))))
                    def pyxtnm414(arg1, arg2): ## timp: p2tr_set(2152)
                      pyxtnm412 = arg1
                      pyxtnm413 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm412, pyxtnm413)
                      ## I1CMP:return:[]
                      return []
                    ## endtimp(p2tr_set(2152))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6094(line=389,offs=24)--6095(line=389,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(870)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2816(line=127,offs=1)--2829(line=127,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(870), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(870)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(870);$list()))))
                    def pyxtnm421(arg1, arg2): ## timp: sint_add$sint(870)
                      pyxtnm415 = arg1
                      pyxtnm416 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm420 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2445));$list(I1FUNDCL(XATS2PY_sint_add$sint(4657);$list(FJARGdarg($list(I1BNDcons(I1TNM(417);I0Pvar(i1(4658));$list(@(i1(4658),I1Vtnm(I1TNM(417))))),I1BNDcons(I1TNM(418);I0Pvar(i2(4659));$list(@(i2(4659),I1Vtnm(I1TNM(418))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm419 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm415, pyxtnm416))
                      pyxtnm420 = pyxtnm419
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm420
                      return pyxtnm420
                    ## endtimp(sint_add$sint(870))
                    pyxtnm422 = XATSDAPP(pyxtnm421(pyxtnm373, XATSINT1(1)))
                    pyxtnm423 = XATSDAPP(pyxtnm414(pyxtnm355, pyxtnm422))
                    pyxtnm424 = pyxtnm411
                    ## end-of(let)
                    ## I1CMP:return:pyxtnm424
                    return pyxtnm424
                  ## endtimp(forall$test1(1340))
                  pyxtnm426 = XATSDAPP(pyxtnm425(XATSP1CN("list_vt_cons", pyxtnm367[0+1])))
                  pyxtnm427 = pyxtnm426
                  XATS000_patck(True)
                  pyxtnm429 = None
                  if (pyxtnm427):
                    pyxtnm428 = XATSDAPP(loop_1774(XATSP1CN("list_vt_cons", pyxtnm367[1+1])))
                    pyxtnm429 = pyxtnm428
                  else:
                    pyxtnm429 = XATSBOOL(False)
                  ## end-of(if)
                  pyxtnm430 = pyxtnm429
                  ## end-of(let)
                  pyxtnm431 = pyxtnm430
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:pyxtnm431
              return pyxtnm431
            pyxtnm432 = XATSDAPP(loop_1774(pyxtnm364))
            pyxtnm433 = pyxtnm432
            ## end-of(let)
            ## I1CMP:return:pyxtnm433
            return pyxtnm433
          ## endtimp(list_vt_forall1(1908))
          pyxtnm435 = pyxtnm434
          pyxtnm436 = XATSDAPP(pyxtnm435(pyxtnm353))
          pyxtnm437 = pyxtnm436
          ## end-of(let)
          pyxtnm438 = pyxtnm437
          XATS000_patck(True)
          pyxtnm439 = pyxtnm438
          ## end-of(let)
          ## I1CMP:return:pyxtnm439
          return pyxtnm439
        ## endtimp(gseq_iforall1(1611))
        pyxtnm441 = XATSDAPP(pyxtnm440(pyxtnm347))
        pyxtnm442 = pyxtnm441
        XATS000_patck(True)
        pyxtnm443 = []
        ## end-of(let)
        pyxtnm444 = pyxtnm443
        ## end-of(let)
        ## I1CMP:return:pyxtnm444
        return pyxtnm444
      ## endtimp(gseq_iforitm1(1635))
      pyxtnm446 = XATSDAPP(pyxtnm445(pyxtnm328))
      pyxtnm447 = pyxtnm446
      ## end-of(let)
      pyxtnm448 = pyxtnm447
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=304,offs=1)--4747(line=305,offs=33)))
      ## I1VALDCL
      pyxtnm457 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=305,offs=1)--4725(line=305,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm453(arg1): ## timp: strn_print(974)
        pyxtnm449 = arg1
        ## I1CMP:start
        ## let
        pyxtnm452 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(450);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(450))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm451 = XATSDAPP(XATS2PY_strn_print(pyxtnm449))
        pyxtnm452 = pyxtnm451
        ## end-of(let)
        ## I1CMP:return:pyxtnm452
        return pyxtnm452
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=305,offs=14)--4736(line=305,offs=22))
      ## I0Etapq(I0Ecst(gseq_end(320)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2412(line=133,offs=1)--2420(line=133,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_end(320), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq_end(320)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_end(320);$list(@(xs[951],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7870])))),@(x0[952],T2Pvar(x0[7870])))))))
      def pyxtnm454(): ## timp: gseq_end(320)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN(")")
        return XATSSTRN(")")
      ## endtimp(gseq_end(320))
      pyxtnm455 = XATSDAPP(pyxtnm454())
      pyxtnm456 = XATSDAPP(pyxtnm453(pyxtnm455))
      pyxtnm457 = pyxtnm456
      XATS000_patck(True)
      pyxtnm458 = []
      ## end-of(let)
      ## I1CMP:return:pyxtnm458
      return pyxtnm458
    ## endtimp(gseq_print1(1561))
    pyxtnm460 = XATSDAPP(pyxtnm459(pyxtnm327))
    ## I1CMP:return:pyxtnm460
    return pyxtnm460
  ## endtimp(g_print1(1329))
  pyxtnm462 = XATSDAPP(pyxtnm461(pyxtnm314))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5636(line=282,offs=21)--5644(line=282,offs=29))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[7770])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm469 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2611(line=136,offs=1)--2648(line=137,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(char)))))))
  pyxtnm468 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2636(line=137,offs=17)--2646(line=137,offs=27))
  ## I0Etapq(I0Ecst(char_print(826)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/char000.sats)@(2501(line=119,offs=1)--2511(line=119,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(char_print(826), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2887(line=170,offs=1)--3027(line=181,offs=2)))
  ## T1IMPallx(char_print(826)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(char_print(826);$list()))))
  def pyxtnm467(arg1): ## timp: char_print(826)
    pyxtnm463 = arg1
    ## I1CMP:start
    ## let
    pyxtnm466 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2967(line=178,offs=1)--3025(line=180,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_char_print(2437));$list(I1FUNDCL(XATS2PY_char_print(4620);$list(FJARGdarg($list(I1BNDcons(I1TNM(464);I0Pvar(c0(4621));$list(@(c0(4621),I1Vtnm(I1TNM(464))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_char_print);G1Nlist($list())))))))
    pyxtnm465 = XATSDAPP(XATS2PY_char_print(pyxtnm463))
    pyxtnm466 = pyxtnm465
    ## end-of(let)
    ## I1CMP:return:pyxtnm466
    return pyxtnm466
  ## endtimp(char_print(826))
  pyxtnm468 = pyxtnm467
  pyxtnm469 = pyxtnm468
  pyxtnm470 = XATSDAPP(pyxtnm469(pyxtnm315))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5656(line=283,offs=3)--5669(line=283,offs=16))
  ## I0Etapq(I0Ecst(gs_print$end1(1842)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end1(1842), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
  ## T1IMPallx(gs_print$end1(1842)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end1(1842);$list()))))
  def pyxtnm472(): ## timp: gs_print$end1(1842)
    ## I1CMP:start
    pyxtnm471 = XATSTUP0([])
    ## I1CMP:return:pyxtnm471
    return pyxtnm471
  ## endtimp(gs_print$end1(1842))
  pyxtnm473 = XATSDAPP(pyxtnm472())
  ## I1CMP:return:pyxtnm473
  return pyxtnm473
## endtimp(gs_print1_a3(1857))
pyxtnm475 = XATSDAPP(pyxtnm474(XATSSTRN("nint_digitize(123456789) = "), pyxtnm312, XATSCHR2('\n')))
pyxtnm476 = pyxtnm475
## end-of(let)
pyxtnm477 = pyxtnm476
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(687(line=42,offs=1)--797(line=47,offs=47)))
## I1VALDCL
pyxtnm698 = None
## let
pyxtnm697 = None
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(700(line=44,offs=1)--736(line=45,offs=28)))
## I1VALDCL
pyxtnm533 = None
## LCSRCsome1(test01_pre2026.dats)@(709(line=45,offs=1)--727(line=45,offs=19))
## I0Etapq(I0Ecst(nint_base$digitize(2129)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2000(line=82,offs=1)--2018(line=82,offs=19))));$list(T2JAG($list())))
## T1IMPallx(nint_base$digitize(2129), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2567(line=117,offs=1)--2672(line=123,offs=31)))
## T1IMPallx(nint_base$digitize(2129)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$digitize(2129);$list()))))
def pyxtnm531(arg1, arg2): ## timp: nint_base$digitize(2129)
  pyxtnm478 = arg1
  pyxtnm479 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2618(line=121,offs=1)--2635(line=121,offs=18))
  ## I0Etapq(I0Ecst(strm_vt_rlistize0(2074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm001_vt.sats)@(8509(line=433,offs=1)--8526(line=433,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  ## T1IMPallx(strm_vt_rlistize0(2074), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7032(line=445,offs=1)--7325(line=468,offs=2)))
  ## T1IMPallx(strm_vt_rlistize0(2074)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8065],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_rlistize0(2074);$list(@(x0[5158],T2Pvar(x0[8065])))))))
  def pyxtnm493(arg1): ## timp: strm_vt_rlistize0(2074)
    pyxtnm480 = arg1
    ## I1CMP:start
    ## let
    pyxtnm492 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7109(line=453,offs=1)--7131(line=453,offs=23)))
    ## I1VALDCL
    pyxtnm482 = None
    pyxtnm481 = XATSCAPP("list_vt_nil", [0])
    pyxtnm482 = pyxtnm481
    XATS000_patck(True)
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7135(line=455,offs=1)--7323(line=467,offs=35)))
    ## I1FUNDCL
    def loop_7138(arg1, arg2): ## fun
      pyxtnm483 = arg1
      pyxtnm484 = arg2
      ## I1CMP:start
      pyxtnm485 = XATS000_dl1az(pyxtnm483)
      pyxtnm490 = None
      while True: ## do {
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(486);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
        if (XATS000_ctgeq(pyxtnm485, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
          pyxtnm486 = pyxtnm485
          pyxtnm490 = pyxtnm484
          break ## cls
        ## } // gpt
        ## } // cls
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(487);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(4259)),I0Pvar(xs(4260)))));$list(@(x1(4259),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(487));0)),@(xs(4260),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(487));1)))))
        if (XATS000_ctgeq(pyxtnm485, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
          pyxtnm487 = pyxtnm485
          pyxtnm488 = XATSCAPP("list_vt_cons", [1, XATSP1CN("strmcon_vt_cons", pyxtnm487[0+1]), pyxtnm484])
          pyxtnm489 = XATSDAPP(loop_7138(XATSP1CN("strmcon_vt_cons", pyxtnm487[1+1]), pyxtnm488))
          pyxtnm490 = pyxtnm489
          break ## cls
        ## } // gpt
        ## } // cls
        XATS000_cfail()
      ## } while True // end-of(do-cls)
      ## I1CMP:return:pyxtnm490
      return pyxtnm490
    pyxtnm491 = XATSDAPP(loop_7138(pyxtnm480, pyxtnm482))
    pyxtnm492 = pyxtnm491
    ## end-of(let)
    ## I1CMP:return:pyxtnm492
    return pyxtnm492
  ## endtimp(strm_vt_rlistize0(2074))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2642(line=123,offs=1)--2661(line=123,offs=20))
  ## I0Etapq(I0Ecst(nint_base$rdigitize(2130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2067(line=85,offs=1)--2086(line=85,offs=20))));$list(T2JAG($list())))
  ## T1IMPallx(nint_base$rdigitize(2130), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2676(line=125,offs=1)--2903(line=144,offs=2)))
  ## T1IMPallx(nint_base$rdigitize(2130)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$rdigitize(2130);$list()))))
  def pyxtnm528(arg1, arg2): ## timp: nint_base$rdigitize(2130)
    pyxtnm494 = arg1
    pyxtnm495 = arg2
    ## I1CMP:start
    ## let
    pyxtnm527 = None
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2756(line=133,offs=1)--2898(line=142,offs=43)))
    ## I1FUNDCL
    def auxmain_2759(arg1): ## fun
      pyxtnm496 = arg1
      ## I1CMP:start
      def pyxtnm525(tlaz): ## { // l1azy
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2818(line=139,offs=5)--2820(line=139,offs=7))
        ## I0Etapq(I0Ecst(sint_lte$sint(866)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2344(line=100,offs=1)--2357(line=100,offs=14))));$list(T2JAG($list())))
        ## T1IMPallx(sint_lte$sint(866), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2130(line=100,offs=1)--2294(line=112,offs=2)))
        ## T1IMPallx(sint_lte$sint(866)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_lte$sint(866);$list()))))
        def pyxtnm503(arg1, arg2): ## timp: sint_lte$sint(866)
          pyxtnm497 = arg1
          pyxtnm498 = arg2
          ## I1CMP:start
          ## let
          pyxtnm502 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2220(line=108,offs=1)--2292(line=111,offs=39)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_lte$sint(2442));$list(I1FUNDCL(XATS2PY_sint_lte$sint(4642);$list(FJARGdarg($list(I1BNDcons(I1TNM(499);I0Pvar(i1(4643));$list(@(i1(4643),I1Vtnm(I1TNM(499))))),I1BNDcons(I1TNM(500);I0Pvar(i2(4644));$list(@(i2(4644),I1Vtnm(I1TNM(500))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_lte$sint);G1Nlist($list())))))))
          pyxtnm501 = XATSDAPP(XATS2PY_sint_lte_sint(pyxtnm497, pyxtnm498))
          pyxtnm502 = pyxtnm501
          ## end-of(let)
          ## I1CMP:return:pyxtnm502
          return pyxtnm502
        ## endtimp(sint_lte$sint(866))
        pyxtnm504 = XATSDAPP(pyxtnm503(pyxtnm496, XATSINT1(0)))
        pyxtnm524 = None
        if (pyxtnm504):
          pyxtnm505 = XATSCAPP("strmcon_vt_nil", [0])
          pyxtnm524 = pyxtnm505
        else:
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2876(line=142,offs=21)--2877(line=142,offs=22))
          ## I0Etapq(I0Ecst(sint_mod$sint(874)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3076(line=143,offs=1)--3089(line=143,offs=14))));$list(T2JAG($list())))
          ## T1IMPallx(sint_mod$sint(874), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3349(line=201,offs=1)--3513(line=213,offs=2)))
          ## T1IMPallx(sint_mod$sint(874)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mod$sint(874);$list()))))
          def pyxtnm512(arg1, arg2): ## timp: sint_mod$sint(874)
            pyxtnm506 = arg1
            pyxtnm507 = arg2
            ## I1CMP:start
            ## let
            pyxtnm511 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3439(line=209,offs=1)--3511(line=212,offs=39)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mod$sint(2449));$list(I1FUNDCL(XATS2PY_sint_mod$sint(4677);$list(FJARGdarg($list(I1BNDcons(I1TNM(508);I0Pvar(i1(4678));$list(@(i1(4678),I1Vtnm(I1TNM(508))))),I1BNDcons(I1TNM(509);I0Pvar(i2(4679));$list(@(i2(4679),I1Vtnm(I1TNM(509))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mod$sint);G1Nlist($list())))))))
            pyxtnm510 = XATSDAPP(XATS2PY_sint_mod_sint(pyxtnm506, pyxtnm507))
            pyxtnm511 = pyxtnm510
            ## end-of(let)
            ## I1CMP:return:pyxtnm511
            return pyxtnm511
          ## endtimp(sint_mod$sint(874))
          pyxtnm513 = XATSDAPP(pyxtnm512(pyxtnm496, pyxtnm495))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2891(line=142,offs=36)--2892(line=142,offs=37))
          ## I0Etapq(I0Ecst(sint_div$sint(873)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3011(line=139,offs=1)--3024(line=139,offs=14))));$list(T2JAG($list())))
          ## T1IMPallx(sint_div$sint(873), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3181(line=187,offs=1)--3345(line=199,offs=2)))
          ## T1IMPallx(sint_div$sint(873)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_div$sint(873);$list()))))
          def pyxtnm520(arg1, arg2): ## timp: sint_div$sint(873)
            pyxtnm514 = arg1
            pyxtnm515 = arg2
            ## I1CMP:start
            ## let
            pyxtnm519 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3271(line=195,offs=1)--3343(line=198,offs=39)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_div$sint(2448));$list(I1FUNDCL(XATS2PY_sint_div$sint(4672);$list(FJARGdarg($list(I1BNDcons(I1TNM(516);I0Pvar(i1(4673));$list(@(i1(4673),I1Vtnm(I1TNM(516))))),I1BNDcons(I1TNM(517);I0Pvar(i2(4674));$list(@(i2(4674),I1Vtnm(I1TNM(517))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_div$sint);G1Nlist($list())))))))
            pyxtnm518 = XATSDAPP(XATS2PY_sint_div_sint(pyxtnm514, pyxtnm515))
            pyxtnm519 = pyxtnm518
            ## end-of(let)
            ## I1CMP:return:pyxtnm519
            return pyxtnm519
          ## endtimp(sint_div$sint(873))
          pyxtnm521 = XATSDAPP(pyxtnm520(pyxtnm496, pyxtnm495))
          pyxtnm522 = XATSDAPP(auxmain_2759(pyxtnm521))
          pyxtnm523 = XATSCAPP("strmcon_vt_cons", [1, pyxtnm513, pyxtnm522])
          pyxtnm524 = pyxtnm523
        ## end-of(if)
        ## I1CMP:return:pyxtnm524
        return pyxtnm524
      ## } // end(l1azy)
      ## I1CMP:return:pyxtnm525
      return pyxtnm525
    pyxtnm526 = XATSDAPP(auxmain_2759(pyxtnm494))
    pyxtnm527 = pyxtnm526
    ## end-of(let)
    ## I1CMP:return:pyxtnm527
    return pyxtnm527
  ## endtimp(nint_base$rdigitize(2130))
  pyxtnm529 = XATSDAPP(pyxtnm528(pyxtnm478, pyxtnm479))
  pyxtnm530 = XATSDAPP(pyxtnm493(pyxtnm529))
  ## I1CMP:return:pyxtnm530
  return pyxtnm530
## endtimp(nint_base$digitize(2129))
pyxtnm532 = XATSDAPP(pyxtnm531(XATSINT1(1024), XATSINT1(2)))
pyxtnm533 = pyxtnm532
XATS000_patck(True)
## LCSRCsome1(test01_pre2026.dats)@(740(line=46,offs=1)--747(line=46,offs=8))
## I0Etapq(I0Ecst(gs_print1_a3(1857)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3614(line=218,offs=1)--3626(line=218,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
## T1IMPallx(gs_print1_a3(1857), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5507(line=274,offs=1)--5674(line=283,offs=21)))
## T1IMPallx(gs_print1_a3(1857)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7768],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7769],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7770],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a3(1857);$list(@(x0[4737],T2Pvar(x0[7768])),@(x1[4738],T2Pvar(x1[7769])),@(x2[4739],T2Pvar(x2[7770])))))))
def pyxtnm695(arg1, arg2, arg3): ## timp: gs_print1_a3(1857)
  pyxtnm534 = arg1
  pyxtnm535 = arg2
  pyxtnm536 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5578(line=280,offs=3)--5591(line=280,offs=16))
  ## I0Etapq(I0Ecst(gs_print$beg1(1841)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg1(1841), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
  ## T1IMPallx(gs_print$beg1(1841)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg1(1841);$list()))))
  def pyxtnm538(): ## timp: gs_print$beg1(1841)
    ## I1CMP:start
    pyxtnm537 = XATSTUP0([])
    ## I1CMP:return:pyxtnm537
    return pyxtnm537
  ## endtimp(gs_print$beg1(1841))
  pyxtnm539 = XATSDAPP(pyxtnm538())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5599(line=281,offs=3)--5607(line=281,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7768])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm546 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(strn)))))))
  pyxtnm545 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
  def pyxtnm544(arg1): ## timp: strn_print(974)
    pyxtnm540 = arg1
    ## I1CMP:start
    ## let
    pyxtnm543 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(541);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(541))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm542 = XATSDAPP(XATS2PY_strn_print(pyxtnm540))
    pyxtnm543 = pyxtnm542
    ## end-of(let)
    ## I1CMP:return:pyxtnm543
    return pyxtnm543
  ## endtimp(strn_print(974))
  pyxtnm545 = pyxtnm544
  pyxtnm546 = pyxtnm545
  pyxtnm547 = XATSDAPP(pyxtnm546(pyxtnm534))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5618(line=282,offs=3)--5626(line=282,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[7769])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2935(line=156,offs=1)--3019(line=162,offs=2)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7873],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7873])))))))))
  def pyxtnm682(arg1): ## timp: g_print1(1329)
    pyxtnm548 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2985(line=161,offs=1)--2996(line=161,offs=12))
    ## I0Etapq(I0Ecst(gseq_print1(1561)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3970(line=243,offs=1)--3981(line=243,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[7873]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7873])))))
    ## T1IMPallx(gseq_print1(1561), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4437(line=281,offs=1)--4754(line=306,offs=7)))
    ## T1IMPallx(gseq_print1(1561)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1561);$list(@(xs[3852],T2Pvar(xs[7298])),@(x0[3853],T2Pvar(x0[7299])))))))
    def pyxtnm680(arg1): ## timp: gseq_print1(1561)
      pyxtnm549 = arg1
      ## I1CMP:start
      ## let
      pyxtnm679 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4488(line=286,offs=1)--4530(line=288,offs=21)))
      ## I1VALDCL
      pyxtnm558 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4497(line=287,offs=1)--4507(line=287,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm554(arg1): ## timp: strn_print(974)
        pyxtnm550 = arg1
        ## I1CMP:start
        ## let
        pyxtnm553 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(551);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(551))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm552 = XATSDAPP(XATS2PY_strn_print(pyxtnm550))
        pyxtnm553 = pyxtnm552
        ## end-of(let)
        ## I1CMP:return:pyxtnm553
        return pyxtnm553
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4511(line=288,offs=2)--4519(line=288,offs=10))
      ## I0Etapq(I0Ecst(gseq_beg(319)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2370(line=129,offs=1)--2378(line=129,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_beg(319), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq_beg(319)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_beg(319);$list(@(xs[949],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7871])))),@(x0[950],T2Pvar(x0[7871])))))))
      def pyxtnm555(): ## timp: gseq_beg(319)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN("list_vt(")
        return XATSSTRN("list_vt(")
      ## endtimp(gseq_beg(319))
      pyxtnm556 = XATSDAPP(pyxtnm555())
      pyxtnm557 = XATSDAPP(pyxtnm554(pyxtnm556))
      pyxtnm558 = pyxtnm557
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4531(line=289,offs=1)--4705(line=303,offs=2)))
      ## I1VALDCL
      pyxtnm669 = None
      ## let
      pyxtnm668 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Pvar(x0[7299]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4542(line=291,offs=1)--4555(line=291,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1635)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10879(line=588,offs=1)--10892(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_iforitm1(1635), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9859(line=671,offs=1)--10064(line=688,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1635)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1635);$list(@(xs[4038],T2Pvar(xs[7435])),@(x0[4039],T2Pvar(x0[7436])))))))
      def pyxtnm666(arg1): ## timp: gseq_iforitm1(1635)
        pyxtnm568 = arg1
        ## I1CMP:start
        ## let
        pyxtnm665 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Pvar(x0[7436]))))):timp
        ## let
        pyxtnm664 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9919(line=678,offs=1)--9955(line=680,offs=15)))
        ## I1VALDCL
        pyxtnm663 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9927(line=679,offs=1)--9940(line=679,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1611)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6521(line=346,offs=1)--6534(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[7435]))),T2JAG($list(T2Pvar(x0[7436])))))
        ## T1IMPallx(gseq_iforall1(1611), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5881(line=370,offs=1)--6184(line=396,offs=2)))
        ## T1IMPallx(gseq_iforall1(1611)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1611);$list(@(xs[3990],T2Pvar(xs[7403])),@(x0[3991],T2Pvar(x0[7404])))))))
        def pyxtnm661(arg1): ## timp: gseq_iforall1(1611)
          pyxtnm574 = arg1
          ## I1CMP:start
          ## let
          pyxtnm660 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5949(line=377,offs=1)--5965(line=377,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:XATSINT1(0)
          pyxtnm575 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5969(line=379,offs=1)--5987(line=379,offs=19)))
          ## I1VALDCL
          pyxtnm576 = None
          pyxtnm576 = XATSADDR(pyxtnm575)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5991(line=381,offs=1)--6179(line=394,offs=2)))
          ## I1VALDCL
          pyxtnm659 = None
          ## let
          pyxtnm658 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Pvar(x0[7404]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6002(line=383,offs=1)--6014(line=383,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1595)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[7403]))),T2JAG($list(T2Pvar(x0[7404])))))
          ## T1IMPallx(gseq_forall1(1595), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2042(line=92,offs=1)--2113(line=95,offs=40)))
          ## T1IMPallx(gseq_forall1(1595)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1595);$list(@(xs[3958],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7912])))),@(x0[3959],T2Pvar(x0[7912])))))))
          pyxtnm656 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2094(line=95,offs=21)--2109(line=95,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall1(1908)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1481(line=47,offs=1)--1496(line=47,offs=16))));$list(T2JAG($list(T2Pvar(x0[7912])))))
          ## T1IMPallx(list_vt_forall1(1908), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1701(line=65,offs=1)--1958(line=86,offs=2)))
          ## T1IMPallx(list_vt_forall1(1908)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7910],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall1(1908);$list(@(x0[4880],T2Pvar(x0[7910])))))))
          def pyxtnm655(arg1): ## timp: list_vt_forall1(1908)
            pyxtnm585 = arg1
            ## I1CMP:start
            ## let
            pyxtnm654 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1771(line=72,offs=1)--1956(line=85,offs=38)))
            ## I1FUNDCL
            def loop_1774(arg1): ## fun
              pyxtnm586 = arg1
              ## I1CMP:start
              pyxtnm652 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(587);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
                if (XATS000_ctgeq(pyxtnm586, XATSCTAG("list_vt_nil",0))): ## { // gpt
                  pyxtnm587 = pyxtnm586
                  pyxtnm652 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(588);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(4054)),I0Pvar(xs(4055))));$list(@(x1(4054),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(588));0)),@(xs(4055),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(588));1)))))
                if (XATS000_ctgeq(pyxtnm586, XATSCTAG("list_vt_cons",1))): ## { // gpt
                  pyxtnm588 = pyxtnm586
                  ## let
                  pyxtnm651 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1884(line=83,offs=1)--1915(line=84,offs=21)))
                  ## I1VALDCL
                  pyxtnm648 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1895(line=84,offs=1)--1907(line=84,offs=13))
                  ## I0Etapq(I0Ecst(forall$test1(1340)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[7910])))))
                  ## T1IMPallx(forall$test1(1340), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
                  ## T1IMPallx(forall$test1(1340)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm646(arg1): ## timp: forall$test1(1340)
                    pyxtnm589 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm645 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6111(line=392,offs=1)--6140(line=392,offs=30)))
                    ## I1VALDCL
                    pyxtnm594 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6124(line=392,offs=14)--6132(line=392,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2151)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2151), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2151)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5486],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2151);$list(@(a[5302],T2Pvar(a[5486])))))))
                    def pyxtnm592(arg1): ## timp: p2tr_get(2151)
                      pyxtnm590 = arg1
                      ## I1CMP:start
                      pyxtnm591 = XATS000_dp2tr(pyxtnm590)
                      ## I1CMP:return:pyxtnm591
                      return pyxtnm591
                    ## endtimp(p2tr_get(2151))
                    pyxtnm593 = XATSDAPP(pyxtnm592(pyxtnm576))
                    pyxtnm594 = pyxtnm593
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6141(line=393,offs=1)--6175(line=393,offs=35)))
                    ## I1VALDCL
                    pyxtnm632 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6150(line=393,offs=10)--6163(line=393,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test1(1352)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2693(line=154,offs=1)--2706(line=154,offs=14))));$list(T2JAG($list(T2Pvar(x0[7404])))))
                    ## T1IMPallx(iforall$test1(1352), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
                    ## T1IMPallx(iforall$test1(1352)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm630(arg1, arg2): ## timp: iforall$test1(1352)
                      pyxtnm595 = arg1
                      pyxtnm596 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm629 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10016(line=686,offs=1)--10050(line=687,offs=26)))
                      ## I1VALDCL
                      pyxtnm628 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10025(line=687,offs=1)--10038(line=687,offs=14))
                      ## I0Etapq(I0Ecst(iforitm$work1(1366)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[7436])))))
                      ## T1IMPallx(iforitm$work1(1366), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
                      ## T1IMPallx(iforitm$work1(1366)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm626(arg1, arg2): ## timp: iforitm$work1(1366)
                        pyxtnm597 = arg1
                        pyxtnm598 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm625 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4645(line=299,offs=1)--4701(line=301,offs=33)))
                        ## I1VALDCL
                        pyxtnm616 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4660(line=300,offs=7)--4661(line=300,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(864)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(864), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(864)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(864);$list()))))
                        def pyxtnm605(arg1, arg2): ## timp: sint_gt$sint(864)
                          pyxtnm599 = arg1
                          pyxtnm600 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm604 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2440));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4632);$list(FJARGdarg($list(I1BNDcons(I1TNM(601);I0Pvar(i1(4633));$list(@(i1(4633),I1Vtnm(I1TNM(601))))),I1BNDcons(I1TNM(602);I0Pvar(i2(4634));$list(@(i2(4634),I1Vtnm(I1TNM(602))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm603 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm599, pyxtnm600))
                          pyxtnm604 = pyxtnm603
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm604
                          return pyxtnm604
                        ## endtimp(sint_gt$sint(864))
                        pyxtnm606 = XATSDAPP(pyxtnm605(pyxtnm597, XATSINT1(0)))
                        pyxtnm615 = None
                        if (pyxtnm606):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4669(line=301,offs=1)--4679(line=301,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
                          def pyxtnm611(arg1): ## timp: strn_print(974)
                            pyxtnm607 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm610 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(608);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(608))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm609 = XATSDAPP(XATS2PY_strn_print(pyxtnm607))
                            pyxtnm610 = pyxtnm609
                            ## end-of(let)
                            ## I1CMP:return:pyxtnm610
                            return pyxtnm610
                          ## endtimp(strn_print(974))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4682(line=301,offs=14)--4690(line=301,offs=22))
                          ## I0Etapq(I0Ecst(gseq_sep(321)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2454(line=137,offs=1)--2462(line=137,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
                          ## T1IMPallx(gseq_sep(321), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                          ## T1IMPallx(gseq_sep(321)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_sep(321);$list(@(xs[953],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7869])))),@(x0[954],T2Pvar(x0[7869])))))))
                          def pyxtnm612(): ## timp: gseq_sep(321)
                            ## I1CMP:start
                            ## I1CMP:return:XATSSTRN(",")
                            return XATSSTRN(",")
                          ## endtimp(gseq_sep(321))
                          pyxtnm613 = XATSDAPP(pyxtnm612())
                          pyxtnm614 = XATSDAPP(pyxtnm611(pyxtnm613))
                          pyxtnm615 = pyxtnm614
                        ## else: None
                        ## end-of(if)
                        pyxtnm616 = pyxtnm615
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4619(line=297,offs=3)--4627(line=297,offs=11))
                        ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7299])))))
                        ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                        ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
                        pyxtnm623 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                        ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
                        ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                        ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(si)))))))
                        pyxtnm622 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                        ## I0Etapq(I0Ecst(sint_print(858)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_print(858), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                        ## T1IMPallx(sint_print(858)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(858);$list()))))
                        def pyxtnm621(arg1): ## timp: sint_print(858)
                          pyxtnm617 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm620 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2450));$list(I1FUNDCL(XATS2PY_sint_print(4681);$list(FJARGdarg($list(I1BNDcons(I1TNM(618);I0Pvar(i0(4682));$list(@(i0(4682),I1Vtnm(I1TNM(618))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                          pyxtnm619 = XATSDAPP(XATS2PY_sint_print(pyxtnm617))
                          pyxtnm620 = pyxtnm619
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm620
                          return pyxtnm620
                        ## endtimp(sint_print(858))
                        pyxtnm622 = pyxtnm621
                        pyxtnm623 = pyxtnm622
                        pyxtnm624 = XATSDAPP(pyxtnm623(pyxtnm598))
                        pyxtnm625 = pyxtnm624
                        ## end-of(let)
                        ## I1CMP:return:pyxtnm625
                        return pyxtnm625
                      ## endtimp(iforitm$work1(1366))
                      pyxtnm627 = XATSDAPP(pyxtnm626(pyxtnm595, pyxtnm596))
                      pyxtnm628 = pyxtnm627
                      XATS000_patck(True)
                      pyxtnm629 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm629
                      return pyxtnm629
                    ## endtimp(iforall$test1(1352))
                    pyxtnm631 = XATSDAPP(pyxtnm630(pyxtnm594, pyxtnm589))
                    pyxtnm632 = pyxtnm631
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6075(line=389,offs=5)--6083(line=389,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2152)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2152), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2152)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5487],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2152);$list(@(a[5303],T2Pvar(a[5487])))))))
                    def pyxtnm635(arg1, arg2): ## timp: p2tr_set(2152)
                      pyxtnm633 = arg1
                      pyxtnm634 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm633, pyxtnm634)
                      ## I1CMP:return:[]
                      return []
                    ## endtimp(p2tr_set(2152))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6094(line=389,offs=24)--6095(line=389,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(870)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2816(line=127,offs=1)--2829(line=127,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(870), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(870)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(870);$list()))))
                    def pyxtnm642(arg1, arg2): ## timp: sint_add$sint(870)
                      pyxtnm636 = arg1
                      pyxtnm637 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm641 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2445));$list(I1FUNDCL(XATS2PY_sint_add$sint(4657);$list(FJARGdarg($list(I1BNDcons(I1TNM(638);I0Pvar(i1(4658));$list(@(i1(4658),I1Vtnm(I1TNM(638))))),I1BNDcons(I1TNM(639);I0Pvar(i2(4659));$list(@(i2(4659),I1Vtnm(I1TNM(639))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm640 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm636, pyxtnm637))
                      pyxtnm641 = pyxtnm640
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm641
                      return pyxtnm641
                    ## endtimp(sint_add$sint(870))
                    pyxtnm643 = XATSDAPP(pyxtnm642(pyxtnm594, XATSINT1(1)))
                    pyxtnm644 = XATSDAPP(pyxtnm635(pyxtnm576, pyxtnm643))
                    pyxtnm645 = pyxtnm632
                    ## end-of(let)
                    ## I1CMP:return:pyxtnm645
                    return pyxtnm645
                  ## endtimp(forall$test1(1340))
                  pyxtnm647 = XATSDAPP(pyxtnm646(XATSP1CN("list_vt_cons", pyxtnm588[0+1])))
                  pyxtnm648 = pyxtnm647
                  XATS000_patck(True)
                  pyxtnm650 = None
                  if (pyxtnm648):
                    pyxtnm649 = XATSDAPP(loop_1774(XATSP1CN("list_vt_cons", pyxtnm588[1+1])))
                    pyxtnm650 = pyxtnm649
                  else:
                    pyxtnm650 = XATSBOOL(False)
                  ## end-of(if)
                  pyxtnm651 = pyxtnm650
                  ## end-of(let)
                  pyxtnm652 = pyxtnm651
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:pyxtnm652
              return pyxtnm652
            pyxtnm653 = XATSDAPP(loop_1774(pyxtnm585))
            pyxtnm654 = pyxtnm653
            ## end-of(let)
            ## I1CMP:return:pyxtnm654
            return pyxtnm654
          ## endtimp(list_vt_forall1(1908))
          pyxtnm656 = pyxtnm655
          pyxtnm657 = XATSDAPP(pyxtnm656(pyxtnm574))
          pyxtnm658 = pyxtnm657
          ## end-of(let)
          pyxtnm659 = pyxtnm658
          XATS000_patck(True)
          pyxtnm660 = pyxtnm659
          ## end-of(let)
          ## I1CMP:return:pyxtnm660
          return pyxtnm660
        ## endtimp(gseq_iforall1(1611))
        pyxtnm662 = XATSDAPP(pyxtnm661(pyxtnm568))
        pyxtnm663 = pyxtnm662
        XATS000_patck(True)
        pyxtnm664 = []
        ## end-of(let)
        pyxtnm665 = pyxtnm664
        ## end-of(let)
        ## I1CMP:return:pyxtnm665
        return pyxtnm665
      ## endtimp(gseq_iforitm1(1635))
      pyxtnm667 = XATSDAPP(pyxtnm666(pyxtnm549))
      pyxtnm668 = pyxtnm667
      ## end-of(let)
      pyxtnm669 = pyxtnm668
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=304,offs=1)--4747(line=305,offs=33)))
      ## I1VALDCL
      pyxtnm678 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=305,offs=1)--4725(line=305,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm674(arg1): ## timp: strn_print(974)
        pyxtnm670 = arg1
        ## I1CMP:start
        ## let
        pyxtnm673 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(671);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(671))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm672 = XATSDAPP(XATS2PY_strn_print(pyxtnm670))
        pyxtnm673 = pyxtnm672
        ## end-of(let)
        ## I1CMP:return:pyxtnm673
        return pyxtnm673
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=305,offs=14)--4736(line=305,offs=22))
      ## I0Etapq(I0Ecst(gseq_end(320)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2412(line=133,offs=1)--2420(line=133,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_end(320), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq_end(320)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_end(320);$list(@(xs[951],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7870])))),@(x0[952],T2Pvar(x0[7870])))))))
      def pyxtnm675(): ## timp: gseq_end(320)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN(")")
        return XATSSTRN(")")
      ## endtimp(gseq_end(320))
      pyxtnm676 = XATSDAPP(pyxtnm675())
      pyxtnm677 = XATSDAPP(pyxtnm674(pyxtnm676))
      pyxtnm678 = pyxtnm677
      XATS000_patck(True)
      pyxtnm679 = []
      ## end-of(let)
      ## I1CMP:return:pyxtnm679
      return pyxtnm679
    ## endtimp(gseq_print1(1561))
    pyxtnm681 = XATSDAPP(pyxtnm680(pyxtnm548))
    ## I1CMP:return:pyxtnm681
    return pyxtnm681
  ## endtimp(g_print1(1329))
  pyxtnm683 = XATSDAPP(pyxtnm682(pyxtnm535))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5636(line=282,offs=21)--5644(line=282,offs=29))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[7770])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm690 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2611(line=136,offs=1)--2648(line=137,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(char)))))))
  pyxtnm689 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2636(line=137,offs=17)--2646(line=137,offs=27))
  ## I0Etapq(I0Ecst(char_print(826)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/char000.sats)@(2501(line=119,offs=1)--2511(line=119,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(char_print(826), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2887(line=170,offs=1)--3027(line=181,offs=2)))
  ## T1IMPallx(char_print(826)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(char_print(826);$list()))))
  def pyxtnm688(arg1): ## timp: char_print(826)
    pyxtnm684 = arg1
    ## I1CMP:start
    ## let
    pyxtnm687 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2967(line=178,offs=1)--3025(line=180,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_char_print(2437));$list(I1FUNDCL(XATS2PY_char_print(4620);$list(FJARGdarg($list(I1BNDcons(I1TNM(685);I0Pvar(c0(4621));$list(@(c0(4621),I1Vtnm(I1TNM(685))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_char_print);G1Nlist($list())))))))
    pyxtnm686 = XATSDAPP(XATS2PY_char_print(pyxtnm684))
    pyxtnm687 = pyxtnm686
    ## end-of(let)
    ## I1CMP:return:pyxtnm687
    return pyxtnm687
  ## endtimp(char_print(826))
  pyxtnm689 = pyxtnm688
  pyxtnm690 = pyxtnm689
  pyxtnm691 = XATSDAPP(pyxtnm690(pyxtnm536))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5656(line=283,offs=3)--5669(line=283,offs=16))
  ## I0Etapq(I0Ecst(gs_print$end1(1842)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end1(1842), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
  ## T1IMPallx(gs_print$end1(1842)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end1(1842);$list()))))
  def pyxtnm693(): ## timp: gs_print$end1(1842)
    ## I1CMP:start
    pyxtnm692 = XATSTUP0([])
    ## I1CMP:return:pyxtnm692
    return pyxtnm692
  ## endtimp(gs_print$end1(1842))
  pyxtnm694 = XATSDAPP(pyxtnm693())
  ## I1CMP:return:pyxtnm694
  return pyxtnm694
## endtimp(gs_print1_a3(1857))
pyxtnm696 = XATSDAPP(pyxtnm695(XATSSTRN("nint_base$digitize(1024, 2) = "), pyxtnm533, XATSCHR2('\n')))
pyxtnm697 = pyxtnm696
## end-of(let)
pyxtnm698 = pyxtnm697
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(798(line=48,offs=1)--910(line=53,offs=48)))
## I1VALDCL
pyxtnm919 = None
## let
pyxtnm918 = None
## I1Dvaldclist(LCSRCsome1(test01_pre2026.dats)@(811(line=50,offs=1)--848(line=51,offs=29)))
## I1VALDCL
pyxtnm754 = None
## LCSRCsome1(test01_pre2026.dats)@(820(line=51,offs=1)--838(line=51,offs=19))
## I0Etapq(I0Ecst(nint_base$digitize(2129)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2000(line=82,offs=1)--2018(line=82,offs=19))));$list(T2JAG($list())))
## T1IMPallx(nint_base$digitize(2129), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2567(line=117,offs=1)--2672(line=123,offs=31)))
## T1IMPallx(nint_base$digitize(2129)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$digitize(2129);$list()))))
def pyxtnm752(arg1, arg2): ## timp: nint_base$digitize(2129)
  pyxtnm699 = arg1
  pyxtnm700 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2618(line=121,offs=1)--2635(line=121,offs=18))
  ## I0Etapq(I0Ecst(strm_vt_rlistize0(2074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm001_vt.sats)@(8509(line=433,offs=1)--8526(line=433,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  ## T1IMPallx(strm_vt_rlistize0(2074), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7032(line=445,offs=1)--7325(line=468,offs=2)))
  ## T1IMPallx(strm_vt_rlistize0(2074)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8065],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_rlistize0(2074);$list(@(x0[5158],T2Pvar(x0[8065])))))))
  def pyxtnm714(arg1): ## timp: strm_vt_rlistize0(2074)
    pyxtnm701 = arg1
    ## I1CMP:start
    ## let
    pyxtnm713 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7109(line=453,offs=1)--7131(line=453,offs=23)))
    ## I1VALDCL
    pyxtnm703 = None
    pyxtnm702 = XATSCAPP("list_vt_nil", [0])
    pyxtnm703 = pyxtnm702
    XATS000_patck(True)
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(7135(line=455,offs=1)--7323(line=467,offs=35)))
    ## I1FUNDCL
    def loop_7138(arg1, arg2): ## fun
      pyxtnm704 = arg1
      pyxtnm705 = arg2
      ## I1CMP:start
      pyxtnm706 = XATS000_dl1az(pyxtnm704)
      pyxtnm711 = None
      while True: ## do {
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(707);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
        if (XATS000_ctgeq(pyxtnm706, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
          pyxtnm707 = pyxtnm706
          pyxtnm711 = pyxtnm705
          break ## cls
        ## } // gpt
        ## } // cls
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(708);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(4259)),I0Pvar(xs(4260)))));$list(@(x1(4259),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(708));0)),@(xs(4260),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(708));1)))))
        if (XATS000_ctgeq(pyxtnm706, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
          pyxtnm708 = pyxtnm706
          pyxtnm709 = XATSCAPP("list_vt_cons", [1, XATSP1CN("strmcon_vt_cons", pyxtnm708[0+1]), pyxtnm705])
          pyxtnm710 = XATSDAPP(loop_7138(XATSP1CN("strmcon_vt_cons", pyxtnm708[1+1]), pyxtnm709))
          pyxtnm711 = pyxtnm710
          break ## cls
        ## } // gpt
        ## } // cls
        XATS000_cfail()
      ## } while True // end-of(do-cls)
      ## I1CMP:return:pyxtnm711
      return pyxtnm711
    pyxtnm712 = XATSDAPP(loop_7138(pyxtnm701, pyxtnm703))
    pyxtnm713 = pyxtnm712
    ## end-of(let)
    ## I1CMP:return:pyxtnm713
    return pyxtnm713
  ## endtimp(strm_vt_rlistize0(2074))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2642(line=123,offs=1)--2661(line=123,offs=20))
  ## I0Etapq(I0Ecst(nint_base$rdigitize(2130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/SATS/pre2026.sats)@(2067(line=85,offs=1)--2086(line=85,offs=20))));$list(T2JAG($list())))
  ## T1IMPallx(nint_base$rdigitize(2130), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2676(line=125,offs=1)--2903(line=144,offs=2)))
  ## T1IMPallx(nint_base$rdigitize(2130)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_base$rdigitize(2130);$list()))))
  def pyxtnm749(arg1, arg2): ## timp: nint_base$rdigitize(2130)
    pyxtnm715 = arg1
    pyxtnm716 = arg2
    ## I1CMP:start
    ## let
    pyxtnm748 = None
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2756(line=133,offs=1)--2898(line=142,offs=43)))
    ## I1FUNDCL
    def auxmain_2759(arg1): ## fun
      pyxtnm717 = arg1
      ## I1CMP:start
      def pyxtnm746(tlaz): ## { // l1azy
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2818(line=139,offs=5)--2820(line=139,offs=7))
        ## I0Etapq(I0Ecst(sint_lte$sint(866)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2344(line=100,offs=1)--2357(line=100,offs=14))));$list(T2JAG($list())))
        ## T1IMPallx(sint_lte$sint(866), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2130(line=100,offs=1)--2294(line=112,offs=2)))
        ## T1IMPallx(sint_lte$sint(866)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_lte$sint(866);$list()))))
        def pyxtnm724(arg1, arg2): ## timp: sint_lte$sint(866)
          pyxtnm718 = arg1
          pyxtnm719 = arg2
          ## I1CMP:start
          ## let
          pyxtnm723 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2220(line=108,offs=1)--2292(line=111,offs=39)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_lte$sint(2442));$list(I1FUNDCL(XATS2PY_sint_lte$sint(4642);$list(FJARGdarg($list(I1BNDcons(I1TNM(720);I0Pvar(i1(4643));$list(@(i1(4643),I1Vtnm(I1TNM(720))))),I1BNDcons(I1TNM(721);I0Pvar(i2(4644));$list(@(i2(4644),I1Vtnm(I1TNM(721))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_lte$sint);G1Nlist($list())))))))
          pyxtnm722 = XATSDAPP(XATS2PY_sint_lte_sint(pyxtnm718, pyxtnm719))
          pyxtnm723 = pyxtnm722
          ## end-of(let)
          ## I1CMP:return:pyxtnm723
          return pyxtnm723
        ## endtimp(sint_lte$sint(866))
        pyxtnm725 = XATSDAPP(pyxtnm724(pyxtnm717, XATSINT1(0)))
        pyxtnm745 = None
        if (pyxtnm725):
          pyxtnm726 = XATSCAPP("strmcon_vt_nil", [0])
          pyxtnm745 = pyxtnm726
        else:
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2876(line=142,offs=21)--2877(line=142,offs=22))
          ## I0Etapq(I0Ecst(sint_mod$sint(874)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3076(line=143,offs=1)--3089(line=143,offs=14))));$list(T2JAG($list())))
          ## T1IMPallx(sint_mod$sint(874), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3349(line=201,offs=1)--3513(line=213,offs=2)))
          ## T1IMPallx(sint_mod$sint(874)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mod$sint(874);$list()))))
          def pyxtnm733(arg1, arg2): ## timp: sint_mod$sint(874)
            pyxtnm727 = arg1
            pyxtnm728 = arg2
            ## I1CMP:start
            ## let
            pyxtnm732 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3439(line=209,offs=1)--3511(line=212,offs=39)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mod$sint(2449));$list(I1FUNDCL(XATS2PY_sint_mod$sint(4677);$list(FJARGdarg($list(I1BNDcons(I1TNM(729);I0Pvar(i1(4678));$list(@(i1(4678),I1Vtnm(I1TNM(729))))),I1BNDcons(I1TNM(730);I0Pvar(i2(4679));$list(@(i2(4679),I1Vtnm(I1TNM(730))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mod$sint);G1Nlist($list())))))))
            pyxtnm731 = XATSDAPP(XATS2PY_sint_mod_sint(pyxtnm727, pyxtnm728))
            pyxtnm732 = pyxtnm731
            ## end-of(let)
            ## I1CMP:return:pyxtnm732
            return pyxtnm732
          ## endtimp(sint_mod$sint(874))
          pyxtnm734 = XATSDAPP(pyxtnm733(pyxtnm717, pyxtnm716))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/almanac/DATS/pre2026.dats)@(2891(line=142,offs=36)--2892(line=142,offs=37))
          ## I0Etapq(I0Ecst(sint_div$sint(873)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3011(line=139,offs=1)--3024(line=139,offs=14))));$list(T2JAG($list())))
          ## T1IMPallx(sint_div$sint(873), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3181(line=187,offs=1)--3345(line=199,offs=2)))
          ## T1IMPallx(sint_div$sint(873)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_div$sint(873);$list()))))
          def pyxtnm741(arg1, arg2): ## timp: sint_div$sint(873)
            pyxtnm735 = arg1
            pyxtnm736 = arg2
            ## I1CMP:start
            ## let
            pyxtnm740 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3271(line=195,offs=1)--3343(line=198,offs=39)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_div$sint(2448));$list(I1FUNDCL(XATS2PY_sint_div$sint(4672);$list(FJARGdarg($list(I1BNDcons(I1TNM(737);I0Pvar(i1(4673));$list(@(i1(4673),I1Vtnm(I1TNM(737))))),I1BNDcons(I1TNM(738);I0Pvar(i2(4674));$list(@(i2(4674),I1Vtnm(I1TNM(738))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_div$sint);G1Nlist($list())))))))
            pyxtnm739 = XATSDAPP(XATS2PY_sint_div_sint(pyxtnm735, pyxtnm736))
            pyxtnm740 = pyxtnm739
            ## end-of(let)
            ## I1CMP:return:pyxtnm740
            return pyxtnm740
          ## endtimp(sint_div$sint(873))
          pyxtnm742 = XATSDAPP(pyxtnm741(pyxtnm717, pyxtnm716))
          pyxtnm743 = XATSDAPP(auxmain_2759(pyxtnm742))
          pyxtnm744 = XATSCAPP("strmcon_vt_cons", [1, pyxtnm734, pyxtnm743])
          pyxtnm745 = pyxtnm744
        ## end-of(if)
        ## I1CMP:return:pyxtnm745
        return pyxtnm745
      ## } // end(l1azy)
      ## I1CMP:return:pyxtnm746
      return pyxtnm746
    pyxtnm747 = XATSDAPP(auxmain_2759(pyxtnm715))
    pyxtnm748 = pyxtnm747
    ## end-of(let)
    ## I1CMP:return:pyxtnm748
    return pyxtnm748
  ## endtimp(nint_base$rdigitize(2130))
  pyxtnm750 = XATSDAPP(pyxtnm749(pyxtnm699, pyxtnm700))
  pyxtnm751 = XATSDAPP(pyxtnm714(pyxtnm750))
  ## I1CMP:return:pyxtnm751
  return pyxtnm751
## endtimp(nint_base$digitize(2129))
pyxtnm753 = XATSDAPP(pyxtnm752(XATSINT1(59049), XATSINT1(3)))
pyxtnm754 = pyxtnm753
XATS000_patck(True)
## LCSRCsome1(test01_pre2026.dats)@(852(line=52,offs=1)--859(line=52,offs=8))
## I0Etapq(I0Ecst(gs_print1_a3(1857)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3614(line=218,offs=1)--3626(line=218,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
## T1IMPallx(gs_print1_a3(1857), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5507(line=274,offs=1)--5674(line=283,offs=21)))
## T1IMPallx(gs_print1_a3(1857)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7768],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7769],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7770],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a3(1857);$list(@(x0[4737],T2Pvar(x0[7768])),@(x1[4738],T2Pvar(x1[7769])),@(x2[4739],T2Pvar(x2[7770])))))))
def pyxtnm916(arg1, arg2, arg3): ## timp: gs_print1_a3(1857)
  pyxtnm755 = arg1
  pyxtnm756 = arg2
  pyxtnm757 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5578(line=280,offs=3)--5591(line=280,offs=16))
  ## I0Etapq(I0Ecst(gs_print$beg1(1841)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg1(1841), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
  ## T1IMPallx(gs_print$beg1(1841)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg1(1841);$list()))))
  def pyxtnm759(): ## timp: gs_print$beg1(1841)
    ## I1CMP:start
    pyxtnm758 = XATSTUP0([])
    ## I1CMP:return:pyxtnm758
    return pyxtnm758
  ## endtimp(gs_print$beg1(1841))
  pyxtnm760 = XATSDAPP(pyxtnm759())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5599(line=281,offs=3)--5607(line=281,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7768])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm767 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(strn)))))))
  pyxtnm766 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
  def pyxtnm765(arg1): ## timp: strn_print(974)
    pyxtnm761 = arg1
    ## I1CMP:start
    ## let
    pyxtnm764 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(762);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(762))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm763 = XATSDAPP(XATS2PY_strn_print(pyxtnm761))
    pyxtnm764 = pyxtnm763
    ## end-of(let)
    ## I1CMP:return:pyxtnm764
    return pyxtnm764
  ## endtimp(strn_print(974))
  pyxtnm766 = pyxtnm765
  pyxtnm767 = pyxtnm766
  pyxtnm768 = XATSDAPP(pyxtnm767(pyxtnm755))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5618(line=282,offs=3)--5626(line=282,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[7769])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2935(line=156,offs=1)--3019(line=162,offs=2)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7873],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7873])))))))))
  def pyxtnm903(arg1): ## timp: g_print1(1329)
    pyxtnm769 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2985(line=161,offs=1)--2996(line=161,offs=12))
    ## I0Etapq(I0Ecst(gseq_print1(1561)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3970(line=243,offs=1)--3981(line=243,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[7873]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7873])))))
    ## T1IMPallx(gseq_print1(1561), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4437(line=281,offs=1)--4754(line=306,offs=7)))
    ## T1IMPallx(gseq_print1(1561)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1561);$list(@(xs[3852],T2Pvar(xs[7298])),@(x0[3853],T2Pvar(x0[7299])))))))
    def pyxtnm901(arg1): ## timp: gseq_print1(1561)
      pyxtnm770 = arg1
      ## I1CMP:start
      ## let
      pyxtnm900 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4488(line=286,offs=1)--4530(line=288,offs=21)))
      ## I1VALDCL
      pyxtnm779 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4497(line=287,offs=1)--4507(line=287,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm775(arg1): ## timp: strn_print(974)
        pyxtnm771 = arg1
        ## I1CMP:start
        ## let
        pyxtnm774 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(772);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(772))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm773 = XATSDAPP(XATS2PY_strn_print(pyxtnm771))
        pyxtnm774 = pyxtnm773
        ## end-of(let)
        ## I1CMP:return:pyxtnm774
        return pyxtnm774
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4511(line=288,offs=2)--4519(line=288,offs=10))
      ## I0Etapq(I0Ecst(gseq_beg(319)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2370(line=129,offs=1)--2378(line=129,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_beg(319), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq_beg(319)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7871],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_beg(319);$list(@(xs[949],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7871])))),@(x0[950],T2Pvar(x0[7871])))))))
      def pyxtnm776(): ## timp: gseq_beg(319)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN("list_vt(")
        return XATSSTRN("list_vt(")
      ## endtimp(gseq_beg(319))
      pyxtnm777 = XATSDAPP(pyxtnm776())
      pyxtnm778 = XATSDAPP(pyxtnm775(pyxtnm777))
      pyxtnm779 = pyxtnm778
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4531(line=289,offs=1)--4705(line=303,offs=2)))
      ## I1VALDCL
      pyxtnm890 = None
      ## let
      pyxtnm889 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Pvar(x0[7299]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4542(line=291,offs=1)--4555(line=291,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1635)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10879(line=588,offs=1)--10892(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_iforitm1(1635), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9859(line=671,offs=1)--10064(line=688,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1635)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1635);$list(@(xs[4038],T2Pvar(xs[7435])),@(x0[4039],T2Pvar(x0[7436])))))))
      def pyxtnm887(arg1): ## timp: gseq_iforitm1(1635)
        pyxtnm789 = arg1
        ## I1CMP:start
        ## let
        pyxtnm886 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Pvar(x0[7436]))))):timp
        ## let
        pyxtnm885 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9919(line=678,offs=1)--9955(line=680,offs=15)))
        ## I1VALDCL
        pyxtnm884 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9927(line=679,offs=1)--9940(line=679,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1611)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6521(line=346,offs=1)--6534(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[7435]))),T2JAG($list(T2Pvar(x0[7436])))))
        ## T1IMPallx(gseq_iforall1(1611), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5881(line=370,offs=1)--6184(line=396,offs=2)))
        ## T1IMPallx(gseq_iforall1(1611)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1611);$list(@(xs[3990],T2Pvar(xs[7403])),@(x0[3991],T2Pvar(x0[7404])))))))
        def pyxtnm882(arg1): ## timp: gseq_iforall1(1611)
          pyxtnm795 = arg1
          ## I1CMP:start
          ## let
          pyxtnm881 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5949(line=377,offs=1)--5965(line=377,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:XATSINT1(0)
          pyxtnm796 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5969(line=379,offs=1)--5987(line=379,offs=19)))
          ## I1VALDCL
          pyxtnm797 = None
          pyxtnm797 = XATSADDR(pyxtnm796)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5991(line=381,offs=1)--6179(line=394,offs=2)))
          ## I1VALDCL
          pyxtnm880 = None
          ## let
          pyxtnm879 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Pvar(x0[7404]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6002(line=383,offs=1)--6014(line=383,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1595)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[7403]))),T2JAG($list(T2Pvar(x0[7404])))))
          ## T1IMPallx(gseq_forall1(1595), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2042(line=92,offs=1)--2113(line=95,offs=40)))
          ## T1IMPallx(gseq_forall1(1595)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7912],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1595);$list(@(xs[3958],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7912])))),@(x0[3959],T2Pvar(x0[7912])))))))
          pyxtnm877 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2094(line=95,offs=21)--2109(line=95,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall1(1908)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1481(line=47,offs=1)--1496(line=47,offs=16))));$list(T2JAG($list(T2Pvar(x0[7912])))))
          ## T1IMPallx(list_vt_forall1(1908), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1701(line=65,offs=1)--1958(line=86,offs=2)))
          ## T1IMPallx(list_vt_forall1(1908)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7910],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall1(1908);$list(@(x0[4880],T2Pvar(x0[7910])))))))
          def pyxtnm876(arg1): ## timp: list_vt_forall1(1908)
            pyxtnm806 = arg1
            ## I1CMP:start
            ## let
            pyxtnm875 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1771(line=72,offs=1)--1956(line=85,offs=38)))
            ## I1FUNDCL
            def loop_1774(arg1): ## fun
              pyxtnm807 = arg1
              ## I1CMP:start
              pyxtnm873 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(808);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
                if (XATS000_ctgeq(pyxtnm807, XATSCTAG("list_vt_nil",0))): ## { // gpt
                  pyxtnm808 = pyxtnm807
                  pyxtnm873 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(809);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(4054)),I0Pvar(xs(4055))));$list(@(x1(4054),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(809));0)),@(xs(4055),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(809));1)))))
                if (XATS000_ctgeq(pyxtnm807, XATSCTAG("list_vt_cons",1))): ## { // gpt
                  pyxtnm809 = pyxtnm807
                  ## let
                  pyxtnm872 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1884(line=83,offs=1)--1915(line=84,offs=21)))
                  ## I1VALDCL
                  pyxtnm869 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1895(line=84,offs=1)--1907(line=84,offs=13))
                  ## I0Etapq(I0Ecst(forall$test1(1340)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[7910])))))
                  ## T1IMPallx(forall$test1(1340), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6037(line=386,offs=1)--6177(line=393,offs=37)))
                  ## T1IMPallx(forall$test1(1340)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7403],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7404],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1340);$list(@(x0[3477],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm867(arg1): ## timp: forall$test1(1340)
                    pyxtnm810 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm866 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6111(line=392,offs=1)--6140(line=392,offs=30)))
                    ## I1VALDCL
                    pyxtnm815 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6124(line=392,offs=14)--6132(line=392,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2151)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2151), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2151)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5486],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2151);$list(@(a[5302],T2Pvar(a[5486])))))))
                    def pyxtnm813(arg1): ## timp: p2tr_get(2151)
                      pyxtnm811 = arg1
                      ## I1CMP:start
                      pyxtnm812 = XATS000_dp2tr(pyxtnm811)
                      ## I1CMP:return:pyxtnm812
                      return pyxtnm812
                    ## endtimp(p2tr_get(2151))
                    pyxtnm814 = XATSDAPP(pyxtnm813(pyxtnm797))
                    pyxtnm815 = pyxtnm814
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6141(line=393,offs=1)--6175(line=393,offs=35)))
                    ## I1VALDCL
                    pyxtnm853 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6150(line=393,offs=10)--6163(line=393,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test1(1352)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2693(line=154,offs=1)--2706(line=154,offs=14))));$list(T2JAG($list(T2Pvar(x0[7404])))))
                    ## T1IMPallx(iforall$test1(1352), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9975(line=683,offs=1)--10062(line=687,offs=38)))
                    ## T1IMPallx(iforall$test1(1352)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7435],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7436],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1352);$list(@(x0[3489],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm851(arg1, arg2): ## timp: iforall$test1(1352)
                      pyxtnm816 = arg1
                      pyxtnm817 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm850 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10016(line=686,offs=1)--10050(line=687,offs=26)))
                      ## I1VALDCL
                      pyxtnm849 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10025(line=687,offs=1)--10038(line=687,offs=14))
                      ## I0Etapq(I0Ecst(iforitm$work1(1366)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[7436])))))
                      ## T1IMPallx(iforitm$work1(1366), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4578(line=294,offs=1)--4703(line=302,offs=2)))
                      ## T1IMPallx(iforitm$work1(1366)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7298],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7299],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1366);$list(@(x0[3503],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm847(arg1, arg2): ## timp: iforitm$work1(1366)
                        pyxtnm818 = arg1
                        pyxtnm819 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm846 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4645(line=299,offs=1)--4701(line=301,offs=33)))
                        ## I1VALDCL
                        pyxtnm837 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4660(line=300,offs=7)--4661(line=300,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(864)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(864), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(864)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(864);$list()))))
                        def pyxtnm826(arg1, arg2): ## timp: sint_gt$sint(864)
                          pyxtnm820 = arg1
                          pyxtnm821 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm825 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2440));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4632);$list(FJARGdarg($list(I1BNDcons(I1TNM(822);I0Pvar(i1(4633));$list(@(i1(4633),I1Vtnm(I1TNM(822))))),I1BNDcons(I1TNM(823);I0Pvar(i2(4634));$list(@(i2(4634),I1Vtnm(I1TNM(823))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm824 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm820, pyxtnm821))
                          pyxtnm825 = pyxtnm824
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm825
                          return pyxtnm825
                        ## endtimp(sint_gt$sint(864))
                        pyxtnm827 = XATSDAPP(pyxtnm826(pyxtnm818, XATSINT1(0)))
                        pyxtnm836 = None
                        if (pyxtnm827):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4669(line=301,offs=1)--4679(line=301,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
                          def pyxtnm832(arg1): ## timp: strn_print(974)
                            pyxtnm828 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm831 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(829);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(829))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm830 = XATSDAPP(XATS2PY_strn_print(pyxtnm828))
                            pyxtnm831 = pyxtnm830
                            ## end-of(let)
                            ## I1CMP:return:pyxtnm831
                            return pyxtnm831
                          ## endtimp(strn_print(974))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4682(line=301,offs=14)--4690(line=301,offs=22))
                          ## I0Etapq(I0Ecst(gseq_sep(321)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2454(line=137,offs=1)--2462(line=137,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
                          ## T1IMPallx(gseq_sep(321), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                          ## T1IMPallx(gseq_sep(321)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_sep(321);$list(@(xs[953],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7869])))),@(x0[954],T2Pvar(x0[7869])))))))
                          def pyxtnm833(): ## timp: gseq_sep(321)
                            ## I1CMP:start
                            ## I1CMP:return:XATSSTRN(",")
                            return XATSSTRN(",")
                          ## endtimp(gseq_sep(321))
                          pyxtnm834 = XATSDAPP(pyxtnm833())
                          pyxtnm835 = XATSDAPP(pyxtnm832(pyxtnm834))
                          pyxtnm836 = pyxtnm835
                        ## else: None
                        ## end-of(if)
                        pyxtnm837 = pyxtnm836
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4619(line=297,offs=3)--4627(line=297,offs=11))
                        ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7299])))))
                        ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                        ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
                        pyxtnm844 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                        ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
                        ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                        ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(si)))))))
                        pyxtnm843 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                        ## I0Etapq(I0Ecst(sint_print(858)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_print(858), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                        ## T1IMPallx(sint_print(858)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(858);$list()))))
                        def pyxtnm842(arg1): ## timp: sint_print(858)
                          pyxtnm838 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm841 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2450));$list(I1FUNDCL(XATS2PY_sint_print(4681);$list(FJARGdarg($list(I1BNDcons(I1TNM(839);I0Pvar(i0(4682));$list(@(i0(4682),I1Vtnm(I1TNM(839))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                          pyxtnm840 = XATSDAPP(XATS2PY_sint_print(pyxtnm838))
                          pyxtnm841 = pyxtnm840
                          ## end-of(let)
                          ## I1CMP:return:pyxtnm841
                          return pyxtnm841
                        ## endtimp(sint_print(858))
                        pyxtnm843 = pyxtnm842
                        pyxtnm844 = pyxtnm843
                        pyxtnm845 = XATSDAPP(pyxtnm844(pyxtnm819))
                        pyxtnm846 = pyxtnm845
                        ## end-of(let)
                        ## I1CMP:return:pyxtnm846
                        return pyxtnm846
                      ## endtimp(iforitm$work1(1366))
                      pyxtnm848 = XATSDAPP(pyxtnm847(pyxtnm816, pyxtnm817))
                      pyxtnm849 = pyxtnm848
                      XATS000_patck(True)
                      pyxtnm850 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm850
                      return pyxtnm850
                    ## endtimp(iforall$test1(1352))
                    pyxtnm852 = XATSDAPP(pyxtnm851(pyxtnm815, pyxtnm810))
                    pyxtnm853 = pyxtnm852
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6075(line=389,offs=5)--6083(line=389,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2152)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2152), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2152)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5487],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2152);$list(@(a[5303],T2Pvar(a[5487])))))))
                    def pyxtnm856(arg1, arg2): ## timp: p2tr_set(2152)
                      pyxtnm854 = arg1
                      pyxtnm855 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm854, pyxtnm855)
                      ## I1CMP:return:[]
                      return []
                    ## endtimp(p2tr_set(2152))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6094(line=389,offs=24)--6095(line=389,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(870)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2816(line=127,offs=1)--2829(line=127,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(870), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(870)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(870);$list()))))
                    def pyxtnm863(arg1, arg2): ## timp: sint_add$sint(870)
                      pyxtnm857 = arg1
                      pyxtnm858 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm862 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2445));$list(I1FUNDCL(XATS2PY_sint_add$sint(4657);$list(FJARGdarg($list(I1BNDcons(I1TNM(859);I0Pvar(i1(4658));$list(@(i1(4658),I1Vtnm(I1TNM(859))))),I1BNDcons(I1TNM(860);I0Pvar(i2(4659));$list(@(i2(4659),I1Vtnm(I1TNM(860))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm861 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm857, pyxtnm858))
                      pyxtnm862 = pyxtnm861
                      ## end-of(let)
                      ## I1CMP:return:pyxtnm862
                      return pyxtnm862
                    ## endtimp(sint_add$sint(870))
                    pyxtnm864 = XATSDAPP(pyxtnm863(pyxtnm815, XATSINT1(1)))
                    pyxtnm865 = XATSDAPP(pyxtnm856(pyxtnm797, pyxtnm864))
                    pyxtnm866 = pyxtnm853
                    ## end-of(let)
                    ## I1CMP:return:pyxtnm866
                    return pyxtnm866
                  ## endtimp(forall$test1(1340))
                  pyxtnm868 = XATSDAPP(pyxtnm867(XATSP1CN("list_vt_cons", pyxtnm809[0+1])))
                  pyxtnm869 = pyxtnm868
                  XATS000_patck(True)
                  pyxtnm871 = None
                  if (pyxtnm869):
                    pyxtnm870 = XATSDAPP(loop_1774(XATSP1CN("list_vt_cons", pyxtnm809[1+1])))
                    pyxtnm871 = pyxtnm870
                  else:
                    pyxtnm871 = XATSBOOL(False)
                  ## end-of(if)
                  pyxtnm872 = pyxtnm871
                  ## end-of(let)
                  pyxtnm873 = pyxtnm872
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:pyxtnm873
              return pyxtnm873
            pyxtnm874 = XATSDAPP(loop_1774(pyxtnm806))
            pyxtnm875 = pyxtnm874
            ## end-of(let)
            ## I1CMP:return:pyxtnm875
            return pyxtnm875
          ## endtimp(list_vt_forall1(1908))
          pyxtnm877 = pyxtnm876
          pyxtnm878 = XATSDAPP(pyxtnm877(pyxtnm795))
          pyxtnm879 = pyxtnm878
          ## end-of(let)
          pyxtnm880 = pyxtnm879
          XATS000_patck(True)
          pyxtnm881 = pyxtnm880
          ## end-of(let)
          ## I1CMP:return:pyxtnm881
          return pyxtnm881
        ## endtimp(gseq_iforall1(1611))
        pyxtnm883 = XATSDAPP(pyxtnm882(pyxtnm789))
        pyxtnm884 = pyxtnm883
        XATS000_patck(True)
        pyxtnm885 = []
        ## end-of(let)
        pyxtnm886 = pyxtnm885
        ## end-of(let)
        ## I1CMP:return:pyxtnm886
        return pyxtnm886
      ## endtimp(gseq_iforitm1(1635))
      pyxtnm888 = XATSDAPP(pyxtnm887(pyxtnm770))
      pyxtnm889 = pyxtnm888
      ## end-of(let)
      pyxtnm890 = pyxtnm889
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=304,offs=1)--4747(line=305,offs=33)))
      ## I1VALDCL
      pyxtnm899 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=305,offs=1)--4725(line=305,offs=11))
      ## I0Etapq(I0Ecst(strn_print(974)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(974), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(974)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(974);$list()))))
      def pyxtnm895(arg1): ## timp: strn_print(974)
        pyxtnm891 = arg1
        ## I1CMP:start
        ## let
        pyxtnm894 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2474));$list(I1FUNDCL(XATS2PY_strn_print(4777);$list(FJARGdarg($list(I1BNDcons(I1TNM(892);I0Pvar(cs(4778));$list(@(cs(4778),I1Vtnm(I1TNM(892))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm893 = XATSDAPP(XATS2PY_strn_print(pyxtnm891))
        pyxtnm894 = pyxtnm893
        ## end-of(let)
        ## I1CMP:return:pyxtnm894
        return pyxtnm894
      ## endtimp(strn_print(974))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=305,offs=14)--4736(line=305,offs=22))
      ## I0Etapq(I0Ecst(gseq_end(320)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2412(line=133,offs=1)--2420(line=133,offs=9))));$list(T2JAG($list(T2Pvar(xs[7298]))),T2JAG($list(T2Pvar(x0[7299])))))
      ## T1IMPallx(gseq_end(320), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq_end(320)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7870],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_end(320);$list(@(xs[951],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[7870])))),@(x0[952],T2Pvar(x0[7870])))))))
      def pyxtnm896(): ## timp: gseq_end(320)
        ## I1CMP:start
        ## I1CMP:return:XATSSTRN(")")
        return XATSSTRN(")")
      ## endtimp(gseq_end(320))
      pyxtnm897 = XATSDAPP(pyxtnm896())
      pyxtnm898 = XATSDAPP(pyxtnm895(pyxtnm897))
      pyxtnm899 = pyxtnm898
      XATS000_patck(True)
      pyxtnm900 = []
      ## end-of(let)
      ## I1CMP:return:pyxtnm900
      return pyxtnm900
    ## endtimp(gseq_print1(1561))
    pyxtnm902 = XATSDAPP(pyxtnm901(pyxtnm769))
    ## I1CMP:return:pyxtnm902
    return pyxtnm902
  ## endtimp(g_print1(1329))
  pyxtnm904 = XATSDAPP(pyxtnm903(pyxtnm756))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5636(line=282,offs=21)--5644(line=282,offs=29))
  ## I0Etapq(I0Ecst(g_print1(1329)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[7770])))))
  ## T1IMPallx(g_print1(1329), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1329)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8143],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1329);$list(@(x0[3461],T2Pvar(x0[8143])))))))
  pyxtnm911 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(38)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2691(line=158,offs=1)--2698(line=158,offs=8))));$list(T2JAG($list(T2Pvar(x0[8143])))))
  ## T1IMPallx(g_print(38), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2611(line=136,offs=1)--2648(line=137,offs=29)))
  ## T1IMPallx(g_print(38)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(38);$list(@(x0[380],T2Pcst(char)))))))
  pyxtnm910 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats)@(2636(line=137,offs=17)--2646(line=137,offs=27))
  ## I0Etapq(I0Ecst(char_print(826)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/char000.sats)@(2501(line=119,offs=1)--2511(line=119,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(char_print(826), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2887(line=170,offs=1)--3027(line=181,offs=2)))
  ## T1IMPallx(char_print(826)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(char_print(826);$list()))))
  def pyxtnm909(arg1): ## timp: char_print(826)
    pyxtnm905 = arg1
    ## I1CMP:start
    ## let
    pyxtnm908 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/char000.dats)@(2967(line=178,offs=1)--3025(line=180,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_char_print(2437));$list(I1FUNDCL(XATS2PY_char_print(4620);$list(FJARGdarg($list(I1BNDcons(I1TNM(906);I0Pvar(c0(4621));$list(@(c0(4621),I1Vtnm(I1TNM(906))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_char_print);G1Nlist($list())))))))
    pyxtnm907 = XATSDAPP(XATS2PY_char_print(pyxtnm905))
    pyxtnm908 = pyxtnm907
    ## end-of(let)
    ## I1CMP:return:pyxtnm908
    return pyxtnm908
  ## endtimp(char_print(826))
  pyxtnm910 = pyxtnm909
  pyxtnm911 = pyxtnm910
  pyxtnm912 = XATSDAPP(pyxtnm911(pyxtnm757))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5656(line=283,offs=3)--5669(line=283,offs=16))
  ## I0Etapq(I0Ecst(gs_print$end1(1842)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end1(1842), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
  ## T1IMPallx(gs_print$end1(1842)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end1(1842);$list()))))
  def pyxtnm914(): ## timp: gs_print$end1(1842)
    ## I1CMP:start
    pyxtnm913 = XATSTUP0([])
    ## I1CMP:return:pyxtnm913
    return pyxtnm913
  ## endtimp(gs_print$end1(1842))
  pyxtnm915 = XATSDAPP(pyxtnm914())
  ## I1CMP:return:pyxtnm915
  return pyxtnm915
## endtimp(gs_print1_a3(1857))
pyxtnm917 = XATSDAPP(pyxtnm916(XATSSTRN("nint_base$digitize(59049, 3) = "), pyxtnm754, XATSCHR2('\n')))
pyxtnm918 = pyxtnm917
## end-of(let)
pyxtnm919 = pyxtnm918
XATS000_patck(True)
## LCSRCsome1(test01_pre2026.dats)@(1181(line=61,offs=1)--1181(line=61,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test01_pre2026.dats)@(1181(line=61,offs=1)--1181(line=61,offs=1));D3Cnone0()))
