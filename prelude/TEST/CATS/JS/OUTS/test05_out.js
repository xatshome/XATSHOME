// Sun Aug 16 12:16:00 PM EDT 2026
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
// Wed Aug  5 06:17:44 PM EDT 2026
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
/*
the beg of
[ATS3-XANADU/srcgen2/xats2js/srcgen1/xshared/runtime/srcgen2_prelude_node.js]
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
Sun 01 Sep 2024 08:04:48 AM EDT
Authoremail: gmhwxiATgmailDOTcom
*/
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
const
XATS2JS_NODE_fs =
require('node:fs')
// HX: the same as require('fs')
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_NODE_g_print
  (x0)
{
  let rep = x0.toString();
  process.stdout.write(rep);
  return; // XATS2JS_NODE_g_print
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_NODE_sint_print
  (i0)
{
  XATS2JS_NODE_g_print(i0);
  return; // XATS2JS_NODE_sint_print
}
//
function
XATS2JS_NODE_uint_print
  (u0)
{
  XATS2JS_NODE_g_print(u0);
  return; // XATS2JS_NODE_uint_print
}
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_NODE_bool_print
  (b0)
{
  XATS2JS_NODE_g_print(b0);
  return; // XATS2JS_NODE_bool_print
}
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_NODE_char_print
  (c0)
{
  let cs =
  String.fromCharCode(c0)
  XATS2JS_NODE_g_print(cs);
  return; // XATS2JS_NODE_char_print
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_NODE_dflt_print
  (f0)
{
  XATS2JS_NODE_g_print(f0);
  return; // XATS2JS_NODE_dflt_print
}
//
////////////////////////////////////////////////////////////////////////.
//
function
XATS2JS_NODE_strn_print
  (cs)
{
  XATS2JS_NODE_g_print(cs);
  return; // XATS2JS_NODE_strn_print
}
//
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// end of [ATS3/XANADU_prelude_DATS_CATS_JS_NODE_node000.cats]
////////////////////////////////////////////////////////////////////////.
////////////////////////////////////////////////////////////////////////.
// LCSRCsome1(test05_gdbg000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
// I1Dinclude(LCSRCsome1(test05_gdbg000.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
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
// I1Dinclude(LCSRCsome1(test05_gdbg000.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
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
// I1Dinclude(LCSRCsome1(test05_gdbg000.dats)@(277(line=17,offs=1)--323(line=18,offs=38)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_NODE_dats.hats)@(202(line=15,offs=1)--255(line=16,offs=41))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/CATS/JS/NODE/node000.dats";40)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats));...)))
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_NODE_dats.hats)@(508(line=24,offs=1)--508(line=24,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/HATS/prelude_NODE_dats.hats)@(508(line=24,offs=1)--508(line=24,offs=1));D3Cnone0()))
// I1Dfundclist(LCSRCsome1(test05_gdbg000.dats)@(370(line=23,offs=1)--432(line=27,offs=26)))
// I1FUNDCL
function fact_373(arg1)
{ // fun
  let jsxtnm1 = arg1
  // I1CMP:start
  // LCSRCsome1(test05_gdbg000.dats)@(402(line=26,offs=4)--403(line=26,offs=5))
  // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
  // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
  // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
  let jsxtnm8 = function (arg1, arg2) { // timp: sint_gt$sint(928)
    let jsxtnm2 = arg1
    let jsxtnm3 = arg2
    // I1CMP:start
    let jsxtnm7 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
      // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
      // XATS2JS_sint_gt$sint_1876
        // FJARGdarg($list(I1BNDcons(I1TNM(4);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(4))))),I1BNDcons(I1TNM(5);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(5)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
      let jsxtnm6 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm2, jsxtnm3))
      jsxtnm7 = jsxtnm6
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(7))
    return jsxtnm7
  } // endtimp(sint_gt$sint(928))
  let jsxtnm9 = XATSDAPP(jsxtnm8(jsxtnm1, XATSINT1(0)))
  let jsxtnm27 // ift
  if (jsxtnm9) // ift
  {
    // LCSRCsome1(test05_gdbg000.dats)@(414(line=27,offs=8)--415(line=27,offs=9))
    // I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
    // T1IMPallx(sint_mul$sint(938);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
    // T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
    let jsxtnm16 = function (arg1, arg2) { // timp: sint_mul$sint(938)
      let jsxtnm10 = arg1
      let jsxtnm11 = arg2
      // I1CMP:start
      let jsxtnm15 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3111(line=182,offs=1)--3175(line=184,offs=39))
        // I1FUNDCL: XATS2JS_sint_mul$sint(4932)
        // XATS2JS_sint_mul$sint_3114
          // FJARGdarg($list(I1BNDcons(I1TNM(12);I0Pvar(i1(4933));$list(@(i1(4933),I1Vtnm(I1TNM(12))))),I1BNDcons(I1TNM(13);I0Pvar(i2(4934));$list(@(i2(4934),I1Vtnm(I1TNM(13)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_mul$sint);G1Nlist($list()))// I1CMP:return
        let jsxtnm14 = XATSDAPP(XATS2JS_sint_mul$sint(jsxtnm10, jsxtnm11))
        jsxtnm15 = jsxtnm14
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(15))
      return jsxtnm15
    } // endtimp(sint_mul$sint(938))
    // LCSRCsome1(test05_gdbg000.dats)@(422(line=27,offs=16)--423(line=27,offs=17))
    // I0Etapq(I0Ecst(sint_sub$sint(937)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3146(line=146,offs=1)--3159(line=146,offs=14))));$list(T2JAG($list())))
    // T1IMPallx(sint_sub$sint(937);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2845(line=159,offs=1)--3009(line=171,offs=2)))
    // T1IMPallx(sint_sub$sint(937)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_sub$sint(937);$list()))))
    let jsxtnm23 = function (arg1, arg2) { // timp: sint_sub$sint(937)
      let jsxtnm17 = arg1
      let jsxtnm18 = arg2
      // I1CMP:start
      let jsxtnm22 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2935(line=167,offs=1)--3007(line=170,offs=39)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2943(line=168,offs=1)--3007(line=170,offs=39))
        // I1FUNDCL: XATS2JS_sint_sub$sint(4927)
        // XATS2JS_sint_sub$sint_2946
          // FJARGdarg($list(I1BNDcons(I1TNM(19);I0Pvar(i1(4928));$list(@(i1(4928),I1Vtnm(I1TNM(19))))),I1BNDcons(I1TNM(20);I0Pvar(i2(4929));$list(@(i2(4929),I1Vtnm(I1TNM(20)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_sub$sint);G1Nlist($list()))// I1CMP:return
        let jsxtnm21 = XATSDAPP(XATS2JS_sint_sub$sint(jsxtnm17, jsxtnm18))
        jsxtnm22 = jsxtnm21
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(22))
      return jsxtnm22
    } // endtimp(sint_sub$sint(937))
    let jsxtnm24 = XATSDAPP(jsxtnm23(jsxtnm1, XATSINT1(1)))
    let jsxtnm25 = XATSDAPP(fact_373(jsxtnm24))
    let jsxtnm26 = XATSDAPP(jsxtnm16(jsxtnm1, jsxtnm25))
    jsxtnm27 = jsxtnm26
  } else {
    jsxtnm27 = XATSINT1(1)
  } // end(if)
  // I1CMP:return:I1Vtnm(I1TNM(27))
  return jsxtnm27
} // endfun(fact_373)
// I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(479(line=32,offs=1)--509(line=33,offs=27)))
// I1VALDCL
let jsxtnm118
// LCSRCsome1(test05_gdbg000.dats)@(490(line=33,offs=8)--495(line=33,offs=13))
// I0Etapq(I0Ecst(f1un_trace(316)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gfun000.sats)@(3453(line=188,offs=1)--3463(line=188,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(f1un_trace(316);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2559(line=124,offs=1)--2769(line=137,offs=39)))
// T1IMPallx(f1un_trace(316)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a1[5966],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[5967],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(f1un_trace(316);$list(@(a1[986],T2Pvar(a1[5966])),@(r0[987],T2Pvar(r0[5967])))))))
let jsxtnm116 = function (arg1, arg2) { // timp: f1un_trace(316)
  let jsxtnm28 = arg1
  let jsxtnm29 = arg2
  // I1CMP:start
  let jsxtnm115 = function (arg1) { // lam0(T_LAM(0))
    let jsxtnm30 = arg1
    // I1CMP:start
    let jsxtnm114 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2634(line=131,offs=1)--2678(line=132,offs=29)))
      // I1VALDCL
      let jsxtnm74
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2643(line=131,offs=10)--2649(line=131,offs=16))
      // I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(a1[5966]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
      // T1IMPallx(gs_print_a4(809);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
      // T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[7025],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
      let jsxtnm72 = function (arg1, arg2, arg3, arg4) { // timp: gs_print_a4(809)
        let jsxtnm31 = arg1
        let jsxtnm32 = arg2
        let jsxtnm33 = arg3
        let jsxtnm34 = arg4
        // I1CMP:start
        let jsxtnm71 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
          // I1VALDCL
          let jsxtnm38
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
          // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
          // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
          let jsxtnm36 = function () { // timp: gs_print$beg(802)
            // I1CMP:start
            let jsxtnm35 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(35))
            return jsxtnm35
          } // endtimp(gs_print$beg(802))
          let jsxtnm37 = XATSDAPP(jsxtnm36())
          jsxtnm38 = jsxtnm37
          XATS000_patck(true)
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm42
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm41
          let jsxtnm40 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(39);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(39)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm40 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm41 = jsxtnm40
          jsxtnm42 = jsxtnm41
          let jsxtnm43 = XATSDAPP(jsxtnm42(jsxtnm31))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm45 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm44 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(44))
            return jsxtnm44
          } // endtimp(gs_print$sep(803))
          let jsxtnm46 = XATSDAPP(jsxtnm45())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm50
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm49
          let jsxtnm48 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(47);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(47)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm48 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm49 = jsxtnm48
          jsxtnm50 = jsxtnm49
          let jsxtnm51 = XATSDAPP(jsxtnm50(jsxtnm32))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm53 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm52 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(52))
            return jsxtnm52
          } // endtimp(gs_print$sep(803))
          let jsxtnm54 = XATSDAPP(jsxtnm53())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
          let jsxtnm58
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
          // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(1430(line=40,offs=1)--1551(line=48,offs=2)))
          // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
          let jsxtnm57
          let jsxtnm56 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(1486(line=45,offs=1)--1549(line=47,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(1494(line=46,offs=1)--1549(line=47,offs=52))
            // I1FUNDCL: XATS2JS_NODE_sint_print(5204)
            // XATS2JS_NODE_sint_print_1497
              // FJARGdarg($list(I1BNDcons(I1TNM(55);I0Pvar(i0(5205));$list(@(i0(5205),I1Vtnm(I1TNM(55)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_sint_print);G1Nlist($list()))// I1CMP:return
            jsxtnm56 = XATS2JS_NODE_sint_print
          } // endlet
          jsxtnm57 = jsxtnm56
          jsxtnm58 = jsxtnm57
          let jsxtnm59 = XATSDAPP(jsxtnm58(jsxtnm33))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm61 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm60 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(60))
            return jsxtnm60
          } // endtimp(gs_print$sep(803))
          let jsxtnm62 = XATSDAPP(jsxtnm61())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm66
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm65
          let jsxtnm64 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(63);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(63)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm64 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm65 = jsxtnm64
          jsxtnm66 = jsxtnm65
          let jsxtnm67 = XATSDAPP(jsxtnm66(jsxtnm34))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
          // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
          // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
          let jsxtnm69 = function () { // timp: gs_print$end(804)
            // I1CMP:start
            let jsxtnm68 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(68))
            return jsxtnm68
          } // endtimp(gs_print$end(804))
          let jsxtnm70 = XATSDAPP(jsxtnm69())
          jsxtnm71 = jsxtnm70
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(71))
        return jsxtnm71
      } // endtimp(gs_print_a4(809))
      let jsxtnm73 = XATSDAPP(jsxtnm72(jsxtnm29, XATSSTRN(": arg1 = "), jsxtnm30, XATSSTRN("\n")))
      jsxtnm74 = jsxtnm73
      XATS000_patck(true)
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2682(line=134,offs=1)--2710(line=134,offs=29)))
      // I1VALDCL
      let jsxtnm76
      let jsxtnm75 = XATSDAPP(jsxtnm28(jsxtnm30))
      jsxtnm76 = jsxtnm75
      XATS000_patck(true)
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2714(line=136,offs=1)--2759(line=137,offs=29)))
      // I1VALDCL
      let jsxtnm113
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2723(line=136,offs=10)--2730(line=136,offs=17))
      // I0Etapq(I0Ecst(gs_print1_a4(1989)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3688(line=226,offs=1)--3700(line=226,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(r0[5967]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
      // T1IMPallx(gs_print1_a4(1989);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5678(line=285,offs=1)--5877(line=295,offs=21)))
      // T1IMPallx(gs_print1_a4(1989)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8384],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8385],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[8386],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x3[8387],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a4(1989);$list(@(x0[5122],T2Pvar(x0[8384])),@(x1[5123],T2Pvar(x1[8385])),@(x2[5124],T2Pvar(x2[8386])),@(x3[5125],T2Pvar(x3[8387])))))))
      let jsxtnm111 = function (arg1, arg2, arg3, arg4) { // timp: gs_print1_a4(1989)
        let jsxtnm77 = arg1
        let jsxtnm78 = arg2
        let jsxtnm79 = arg3
        let jsxtnm80 = arg4
        // I1CMP:start
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5763(line=292,offs=3)--5776(line=292,offs=16))
        // I0Etapq(I0Ecst(gs_print1$beg(1972)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
        // T1IMPallx(gs_print1$beg(1972);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
        // T1IMPallx(gs_print1$beg(1972)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$beg(1972);$list()))))
        let jsxtnm82 = function () { // timp: gs_print1$beg(1972)
          // I1CMP:start
          let jsxtnm81 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(81))
          return jsxtnm81
        } // endtimp(gs_print1$beg(1972))
        let jsxtnm83 = XATSDAPP(jsxtnm82())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5784(line=293,offs=3)--5792(line=293,offs=11))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[8384])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm88
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm87
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm86
        let jsxtnm85 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(84);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(84)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm85 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm86 = jsxtnm85
        jsxtnm87 = jsxtnm86
        jsxtnm88 = jsxtnm87
        let jsxtnm89 = XATSDAPP(jsxtnm88(jsxtnm77))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5802(line=293,offs=21)--5810(line=293,offs=29))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[8385])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm94
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm93
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm92
        let jsxtnm91 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(90);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(90)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm91 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm92 = jsxtnm91
        jsxtnm93 = jsxtnm92
        jsxtnm94 = jsxtnm93
        let jsxtnm95 = XATSDAPP(jsxtnm94(jsxtnm78))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5821(line=294,offs=3)--5829(line=294,offs=11))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[8386])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm100
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
        let jsxtnm99
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
        // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(1430(line=40,offs=1)--1551(line=48,offs=2)))
        // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
        let jsxtnm98
        let jsxtnm97 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(1486(line=45,offs=1)--1549(line=47,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(1494(line=46,offs=1)--1549(line=47,offs=52))
          // I1FUNDCL: XATS2JS_NODE_sint_print(5204)
          // XATS2JS_NODE_sint_print_1497
            // FJARGdarg($list(I1BNDcons(I1TNM(96);I0Pvar(i0(5205));$list(@(i0(5205),I1Vtnm(I1TNM(96)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_sint_print);G1Nlist($list()))// I1CMP:return
          jsxtnm97 = XATS2JS_NODE_sint_print
        } // endlet
        jsxtnm98 = jsxtnm97
        jsxtnm99 = jsxtnm98
        jsxtnm100 = jsxtnm99
        let jsxtnm101 = XATSDAPP(jsxtnm100(jsxtnm79))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5839(line=294,offs=21)--5847(line=294,offs=29))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x3[8387])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm106
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm105
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm104
        let jsxtnm103 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(102);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(102)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm103 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm104 = jsxtnm103
        jsxtnm105 = jsxtnm104
        jsxtnm106 = jsxtnm105
        let jsxtnm107 = XATSDAPP(jsxtnm106(jsxtnm80))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5859(line=295,offs=3)--5872(line=295,offs=16))
        // I0Etapq(I0Ecst(gs_print1$end(1973)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
        // T1IMPallx(gs_print1$end(1973);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
        // T1IMPallx(gs_print1$end(1973)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$end(1973);$list()))))
        let jsxtnm109 = function () { // timp: gs_print1$end(1973)
          // I1CMP:start
          let jsxtnm108 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(108))
          return jsxtnm108
        } // endtimp(gs_print1$end(1973))
        let jsxtnm110 = XATSDAPP(jsxtnm109())
        // I1CMP:return:I1Vtnm(I1TNM(110))
        return jsxtnm110
      } // endtimp(gs_print1_a4(1989))
      let jsxtnm112 = XATSDAPP(jsxtnm111(jsxtnm29, XATSSTRN(": res0 = "), jsxtnm76, XATSSTRN("\n")))
      jsxtnm113 = jsxtnm112
      XATS000_patck(true)
      jsxtnm114 = jsxtnm76
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(114))
    return jsxtnm114
  } // endfun(lam0)
  // I1CMP:return:I1Vtnm(I1TNM(115))
  return jsxtnm115
} // endtimp(f1un_trace(316))
let jsxtnm117 = XATSDAPP(jsxtnm116(fact_373, XATSSTRN("fact")))
jsxtnm118 = jsxtnm117
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(513(line=35,offs=1)--566(line=37,offs=31)))
// I1VALDCL
let jsxtnm180
// LCSRCsome1(test05_gdbg000.dats)@(528(line=36,offs=5)--566(line=37,offs=31))
// I0Etapq(I0Ecst(nint_foritm$f1un(964)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3054(line=146,offs=1)--3070(line=146,offs=17))));$list(T2JAG($list())))
// T1IMPallx(nint_foritm$f1un(964);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4008(line=237,offs=1)--4137(line=246,offs=2)))
// T1IMPallx(nint_foritm$f1un(964)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_foritm$f1un(964);$list()))))
let jsxtnm171 = function (arg1, arg2) { // timp: nint_foritm$f1un(964)
  let jsxtnm119 = arg1
  let jsxtnm120 = arg2
  // I1CMP:start
  let jsxtnm170 // let
  { // let
    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4090(line=244,offs=1)--4135(line=245,offs=37)))
    // I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(ni))))):timp
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4063(line=242,offs=3)--4074(line=242,offs=14))
    // I0Etapq(I0Ecst(nint_foritm(962)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(2701(line=122,offs=1)--2712(line=122,offs=12))));$list(T2JAG($list())))
    // T1IMPallx(nint_foritm(962);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3945(line=233,offs=1)--3999(line=236,offs=22)))
    // T1IMPallx(nint_foritm(962)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_foritm(962);$list()))))
    let jsxtnm168
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3978(line=236,offs=1)--3989(line=236,offs=12))
    // I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
    // T1IMPallx(gseq_foritm(402);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
    // T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
    let jsxtnm167 = function (arg1) { // timp: gseq_foritm(402)
      let jsxtnm123 = arg1
      // I1CMP:start
      let jsxtnm166 // let
      { // let
        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
        // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
        let jsxtnm165 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
          // I1VALDCL
          let jsxtnm164
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
          // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
          // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3103(line=172,offs=1)--3149(line=173,offs=38)))
          // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(nint)),@(x0[1168],T2Pcst(ni)))))))
          let jsxtnm162
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3136(line=173,offs=25)--3147(line=173,offs=36))
          // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
          // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
          // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
          let jsxtnm161 = function (arg1) { // timp: nint_forall(958)
            let jsxtnm128 = arg1
            // I1CMP:start
            let jsxtnm160 // let
            { // let
              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
              // I1FUNDCL
              function loop_2862(arg1, arg2)
              { // fun
                let jsxtnm129 = arg1
                let jsxtnm130 = arg2
                // I1CMP:start
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                let jsxtnm137 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                  let jsxtnm131 = arg1
                  let jsxtnm132 = arg2
                  // I1CMP:start
                  let jsxtnm136 // let
                  { // let
                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                    // XATS2JS_sint_gte$sint_2399
                      // FJARGdarg($list(I1BNDcons(I1TNM(133);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(133))))),I1BNDcons(I1TNM(134);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(134)))))))
                      // I1CMP:start
                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                    let jsxtnm135 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm131, jsxtnm132))
                    jsxtnm136 = jsxtnm135
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(136))
                  return jsxtnm136
                } // endtimp(sint_gte$sint(931))
                let jsxtnm138 = XATSDAPP(jsxtnm137(jsxtnm130, jsxtnm129))
                let jsxtnm158 // ift
                if (jsxtnm138) // ift
                {
                  jsxtnm158 = XATSBOOL(true)
                } else {
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                  // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                  // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                  // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  let jsxtnm146 = function (arg1) { // timp: forall$test(47)
                    let jsxtnm139 = arg1
                    // I1CMP:start
                    let jsxtnm145 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                      // I1VALDCL
                      let jsxtnm144
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                      // I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                      // T1IMPallx(foritm$work(51);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4090(line=244,offs=1)--4135(line=245,offs=37)))
                      // T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(ni)))))))
                      let jsxtnm142 = function (arg1) { // timp: foritm$work(51)
                        let jsxtnm140 = arg1
                        // I1CMP:start
                        let jsxtnm141 = XATSDAPP(jsxtnm120(jsxtnm140))
                        // I1CMP:return:I1Vtnm(I1TNM(141))
                        return jsxtnm141
                      } // endtimp(foritm$work(51))
                      let jsxtnm143 = XATSDAPP(jsxtnm142(jsxtnm139))
                      jsxtnm144 = jsxtnm143
                      XATS000_patck(true)
                      jsxtnm145 = XATSBOOL(true)
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(145))
                    return jsxtnm145
                  } // endtimp(forall$test(47))
                  let jsxtnm147 = XATSDAPP(jsxtnm146(jsxtnm130))
                  let jsxtnm157 // ift
                  if (jsxtnm147) // ift
                  {
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                    // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                    // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                    let jsxtnm154 = function (arg1, arg2) { // timp: sint_add$sint(936)
                      let jsxtnm148 = arg1
                      let jsxtnm149 = arg2
                      // I1CMP:start
                      let jsxtnm153 // let
                      { // let
                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                        // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                        // XATS2JS_sint_add$sint_2778
                          // FJARGdarg($list(I1BNDcons(I1TNM(150);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(150))))),I1BNDcons(I1TNM(151);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(151)))))))
                          // I1CMP:start
                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                        let jsxtnm152 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm148, jsxtnm149))
                        jsxtnm153 = jsxtnm152
                      } // endlet
                      // I1CMP:return:I1Vtnm(I1TNM(153))
                      return jsxtnm153
                    } // endtimp(sint_add$sint(936))
                    let jsxtnm155 = XATSDAPP(jsxtnm154(jsxtnm130, XATSINT1(1)))
                    let jsxtnm156 = XATSDAPP(loop_2862(jsxtnm129, jsxtnm155))
                    jsxtnm157 = jsxtnm156
                  } else {
                    jsxtnm157 = XATSBOOL(false)
                  } // end(if)
                  jsxtnm158 = jsxtnm157
                } // end(if)
                // I1CMP:return:I1Vtnm(I1TNM(158))
                return jsxtnm158
              } // endfun(loop_2862)
              let jsxtnm159 = XATSDAPP(loop_2862(jsxtnm128, XATSINT1(0)))
              jsxtnm160 = jsxtnm159
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(160))
            return jsxtnm160
          } // endtimp(nint_forall(958))
          jsxtnm162 = jsxtnm161
          let jsxtnm163 = XATSDAPP(jsxtnm162(jsxtnm123))
          jsxtnm164 = jsxtnm163
          XATS000_patck(true)
          jsxtnm165 = XATSVOID
        } // endlet
        jsxtnm166 = jsxtnm165
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(166))
      return jsxtnm166
    } // endtimp(gseq_foritm(402))
    jsxtnm168 = jsxtnm167
    let jsxtnm169 = XATSDAPP(jsxtnm168(jsxtnm119))
    jsxtnm170 = jsxtnm169
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(170))
  return jsxtnm170
} // endtimp(nint_foritm$f1un(964))
let jsxtnm178 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm172 = arg1
  // I1CMP:start
  // LCSRCsome1(test05_gdbg000.dats)@(550(line=37,offs=15)--556(line=37,offs=21))
  // I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  // T1IMPallx(g_void(22);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
  // T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
  let jsxtnm175 = function (arg1) { // timp: g_void(22)
    let jsxtnm173 = arg1
    // I1CMP:start
    let jsxtnm174 = XATSTUP0([])
    // I1CMP:return:I1Vtnm(I1TNM(174))
    return jsxtnm174
  } // endtimp(g_void(22))
  let jsxtnm176 = XATSDAPP(jsxtnm118(jsxtnm172))
  let jsxtnm177 = XATSDAPP(jsxtnm175(jsxtnm176))
  // I1CMP:return:I1Vtnm(I1TNM(177))
  return jsxtnm177
} // endfun(lam0)
let jsxtnm179 = XATSDAPP(jsxtnm171(XATSINT1(20), jsxtnm178))
jsxtnm180 = jsxtnm179
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(613(line=42,offs=1)--666(line=44,offs=36)))
// I1VALDCL
let jsxtnm493
// LCSRCsome1(test05_gdbg000.dats)@(631(line=44,offs=1)--636(line=44,offs=6))
// I0Etapq(I0Ecst(f2un_trace(317)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gfun000.sats)@(3536(line=196,offs=1)--3546(line=196,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
// T1IMPallx(f2un_trace(317);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2796(line=141,offs=1)--3068(line=158,offs=39)))
// T1IMPallx(f2un_trace(317)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(a1[5968],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(a2[5969],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(r0[5970],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(f2un_trace(317);$list(@(a1[988],T2Pvar(a1[5968])),@(a2[989],T2Pvar(a2[5969])),@(r0[990],T2Pvar(r0[5970])))))))
let jsxtnm314 = function (arg1, arg2) { // timp: f2un_trace(317)
  let jsxtnm181 = arg1
  let jsxtnm182 = arg2
  // I1CMP:start
  let jsxtnm313 = function (arg1, arg2) { // lam0(T_LAM(0))
    let jsxtnm183 = arg1
    let jsxtnm184 = arg2
    // I1CMP:start
    let jsxtnm312 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2888(line=150,offs=1)--2932(line=151,offs=29)))
      // I1VALDCL
      let jsxtnm228
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2897(line=150,offs=10)--2903(line=150,offs=16))
      // I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(a1[5968]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
      // T1IMPallx(gs_print_a4(809);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
      // T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
      let jsxtnm226 = function (arg1, arg2, arg3, arg4) { // timp: gs_print_a4(809)
        let jsxtnm185 = arg1
        let jsxtnm186 = arg2
        let jsxtnm187 = arg3
        let jsxtnm188 = arg4
        // I1CMP:start
        let jsxtnm225 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
          // I1VALDCL
          let jsxtnm192
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
          // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
          // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
          let jsxtnm190 = function () { // timp: gs_print$beg(802)
            // I1CMP:start
            let jsxtnm189 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(189))
            return jsxtnm189
          } // endtimp(gs_print$beg(802))
          let jsxtnm191 = XATSDAPP(jsxtnm190())
          jsxtnm192 = jsxtnm191
          XATS000_patck(true)
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm196
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm195
          let jsxtnm194 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(193);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(193)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm194 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm195 = jsxtnm194
          jsxtnm196 = jsxtnm195
          let jsxtnm197 = XATSDAPP(jsxtnm196(jsxtnm185))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm199 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm198 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(198))
            return jsxtnm198
          } // endtimp(gs_print$sep(803))
          let jsxtnm200 = XATSDAPP(jsxtnm199())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm204
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm203
          let jsxtnm202 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(201);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(201)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm202 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm203 = jsxtnm202
          jsxtnm204 = jsxtnm203
          let jsxtnm205 = XATSDAPP(jsxtnm204(jsxtnm186))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm207 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm206 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(206))
            return jsxtnm206
          } // endtimp(gs_print$sep(803))
          let jsxtnm208 = XATSDAPP(jsxtnm207())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm212
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm211
          let jsxtnm210 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(209);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(209)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm210 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm211 = jsxtnm210
          jsxtnm212 = jsxtnm211
          let jsxtnm213 = XATSDAPP(jsxtnm212(jsxtnm187))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm215 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm214 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(214))
            return jsxtnm214
          } // endtimp(gs_print$sep(803))
          let jsxtnm216 = XATSDAPP(jsxtnm215())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm220
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm219
          let jsxtnm218 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(217);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(217)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm218 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm219 = jsxtnm218
          jsxtnm220 = jsxtnm219
          let jsxtnm221 = XATSDAPP(jsxtnm220(jsxtnm188))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
          // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
          // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
          let jsxtnm223 = function () { // timp: gs_print$end(804)
            // I1CMP:start
            let jsxtnm222 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(222))
            return jsxtnm222
          } // endtimp(gs_print$end(804))
          let jsxtnm224 = XATSDAPP(jsxtnm223())
          jsxtnm225 = jsxtnm224
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(225))
        return jsxtnm225
      } // endtimp(gs_print_a4(809))
      let jsxtnm227 = XATSDAPP(jsxtnm226(jsxtnm182, XATSSTRN(": arg1 = "), jsxtnm183, XATSSTRN("\n")))
      jsxtnm228 = jsxtnm227
      XATS000_patck(true)
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2933(line=152,offs=1)--2977(line=153,offs=29)))
      // I1VALDCL
      let jsxtnm272
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2942(line=152,offs=10)--2948(line=152,offs=16))
      // I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(a2[5969]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
      // T1IMPallx(gs_print_a4(809);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
      // T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
      let jsxtnm270 = function (arg1, arg2, arg3, arg4) { // timp: gs_print_a4(809)
        let jsxtnm229 = arg1
        let jsxtnm230 = arg2
        let jsxtnm231 = arg3
        let jsxtnm232 = arg4
        // I1CMP:start
        let jsxtnm269 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
          // I1VALDCL
          let jsxtnm236
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
          // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
          // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
          let jsxtnm234 = function () { // timp: gs_print$beg(802)
            // I1CMP:start
            let jsxtnm233 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(233))
            return jsxtnm233
          } // endtimp(gs_print$beg(802))
          let jsxtnm235 = XATSDAPP(jsxtnm234())
          jsxtnm236 = jsxtnm235
          XATS000_patck(true)
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm240
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm239
          let jsxtnm238 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(237);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(237)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm238 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm239 = jsxtnm238
          jsxtnm240 = jsxtnm239
          let jsxtnm241 = XATSDAPP(jsxtnm240(jsxtnm229))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm243 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm242 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(242))
            return jsxtnm242
          } // endtimp(gs_print$sep(803))
          let jsxtnm244 = XATSDAPP(jsxtnm243())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm248
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm247
          let jsxtnm246 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(245);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(245)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm246 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm247 = jsxtnm246
          jsxtnm248 = jsxtnm247
          let jsxtnm249 = XATSDAPP(jsxtnm248(jsxtnm230))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm251 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm250 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(250))
            return jsxtnm250
          } // endtimp(gs_print$sep(803))
          let jsxtnm252 = XATSDAPP(jsxtnm251())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm256
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm255
          let jsxtnm254 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(253);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(253)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm254 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm255 = jsxtnm254
          jsxtnm256 = jsxtnm255
          let jsxtnm257 = XATSDAPP(jsxtnm256(jsxtnm231))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
          // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
          // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
          let jsxtnm259 = function () { // timp: gs_print$sep(803)
            // I1CMP:start
            let jsxtnm258 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(258))
            return jsxtnm258
          } // endtimp(gs_print$sep(803))
          let jsxtnm260 = XATSDAPP(jsxtnm259())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
          let jsxtnm264
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm263
          let jsxtnm262 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
            // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
            // XATS2JS_NODE_strn_print_2214
              // FJARGdarg($list(I1BNDcons(I1TNM(261);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(261)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
            jsxtnm262 = XATS2JS_NODE_strn_print
          } // endlet
          jsxtnm263 = jsxtnm262
          jsxtnm264 = jsxtnm263
          let jsxtnm265 = XATSDAPP(jsxtnm264(jsxtnm232))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
          // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
          // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
          // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
          let jsxtnm267 = function () { // timp: gs_print$end(804)
            // I1CMP:start
            let jsxtnm266 = XATSTUP0([])
            // I1CMP:return:I1Vtnm(I1TNM(266))
            return jsxtnm266
          } // endtimp(gs_print$end(804))
          let jsxtnm268 = XATSDAPP(jsxtnm267())
          jsxtnm269 = jsxtnm268
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(269))
        return jsxtnm269
      } // endtimp(gs_print_a4(809))
      let jsxtnm271 = XATSDAPP(jsxtnm270(jsxtnm182, XATSSTRN(": arg2 = "), jsxtnm184, XATSSTRN("\n")))
      jsxtnm272 = jsxtnm271
      XATS000_patck(true)
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(2981(line=155,offs=1)--3009(line=155,offs=29)))
      // I1VALDCL
      let jsxtnm274
      let jsxtnm273 = XATSDAPP(jsxtnm181(jsxtnm183, jsxtnm184))
      jsxtnm274 = jsxtnm273
      XATS000_patck(true)
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(3013(line=157,offs=1)--3058(line=158,offs=29)))
      // I1VALDCL
      let jsxtnm311
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gfun000.dats)@(3022(line=157,offs=10)--3029(line=157,offs=17))
      // I0Etapq(I0Ecst(gs_print1_a4(1989)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3688(line=226,offs=1)--3700(line=226,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Pvar(r0[5970]))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
      // T1IMPallx(gs_print1_a4(1989);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5678(line=285,offs=1)--5877(line=295,offs=21)))
      // T1IMPallx(gs_print1_a4(1989)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8384],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8385],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x2[8386],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[8387],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a4(1989);$list(@(x0[5122],T2Pvar(x0[8384])),@(x1[5123],T2Pvar(x1[8385])),@(x2[5124],T2Pvar(x2[8386])),@(x3[5125],T2Pvar(x3[8387])))))))
      let jsxtnm309 = function (arg1, arg2, arg3, arg4) { // timp: gs_print1_a4(1989)
        let jsxtnm275 = arg1
        let jsxtnm276 = arg2
        let jsxtnm277 = arg3
        let jsxtnm278 = arg4
        // I1CMP:start
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5763(line=292,offs=3)--5776(line=292,offs=16))
        // I0Etapq(I0Ecst(gs_print1$beg(1972)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
        // T1IMPallx(gs_print1$beg(1972);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
        // T1IMPallx(gs_print1$beg(1972)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$beg(1972);$list()))))
        let jsxtnm280 = function () { // timp: gs_print1$beg(1972)
          // I1CMP:start
          let jsxtnm279 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(279))
          return jsxtnm279
        } // endtimp(gs_print1$beg(1972))
        let jsxtnm281 = XATSDAPP(jsxtnm280())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5784(line=293,offs=3)--5792(line=293,offs=11))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[8384])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm286
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm285
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm284
        let jsxtnm283 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(282);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(282)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm283 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm284 = jsxtnm283
        jsxtnm285 = jsxtnm284
        jsxtnm286 = jsxtnm285
        let jsxtnm287 = XATSDAPP(jsxtnm286(jsxtnm275))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5802(line=293,offs=21)--5810(line=293,offs=29))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[8385])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm292
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm291
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm290
        let jsxtnm289 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(288);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(288)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm289 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm290 = jsxtnm289
        jsxtnm291 = jsxtnm290
        jsxtnm292 = jsxtnm291
        let jsxtnm293 = XATSDAPP(jsxtnm292(jsxtnm276))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5821(line=294,offs=3)--5829(line=294,offs=11))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[8386])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm298
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm297
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm296
        let jsxtnm295 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(294);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(294)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm295 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm296 = jsxtnm295
        jsxtnm297 = jsxtnm296
        jsxtnm298 = jsxtnm297
        let jsxtnm299 = XATSDAPP(jsxtnm298(jsxtnm277))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5839(line=294,offs=21)--5847(line=294,offs=29))
        // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x3[8387])))))
        // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
        // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
        let jsxtnm304
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm303
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2147(line=98,offs=1)--2268(line=106,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm302
        let jsxtnm301 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2203(line=103,offs=1)--2266(line=105,offs=52)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/NODE/node000.dats)@(2211(line=104,offs=1)--2266(line=105,offs=52))
          // I1FUNDCL: XATS2JS_NODE_strn_print(5214)
          // XATS2JS_NODE_strn_print_2214
            // FJARGdarg($list(I1BNDcons(I1TNM(300);I0Pvar(cs(5215));$list(@(cs(5215),I1Vtnm(I1TNM(300)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_NODE_strn_print);G1Nlist($list()))// I1CMP:return
          jsxtnm301 = XATS2JS_NODE_strn_print
        } // endlet
        jsxtnm302 = jsxtnm301
        jsxtnm303 = jsxtnm302
        jsxtnm304 = jsxtnm303
        let jsxtnm305 = XATSDAPP(jsxtnm304(jsxtnm278))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5859(line=295,offs=3)--5872(line=295,offs=16))
        // I0Etapq(I0Ecst(gs_print1$end(1973)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
        // T1IMPallx(gs_print1$end(1973);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
        // T1IMPallx(gs_print1$end(1973)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$end(1973);$list()))))
        let jsxtnm307 = function () { // timp: gs_print1$end(1973)
          // I1CMP:start
          let jsxtnm306 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(306))
          return jsxtnm306
        } // endtimp(gs_print1$end(1973))
        let jsxtnm308 = XATSDAPP(jsxtnm307())
        // I1CMP:return:I1Vtnm(I1TNM(308))
        return jsxtnm308
      } // endtimp(gs_print1_a4(1989))
      let jsxtnm310 = XATSDAPP(jsxtnm309(jsxtnm182, XATSSTRN(": res0 = "), jsxtnm274, XATSSTRN("\n")))
      jsxtnm311 = jsxtnm310
      XATS000_patck(true)
      jsxtnm312 = jsxtnm274
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(312))
    return jsxtnm312
  } // endfun(lam0)
  // I1CMP:return:I1Vtnm(I1TNM(313))
  return jsxtnm313
} // endtimp(f2un_trace(317))
// LCSRCsome1(test05_gdbg000.dats)@(637(line=44,offs=7)--648(line=44,offs=18))
// I0Etapq(I0Ecst(strn_append(1063)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(5650(line=339,offs=1)--5661(line=339,offs=12))));$list(T2JAG($list())))
// T1IMPallx(strn_append(1063);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3415(line=190,offs=1)--3529(line=197,offs=38)))
// T1IMPallx(strn_append(1063)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_append(1063);$list()))))
let jsxtnm491 = function (arg1, arg2) { // timp: strn_append(1063)
  let jsxtnm315 = arg1
  let jsxtnm316 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3459(line=194,offs=1)--3474(line=194,offs=16))
  // I0Etapq(I0Ecst(strn_make_fwork(1090)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(4102(line=185,offs=1)--4117(line=185,offs=16))));$list(T2JAG($list())))
  // T1IMPallx(strn_make_fwork(1090);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2479(line=126,offs=1)--2658(line=139,offs=2)))
  // T1IMPallx(strn_make_fwork(1090)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_make_fwork(1090);$list()))))
  let jsxtnm321 = function (arg1) { // timp: strn_make_fwork(1090)
    let jsxtnm317 = arg1
    // I1CMP:start
    let jsxtnm320 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2571(line=134,offs=1)--2656(line=138,offs=42)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2579(line=135,offs=1)--2656(line=138,offs=42))
      // I1FUNDCL: XATS000_strn_make_fwork(3302)
      // XATS000_strn_make_fwork_2582
        // FJARGdarg($list(I1BNDcons(I1TNM(318);I0Pvar(fwork(3303));$list(@(fwork(3303),I1Vtnm(I1TNM(318)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS000_strn_make_fwork);G1Nlist($list()))// I1CMP:return
      let jsxtnm319 = XATSDAPP(XATS000_strn_make_fwork(jsxtnm317))
      jsxtnm320 = jsxtnm319
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(320))
    return jsxtnm320
  } // endtimp(strn_make_fwork(1090))
  let jsxtnm489 = function (arg1) { // lam0(T_LAM(0))
    let jsxtnm322 = arg1
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3493(line=197,offs=2)--3499(line=197,offs=8))
    // I0Etapq(I0Ecst(strn_foritm$f1un(1086)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3510(line=153,offs=1)--3526(line=153,offs=17))));$list(T2JAG($list())))
    // T1IMPallx(strn_foritm$f1un(1086);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3971(line=237,offs=1)--4096(line=246,offs=2)))
    // T1IMPallx(strn_foritm$f1un(1086)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm$f1un(1086);$list()))))
    let jsxtnm404 = function (arg1, arg2) { // timp: strn_foritm$f1un(1086)
      let jsxtnm323 = arg1
      let jsxtnm324 = arg2
      // I1CMP:start
      let jsxtnm403 // let
      { // let
        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
        // I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz))))):timp
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4026(line=242,offs=3)--4037(line=242,offs=14))
        // I0Etapq(I0Ecst(strn_foritm(1082)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3113(line=132,offs=1)--3124(line=132,offs=12))));$list(T2JAG($list())))
        // T1IMPallx(strn_foritm(1082);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3914(line=233,offs=1)--3970(line=236,offs=24)))
        // T1IMPallx(strn_foritm(1082)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm(1082);$list()))))
        let jsxtnm401
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3947(line=236,offs=1)--3958(line=236,offs=12))
        // I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
        // T1IMPallx(gseq_foritm(402);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
        // T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
        let jsxtnm400 = function (arg1) { // timp: gseq_foritm(402)
          let jsxtnm327 = arg1
          // I1CMP:start
          let jsxtnm399 // let
          { // let
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
            // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
            let jsxtnm398 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
              // I1VALDCL
              let jsxtnm397
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
              // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
              // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1976(line=85,offs=1)--2025(line=87,offs=29)))
              // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(strn)),@(x0[1168],T2Pcst(cgtz)))))))
              let jsxtnm395
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(2012(line=87,offs=16)--2023(line=87,offs=27))
              // I0Etapq(I0Ecst(strn_forall(1074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(2101(line=80,offs=1)--2112(line=80,offs=12))));$list(T2JAG($list())))
              // T1IMPallx(strn_forall(1074);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1556(line=51,offs=1)--1772(line=72,offs=2)))
              // T1IMPallx(strn_forall(1074)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_forall(1074);$list()))))
              let jsxtnm394 = function (arg1) { // timp: strn_forall(1074)
                let jsxtnm332 = arg1
                // I1CMP:start
                let jsxtnm393 // let
                { // let
                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1627(line=59,offs=1)--1658(line=61,offs=21)))
                  // I1VALDCL
                  let jsxtnm339
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1640(line=61,offs=3)--1651(line=61,offs=14))
                  // I0Etapq(I0Ecst(strn_length(1041)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2709(line=131,offs=1)--2720(line=131,offs=12))));$list(T2JAG($list())))
                  // T1IMPallx(strn_length(1041);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(1610(line=57,offs=1)--1756(line=69,offs=2)))
                  // T1IMPallx(strn_length(1041)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_length(1041);$list()))))
                  let jsxtnm337 = function (arg1) { // timp: strn_length(1041)
                    let jsxtnm333 = arg1
                    // I1CMP:start
                    let jsxtnm336 // let
                    { // let
                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(1692(line=65,offs=1)--1754(line=68,offs=31)))
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(1700(line=66,offs=1)--1754(line=68,offs=31))
                      // I1FUNDCL: XATS2JS_strn_length(5074)
                      // XATS2JS_strn_length_1703
                        // FJARGdarg($list(I1BNDcons(I1TNM(334);I0Pvar(cs(5075));$list(@(cs(5075),I1Vtnm(I1TNM(334)))))))
                        // I1CMP:start
                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_length);G1Nlist($list()))// I1CMP:return
                      let jsxtnm335 = XATSDAPP(XATS2JS_strn_length(jsxtnm333))
                      jsxtnm336 = jsxtnm335
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(336))
                    return jsxtnm336
                  } // endtimp(strn_length(1041))
                  let jsxtnm338 = XATSDAPP(jsxtnm337(jsxtnm332))
                  jsxtnm339 = jsxtnm338
                  XATS000_patck(true)
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
                  // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1597(line=55,offs=3)--1608(line=55,offs=14))
                  // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                  // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                  // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                  let jsxtnm391 = function (arg1) { // timp: nint_forall(958)
                    let jsxtnm345 = arg1
                    // I1CMP:start
                    let jsxtnm390 // let
                    { // let
                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                      // I1FUNDCL
                      function loop_2862(arg1, arg2)
                      { // fun
                        let jsxtnm346 = arg1
                        let jsxtnm347 = arg2
                        // I1CMP:start
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                        // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                        // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                        // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                        let jsxtnm354 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                          let jsxtnm348 = arg1
                          let jsxtnm349 = arg2
                          // I1CMP:start
                          let jsxtnm353 // let
                          { // let
                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                            // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                            // XATS2JS_sint_gte$sint_2399
                              // FJARGdarg($list(I1BNDcons(I1TNM(350);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(350))))),I1BNDcons(I1TNM(351);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(351)))))))
                              // I1CMP:start
                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                            let jsxtnm352 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm348, jsxtnm349))
                            jsxtnm353 = jsxtnm352
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(353))
                          return jsxtnm353
                        } // endtimp(sint_gte$sint(931))
                        let jsxtnm355 = XATSDAPP(jsxtnm354(jsxtnm347, jsxtnm346))
                        let jsxtnm388 // ift
                        if (jsxtnm355) // ift
                        {
                          jsxtnm388 = XATSBOOL(true)
                        } else {
                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                          // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                          // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
                          // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                          let jsxtnm376 = function (arg1) { // timp: forall$test(47)
                            let jsxtnm356 = arg1
                            // I1CMP:start
                            let jsxtnm375 // let
                            { // let
                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1728(line=69,offs=1)--1768(line=70,offs=32)))
                              // I1VALDCL
                              let jsxtnm365
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1743(line=70,offs=7)--1758(line=70,offs=22))
                              // I0Etapq(I0Ecst(strn_get$at$raw(2330)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4484(line=273,offs=1)--4499(line=273,offs=16))));$list(T2JAG($list())))
                              // T1IMPallx(strn_get$at$raw(2330);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2200(line=104,offs=1)--2376(line=116,offs=2)))
                              // T1IMPallx(strn_get$at$raw(2330)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_get$at$raw(2330);$list()))))
                              let jsxtnm363 = function (arg1, arg2) { // timp: strn_get$at$raw(2330)
                                let jsxtnm357 = arg1
                                let jsxtnm358 = arg2
                                // I1CMP:start
                                let jsxtnm362 // let
                                { // let
                                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2298(line=112,offs=1)--2374(line=115,offs=41)))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2306(line=113,offs=1)--2374(line=115,offs=41))
                                  // I1FUNDCL: XATS000_strn_get$at$raw(3298)
                                  // XATS000_strn_get$at$raw_2309
                                    // FJARGdarg($list(I1BNDcons(I1TNM(359);I0Pvar(cs(3299));$list(@(cs(3299),I1Vtnm(I1TNM(359))))),I1BNDcons(I1TNM(360);I0Pvar(i0(3300));$list(@(i0(3300),I1Vtnm(I1TNM(360)))))))
                                    // I1CMP:start
                                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS000_strn_get$at$raw);G1Nlist($list()))// I1CMP:return
                                  let jsxtnm361 = XATSDAPP(XATS000_strn_get$at$raw(jsxtnm357, jsxtnm358))
                                  jsxtnm362 = jsxtnm361
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(362))
                                return jsxtnm362
                              } // endtimp(strn_get$at$raw(2330))
                              let jsxtnm364 = XATSDAPP(jsxtnm363(jsxtnm332, jsxtnm356))
                              jsxtnm365 = jsxtnm364
                              XATS000_patck(true)
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1697(line=66,offs=3)--1708(line=66,offs=14))
                              // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
                              // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                              // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))))
                              let jsxtnm373 = function (arg1) { // timp: forall$test(47)
                                let jsxtnm366 = arg1
                                // I1CMP:start
                                let jsxtnm372 // let
                                { // let
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                                  // I1VALDCL
                                  let jsxtnm371
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                                  // I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                                  // T1IMPallx(foritm$work(51);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
                                  // T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz)))))))
                                  let jsxtnm369 = function (arg1) { // timp: foritm$work(51)
                                    let jsxtnm367 = arg1
                                    // I1CMP:start
                                    let jsxtnm368 = XATSDAPP(jsxtnm324(jsxtnm367))
                                    // I1CMP:return:I1Vtnm(I1TNM(368))
                                    return jsxtnm368
                                  } // endtimp(foritm$work(51))
                                  let jsxtnm370 = XATSDAPP(jsxtnm369(jsxtnm366))
                                  jsxtnm371 = jsxtnm370
                                  XATS000_patck(true)
                                  jsxtnm372 = XATSBOOL(true)
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(372))
                                return jsxtnm372
                              } // endtimp(forall$test(47))
                              let jsxtnm374 = XATSDAPP(jsxtnm373(jsxtnm365))
                              jsxtnm375 = jsxtnm374
                            } // endlet
                            // I1CMP:return:I1Vtnm(I1TNM(375))
                            return jsxtnm375
                          } // endtimp(forall$test(47))
                          let jsxtnm377 = XATSDAPP(jsxtnm376(jsxtnm347))
                          let jsxtnm387 // ift
                          if (jsxtnm377) // ift
                          {
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                            let jsxtnm384 = function (arg1, arg2) { // timp: sint_add$sint(936)
                              let jsxtnm378 = arg1
                              let jsxtnm379 = arg2
                              // I1CMP:start
                              let jsxtnm383 // let
                              { // let
                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                // XATS2JS_sint_add$sint_2778
                                  // FJARGdarg($list(I1BNDcons(I1TNM(380);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(380))))),I1BNDcons(I1TNM(381);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(381)))))))
                                  // I1CMP:start
                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                let jsxtnm382 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm378, jsxtnm379))
                                jsxtnm383 = jsxtnm382
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(383))
                              return jsxtnm383
                            } // endtimp(sint_add$sint(936))
                            let jsxtnm385 = XATSDAPP(jsxtnm384(jsxtnm347, XATSINT1(1)))
                            let jsxtnm386 = XATSDAPP(loop_2862(jsxtnm346, jsxtnm385))
                            jsxtnm387 = jsxtnm386
                          } else {
                            jsxtnm387 = XATSBOOL(false)
                          } // end(if)
                          jsxtnm388 = jsxtnm387
                        } // end(if)
                        // I1CMP:return:I1Vtnm(I1TNM(388))
                        return jsxtnm388
                      } // endfun(loop_2862)
                      let jsxtnm389 = XATSDAPP(loop_2862(jsxtnm345, XATSINT1(0)))
                      jsxtnm390 = jsxtnm389
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(390))
                    return jsxtnm390
                  } // endtimp(nint_forall(958))
                  let jsxtnm392 = XATSDAPP(jsxtnm391(jsxtnm339))
                  jsxtnm393 = jsxtnm392
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(393))
                return jsxtnm393
              } // endtimp(strn_forall(1074))
              jsxtnm395 = jsxtnm394
              let jsxtnm396 = XATSDAPP(jsxtnm395(jsxtnm327))
              jsxtnm397 = jsxtnm396
              XATS000_patck(true)
              jsxtnm398 = XATSVOID
            } // endlet
            jsxtnm399 = jsxtnm398
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(399))
          return jsxtnm399
        } // endtimp(gseq_foritm(402))
        jsxtnm401 = jsxtnm400
        let jsxtnm402 = XATSDAPP(jsxtnm401(jsxtnm323))
        jsxtnm403 = jsxtnm402
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(403))
      return jsxtnm403
    } // endtimp(strn_foritm$f1un(1086))
    let jsxtnm405 = XATSDAPP(jsxtnm404(jsxtnm315, jsxtnm322))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(3511(line=197,offs=20)--3517(line=197,offs=26))
    // I0Etapq(I0Ecst(strn_foritm$f1un(1086)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3510(line=153,offs=1)--3526(line=153,offs=17))));$list(T2JAG($list())))
    // T1IMPallx(strn_foritm$f1un(1086);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3971(line=237,offs=1)--4096(line=246,offs=2)))
    // T1IMPallx(strn_foritm$f1un(1086)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm$f1un(1086);$list()))))
    let jsxtnm487 = function (arg1, arg2) { // timp: strn_foritm$f1un(1086)
      let jsxtnm406 = arg1
      let jsxtnm407 = arg2
      // I1CMP:start
      let jsxtnm486 // let
      { // let
        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
        // I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz))))):timp
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4026(line=242,offs=3)--4037(line=242,offs=14))
        // I0Etapq(I0Ecst(strn_foritm(1082)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(3113(line=132,offs=1)--3124(line=132,offs=12))));$list(T2JAG($list())))
        // T1IMPallx(strn_foritm(1082);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3914(line=233,offs=1)--3970(line=236,offs=24)))
        // T1IMPallx(strn_foritm(1082)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_foritm(1082);$list()))))
        let jsxtnm484
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(3947(line=236,offs=1)--3958(line=236,offs=12))
        // I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
        // T1IMPallx(gseq_foritm(402);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
        // T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
        let jsxtnm483 = function (arg1) { // timp: gseq_foritm(402)
          let jsxtnm410 = arg1
          // I1CMP:start
          let jsxtnm482 // let
          { // let
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
            // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
            let jsxtnm481 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
              // I1VALDCL
              let jsxtnm480
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
              // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
              // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1976(line=85,offs=1)--2025(line=87,offs=29)))
              // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(strn)),@(x0[1168],T2Pcst(cgtz)))))))
              let jsxtnm478
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(2012(line=87,offs=16)--2023(line=87,offs=27))
              // I0Etapq(I0Ecst(strn_forall(1074)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn001.sats)@(2101(line=80,offs=1)--2112(line=80,offs=12))));$list(T2JAG($list())))
              // T1IMPallx(strn_forall(1074);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1556(line=51,offs=1)--1772(line=72,offs=2)))
              // T1IMPallx(strn_forall(1074)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_forall(1074);$list()))))
              let jsxtnm477 = function (arg1) { // timp: strn_forall(1074)
                let jsxtnm415 = arg1
                // I1CMP:start
                let jsxtnm476 // let
                { // let
                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1627(line=59,offs=1)--1658(line=61,offs=21)))
                  // I1VALDCL
                  let jsxtnm422
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1640(line=61,offs=3)--1651(line=61,offs=14))
                  // I0Etapq(I0Ecst(strn_length(1041)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2709(line=131,offs=1)--2720(line=131,offs=12))));$list(T2JAG($list())))
                  // T1IMPallx(strn_length(1041);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(1610(line=57,offs=1)--1756(line=69,offs=2)))
                  // T1IMPallx(strn_length(1041)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_length(1041);$list()))))
                  let jsxtnm420 = function (arg1) { // timp: strn_length(1041)
                    let jsxtnm416 = arg1
                    // I1CMP:start
                    let jsxtnm419 // let
                    { // let
                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(1692(line=65,offs=1)--1754(line=68,offs=31)))
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(1700(line=66,offs=1)--1754(line=68,offs=31))
                      // I1FUNDCL: XATS2JS_strn_length(5074)
                      // XATS2JS_strn_length_1703
                        // FJARGdarg($list(I1BNDcons(I1TNM(417);I0Pvar(cs(5075));$list(@(cs(5075),I1Vtnm(I1TNM(417)))))))
                        // I1CMP:start
                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_length);G1Nlist($list()))// I1CMP:return
                      let jsxtnm418 = XATSDAPP(XATS2JS_strn_length(jsxtnm416))
                      jsxtnm419 = jsxtnm418
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(419))
                    return jsxtnm419
                  } // endtimp(strn_length(1041))
                  let jsxtnm421 = XATSDAPP(jsxtnm420(jsxtnm415))
                  jsxtnm422 = jsxtnm421
                  XATS000_patck(true)
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
                  // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1597(line=55,offs=3)--1608(line=55,offs=14))
                  // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                  // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                  // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                  let jsxtnm474 = function (arg1) { // timp: nint_forall(958)
                    let jsxtnm428 = arg1
                    // I1CMP:start
                    let jsxtnm473 // let
                    { // let
                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                      // I1FUNDCL
                      function loop_2862(arg1, arg2)
                      { // fun
                        let jsxtnm429 = arg1
                        let jsxtnm430 = arg2
                        // I1CMP:start
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                        // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                        // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                        // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                        let jsxtnm437 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                          let jsxtnm431 = arg1
                          let jsxtnm432 = arg2
                          // I1CMP:start
                          let jsxtnm436 // let
                          { // let
                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                            // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                            // XATS2JS_sint_gte$sint_2399
                              // FJARGdarg($list(I1BNDcons(I1TNM(433);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(433))))),I1BNDcons(I1TNM(434);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(434)))))))
                              // I1CMP:start
                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                            let jsxtnm435 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm431, jsxtnm432))
                            jsxtnm436 = jsxtnm435
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(436))
                          return jsxtnm436
                        } // endtimp(sint_gte$sint(931))
                        let jsxtnm438 = XATSDAPP(jsxtnm437(jsxtnm430, jsxtnm429))
                        let jsxtnm471 // ift
                        if (jsxtnm438) // ift
                        {
                          jsxtnm471 = XATSBOOL(true)
                        } else {
                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                          // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                          // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1662(line=63,offs=1)--1770(line=71,offs=2)))
                          // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                          let jsxtnm459 = function (arg1) { // timp: forall$test(47)
                            let jsxtnm439 = arg1
                            // I1CMP:start
                            let jsxtnm458 // let
                            { // let
                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1728(line=69,offs=1)--1768(line=70,offs=32)))
                              // I1VALDCL
                              let jsxtnm448
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1743(line=70,offs=7)--1758(line=70,offs=22))
                              // I0Etapq(I0Ecst(strn_get$at$raw(2330)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4484(line=273,offs=1)--4499(line=273,offs=16))));$list(T2JAG($list())))
                              // T1IMPallx(strn_get$at$raw(2330);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2200(line=104,offs=1)--2376(line=116,offs=2)))
                              // T1IMPallx(strn_get$at$raw(2330)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_get$at$raw(2330);$list()))))
                              let jsxtnm446 = function (arg1, arg2) { // timp: strn_get$at$raw(2330)
                                let jsxtnm440 = arg1
                                let jsxtnm441 = arg2
                                // I1CMP:start
                                let jsxtnm445 // let
                                { // let
                                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2298(line=112,offs=1)--2374(line=115,offs=41)))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/strn000.dats)@(2306(line=113,offs=1)--2374(line=115,offs=41))
                                  // I1FUNDCL: XATS000_strn_get$at$raw(3298)
                                  // XATS000_strn_get$at$raw_2309
                                    // FJARGdarg($list(I1BNDcons(I1TNM(442);I0Pvar(cs(3299));$list(@(cs(3299),I1Vtnm(I1TNM(442))))),I1BNDcons(I1TNM(443);I0Pvar(i0(3300));$list(@(i0(3300),I1Vtnm(I1TNM(443)))))))
                                    // I1CMP:start
                                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS000_strn_get$at$raw);G1Nlist($list()))// I1CMP:return
                                  let jsxtnm444 = XATSDAPP(XATS000_strn_get$at$raw(jsxtnm440, jsxtnm441))
                                  jsxtnm445 = jsxtnm444
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(445))
                                return jsxtnm445
                              } // endtimp(strn_get$at$raw(2330))
                              let jsxtnm447 = XATSDAPP(jsxtnm446(jsxtnm415, jsxtnm439))
                              jsxtnm448 = jsxtnm447
                              XATS000_patck(true)
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(1697(line=66,offs=3)--1708(line=66,offs=14))
                              // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))
                              // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                              // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(char_type);$list(T2Pnone0()))))))))
                              let jsxtnm456 = function (arg1) { // timp: forall$test(47)
                                let jsxtnm449 = arg1
                                // I1CMP:start
                                let jsxtnm455 // let
                                { // let
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                                  // I1VALDCL
                                  let jsxtnm454
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                                  // I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                                  // T1IMPallx(foritm$work(51);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn001.dats)@(4053(line=244,offs=1)--4094(line=245,offs=33)))
                                  // T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(char_type);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(cgtz)))))))
                                  let jsxtnm452 = function (arg1) { // timp: foritm$work(51)
                                    let jsxtnm450 = arg1
                                    // I1CMP:start
                                    let jsxtnm451 = XATSDAPP(jsxtnm407(jsxtnm450))
                                    // I1CMP:return:I1Vtnm(I1TNM(451))
                                    return jsxtnm451
                                  } // endtimp(foritm$work(51))
                                  let jsxtnm453 = XATSDAPP(jsxtnm452(jsxtnm449))
                                  jsxtnm454 = jsxtnm453
                                  XATS000_patck(true)
                                  jsxtnm455 = XATSBOOL(true)
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(455))
                                return jsxtnm455
                              } // endtimp(forall$test(47))
                              let jsxtnm457 = XATSDAPP(jsxtnm456(jsxtnm448))
                              jsxtnm458 = jsxtnm457
                            } // endlet
                            // I1CMP:return:I1Vtnm(I1TNM(458))
                            return jsxtnm458
                          } // endtimp(forall$test(47))
                          let jsxtnm460 = XATSDAPP(jsxtnm459(jsxtnm430))
                          let jsxtnm470 // ift
                          if (jsxtnm460) // ift
                          {
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                            let jsxtnm467 = function (arg1, arg2) { // timp: sint_add$sint(936)
                              let jsxtnm461 = arg1
                              let jsxtnm462 = arg2
                              // I1CMP:start
                              let jsxtnm466 // let
                              { // let
                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                // XATS2JS_sint_add$sint_2778
                                  // FJARGdarg($list(I1BNDcons(I1TNM(463);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(463))))),I1BNDcons(I1TNM(464);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(464)))))))
                                  // I1CMP:start
                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                let jsxtnm465 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm461, jsxtnm462))
                                jsxtnm466 = jsxtnm465
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(466))
                              return jsxtnm466
                            } // endtimp(sint_add$sint(936))
                            let jsxtnm468 = XATSDAPP(jsxtnm467(jsxtnm430, XATSINT1(1)))
                            let jsxtnm469 = XATSDAPP(loop_2862(jsxtnm429, jsxtnm468))
                            jsxtnm470 = jsxtnm469
                          } else {
                            jsxtnm470 = XATSBOOL(false)
                          } // end(if)
                          jsxtnm471 = jsxtnm470
                        } // end(if)
                        // I1CMP:return:I1Vtnm(I1TNM(471))
                        return jsxtnm471
                      } // endfun(loop_2862)
                      let jsxtnm472 = XATSDAPP(loop_2862(jsxtnm428, XATSINT1(0)))
                      jsxtnm473 = jsxtnm472
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(473))
                    return jsxtnm473
                  } // endtimp(nint_forall(958))
                  let jsxtnm475 = XATSDAPP(jsxtnm474(jsxtnm422))
                  jsxtnm476 = jsxtnm475
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(476))
                return jsxtnm476
              } // endtimp(strn_forall(1074))
              jsxtnm478 = jsxtnm477
              let jsxtnm479 = XATSDAPP(jsxtnm478(jsxtnm410))
              jsxtnm480 = jsxtnm479
              XATS000_patck(true)
              jsxtnm481 = XATSVOID
            } // endlet
            jsxtnm482 = jsxtnm481
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(482))
          return jsxtnm482
        } // endtimp(gseq_foritm(402))
        jsxtnm484 = jsxtnm483
        let jsxtnm485 = XATSDAPP(jsxtnm484(jsxtnm406))
        jsxtnm486 = jsxtnm485
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(486))
      return jsxtnm486
    } // endtimp(strn_foritm$f1un(1086))
    let jsxtnm488 = XATSDAPP(jsxtnm487(jsxtnm316, jsxtnm322))
    // I1CMP:return:I1Vtnm(I1TNM(488))
    return jsxtnm488
  } // endfun(lam0)
  let jsxtnm490 = XATSDAPP(jsxtnm321(jsxtnm489))
  // I1CMP:return:I1Vtnm(I1TNM(490))
  return jsxtnm490
} // endtimp(strn_append(1063))
let jsxtnm492 = XATSDAPP(jsxtnm314(jsxtnm491, XATSSTRN("strn_append")))
jsxtnm493 = jsxtnm492
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(667(line=45,offs=1)--704(line=45,offs=38)))
// I1VALDCL
let jsxtnm495
let jsxtnm494 = XATSDAPP(jsxtnm493(XATSSTRN("a"), XATSSTRN("bc")))
jsxtnm495 = jsxtnm494
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test05_gdbg000.dats)@(705(line=46,offs=1)--742(line=46,offs=38)))
// I1VALDCL
let jsxtnm497
let jsxtnm496 = XATSDAPP(jsxtnm493(XATSSTRN("x"), XATSSTRN("yz")))
jsxtnm497 = jsxtnm496
XATS000_patck(true)
// LCSRCsome1(test05_gdbg000.dats)@(1005(line=54,offs=1)--1005(line=54,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(test05_gdbg000.dats)@(1005(line=54,offs=1)--1005(line=54,offs=1));D3Cnone0()))
