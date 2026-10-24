// Sun Aug 16 12:16:34 PM EDT 2026
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
// HX-2024-06-22:
// ATS3-XANADU/srcgen2/xats2js/srcgen1
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.

'use strict';

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
let XATSVOID = 0
let XATSTOP0 = undefined
//
////////////////////////////////////////////////////////////////////////.
//
let XATSINT0 = (i0) => i0
let XATSINT1 = (i0) => i0
//
let XATSBTF0 = (b0) => b0
let XATSBOOL = (b0) => b0
//
let XATSFLT0 = (f0) => f0
let XATSFLT1 = (f0) => f0
/*
let XATSSFLT = (sf) => sf
let XATSDFLT = (df) => df
*/
let XATSSTR0 = (cs) => cs
let XATSSTRN = (cs) => cs
//
let XATSCNUL = (  ) => (0)
let XATSCHR1 = (  ) => (0)
//
let XATSCHR0 =
    (ch) => ch.charCodeAt(0)
let XATSCHAR =
    (ch) => ch.charCodeAt(0)
let XATSCHR2 =
    (ch) => ch.charCodeAt(0)
//
let XATSCHR3 = (ch) => {
    var c1 // current one
    c1 = ch.charCodeAt(1)
    if (c1 < 48||c1 > 55)
    {
      return c1 ; // ascii
    } else {
	var i1 = 2;
	var ds = (c1 - 48);
	while (i1 < ch.length) {
	    c1 = ch.charCodeAt(i1);
	    if (c1===39) // SQUOTE=39
	    {
		return ds // HX: ascii
	    } else {
		i1 = i1 + 1
		ds = (8*ds) + (c1-48)
	    }
	}
	return ds ; // ascii code of [ch]
    }
}
//
////////////////////////////////////////////////////////////////////////.
/*
HX: this is historic:
let XATSVAR0 = () => [null]
let XATSVAR1 = (init) => [init]
let XATSFLAT = (addr) => addr[0]
*/
////////////////////////////////////////////////////////////////////////.

let XATSDAPP = (dapp) => dapp
let XATSCAPP = (_, capp) => capp
let XATSCAST = (_, args) => args[0]

////////////////////////////////////////////////////////////////////////.
//
let XATSPCON =
  (pcon, argi) => pcon[argi+1]
//
let XATSPFLT = (pflt) => pflt
let XATSPROJ = (proj) => proj
let XATSP0RJ = (p0rj) => p0rj
let XATSP1RJ = (_, p1rj) => p1rj
let XATSP1CN = (_, p1cn) => p1cn
//
////////////////////////////////////////////////////////////////////////.
//
let XATSTRCD = (knd0) => knd0
//
let XATSTUP0 = (tpl0) => tpl0
let XATSTUP1 = (knd0, tpl1) => tpl1
let XATSRCD2 = (knd0, rcd2) => rcd2
//
////////////////////////////////////////////////////////////////////////.
//
let XATSROOT = (x) => [0, x]
let XATSLPFT = (i, x) => [1+0, x, i]
let XATSLPBX = (i, x) => [1+1, x, i]
let XATSLPCN = (i, x) => [1+2, x, i+1]
//
let XATSVAR0 = (    ) => XATSROOT([null])
let XATSVAR1 = (init) => XATSROOT([init])
//
let XATSADDR = (addr) => addr // HX: no-op
let XATSFLAT = (addr) => XATS000_lvget(addr)
//
////////////////////////////////////////////////////////////////////////.
//
let XATSCTAG = (_, t) => t
//
let XATS000_inteq = (x, y) => (x===y)
let XATS000_btfeq = (x, y) => (x===y)
let XATS000_chreq = (x, y) => (x===y)
//
let XATS000_streq = (x, y) => (x == y)
//
let XATS000_ctgeq = (v, t) => (v[0] == t)
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
function
XATS2JS_optn_nil()
{
  return XATSCAPP("optn_nil", [0])
}
function
XATS2JS_optn_cons(x0)
{
  return XATSCAPP("optn_cons", [1, x0])
}
////////////////////////////////////////////////////////////////////////.
function
XATS2JS_list_nil()
{
  return XATSCAPP("list_nil", [0])
}
function
XATS2JS_list_cons(x0, xs)
{
  return XATSCAPP("list_cons", [1, x0, xs])
}
////////////////////////////////////////////////////////////////////////.
function
XATS2JS_optn_vt_nil()
{
  return XATSCAPP("optn_vt_nil", [0])
}
function
XATS2JS_optn_vt_cons(x0)
{
  return XATSCAPP("optn_vt_cons", [1, x0])
}
////////////////////////////////////////////////////////////////////////.
function
XATS2JS_list_vt_nil()
{
  return XATSCAPP("list_vt_nil", [0])
}
function
XATS2JS_list_vt_cons(x0, xs)
{
  return XATSCAPP("list_vt_cons", [1, x0, xs])
}
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.

let XATS000_cfail = function()
  {
    throw new Error("XATS000_cfail");
  }

let XATS000_patck = function(pck)
  {
    if (!pck) {
      throw new Error("XATS000_patck");
    } // end-of-[if]
  }

////////////////////////////////////////////////////////////////////////.

let XATS000_fold = (pcon) => null
let XATS000_free = (pcon) => null

////////////////////////////////////////////////////////////////////////.
//
let XATS000_dp2tr =
  (p2tr) => XATS000_lvget(p2tr)
//
let XATS000_l0azy = function(lfun)
{
  return [0, lfun]
}
let XATS000_dl0az = function(l0az)
{
  if (l0az[0] > 0) {
    l0az[0] += 1; return l0az[1]
  } else {
    let res = l0az[1]()
    l0az[0] = 0+1; l0az[1] = res; return res
  }
}
//
let XATS000_l1azy = (lfun) => lfun
let XATS000_dl1az = (l1az) => l1az(1)
//
let XATS000_assgn =
  (lval, rval) => XATS000_lvset(lval, rval)
//
////////////////////////////////////////////////////////////////////////.
//
let XATS000_ftset =
  function(tpl0, idx1, rval)
  {
    let tpl1 = tpl0.slice();
    tpl1[idx1] = rval; return tpl1
  }
//
let XATS000_lvget = function(lval)
  {
    let ctag = lval[0]
    if (ctag === 0)
      return lval[1][0]
    if (ctag === 1+0)
      return XATS000_lvget(lval[1])[lval[2]]
    if (ctag === 1+1)
      return lval[1][lval[2]]
    if (ctag === 1+2)
      return lval[1][lval[2]]
  }
//
let XATS000_lvset = function(lval, rval)
  {
    let ctag = lval[0]
    if (ctag === 0) return ( lval[1][0] = rval )
    if (ctag === 1+0)
    {
      return XATS000_lvset
	(lval[1], XATS000_ftset(XATS000_lvget(lval[1]), lval[2], rval))
    }
    if (ctag === 1+1) return ( lval[1][lval[2]] = rval )
    if (ctag === 1+2) return ( lval[1][lval[2]] = rval )
  }
//
////////////////////////////////////////////////////////////////////////.
//
let XATS000_raise = (xcon) => { throw(xcon) }
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
the end of
[ATS3-XANADU/srcgen2/xats2js/srcgen1/xshared/runtime/xats2js_js1emit.js]
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// Wed Aug  5 06:17:43 PM EDT 2026
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
/*
the beg of
[ATS3-XANADU/srcgen2/xats2js/srcgen1/xshared/runtime/srcgen2_prelude.js]
*/
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Thu 05 Sep 2024 11:21:07 AM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_console_log
  (x0)
{
  return console.log(x0) // HX: void
}
//
////////////////////////////////////////////////////////////////////////.
//
const
XATS2JS_the_print_store = [] // HX: for prints?
//
const
XATS2JS_the_prout_store = [] // HX: for general output
//
const
XATS2JS_the_prerr_store = [] // HX: for reporting errors
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_the_print_store_clear
  ( /*void*/ )
{
  XATS2JS_the_print_store.length = 0; return
}
//
function
XATS2JS_the_print_store_flush
  ( /*void*/ )
{
  let cs =
  XATS2JS_the_print_store.join("")
  XATS2JS_the_print_store.length = 0; return cs
}
//
function
XATS2JS_the_prout_store_flush
  ( /*void*/ )
{
  let cs =
  XATS2JS_the_prout_store.join("")
  XATS2JS_the_prout_store.length = 0; return cs
}
//
function
XATS2JS_the_prerr_store_flush
  ( /*void*/ )
{
  let cs =
  XATS2JS_the_prerr_store.join("")
  XATS2JS_the_prerr_store.length = 0; return cs
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_xtop000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Mon 09 Sep 2024 09:31:27 AM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_g_tostr
  ( obj )
{
  return String(obj) }
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strn_sint$parse$fwork
  (rep0, work)
{
  let i0 = parseInt(rep0)
  if (!isNaN(i0)) { work(i0) }; return
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strn_dflt$parse$fwork
  (rep0, work)
{
  let f0 = parseFloat(rep0)
  if (!isNaN(f0)) { work(f0) }; return
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_gbas000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Fri Sep 20 09:05:02 AM EDT 2024
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_bool_assert$errmsg
  (cond, emsg)
{
  if (!cond) {
    throw new Error("XATS2JS_bool_assert$errmsg: emsg = " + emsg)
  } ; return // HX: void is returned!
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_gdbg000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Sun 01 Sep 2024 04:27:52 PM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_sint_neg
  ( i1 )
{
  return ( -i1 ) // HX: neg
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_sint_lt$sint
  (i1, i2)
{
  return (i1 < i2) // HX: lt
}
function
XATS2JS_sint_gt$sint
  (i1, i2)
{
  return (i1 > i2) // HX: gt
}
//
function
XATS2JS_sint_lte$sint
  (i1, i2)
{
  return (i1 <= i2) // HX: lte
}
function
XATS2JS_sint_gte$sint
  (i1, i2)
{
  return (i1 >= i2) // HX: gte
}
//
function
XATS2JS_sint_eq$sint
  (i1, i2)
{
  return (i1 === i2) // HX: equal
}
function
XATS2JS_sint_neq$sint
  (i1, i2)
{
  return (i1 !== i2) // HX: noteq
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_sint_add$sint
  (i1, i2)
{
  return (i1 + i2) // HX: add
}
//
function
XATS2JS_sint_sub$sint
  (i1, i2)
{
  return (i1 - i2) // HX: sub
}
//
function
XATS2JS_sint_mul$sint
  (i1, i2)
{
  return (i1 * i2) // HX: mul
}
//
function
XATS2JS_sint_div$sint
  (i1, i2)
{
  return Math.trunc(i1 / i2)
}
//
function
XATS2JS_sint_mod$sint
  (i1, i2)
{
  return (i1 % i2) // HX: mod
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_sint_print
  ( i0 )
{
  let cs = i0.toString()
  XATS2JS_the_print_store.push(cs); return
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
// HX-2025-09-27:
// for unsigned ints
// Sat Sep 27 12:38:38 PM EDT 2025
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_uint_print
  ( u0 )
{
  let cs = u0.toString()
  XATS2JS_the_print_store.push(cs); return
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_sint_to$uint
  ( i0 )
{
  if (i0>=0)
  {
    return i0 // i0>=0
  } else {
    throw new Error("XATS2JS_sint_to$uint: i0 = " + i0.toString())
  } // end of [if(i0>=0)]
}
function
XATS2JS_uint_to$sint
  ( u0 )
{
  if (u0>=0)
  {
    return u0 // always?
  } else {
    throw new Error("XATS2JS_uint_to$sint: u0 = " + u0.toString())
  } // end of [if(u0>=0)]
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_gint000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Sun 01 Sep 2024 05:07:38 PM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_bool_lt
  (b1, b2)
{
  return (b1 < b2) // HX: lt
}
function
XATS2JS_bool_gt
  (b1, b2)
{
  return (b1 > b2) // HX: gt
}
//
function
XATS2JS_bool_lte
  (b1, b2)
{
  return (b1 <= b2) // HX: lte
}
function
XATS2JS_bool_gte
  (b1, b2)
{
  return (b1 >= b2) // HX: gte
}
//
function
XATS2JS_bool_eq
  (b1, b2)
{
  return (b1 === b2) // HX: equal
}
function
XATS2JS_bool_neq
  (b1, b2)
{
  return (b1 !== b2) // HX: noteq
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_bool000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Sun 01 Sep 2024 05:08:01 PM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_char_lt
  (c1, c2)
{
  return (c1 < c2) // HX: lt
}
function
XATS2JS_char_gt
  (c1, c2)
{
  return (c1 > c2) // HX: gt
}
//
function
XATS2JS_char_lte
  (c1, c2)
{
  return (c1 <= c2) // HX: lte
}
function
XATS2JS_char_gte
  (c1, c2)
{
  return (c1 >= c2) // HX: gte
}
//
function
XATS2JS_char_eq
  (c1, c2)
{
  return (c1 === c2) // HX: equal
}
function
XATS2JS_char_neq
  (c1, c2)
{
  return (c1 !== c2) // HX: noteq
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_char_add$sint
  (c1, i2)
{
  let c2 = c1+i2
  return (c2%256) // HX: char=int8
}
//
function
XATS2JS_char_sub$char
  (c1, c2)
{
  return (c1 - c2) // HX: char=int8
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_char_print
  ( c0 )
{
  let cs = String.fromCharCode(c0)
  XATS2JS_the_print_store.push(cs); return
}
//
////////////////////////////////////////////////////////////////////////.
//
/*
HX-2025-01-10:
Taken from gavinz
Sun Jan 19 01:11:19 AM EST 2025
*/
function
XATS2JS_char_make_sint( i0 ) { return i0 }
//
/*
HX-2026-01-15:
Thu Jan 15 06:47:03 PM EST 2026
*/
function
XATS2JS_sint_make_char( ch ) { return ch }
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_char000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Mon 09 Sep 2024 06:14:11 PM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_neg
  ( df )
{
  return ( -df ) //HX:neg
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_abs
  ( df )
{
  if (df >= 0.0)
    return df
  else
    return (-df) //HX:abs
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_sqrt
  ( df )
{
  return Math.sqrt(  df  )
}
//
function
XATS2JS_dflt_cbrt
  ( df )
{
  return Math.cbrt(  df  )
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_lt$dflt
  (f1, f2)
{
  return (f1 < f2) // HX: lt
}
function
XATS2JS_dflt_gt$dflt
  (f1, f2)
{
  return (f1 > f2) // HX: gt
}
//
function
XATS2JS_dflt_lte$dflt
  (f1, f2)
{
  return (f1 <= f2) // HX: lte
}
function
XATS2JS_dflt_gte$dflt
  (f1, f2)
{
  return (f1 >= f2) // HX: gte
}
//
function
XATS2JS_dflt_eq$dflt
  (f1, f2)
{
  return (f1 === f2) // HX: eq
}
function
XATS2JS_dflt_neq$dflt
  (f1, f2)
{
  return (f1 !== f2) // HX: neq
}
//
/*
HX-2025-12-13:
Sat Dec 13 05:19:31 PM EST 2025
*/
//
function
XATS2JS_dflt_cmp$dflt
  (f1, f2)
{
  if (f1 < f2)
    return (-1) // lt
  else // f1 >= f2
    return (f1 > f2 ? 1 : 0)
  // HX: end-of-if( f1 < f2 )
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_add$dflt
  (f1, f2)
{
  return (f1 + f2) // HX: add
}
//
function
XATS2JS_dflt_sub$dflt
  (f1, f2)
{
  return (f1 - f2) // HX: sub
}
//
//
function
XATS2JS_dflt_mul$dflt
  (f1, f2)
{
  return (f1 * f2) // HX: mul
}
//
function
XATS2JS_dflt_div$dflt
  (f1, f2)
{
  return (f1 / f2) // HX: div
}
//
function
XATS2JS_dflt_mod$dflt
  (f1, f2)
{
  return (f1 % f2) // HX: mod
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_ceil
  ( df )
{
  return Math.ceil(df) // (1.2) = 2
}
function
XATS2JS_dflt_floor
  ( df )
{
  return Math.floor(df) // (1.2) = 1
}
function
XATS2JS_dflt_round
  ( df )
{
  // HX: (1.2) = 1 // (1.5) = 2
  return Math.round(df) // (-1.5) = 1
}
function
XATS2JS_dflt_trunc
  ( df )
{
  // HX: (1.2) = 1 // (1.9) = 1
  return Math.trunc(df) // (-1.2) = -1
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_dflt_print
  ( f0 )
{
  let cs = f0.toString()
  XATS2JS_the_print_store.push(cs); return
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_gflt000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Fri 16 Aug 2024 05:26:45 PM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strn_cmp
  (x1, x2)
{
  var df
  var i0 = 0
  var n1 = x1.length;
  var n2 = x2.length;
  var n0 =
  (n1 <= n2) ? n1 : n2;
  while (i0 < n0) {
    df =
    x1.charCodeAt(i0)
    -
    x2.charCodeAt(i0)
    if (df !== 0) return df;
    i0 = (  i0 + 1  )
  }
  return (      n1 - n2      );
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strn_length
  (cs)
{
  return cs.length // HX: field
}
function
XATS000_strn_length
  (cs)
{
  return cs.length // HX: field
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strn_get$at$raw
  (cs, i0)
{
  return cs.charCodeAt(i0) // HX: ascii
}
function
XATS000_strn_get$at$raw
  (cs, i0)
{
  return XATS2JS_strn_get$at$raw(cs, i0)
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strn_make_fwork
  (fwork)
{
  var cs = []
  fwork((ch) => {cs.push(ch);return})
  return String.fromCharCode.apply(null, cs)
}
//
function
XATS000_strn_make_fwork
  (fwork)
{
  return XATS2JS_strn_make_fwork(fwork)
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS000_strn_print
  ( cs )
{
  return XATS2JS_strn_print(cs)
}
function
XATS2JS_strn_print
  ( cs )
{
  XATS2JS_the_print_store.push(cs); return
}
//
////////////////////////////////////////////////////////////////////////.
//
/*
HX-2025-04-26:
Sat Apr 26 08:48:02 PM EDT 2025
*/
//
function
XATS2JS_strn_make_env$fwork
  (env, fwork)
{
  var cs = []
  fwork(env, (ch) => {cs.push(ch);return})
  return String.fromCharCode.apply(null, cs)
}
function
XATS2JS_strn_make1_env$fwork
  (env, fwork)
{
  var cs = []
  fwork(env, (ch) => {cs.push(ch);return})
  return String.fromCharCode.apply(null, cs)
}
//
function
XATS000_strn_make_env$fwork
  (env, fwork)
{
  return XATS2JS_strn_make_env$fwork(env, fwork)
}
function
XATS000_strn_make1_env$fwork
  (env, fwork)
{
  return XATS2JS_strn_make1_env$fwork(env, fwork)
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_strn000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Fri Jan  2 03:23:26 PM EST 2026
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_list_vt_foritm0$f1un
  (xs, work)
{
  let nilq1 =
    XATS2JS_list_vt_nilq1
  while (1) {
    if (nilq1(xs)) {
      break;
    } else {
      let x1 =
        XATS2JS_list_vt_head$raw1(xs)
      work(x1)
      xs = XATS2JS_list_vt_tail$raw0(xs)
    }
  }
  return // XATS2JS_list_vt_foritm0$f1un
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_list_vt_forall0$f1un
  (xs, test, free)
{
  let nilq1 =
    XATS2JS_list_vt_nilq1
  while (1) {
    if (nilq1(xs)) {
      break;
    } else {
      let x1 =
        XATS2JS_list_vt_head$raw1(xs)
      if (test(x1)) {
        xs = XATS2JS_list_vt_tail$raw0(xs)
      } else {
        xs = XATS2JS_list_vt_tail$raw0(xs)
        XATS2JS_list_vt_foritm0$f1un(xs, free); return false
      }
    }
  }
  return true // XATS2JS_list_vt_forall0$f1un
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_list000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Fri Jan  2 03:23:26 PM EST 2026
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
// HX: It is yet to be populated!
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_optn000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Fri Jan  2 03:23:26 PM EST 2026
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strm_vt_forall0$f1un
  (fxs, test)
{
  let nilq1 =
    XATS2JS_strmcon_vt_nilq1
  while (1) {
    let cxs =
      XATS2JS_lazy_vt_eval(fxs)
    if (nilq1(cxs))
    {
      break;
    } else {
      let x01 =
        XATS2JS_strmcon_vt_head$raw1(cxs)
      if (test(x01))
      {
        fxs = XATS2JS_strmcon_vt_tail$raw0(cxs)
      } else {
        fxs = XATS2JS_strmcon_vt_tail$raw0(cxs)
        XATS2JS_lazy_vt_free(fxs); return false
      }
    }
  }
  return true // XATS2JS_strm_vt_forall0$f1un(...)
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strm_vt_filter0$f1un
  (fxs, test, free)
{
  return XATS2JS_lazy_vt_make_f0un(
    () => XATS2JS_strmcon_vt_filter0$f1un(XATS2JS_lazy_vt_eval(fxs), test, free)
  )
}
//
function
XATS2JS_strmcon_vt_filter0$f1un
  (cxs, test, free)
{
  let nilq1 =
    XATS2JS_strmcon_vt_nilq1
  while (1) {
    if (nilq1(cxs))
    {
      return XATS2JS_strmcon_vt_nil()
    } else {
      let x01 = XATS2JS_strmcon_vt_head$raw1(cxs)
      let fxs = XATS2JS_strmcon_vt_tail$raw0(cxs)
      if (test(x01)) {
        return XATS2JS_strmcon_vt_cons(x01, XATS2JS_strm_vt_filter0$f1un(fxs, test, free))
      } else {
        free(x01);
        cxs = XATS2JS_lazy_vt_eval(fxs); continue;
      }
    }
  }
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_strm000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2026 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Wed Jan 14 01:17:42 PM EST 2026
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strx_vt_forall0$f1un
  (fxs, test)
{
  while (1) {
    let cxs =
      XATS2JS_lazy_vt_eval(fxs)
    let x01 =
      XATS2JS_strxcon_vt_head$raw1(cxs)
    if (test(x01))
    {
      fxs = XATS2JS_strxcon_vt_tail$raw0(cxs)
    } else {
      fxs = XATS2JS_strxcon_vt_tail$raw0(cxs)
      XATS2JS_lazy_vt_free(fxs); return false
    }
  }
  return true // XATS2JS_strx_vt_forall0$f1un(...)
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_strx_vt_filter0$f1un
  (fxs, test, free)
{
  return XATS2JS_lazy_vt_make_f0un(
    () => XATS2JS_strxcon_vt_filter0$f1un(XATS2JS_lazy_vt_eval(fxs), test, free)
  )
}
//
function
XATS2JS_strxcon_vt_filter0$f1un
  (cxs, test, free)
{
  while (1) {
    let x01 = XATS2JS_strxcon_vt_head$raw1(cxs)
    let fxs = XATS2JS_strxcon_vt_tail$raw0(cxs)
    if (test(x01)) {
      return XATS2JS_strxcon_vt_cons(x01, XATS2JS_strx_vt_filter0$f1un(fxs, test, free))
    } else {
      free(x01);
      cxs = XATS2JS_lazy_vt_eval(fxs); continue;
    }
  }
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_strx000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Mon 12 Aug 2024 09:36:59 AM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_a0rf_lget
  ( A0 )
{
  return A0[0]
}
function
XATS2JS_a0rf_lset
  (A0, x1)
{
  A0[0] = x1; return
}
//
function
XATS2JS_a0rf_make_1val
  ( x0 )
{
  return [x0] // HX: singleton
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_a1rf_lget$at
  (A0, i0)
{
  return A0[i0]
}
function
XATS2JS_a1rf_lset$at
  (A0, i0, x1)
{
  A0[i0] = x1; return
}
//
function
XATS2JS_a1rf_make_ncpy
  (n0, x0)
{
  var i0 = 0
  var A0 = new Array(n0);
  while (i0 < n0) {
    A0[i0] = x0; i0 = i0 + 1
  }
  return A0 // HX: A0=[x0, x0, ..., x0]
}
//
function
XATS2JS_a1rf_make_nfun
  (n0, fopr)
{
  var i0 = 0
  var A0 = new Array(n0);
  while (i0 < n0) {
    A0[i0] = fopr(i0); i0 = i0 + 1
  }
  return A0 // HX: A0 = [fopr(0),...,fopr(n-1)]
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_axrf000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//                                                                    //.
//                         Applied Type System                        //.
//                                                                    //.
////////////////////////////////////////////////////////////////////////.

/*
** ATS/Xanadu - Unleashing the Potential of Types!
** Copyright (C) 2024 Hongwei Xi, ATS Trustful Software, Inc.
** All rights reserved
**
** ATS is free software;  you can  redistribute it and/or modify it under
** the terms of  the GNU GENERAL PUBLIC LICENSE (GPL) as published by the
** Free Software Foundation; either version 3, or (at  your  option)  any
** later version.
** 
** ATS is distributed in the hope that it will be useful, but WITHOUT ANY
** WARRANTY; without  even  the  implied  warranty  of MERCHANTABILITY or
** FITNESS FOR A PARTICULAR PURPOSE.  See the  GNU General Public License
** for more details.
** 
** You  should  have  received  a  copy of the GNU General Public License
** along  with  ATS;  see the  file COPYING.  If not, please write to the
** Free Software Foundation,  51 Franklin Street, Fifth Floor, Boston, MA
** 02110-1301, USA.
*/

////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
/*
Author: Hongwei Xi
Thu 15 Aug 2024 01:42:20 PM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_a1sz_length
  ( A0 )
{
  return A0.length
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_a1sz_lget$at
  (A0, i0)
{
  return A0[i0]
}
function
XATS2JS_a1sz_lset$at
  (A0, i0, x1)
{
  A0[i0] = x1; return
}
//
////////////////////////////////////////////////////////////////////////.
/*
HX-2024-09-06:
Fri 06 Sep 2024 04:18:38 PM EDT
*/
//
function
XATS2JS_a1sz_make_none
  ( n0 )
{
  var A0 = new Array(n0)
  return A0 // HX: A0 = [?, ..., ?]
}
////////////////////////////////////////////////////////////////////////.
//
/*
HX-2024-08-15:
Thu 15 Aug 2024 01:50:45 PM EDT
*/
//
function
XATS2JS_a1sz_make_ncpy
  (n0, x0)
{
  var i0 = 0
  var A0 = new Array(n0)
  while (i0 < n0) {
    A0[i0] = x0; i0 = i0 + 1
  }
  return A0 // HX: A0 = [x0, ..., x0]
}
//
function
XATS2JS_a1sz_make_nfun
  (n0, fopr)
{
  var i0 = 0
  var A0 = new Array(n0)
  while (i0 < n0) {
    A0[i0] = fopr(i0); i0 = i0 + 1
  }
  return A0 // HX: A0 = [fopr(0),...,fopr(n-1)]
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_a1sz_make_fwork
  (fwork)
{
  var A0 = []
  fwork((x0) => {A0.push(x0);return}); return A0
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_axsz000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// LCSRCsome1(test08_optn000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
// I1Dinclude(LCSRCsome1(test08_optn000.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(352(line=24,offs=1)--399(line=26,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(446(line=31,offs=1)--493(line=33,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(494(line=34,offs=1)--541(line=36,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(542(line=37,offs=1)--589(line=39,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gbas002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(616(line=43,offs=1)--669(line=45,offs=34))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gbas000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(670(line=46,offs=1)--723(line=48,offs=34))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gbas001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(895(line=59,offs=1)--935(line=59,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gxyz000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gxyz000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(982(line=64,offs=1)--1022(line=64,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/unsfx00.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1166(line=73,offs=1)--1206(line=73,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gnum000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gnum000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1207(line=74,offs=1)--1247(line=74,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gord000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gord000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1248(line=75,offs=1)--1288(line=75,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gfun000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1292(line=77,offs=1)--1332(line=77,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1333(line=78,offs=1)--1373(line=78,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1374(line=79,offs=1)--1414(line=79,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gseq002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1418(line=81,offs=1)--1458(line=81,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1459(line=82,offs=1)--1499(line=82,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1500(line=83,offs=1)--1540(line=83,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gasq002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq002.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1544(line=85,offs=1)--1584(line=85,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gmap000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gmap000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1585(line=86,offs=1)--1625(line=86,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gmap001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gmap001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1629(line=88,offs=1)--1669(line=88,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gcls000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1670(line=89,offs=1)--1710(line=89,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gsyn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1711(line=90,offs=1)--1751(line=90,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gsyn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1778(line=94,offs=1)--1818(line=94,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/bool000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/bool000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1819(line=95,offs=1)--1859(line=95,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/char000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/char000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1860(line=96,offs=1)--1900(line=96,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gint000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1901(line=97,offs=1)--1941(line=97,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gint001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(1942(line=98,offs=1)--1982(line=98,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gflt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gflt000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2009(line=102,offs=1)--2049(line=102,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2050(line=103,offs=1)--2090(line=103,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2117(line=107,offs=1)--2157(line=107,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axrf000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2158(line=108,offs=1)--2198(line=108,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axrf001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2199(line=109,offs=1)--2239(line=109,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axsz000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2240(line=110,offs=1)--2280(line=110,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/axsz001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2281(line=111,offs=1)--2321(line=111,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/asrt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/asrt000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2322(line=112,offs=1)--2362(line=112,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2363(line=113,offs=1)--2403(line=113,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2404(line=114,offs=1)--2444(line=114,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/tupl002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl002.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2445(line=115,offs=1)--2485(line=115,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2486(line=116,offs=1)--2526(line=116,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2527(line=117,offs=1)--2567(line=117,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/list002.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2568(line=118,offs=1)--2608(line=118,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/lsrt000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/lsrt000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2609(line=119,offs=1)--2649(line=119,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/optn000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2650(line=120,offs=1)--2690(line=120,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/optn001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2691(line=121,offs=1)--2731(line=121,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strm000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strm000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2732(line=122,offs=1)--2772(line=122,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strm001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strm001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2773(line=123,offs=1)--2813(line=123,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strx000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strx000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2814(line=124,offs=1)--2854(line=124,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/strx001.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strx001.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2901(line=129,offs=1)--2946(line=129,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gbas000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gbas000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2950(line=131,offs=1)--2995(line=131,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/bool000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/bool000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(2996(line=132,offs=1)--3041(line=132,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/char000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/char000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3045(line=134,offs=1)--3090(line=134,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gint000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gint000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3091(line=135,offs=1)--3136(line=135,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/gflt000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/gflt000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3140(line=137,offs=1)--3185(line=137,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/strn000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3189(line=139,offs=1)--3234(line=139,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/axrf000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/axrf000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3235(line=140,offs=1)--3280(line=140,offs=46))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/axsz000.dats";32)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/axsz000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3386(line=148,offs=1)--3432(line=148,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gnum000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3433(line=149,offs=1)--3479(line=149,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gord000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gord000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3480(line=150,offs=1)--3526(line=150,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gfun000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gfun000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3527(line=151,offs=1)--3573(line=151,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gcls000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gcls000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3574(line=152,offs=1)--3620(line=152,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3621(line=153,offs=1)--3667(line=153,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3668(line=154,offs=1)--3714(line=154,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gseq002_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq002_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3715(line=155,offs=1)--3761(line=155,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gasq000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gasq000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3762(line=156,offs=1)--3808(line=156,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gasq001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gasq001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3809(line=157,offs=1)--3855(line=157,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gsyn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3882(line=161,offs=1)--3928(line=161,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strn000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(3955(line=165,offs=1)--4001(line=165,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/axrf000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/axrf000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4002(line=166,offs=1)--4048(line=166,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/axsz000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/axsz000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4049(line=167,offs=1)--4095(line=167,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/tupl000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/tupl000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4099(line=169,offs=1)--4145(line=169,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/list000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4146(line=170,offs=1)--4192(line=170,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/list001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4193(line=171,offs=1)--4239(line=171,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/lsrt000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/lsrt000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4240(line=172,offs=1)--4286(line=172,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/optn000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/optn000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4287(line=173,offs=1)--4333(line=173,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/optn001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/optn001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4337(line=175,offs=1)--4383(line=175,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4384(line=176,offs=1)--4430(line=176,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4431(line=177,offs=1)--4477(line=177,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strm002_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4478(line=178,offs=1)--4524(line=178,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strx000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strx000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4525(line=179,offs=1)--4571(line=179,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/strx001_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strx001_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(4742(line=190,offs=1)--4788(line=190,offs=47))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/VT/gxyz000_vt.dats";33)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(5117(line=198,offs=1)--5117(line=198,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_dats.hats)@(5117(line=198,offs=1)--5117(line=198,offs=1));D3Cnone0()))
// I1Dinclude(LCSRCsome1(test08_optn000.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(197(line=15,offs=1)--249(line=16,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/xtop000.dats";35));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(296(line=21,offs=1)--344(line=22,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/gbas000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gbas000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(345(line=23,offs=1)--393(line=24,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/gdbg000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gdbg000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(440(line=29,offs=1)--488(line=30,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/bool000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/bool000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(489(line=31,offs=1)--537(line=32,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/char000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/char000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(538(line=33,offs=1)--586(line=34,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/gint000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(587(line=35,offs=1)--635(line=36,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/gflt000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gflt000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(682(line=41,offs=1)--730(line=42,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/strn000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(777(line=47,offs=1)--825(line=48,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/list000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(826(line=49,offs=1)--874(line=50,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/optn000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/optn000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(901(line=54,offs=1)--949(line=55,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/strm000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strm000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(950(line=56,offs=1)--998(line=57,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/strx000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strx000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(1045(line=62,offs=1)--1093(line=63,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/axrf000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(1094(line=64,offs=1)--1142(line=65,offs=36))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/axsz000.dats";35)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(1398(line=73,offs=1)--1398(line=73,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_JS_dats.hats)@(1398(line=73,offs=1)--1398(line=73,offs=1));D3Cnone0()))
// I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(323(line=21,offs=1)--345(line=21,offs=23)))
// I1VALDCL
let jsxtnm2
let jsxtnm1 = XATSCAPP("optn_cons", [1, XATSINT1(10)])
jsxtnm2 = jsxtnm1
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(349(line=23,offs=1)--383(line=24,offs=26)))
// I1VALDCL
let jsxtnm315
// LCSRCsome1(test08_optn000.dats)@(358(line=24,offs=1)--364(line=24,offs=7))
// I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
// T1IMPallx(gs_print_a3(808);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
// T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
let jsxtnm313 = function (arg1, arg2, arg3) { // timp: gs_print_a3(808)
  let jsxtnm3 = arg1
  let jsxtnm4 = arg2
  let jsxtnm5 = arg3
  // I1CMP:start
  let jsxtnm312 // let
  { // let
    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
    // I1VALDCL
    let jsxtnm9
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
    // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    let jsxtnm7 = function () { // timp: gs_print$beg(802)
      // I1CMP:start
      let jsxtnm6 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(6))
      return jsxtnm6
    } // endtimp(gs_print$beg(802))
    let jsxtnm8 = XATSDAPP(jsxtnm7())
    jsxtnm9 = jsxtnm8
    XATS000_patck(true)
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm15
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm14 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm10 = arg1
      // I1CMP:start
      let jsxtnm13 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(11);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(11)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm12 = XATSDAPP(XATS2JS_strn_print(jsxtnm10))
        jsxtnm13 = jsxtnm12
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(13))
      return jsxtnm13
    } // endtimp(strn_print(1040))
    jsxtnm15 = jsxtnm14
    let jsxtnm16 = XATSDAPP(jsxtnm15(jsxtnm3))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
    // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    let jsxtnm18 = function () { // timp: gs_print$sep(803)
      // I1CMP:start
      let jsxtnm17 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(17))
      return jsxtnm17
    } // endtimp(gs_print$sep(803))
    let jsxtnm19 = XATSDAPP(jsxtnm18())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3076(line=178,offs=1)--3151(line=183,offs=30)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7649],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7649])))))))))
    let jsxtnm297 = function (arg1) { // timp: g_print(39)
      let jsxtnm20 = arg1
      // I1CMP:start
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3122(line=183,offs=1)--3132(line=183,offs=11))
      // I0Etapq(I0Ecst(gseq_print(353)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2942(line=185,offs=1)--2952(line=185,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Pvar(x0[7649]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7649])))))
      // T1IMPallx(gseq_print(353);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2867(line=161,offs=1)--2928(line=164,offs=33)))
      // T1IMPallx(gseq_print(353)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6056],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6057],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print(353);$list(@(xs[1081],T2Pvar(xs[6056])),@(x0[1082],T2Pvar(x0[6057])))))))
      let jsxtnm295
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2909(line=164,offs=14)--2920(line=164,offs=25))
      // I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Pvar(xs[6056]))),T2JAG($list(T2Pvar(x0[6057])))))
      // T1IMPallx(gseq_print0(1686);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
      // T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
      let jsxtnm294 = function (arg1) { // timp: gseq_print0(1686)
        let jsxtnm21 = arg1
        // I1CMP:start
        let jsxtnm293 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
          // I1VALDCL
          let jsxtnm30
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm26 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm22 = arg1
            // I1CMP:start
            let jsxtnm25 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(23);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(23)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm24 = XATSDAPP(XATS2JS_strn_print(jsxtnm22))
              jsxtnm25 = jsxtnm24
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(25))
            return jsxtnm25
          } // endtimp(strn_print(1040))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
          // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
          // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3018(line=173,offs=1)--3072(line=176,offs=27)))
          // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7648],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7648],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7648])))),@(x0[1068],T2Pvar(x0[7648])))))))
          let jsxtnm27 = function () { // timp: gseq$beg(346)
            // I1CMP:start
            // I1CMP:return:I1Vstr(...)
            return XATSSTRN("optn(")
          } // endtimp(gseq$beg(346))
          let jsxtnm28 = XATSDAPP(jsxtnm27())
          let jsxtnm29 = XATSDAPP(jsxtnm26(jsxtnm28))
          jsxtnm30 = jsxtnm29
          XATS000_patck(true)
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
          // I1VALDCL
          let jsxtnm283
          let jsxtnm282 // let
          { // let
            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
            // I1VALDCL
            let jsxtnm39
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
            // I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
            // T1IMPallx(gseq$prlen(350);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
            // T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
            let jsxtnm37 = function () { // timp: gseq$prlen(350)
              // I1CMP:start
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
              // I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
              // T1IMPallx(sint_neg(923);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
              // T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
              let jsxtnm35 = function (arg1) { // timp: sint_neg(923)
                let jsxtnm31 = arg1
                // I1CMP:start
                let jsxtnm34 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1514(line=49,offs=1)--1563(line=51,offs=29))
                  // I1FUNDCL: XATS2JS_sint_neg(4888)
                  // XATS2JS_sint_neg_1517
                    // FJARGdarg($list(I1BNDcons(I1TNM(32);I0Pvar(i1(4889));$list(@(i1(4889),I1Vtnm(I1TNM(32)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_neg);G1Nlist($list()))// I1CMP:return
                  let jsxtnm33 = XATSDAPP(XATS2JS_sint_neg(jsxtnm31))
                  jsxtnm34 = jsxtnm33
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(34))
                return jsxtnm34
              } // endtimp(sint_neg(923))
              let jsxtnm36 = XATSDAPP(jsxtnm35(XATSINT1(1)))
              // I1CMP:return:I1Vtnm(I1TNM(36))
              return jsxtnm36
            } // endtimp(gseq$prlen(350))
            let jsxtnm38 = XATSDAPP(jsxtnm37())
            jsxtnm39 = jsxtnm38
            XATS000_patck(true)
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
            // I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
            // I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
            // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
            // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
            // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
            let jsxtnm72 = function (arg1, arg2) { // timp: sint_gte$sint(931)
              let jsxtnm66 = arg1
              let jsxtnm67 = arg2
              // I1CMP:start
              let jsxtnm71 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                // XATS2JS_sint_gte$sint_2399
                  // FJARGdarg($list(I1BNDcons(I1TNM(68);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(68))))),I1BNDcons(I1TNM(69);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(69)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                let jsxtnm70 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm66, jsxtnm67))
                jsxtnm71 = jsxtnm70
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(71))
              return jsxtnm71
            } // endtimp(sint_gte$sint(931))
            let jsxtnm73 = XATSDAPP(jsxtnm72(jsxtnm39, XATSINT1(0)))
            let jsxtnm281 // ift
            if (jsxtnm73) // ift
            {
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
              // I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
              // T1IMPallx(g_void(22);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
              // T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
              let jsxtnm76 = function (arg1) { // timp: g_void(22)
                let jsxtnm74 = arg1
                // I1CMP:start
                let jsxtnm75 = XATSTUP0([])
                // I1CMP:return:I1Vtnm(I1TNM(75))
                return jsxtnm75
              } // endtimp(g_void(22))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
              // I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
              // T1IMPallx(gseq_iforall0(1735);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
              // T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
              let jsxtnm180 = function (arg1) { // timp: gseq_iforall0(1735)
                let jsxtnm77 = arg1
                // I1CMP:start
                let jsxtnm179 // let
                { // let
                  // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
                  // I1VARDCL
                  // I1CMP:start
                  // I1CMP:return:I1Vint(T_INT01(0))
                  let jsxtnm78 = XATSVAR1(XATSINT1(0))
                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
                  // I1VALDCL
                  let jsxtnm79
                  jsxtnm79 = XATSADDR(jsxtnm78)
                  XATS000_patck(true)
                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
                  // I1VALDCL
                  let jsxtnm178
                  let jsxtnm177 // let
                  { // let
                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                    // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
                    // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
                    // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
                    // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
                    let jsxtnm175 = function (arg1) { // timp: gseq_forall0(1719)
                      let jsxtnm88 = arg1
                      // I1CMP:start
                      let jsxtnm174 // let
                      { // let
                        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                        // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
                        // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
                        // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1618(line=55,offs=1)--1681(line=58,offs=33)))
                        // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7655])))),@(x0[1168],T2Pvar(x0[7655])))))))
                        let jsxtnm172
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1666(line=58,offs=18)--1677(line=58,offs=29))
                        // I0Etapq(I0Ecst(optn_forall(1314)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn001.sats)@(1428(line=43,offs=1)--1439(line=43,offs=12))));$list(T2JAG($list(T2Pvar(x0[7655])))))
                        // T1IMPallx(optn_forall(1314);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1498(line=45,offs=1)--1614(line=53,offs=2)))
                        // T1IMPallx(optn_forall(1314)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7654],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_forall(1314);$list(@(x0[3580],T2Pvar(x0[7654])))))))
                        let jsxtnm171 = function (arg1) { // timp: optn_forall(1314)
                          let jsxtnm89 = arg1
                          // I1CMP:start
                          let jsxtnm170 // cas
                          do {
                            // { // cls
                            // I1GPTpat(I1BNDcons(I1TNM(90);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
                            if (XATS000_ctgeq(jsxtnm89, XATSCTAG("optn_nil",0))) { // gpt
                              let jsxtnm90 = jsxtnm89
                              jsxtnm170 = XATSBOOL(true)
                              break // cls
                            } // gpt
                            // } // cls
                            // { // cls
                            // I1GPTpat(I1BNDcons(I1TNM(91);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(2852))));$list(@(x0(2852),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(91));0)))))
                            if (XATS000_ctgeq(jsxtnm89, XATSCTAG("optn_cons",1))) { // gpt
                              let jsxtnm91 = jsxtnm89
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1593(line=52,offs=19)--1604(line=52,offs=30))
                              // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7654])))))
                              // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                              // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                              let jsxtnm168
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                              // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                              // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                              // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                              let jsxtnm167 = function (arg1) { // timp: forall$test0(1422)
                                let jsxtnm92 = arg1
                                // I1CMP:start
                                let jsxtnm166 // let
                                { // let
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                                  // I1VALDCL
                                  let jsxtnm97
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                                  // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                  // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                  let jsxtnm95 = function (arg1) { // timp: p2tr_get(2309)
                                    let jsxtnm93 = arg1
                                    // I1CMP:start
                                    let jsxtnm94 = XATS000_dp2tr(jsxtnm93)
                                    // I1CMP:return:I1Vtnm(I1TNM(94))
                                    return jsxtnm94
                                  } // endtimp(p2tr_get(2309))
                                  let jsxtnm96 = XATSDAPP(jsxtnm95(jsxtnm79))
                                  jsxtnm97 = jsxtnm96
                                  XATS000_patck(true)
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                                  // I1VALDCL
                                  let jsxtnm153
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                                  // I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                                  // T1IMPallx(iforall$test0(1432);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                                  // T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                  let jsxtnm151 = function (arg1, arg2) { // timp: iforall$test0(1432)
                                    let jsxtnm98 = arg1
                                    let jsxtnm99 = arg2
                                    // I1CMP:start
                                    let jsxtnm150 // let
                                    { // let
                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                                      // I1VALDCL
                                      let jsxtnm117
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                                      // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                      // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                      // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                      let jsxtnm106 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                        let jsxtnm100 = arg1
                                        let jsxtnm101 = arg2
                                        // I1CMP:start
                                        let jsxtnm105 // let
                                        { // let
                                          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                          // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                          // XATS2JS_sint_gt$sint_1876
                                            // FJARGdarg($list(I1BNDcons(I1TNM(102);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(102))))),I1BNDcons(I1TNM(103);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(103)))))))
                                            // I1CMP:start
                                            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                          let jsxtnm104 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm100, jsxtnm101))
                                          jsxtnm105 = jsxtnm104
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(105))
                                        return jsxtnm105
                                      } // endtimp(sint_gt$sint(928))
                                      let jsxtnm107 = XATSDAPP(jsxtnm106(jsxtnm98, XATSINT1(0)))
                                      let jsxtnm116 // ift
                                      if (jsxtnm107) // ift
                                      {
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                                        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                        let jsxtnm112 = function (arg1) { // timp: strn_print(1040)
                                          let jsxtnm108 = arg1
                                          // I1CMP:start
                                          let jsxtnm111 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                            // I1FUNDCL: XATS2JS_strn_print(5082)
                                            // XATS2JS_strn_print_2202
                                              // FJARGdarg($list(I1BNDcons(I1TNM(109);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(109)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm110 = XATSDAPP(XATS2JS_strn_print(jsxtnm108))
                                            jsxtnm111 = jsxtnm110
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(111))
                                          return jsxtnm111
                                        } // endtimp(strn_print(1040))
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                                        // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                        // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2916(line=165,offs=1)--2966(line=168,offs=23)))
                                        // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7646])))),@(x0[1072],T2Pvar(x0[7646])))))))
                                        let jsxtnm113 = function () { // timp: gseq$sep(348)
                                          // I1CMP:start
                                          // I1CMP:return:I1Vstr(...)
                                          return XATSSTRN(",")
                                        } // endtimp(gseq$sep(348))
                                        let jsxtnm114 = XATSDAPP(jsxtnm113())
                                        let jsxtnm115 = XATSDAPP(jsxtnm112(jsxtnm114))
                                        jsxtnm116 = jsxtnm115
                                      } else {
                                      } // end(if)
                                      jsxtnm117 = jsxtnm116
                                      XATS000_patck(true)
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                                      // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                      // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                      // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                      let jsxtnm124 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                        let jsxtnm118 = arg1
                                        let jsxtnm119 = arg2
                                        // I1CMP:start
                                        let jsxtnm123 // let
                                        { // let
                                          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                          // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                          // XATS2JS_sint_gte$sint_2399
                                            // FJARGdarg($list(I1BNDcons(I1TNM(120);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(120))))),I1BNDcons(I1TNM(121);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(121)))))))
                                            // I1CMP:start
                                            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                          let jsxtnm122 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm118, jsxtnm119))
                                          jsxtnm123 = jsxtnm122
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(123))
                                        return jsxtnm123
                                      } // endtimp(sint_gte$sint(931))
                                      let jsxtnm125 = XATSDAPP(jsxtnm124(jsxtnm98, jsxtnm39))
                                      let jsxtnm149 // ift
                                      if (jsxtnm125) // ift
                                      {
                                        let jsxtnm140 // let
                                        { // let
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                                          // I1VALDCL
                                          let jsxtnm130
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                                          // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                          // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                          // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                          let jsxtnm128 = function (arg1) { // timp: g_free(23)
                                            let jsxtnm126 = arg1
                                            // I1CMP:start
                                            let jsxtnm127 = XATSTUP0([])
                                            // I1CMP:return:I1Vtnm(I1TNM(127))
                                            return jsxtnm127
                                          } // endtimp(g_free(23))
                                          let jsxtnm129 = XATSDAPP(jsxtnm128(jsxtnm99))
                                          jsxtnm130 = jsxtnm129
                                          XATS000_patck(true)
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                                          // I1VALDCL
                                          let jsxtnm139
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                                          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                          let jsxtnm135 = function (arg1) { // timp: strn_print(1040)
                                            let jsxtnm131 = arg1
                                            // I1CMP:start
                                            let jsxtnm134 // let
                                            { // let
                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                              // I1FUNDCL: XATS2JS_strn_print(5082)
                                              // XATS2JS_strn_print_2202
                                                // FJARGdarg($list(I1BNDcons(I1TNM(132);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(132)))))))
                                                // I1CMP:start
                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                              let jsxtnm133 = XATSDAPP(XATS2JS_strn_print(jsxtnm131))
                                              jsxtnm134 = jsxtnm133
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(134))
                                            return jsxtnm134
                                          } // endtimp(strn_print(1040))
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                                          // I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                          // T1IMPallx(gseq$rst(349);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                                          // T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                                          let jsxtnm136 = function () { // timp: gseq$rst(349)
                                            // I1CMP:start
                                            // I1CMP:return:I1Vstr(...)
                                            return XATSSTRN("...")
                                          } // endtimp(gseq$rst(349))
                                          let jsxtnm137 = XATSDAPP(jsxtnm136())
                                          let jsxtnm138 = XATSDAPP(jsxtnm135(jsxtnm137))
                                          jsxtnm139 = jsxtnm138
                                          XATS000_patck(true)
                                          jsxtnm140 = XATSBOOL(false)
                                        } // endlet
                                        jsxtnm149 = jsxtnm140
                                      } else {
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                                        // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                        // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                                        // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                                        let jsxtnm147
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                                        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                                        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                        let jsxtnm146
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                        // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                        // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                        // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                        let jsxtnm145 = function (arg1) { // timp: sint_print(922)
                                          let jsxtnm141 = arg1
                                          // I1CMP:start
                                          let jsxtnm144 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                            // I1FUNDCL: XATS2JS_sint_print(4946)
                                            // XATS2JS_sint_print_3707
                                              // FJARGdarg($list(I1BNDcons(I1TNM(142);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(142)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm143 = XATSDAPP(XATS2JS_sint_print(jsxtnm141))
                                            jsxtnm144 = jsxtnm143
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(144))
                                          return jsxtnm144
                                        } // endtimp(sint_print(922))
                                        jsxtnm146 = jsxtnm145
                                        jsxtnm147 = jsxtnm146
                                        let jsxtnm148 = XATSDAPP(jsxtnm147(jsxtnm99))
                                        jsxtnm149 = XATSBOOL(true)
                                      } // end(if)
                                      jsxtnm150 = jsxtnm149
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(150))
                                    return jsxtnm150
                                  } // endtimp(iforall$test0(1432))
                                  let jsxtnm152 = XATSDAPP(jsxtnm151(jsxtnm97, jsxtnm92))
                                  jsxtnm153 = jsxtnm152
                                  XATS000_patck(true)
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                                  // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                  // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                  let jsxtnm156 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                    let jsxtnm154 = arg1
                                    let jsxtnm155 = arg2
                                    // I1CMP:start
                                    XATS000_assgn(jsxtnm154, jsxtnm155)
                                    // I1CMP:return:I1V000()
                                    return XATSVOID
                                  } // endtimp(p2tr_set(2310))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                                  // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                  // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                  // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                  let jsxtnm163 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                    let jsxtnm157 = arg1
                                    let jsxtnm158 = arg2
                                    // I1CMP:start
                                    let jsxtnm162 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                      // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                      // XATS2JS_sint_add$sint_2778
                                        // FJARGdarg($list(I1BNDcons(I1TNM(159);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(159))))),I1BNDcons(I1TNM(160);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(160)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm161 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm157, jsxtnm158))
                                      jsxtnm162 = jsxtnm161
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(162))
                                    return jsxtnm162
                                  } // endtimp(sint_add$sint(936))
                                  let jsxtnm164 = XATSDAPP(jsxtnm163(jsxtnm97, XATSINT1(1)))
                                  let jsxtnm165 = XATSDAPP(jsxtnm156(jsxtnm79, jsxtnm164))
                                  jsxtnm166 = jsxtnm153
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(166))
                                return jsxtnm166
                              } // endtimp(forall$test0(1422))
                              jsxtnm168 = jsxtnm167
                              let jsxtnm169 = XATSDAPP(jsxtnm168(XATSP1CN("optn_cons", jsxtnm91[0+1])))
                              jsxtnm170 = jsxtnm169
                              break // cls
                            } // gpt
                            // } // cls
                            XATS000_cfail()
                          } while (false) // end-of(do)
                          // I1CMP:return:I1Vtnm(I1TNM(170))
                          return jsxtnm170
                        } // endtimp(optn_forall(1314))
                        jsxtnm172 = jsxtnm171
                        let jsxtnm173 = XATSDAPP(jsxtnm172(jsxtnm88))
                        jsxtnm174 = jsxtnm173
                      } // endlet
                      // I1CMP:return:I1Vtnm(I1TNM(174))
                      return jsxtnm174
                    } // endtimp(gseq_forall0(1719))
                    let jsxtnm176 = XATSDAPP(jsxtnm175(jsxtnm77))
                    jsxtnm177 = jsxtnm176
                  } // endlet
                  jsxtnm178 = jsxtnm177
                  XATS000_patck(true)
                  jsxtnm179 = jsxtnm178
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(179))
                return jsxtnm179
              } // endtimp(gseq_iforall0(1735))
              let jsxtnm181 = XATSDAPP(jsxtnm180(jsxtnm21))
              let jsxtnm182 = XATSDAPP(jsxtnm76(jsxtnm181))
              jsxtnm281 = jsxtnm182
            } else {
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
              // I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
              // T1IMPallx(gseq_iforitm0(1759);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
              // T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
              let jsxtnm279 = function (arg1) { // timp: gseq_iforitm0(1759)
                let jsxtnm183 = arg1
                // I1CMP:start
                let jsxtnm278 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                  // I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
                  let jsxtnm277 // let
                  { // let
                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
                    // I1VALDCL
                    let jsxtnm276
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
                    // I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
                    // T1IMPallx(gseq_iforall0(1735);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
                    // T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
                    let jsxtnm274 = function (arg1) { // timp: gseq_iforall0(1735)
                      let jsxtnm189 = arg1
                      // I1CMP:start
                      let jsxtnm273 // let
                      { // let
                        // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
                        // I1VARDCL
                        // I1CMP:start
                        // I1CMP:return:I1Vint(T_INT01(0))
                        let jsxtnm190 = XATSVAR1(XATSINT1(0))
                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
                        // I1VALDCL
                        let jsxtnm191
                        jsxtnm191 = XATSADDR(jsxtnm190)
                        XATS000_patck(true)
                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
                        // I1VALDCL
                        let jsxtnm272
                        let jsxtnm271 // let
                        { // let
                          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                          // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
                          // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
                          // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
                          // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
                          let jsxtnm269 = function (arg1) { // timp: gseq_forall0(1719)
                            let jsxtnm200 = arg1
                            // I1CMP:start
                            let jsxtnm268 // let
                            { // let
                              // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                              // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
                              // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
                              // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1618(line=55,offs=1)--1681(line=58,offs=33)))
                              // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7655],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7655])))),@(x0[1168],T2Pvar(x0[7655])))))))
                              let jsxtnm266
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1666(line=58,offs=18)--1677(line=58,offs=29))
                              // I0Etapq(I0Ecst(optn_forall(1314)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn001.sats)@(1428(line=43,offs=1)--1439(line=43,offs=12))));$list(T2JAG($list(T2Pvar(x0[7655])))))
                              // T1IMPallx(optn_forall(1314);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1498(line=45,offs=1)--1614(line=53,offs=2)))
                              // T1IMPallx(optn_forall(1314)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7654],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_forall(1314);$list(@(x0[3580],T2Pvar(x0[7654])))))))
                              let jsxtnm265 = function (arg1) { // timp: optn_forall(1314)
                                let jsxtnm201 = arg1
                                // I1CMP:start
                                let jsxtnm264 // cas
                                do {
                                  // { // cls
                                  // I1GPTpat(I1BNDcons(I1TNM(202);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
                                  if (XATS000_ctgeq(jsxtnm201, XATSCTAG("optn_nil",0))) { // gpt
                                    let jsxtnm202 = jsxtnm201
                                    jsxtnm264 = XATSBOOL(true)
                                    break // cls
                                  } // gpt
                                  // } // cls
                                  // { // cls
                                  // I1GPTpat(I1BNDcons(I1TNM(203);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(2852))));$list(@(x0(2852),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(203));0)))))
                                  if (XATS000_ctgeq(jsxtnm201, XATSCTAG("optn_cons",1))) { // gpt
                                    let jsxtnm203 = jsxtnm201
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn001.dats)@(1593(line=52,offs=19)--1604(line=52,offs=30))
                                    // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7654])))))
                                    // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                                    // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                    let jsxtnm262
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                                    // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                                    // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                                    // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                    let jsxtnm261 = function (arg1) { // timp: forall$test0(1422)
                                      let jsxtnm204 = arg1
                                      // I1CMP:start
                                      let jsxtnm260 // let
                                      { // let
                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                                        // I1VALDCL
                                        let jsxtnm209
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                                        // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                        // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                        // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                        let jsxtnm207 = function (arg1) { // timp: p2tr_get(2309)
                                          let jsxtnm205 = arg1
                                          // I1CMP:start
                                          let jsxtnm206 = XATS000_dp2tr(jsxtnm205)
                                          // I1CMP:return:I1Vtnm(I1TNM(206))
                                          return jsxtnm206
                                        } // endtimp(p2tr_get(2309))
                                        let jsxtnm208 = XATSDAPP(jsxtnm207(jsxtnm191))
                                        jsxtnm209 = jsxtnm208
                                        XATS000_patck(true)
                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                                        // I1VALDCL
                                        let jsxtnm247
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                                        // I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                                        // T1IMPallx(iforall$test0(1432);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                                        // T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                        let jsxtnm245 = function (arg1, arg2) { // timp: iforall$test0(1432)
                                          let jsxtnm210 = arg1
                                          let jsxtnm211 = arg2
                                          // I1CMP:start
                                          let jsxtnm244 // let
                                          { // let
                                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                                            // I1VALDCL
                                            let jsxtnm243
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                                            // I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                                            // T1IMPallx(iforitm$work0(1448);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                                            // T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                            let jsxtnm241 = function (arg1, arg2) { // timp: iforitm$work0(1448)
                                              let jsxtnm212 = arg1
                                              let jsxtnm213 = arg2
                                              // I1CMP:start
                                              let jsxtnm240 // let
                                              { // let
                                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                                                // I1VALDCL
                                                let jsxtnm231
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                                                // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                                // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                                // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                                let jsxtnm220 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                                  let jsxtnm214 = arg1
                                                  let jsxtnm215 = arg2
                                                  // I1CMP:start
                                                  let jsxtnm219 // let
                                                  { // let
                                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                                    // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                                    // XATS2JS_sint_gt$sint_1876
                                                      // FJARGdarg($list(I1BNDcons(I1TNM(216);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(216))))),I1BNDcons(I1TNM(217);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(217)))))))
                                                      // I1CMP:start
                                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                                    let jsxtnm218 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm214, jsxtnm215))
                                                    jsxtnm219 = jsxtnm218
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(219))
                                                  return jsxtnm219
                                                } // endtimp(sint_gt$sint(928))
                                                let jsxtnm221 = XATSDAPP(jsxtnm220(jsxtnm212, XATSINT1(0)))
                                                let jsxtnm230 // ift
                                                if (jsxtnm221) // ift
                                                {
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                                                  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                                  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                                  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                                  let jsxtnm226 = function (arg1) { // timp: strn_print(1040)
                                                    let jsxtnm222 = arg1
                                                    // I1CMP:start
                                                    let jsxtnm225 // let
                                                    { // let
                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                      // I1FUNDCL: XATS2JS_strn_print(5082)
                                                      // XATS2JS_strn_print_2202
                                                        // FJARGdarg($list(I1BNDcons(I1TNM(223);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(223)))))))
                                                        // I1CMP:start
                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                      let jsxtnm224 = XATSDAPP(XATS2JS_strn_print(jsxtnm222))
                                                      jsxtnm225 = jsxtnm224
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(225))
                                                    return jsxtnm225
                                                  } // endtimp(strn_print(1040))
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                                                  // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                                  // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2916(line=165,offs=1)--2966(line=168,offs=23)))
                                                  // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7646],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7646])))),@(x0[1072],T2Pvar(x0[7646])))))))
                                                  let jsxtnm227 = function () { // timp: gseq$sep(348)
                                                    // I1CMP:start
                                                    // I1CMP:return:I1Vstr(...)
                                                    return XATSSTRN(",")
                                                  } // endtimp(gseq$sep(348))
                                                  let jsxtnm228 = XATSDAPP(jsxtnm227())
                                                  let jsxtnm229 = XATSDAPP(jsxtnm226(jsxtnm228))
                                                  jsxtnm230 = jsxtnm229
                                                } else {
                                                } // end(if)
                                                jsxtnm231 = jsxtnm230
                                                XATS000_patck(true)
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                                                // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                                // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                                                // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                                                let jsxtnm238
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                                                // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                                                // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                                // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                                let jsxtnm237
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                                // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                                // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                                // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                                let jsxtnm236 = function (arg1) { // timp: sint_print(922)
                                                  let jsxtnm232 = arg1
                                                  // I1CMP:start
                                                  let jsxtnm235 // let
                                                  { // let
                                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                                    // I1FUNDCL: XATS2JS_sint_print(4946)
                                                    // XATS2JS_sint_print_3707
                                                      // FJARGdarg($list(I1BNDcons(I1TNM(233);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(233)))))))
                                                      // I1CMP:start
                                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                                    let jsxtnm234 = XATSDAPP(XATS2JS_sint_print(jsxtnm232))
                                                    jsxtnm235 = jsxtnm234
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(235))
                                                  return jsxtnm235
                                                } // endtimp(sint_print(922))
                                                jsxtnm237 = jsxtnm236
                                                jsxtnm238 = jsxtnm237
                                                let jsxtnm239 = XATSDAPP(jsxtnm238(jsxtnm213))
                                                jsxtnm240 = jsxtnm239
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(240))
                                              return jsxtnm240
                                            } // endtimp(iforitm$work0(1448))
                                            let jsxtnm242 = XATSDAPP(jsxtnm241(jsxtnm210, jsxtnm211))
                                            jsxtnm243 = jsxtnm242
                                            XATS000_patck(true)
                                            jsxtnm244 = XATSBOOL(true)
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(244))
                                          return jsxtnm244
                                        } // endtimp(iforall$test0(1432))
                                        let jsxtnm246 = XATSDAPP(jsxtnm245(jsxtnm209, jsxtnm204))
                                        jsxtnm247 = jsxtnm246
                                        XATS000_patck(true)
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                                        // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                        // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                        // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                        let jsxtnm250 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                          let jsxtnm248 = arg1
                                          let jsxtnm249 = arg2
                                          // I1CMP:start
                                          XATS000_assgn(jsxtnm248, jsxtnm249)
                                          // I1CMP:return:I1V000()
                                          return XATSVOID
                                        } // endtimp(p2tr_set(2310))
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                                        // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                        // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                        // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                        let jsxtnm257 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                          let jsxtnm251 = arg1
                                          let jsxtnm252 = arg2
                                          // I1CMP:start
                                          let jsxtnm256 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                            // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                            // XATS2JS_sint_add$sint_2778
                                              // FJARGdarg($list(I1BNDcons(I1TNM(253);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(253))))),I1BNDcons(I1TNM(254);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(254)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm255 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm251, jsxtnm252))
                                            jsxtnm256 = jsxtnm255
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(256))
                                          return jsxtnm256
                                        } // endtimp(sint_add$sint(936))
                                        let jsxtnm258 = XATSDAPP(jsxtnm257(jsxtnm209, XATSINT1(1)))
                                        let jsxtnm259 = XATSDAPP(jsxtnm250(jsxtnm191, jsxtnm258))
                                        jsxtnm260 = jsxtnm247
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(260))
                                      return jsxtnm260
                                    } // endtimp(forall$test0(1422))
                                    jsxtnm262 = jsxtnm261
                                    let jsxtnm263 = XATSDAPP(jsxtnm262(XATSP1CN("optn_cons", jsxtnm203[0+1])))
                                    jsxtnm264 = jsxtnm263
                                    break // cls
                                  } // gpt
                                  // } // cls
                                  XATS000_cfail()
                                } while (false) // end-of(do)
                                // I1CMP:return:I1Vtnm(I1TNM(264))
                                return jsxtnm264
                              } // endtimp(optn_forall(1314))
                              jsxtnm266 = jsxtnm265
                              let jsxtnm267 = XATSDAPP(jsxtnm266(jsxtnm200))
                              jsxtnm268 = jsxtnm267
                            } // endlet
                            // I1CMP:return:I1Vtnm(I1TNM(268))
                            return jsxtnm268
                          } // endtimp(gseq_forall0(1719))
                          let jsxtnm270 = XATSDAPP(jsxtnm269(jsxtnm189))
                          jsxtnm271 = jsxtnm270
                        } // endlet
                        jsxtnm272 = jsxtnm271
                        XATS000_patck(true)
                        jsxtnm273 = jsxtnm272
                      } // endlet
                      // I1CMP:return:I1Vtnm(I1TNM(273))
                      return jsxtnm273
                    } // endtimp(gseq_iforall0(1735))
                    let jsxtnm275 = XATSDAPP(jsxtnm274(jsxtnm183))
                    jsxtnm276 = jsxtnm275
                    XATS000_patck(true)
                    jsxtnm277 = XATSVOID
                  } // endlet
                  jsxtnm278 = jsxtnm277
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(278))
                return jsxtnm278
              } // endtimp(gseq_iforitm0(1759))
              let jsxtnm280 = XATSDAPP(jsxtnm279(jsxtnm21))
              jsxtnm281 = jsxtnm280
            } // end(if)
            jsxtnm282 = jsxtnm281
          } // endlet
          jsxtnm283 = jsxtnm282
          XATS000_patck(true)
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
          // I1VALDCL
          let jsxtnm292
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm288 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm284 = arg1
            // I1CMP:start
            let jsxtnm287 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(285);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(285)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm286 = XATSDAPP(XATS2JS_strn_print(jsxtnm284))
              jsxtnm287 = jsxtnm286
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(287))
            return jsxtnm287
          } // endtimp(strn_print(1040))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
          // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
          // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2967(line=169,offs=1)--3017(line=172,offs=23)))
          // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(optn_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7647],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7647],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(optn);$list(T2Pvar(x0[7647])))),@(x0[1070],T2Pvar(x0[7647])))))))
          let jsxtnm289 = function () { // timp: gseq$end(347)
            // I1CMP:start
            // I1CMP:return:I1Vstr(...)
            return XATSSTRN(")")
          } // endtimp(gseq$end(347))
          let jsxtnm290 = XATSDAPP(jsxtnm289())
          let jsxtnm291 = XATSDAPP(jsxtnm288(jsxtnm290))
          jsxtnm292 = jsxtnm291
          XATS000_patck(true)
          jsxtnm293 = XATSVOID
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(293))
        return jsxtnm293
      } // endtimp(gseq_print0(1686))
      jsxtnm295 = jsxtnm294
      let jsxtnm296 = XATSDAPP(jsxtnm295(jsxtnm20))
      // I1CMP:return:I1Vtnm(I1TNM(296))
      return jsxtnm296
    } // endtimp(g_print(39))
    let jsxtnm298 = XATSDAPP(jsxtnm297(jsxtnm4))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
    // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    let jsxtnm300 = function () { // timp: gs_print$sep(803)
      // I1CMP:start
      let jsxtnm299 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(299))
      return jsxtnm299
    } // endtimp(gs_print$sep(803))
    let jsxtnm301 = XATSDAPP(jsxtnm300())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm307
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm306 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm302 = arg1
      // I1CMP:start
      let jsxtnm305 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(303);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(303)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm304 = XATSDAPP(XATS2JS_strn_print(jsxtnm302))
        jsxtnm305 = jsxtnm304
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(305))
      return jsxtnm305
    } // endtimp(strn_print(1040))
    jsxtnm307 = jsxtnm306
    let jsxtnm308 = XATSDAPP(jsxtnm307(jsxtnm5))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
    // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    let jsxtnm310 = function () { // timp: gs_print$end(804)
      // I1CMP:start
      let jsxtnm309 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(309))
      return jsxtnm309
    } // endtimp(gs_print$end(804))
    let jsxtnm311 = XATSDAPP(jsxtnm310())
    jsxtnm312 = jsxtnm311
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(312))
  return jsxtnm312
} // endtimp(gs_print_a3(808))
let jsxtnm314 = XATSDAPP(jsxtnm313(XATSSTRN("ns = "), jsxtnm2, XATSSTRN("\n")))
jsxtnm315 = jsxtnm314
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(384(line=25,offs=1)--429(line=26,offs=30)))
// I1VALDCL
let jsxtnm362
// LCSRCsome1(test08_optn000.dats)@(393(line=25,offs=10)--399(line=25,offs=16))
// I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
// T1IMPallx(gs_print_a3(808);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
// T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
let jsxtnm354 = function (arg1, arg2, arg3) { // timp: gs_print_a3(808)
  let jsxtnm316 = arg1
  let jsxtnm317 = arg2
  let jsxtnm318 = arg3
  // I1CMP:start
  let jsxtnm353 // let
  { // let
    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
    // I1VALDCL
    let jsxtnm322
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
    // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    let jsxtnm320 = function () { // timp: gs_print$beg(802)
      // I1CMP:start
      let jsxtnm319 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(319))
      return jsxtnm319
    } // endtimp(gs_print$beg(802))
    let jsxtnm321 = XATSDAPP(jsxtnm320())
    jsxtnm322 = jsxtnm321
    XATS000_patck(true)
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm328
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm327 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm323 = arg1
      // I1CMP:start
      let jsxtnm326 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(324);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(324)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm325 = XATSDAPP(XATS2JS_strn_print(jsxtnm323))
        jsxtnm326 = jsxtnm325
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(326))
      return jsxtnm326
    } // endtimp(strn_print(1040))
    jsxtnm328 = jsxtnm327
    let jsxtnm329 = XATSDAPP(jsxtnm328(jsxtnm316))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
    // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    let jsxtnm331 = function () { // timp: gs_print$sep(803)
      // I1CMP:start
      let jsxtnm330 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(330))
      return jsxtnm330
    } // endtimp(gs_print$sep(803))
    let jsxtnm332 = XATSDAPP(jsxtnm331())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
    let jsxtnm338
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
    // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
    // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
    let jsxtnm337 = function (arg1) { // timp: sint_print(922)
      let jsxtnm333 = arg1
      // I1CMP:start
      let jsxtnm336 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
        // I1FUNDCL: XATS2JS_sint_print(4946)
        // XATS2JS_sint_print_3707
          // FJARGdarg($list(I1BNDcons(I1TNM(334);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(334)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm335 = XATSDAPP(XATS2JS_sint_print(jsxtnm333))
        jsxtnm336 = jsxtnm335
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(336))
      return jsxtnm336
    } // endtimp(sint_print(922))
    jsxtnm338 = jsxtnm337
    let jsxtnm339 = XATSDAPP(jsxtnm338(jsxtnm317))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
    // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    let jsxtnm341 = function () { // timp: gs_print$sep(803)
      // I1CMP:start
      let jsxtnm340 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(340))
      return jsxtnm340
    } // endtimp(gs_print$sep(803))
    let jsxtnm342 = XATSDAPP(jsxtnm341())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm348
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm347 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm343 = arg1
      // I1CMP:start
      let jsxtnm346 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(344);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(344)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm345 = XATSDAPP(XATS2JS_strn_print(jsxtnm343))
        jsxtnm346 = jsxtnm345
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(346))
      return jsxtnm346
    } // endtimp(strn_print(1040))
    jsxtnm348 = jsxtnm347
    let jsxtnm349 = XATSDAPP(jsxtnm348(jsxtnm318))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
    // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    let jsxtnm351 = function () { // timp: gs_print$end(804)
      // I1CMP:start
      let jsxtnm350 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(350))
      return jsxtnm350
    } // endtimp(gs_print$end(804))
    let jsxtnm352 = XATSDAPP(jsxtnm351())
    jsxtnm353 = jsxtnm352
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(353))
  return jsxtnm353
} // endtimp(gs_print_a3(808))
// LCSRCsome1(test08_optn000.dats)@(412(line=26,offs=13)--418(line=26,offs=19))
// I0Etapq(I0Ecst(optn_length(1313)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn000.sats)@(2061(line=90,offs=1)--2072(line=90,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(optn_length(1313);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(3294(line=195,offs=1)--3387(line=202,offs=21)))
// T1IMPallx(optn_length(1313)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7651],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_length(1313);$list(@(a[3578],T2Pvar(x0[7651])))))))
let jsxtnm359 = function (arg1) { // timp: optn_length(1313)
  let jsxtnm355 = arg1
  // I1CMP:start
  let jsxtnm358 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(356);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
    if (XATS000_ctgeq(jsxtnm355, XATSCTAG("optn_nil",0))) { // gpt
      let jsxtnm356 = jsxtnm355
      jsxtnm358 = XATSINT1(0)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(357);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pany()));$list()))
    if (XATS000_ctgeq(jsxtnm355, XATSCTAG("optn_cons",1))) { // gpt
      let jsxtnm357 = jsxtnm355
      jsxtnm358 = XATSINT1(1)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:I1Vtnm(I1TNM(358))
  return jsxtnm358
} // endtimp(optn_length(1313))
let jsxtnm360 = XATSDAPP(jsxtnm359(jsxtnm2))
let jsxtnm361 = XATSDAPP(jsxtnm354(XATSSTRN("|ns| = "), jsxtnm360, XATSSTRN("\n")))
jsxtnm362 = jsxtnm361
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(430(line=27,offs=1)--477(line=28,offs=32)))
// I1VALDCL
let jsxtnm408
// LCSRCsome1(test08_optn000.dats)@(439(line=27,offs=10)--445(line=27,offs=16))
// I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
// T1IMPallx(gs_print_a3(808);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
// T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
let jsxtnm401 = function (arg1, arg2, arg3) { // timp: gs_print_a3(808)
  let jsxtnm363 = arg1
  let jsxtnm364 = arg2
  let jsxtnm365 = arg3
  // I1CMP:start
  let jsxtnm400 // let
  { // let
    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
    // I1VALDCL
    let jsxtnm369
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
    // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    let jsxtnm367 = function () { // timp: gs_print$beg(802)
      // I1CMP:start
      let jsxtnm366 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(366))
      return jsxtnm366
    } // endtimp(gs_print$beg(802))
    let jsxtnm368 = XATSDAPP(jsxtnm367())
    jsxtnm369 = jsxtnm368
    XATS000_patck(true)
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm375
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm374 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm370 = arg1
      // I1CMP:start
      let jsxtnm373 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(371);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(371)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm372 = XATSDAPP(XATS2JS_strn_print(jsxtnm370))
        jsxtnm373 = jsxtnm372
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(373))
      return jsxtnm373
    } // endtimp(strn_print(1040))
    jsxtnm375 = jsxtnm374
    let jsxtnm376 = XATSDAPP(jsxtnm375(jsxtnm363))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
    // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    let jsxtnm378 = function () { // timp: gs_print$sep(803)
      // I1CMP:start
      let jsxtnm377 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(377))
      return jsxtnm377
    } // endtimp(gs_print$sep(803))
    let jsxtnm379 = XATSDAPP(jsxtnm378())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
    let jsxtnm385
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
    // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
    // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
    let jsxtnm384 = function (arg1) { // timp: sint_print(922)
      let jsxtnm380 = arg1
      // I1CMP:start
      let jsxtnm383 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
        // I1FUNDCL: XATS2JS_sint_print(4946)
        // XATS2JS_sint_print_3707
          // FJARGdarg($list(I1BNDcons(I1TNM(381);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(381)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm382 = XATSDAPP(XATS2JS_sint_print(jsxtnm380))
        jsxtnm383 = jsxtnm382
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(383))
      return jsxtnm383
    } // endtimp(sint_print(922))
    jsxtnm385 = jsxtnm384
    let jsxtnm386 = XATSDAPP(jsxtnm385(jsxtnm364))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
    // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    let jsxtnm388 = function () { // timp: gs_print$sep(803)
      // I1CMP:start
      let jsxtnm387 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(387))
      return jsxtnm387
    } // endtimp(gs_print$sep(803))
    let jsxtnm389 = XATSDAPP(jsxtnm388())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm395
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm394 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm390 = arg1
      // I1CMP:start
      let jsxtnm393 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(391);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(391)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm392 = XATSDAPP(XATS2JS_strn_print(jsxtnm390))
        jsxtnm393 = jsxtnm392
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(393))
      return jsxtnm393
    } // endtimp(strn_print(1040))
    jsxtnm395 = jsxtnm394
    let jsxtnm396 = XATSDAPP(jsxtnm395(jsxtnm365))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
    // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    let jsxtnm398 = function () { // timp: gs_print$end(804)
      // I1CMP:start
      let jsxtnm397 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(397))
      return jsxtnm397
    } // endtimp(gs_print$end(804))
    let jsxtnm399 = XATSDAPP(jsxtnm398())
    jsxtnm400 = jsxtnm399
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(400))
  return jsxtnm400
} // endtimp(gs_print_a3(808))
// LCSRCsome1(test08_optn000.dats)@(462(line=28,offs=17)--466(line=28,offs=21))
// I0Etapq(I0Ecst(optn_head(1311)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/optn000.sats)@(1695(line=64,offs=1)--1704(line=64,offs=10))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(optn_head(1311);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/optn000.dats)@(2478(line=129,offs=1)--2556(line=135,offs=25)))
// T1IMPallx(optn_head(1311)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[7642],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(optn_head(1311);$list(@(a[3576],T2Pvar(a[7642])))))))
let jsxtnm405 = function (arg1) { // timp: optn_head(1311)
  let jsxtnm402 = arg1
  // I1CMP:start
  let jsxtnm404 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(403);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(2844))));$list(@(x0(2844),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(403));0)))))
    if (XATS000_ctgeq(jsxtnm402, XATSCTAG("optn_cons",1))) { // gpt
      let jsxtnm403 = jsxtnm402
      jsxtnm404 = XATSP1CN("optn_cons", jsxtnm403[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:I1Vtnm(I1TNM(404))
  return jsxtnm404
} // endtimp(optn_head(1311))
let jsxtnm406 = XATSDAPP(jsxtnm405(jsxtnm2))
let jsxtnm407 = XATSDAPP(jsxtnm401(XATSSTRN("head(ns) = "), jsxtnm406, XATSSTRN("\n")))
jsxtnm408 = jsxtnm407
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test08_optn000.dats)@(524(line=33,offs=1)--579(line=33,offs=56)))
// I1VALDCL
let jsxtnm419
// LCSRCsome1(test08_optn000.dats)@(533(line=33,offs=10)--544(line=33,offs=21))
// I0Etapq(I0Ecst(console_log(2594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1544(line=50,offs=1)--1555(line=50,offs=12))));$list(T2JAG($list())))
// T1IMPallx(console_log(2594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1581(line=53,offs=1)--1730(line=65,offs=2)))
// T1IMPallx(console_log(2594)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(console_log(2594);$list()))))
let jsxtnm413 = function (arg1) { // timp: console_log(2594)
  let jsxtnm409 = arg1
  // I1CMP:start
  let jsxtnm412 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1663(line=61,offs=1)--1728(line=64,offs=34)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1671(line=62,offs=1)--1728(line=64,offs=34))
    // I1FUNDCL: XATS2JS_console_log(4774)
    // XATS2JS_console_log_1674
      // FJARGdarg($list(I1BNDcons(I1TNM(410);I0Pvar(x0(4775));$list(@(x0(4775),I1Vtnm(I1TNM(410)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_console_log);G1Nlist($list()))// I1CMP:return
    let jsxtnm411 = XATSDAPP(XATS2JS_console_log(jsxtnm409))
    jsxtnm412 = jsxtnm411
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(412))
  return jsxtnm412
} // endtimp(console_log(2594))
// LCSRCsome1(test08_optn000.dats)@(545(line=33,offs=22)--566(line=33,offs=43))
// I0Etapq(I0Ecst(the_print_store_flush(2597)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1836(line=76,offs=1)--1857(line=76,offs=22))));$list(T2JAG($list())))
// T1IMPallx(the_print_store_flush(2597);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1998(line=87,offs=1)--2171(line=98,offs=2)))
// T1IMPallx(the_print_store_flush(2597)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(the_print_store_flush(2597);$list()))))
let jsxtnm416 = function () { // timp: the_print_store_flush(2597)
  // I1CMP:start
  let jsxtnm415 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2108(line=95,offs=1)--2169(line=97,offs=50)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2116(line=96,offs=1)--2169(line=97,offs=50))
    // I1FUNDCL: XATS2JS_the_print_store_flush(4778)
    // XATS2JS_the_print_store_flush_2119
      // FJARGdarg($list())
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_the_print_store_flush);G1Nlist($list()))// I1CMP:return
    let jsxtnm414 = XATSDAPP(XATS2JS_the_print_store_flush())
    jsxtnm415 = jsxtnm414
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(415))
  return jsxtnm415
} // endtimp(the_print_store_flush(2597))
let jsxtnm417 = XATSDAPP(jsxtnm416())
let jsxtnm418 = XATSDAPP(jsxtnm413(jsxtnm417))
jsxtnm419 = jsxtnm418
XATS000_patck(true)
// LCSRCsome1(test08_optn000.dats)@(842(line=41,offs=1)--842(line=41,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(test08_optn000.dats)@(842(line=41,offs=1)--842(line=41,offs=1));D3Cnone0()))
