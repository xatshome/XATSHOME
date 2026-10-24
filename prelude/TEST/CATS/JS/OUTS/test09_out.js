// Sun Aug 16 12:16:43 PM EDT 2026
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
[ATS3-XANADU/srcgen2/xats2js/srcgen1/xshared/runtime/srcgen2_precats.js]
*/
////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////
// Fri Jan 16 11:31:07 PM EST 2026
// LCSRCsome1(precats.dats)@(1291(line=30,offs=1)--1332(line=31,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(0;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(UN);G1Estr(T_STRN1_clsd("prelude/SATS/unsfx00.sats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats));...)))
// I1Dextern(LCSRCsome1(precats.dats)@(1958(line=80,offs=1)--2028(line=85,offs=29)))
// LCSRCsome1(precats.dats)@(1966(line=81,offs=1)--2028(line=85,offs=29))
// I1FUNDCL
// XATS2JS_optn_nilq_1969
  // FJARGdarg($list(I1BNDcons(I1TNM(1);I0Pvar(xs(3));$list(@(xs(3),I1Vtnm(I1TNM(1)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_nilq);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(2029(line=86,offs=1)--2118(line=90,offs=43)))
let XATS2JS_optn_nilq = function (arg1) { // impl
  let jsxtnm2 = arg1
  // I1CMP:start
  let jsxtnm5 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(3);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
    if (XATS000_ctgeq(jsxtnm2, XATSCTAG("optn_nil",0))) { // gpt
      let jsxtnm3 = jsxtnm2
      jsxtnm5 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(4);I0Pdap1(I0Pcon(optn_cons(5)));$list()))
    if (XATS000_ctgeq(jsxtnm2, XATSCTAG("optn_cons",1))) { // gpt
      let jsxtnm4 = jsxtnm2
      jsxtnm5 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm5
  return jsxtnm5
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(2122(line=92,offs=1)--2193(line=97,offs=29)))
// LCSRCsome1(precats.dats)@(2130(line=93,offs=1)--2193(line=97,offs=29))
// I1FUNDCL
// XATS2JS_optn_consq_2133
  // FJARGdarg($list(I1BNDcons(I1TNM(6);I0Pvar(xs(6));$list(@(xs(6),I1Vtnm(I1TNM(6)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_consq);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(2194(line=98,offs=1)--2286(line=102,offs=45)))
let XATS2JS_optn_consq = function (arg1) { // impl
  let jsxtnm7 = arg1
  // I1CMP:start
  let jsxtnm10 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(8);I0Pdapp(I0Pcon(optn_nil(4));$list());$list()))
    if (XATS000_ctgeq(jsxtnm7, XATSCTAG("optn_nil",0))) { // gpt
      let jsxtnm8 = jsxtnm7
      jsxtnm10 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(9);I0Pdap1(I0Pcon(optn_cons(5)));$list()))
    if (XATS000_ctgeq(jsxtnm7, XATSCTAG("optn_cons",1))) { // gpt
      let jsxtnm9 = jsxtnm7
      jsxtnm10 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm10
  return jsxtnm10
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(2313(line=106,offs=1)--2386(line=111,offs=28)))
// LCSRCsome1(precats.dats)@(2321(line=107,offs=1)--2386(line=111,offs=28))
// I1FUNDCL
// XATS2JS_optn_head$raw_2324
  // FJARGdarg($list(I1BNDcons(I1TNM(11);I0Pvar(xs(9));$list(@(xs(9),I1Vtnm(I1TNM(11)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_head$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(2387(line=112,offs=1)--2460(line=115,offs=35)))
let XATS2JS_optn_head$raw = function (arg1) { // impl
  let jsxtnm12 = arg1
  // I1CMP:start
  let jsxtnm14 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(13);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(11))));$list(@(x0(11),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(13));0)))))
    if (XATS000_ctgeq(jsxtnm12, XATSCTAG("optn_cons",1))) { // gpt
      let jsxtnm13 = jsxtnm12
      jsxtnm14 = XATSP1CN("optn_cons", jsxtnm13[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm14
  return jsxtnm14
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(2464(line=117,offs=1)--2539(line=122,offs=28)))
// LCSRCsome1(precats.dats)@(2472(line=118,offs=1)--2539(line=122,offs=28))
// I1FUNDCL
// XATS2JS_optn_uncons$raw_2475
  // FJARGdarg($list(I1BNDcons(I1TNM(15);I0Pvar(xs(13));$list(@(xs(13),I1Vtnm(I1TNM(15)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_uncons$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(2540(line=123,offs=1)--2615(line=126,offs=35)))
let XATS2JS_optn_uncons$raw = function (arg1) { // impl
  let jsxtnm16 = arg1
  // I1CMP:start
  let jsxtnm18 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(17);I0Pdapp(I0Pcon(optn_cons(5));$list(I0Pvar(x0(15))));$list(@(x0(15),I1Vp1cn(I0Pcon(optn_cons(5));I1Vtnm(I1TNM(17));0)))))
    if (XATS000_ctgeq(jsxtnm16, XATSCTAG("optn_cons",1))) { // gpt
      let jsxtnm17 = jsxtnm16
      jsxtnm18 = XATSP1CN("optn_cons", jsxtnm17[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm18
  return jsxtnm18
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(3007(line=159,offs=1)--3077(line=164,offs=29)))
// LCSRCsome1(precats.dats)@(3015(line=160,offs=1)--3077(line=164,offs=29))
// I1FUNDCL
// XATS2JS_list_nilq_3018
  // FJARGdarg($list(I1BNDcons(I1TNM(19);I0Pvar(xs(17));$list(@(xs(17),I1Vtnm(I1TNM(19)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_nilq);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(3078(line=165,offs=1)--3167(line=169,offs=43)))
let XATS2JS_list_nilq = function (arg1) { // impl
  let jsxtnm20 = arg1
  // I1CMP:start
  let jsxtnm23 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(21);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
    if (XATS000_ctgeq(jsxtnm20, XATSCTAG("list_nil",0))) { // gpt
      let jsxtnm21 = jsxtnm20
      jsxtnm23 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(22);I0Pdap1(I0Pcon(list_cons(9)));$list()))
    if (XATS000_ctgeq(jsxtnm20, XATSCTAG("list_cons",1))) { // gpt
      let jsxtnm22 = jsxtnm20
      jsxtnm23 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm23
  return jsxtnm23
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(3171(line=171,offs=1)--3242(line=176,offs=29)))
// LCSRCsome1(precats.dats)@(3179(line=172,offs=1)--3242(line=176,offs=29))
// I1FUNDCL
// XATS2JS_list_consq_3182
  // FJARGdarg($list(I1BNDcons(I1TNM(24);I0Pvar(xs(20));$list(@(xs(20),I1Vtnm(I1TNM(24)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_consq);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(3243(line=177,offs=1)--3335(line=181,offs=45)))
let XATS2JS_list_consq = function (arg1) { // impl
  let jsxtnm25 = arg1
  // I1CMP:start
  let jsxtnm28 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(26);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
    if (XATS000_ctgeq(jsxtnm25, XATSCTAG("list_nil",0))) { // gpt
      let jsxtnm26 = jsxtnm25
      jsxtnm28 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(27);I0Pdap1(I0Pcon(list_cons(9)));$list()))
    if (XATS000_ctgeq(jsxtnm25, XATSCTAG("list_cons",1))) { // gpt
      let jsxtnm27 = jsxtnm25
      jsxtnm28 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm28
  return jsxtnm28
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(3362(line=185,offs=1)--3435(line=190,offs=28)))
// LCSRCsome1(precats.dats)@(3370(line=186,offs=1)--3435(line=190,offs=28))
// I1FUNDCL
// XATS2JS_list_head$raw_3373
  // FJARGdarg($list(I1BNDcons(I1TNM(29);I0Pvar(xs(23));$list(@(xs(23),I1Vtnm(I1TNM(29)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_head$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(3436(line=191,offs=1)--3513(line=194,offs=39)))
let XATS2JS_list_head$raw = function (arg1) { // impl
  let jsxtnm30 = arg1
  // I1CMP:start
  let jsxtnm32 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(31);I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(25)),I0Pvar(xs(26))));$list(@(x1(25),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(31));0)),@(xs(26),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(31));1)))))
    if (XATS000_ctgeq(jsxtnm30, XATSCTAG("list_cons",1))) { // gpt
      let jsxtnm31 = jsxtnm30
      jsxtnm32 = XATSP1CN("list_cons", jsxtnm31[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm32
  return jsxtnm32
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(3560(line=199,offs=1)--3638(line=204,offs=32)))
// LCSRCsome1(precats.dats)@(3568(line=200,offs=1)--3638(line=204,offs=32))
// I1FUNDCL
// XATS2JS_lazy_make_f0un_3571
  // FJARGdarg($list(I1BNDcons(I1TNM(33);I0Pvar(f0(28));$list(@(f0(28),I1Vtnm(I1TNM(33)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_lazy_make_f0un);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(3639(line=205,offs=1)--3688(line=206,offs=41)))
let XATS2JS_lazy_make_f0un = function (arg1) { // impl
  let jsxtnm34 = arg1
  // I1CMP:start
  let jsxtnm36 = XATS000_l0azy(function () { // l0azy
    // I1CMP:start
    let jsxtnm35 = XATSDAPP(jsxtnm34())
    // I1CMP:return:jsxtnm35
    return jsxtnm35
  }) // endfun(l0azy)
  // I1CMP:return:jsxtnm36
  return jsxtnm36
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(3735(line=211,offs=1)--3805(line=215,offs=32)))
// LCSRCsome1(precats.dats)@(3743(line=212,offs=1)--3805(line=215,offs=32))
// I1FUNDCL
// XATS2JS_strmcon_nil_3746
  // FJARGdarg($list())
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_nil);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(3806(line=216,offs=1)--3852(line=217,offs=38)))
let XATS2JS_strmcon_nil = function () { // impl
  // I1CMP:start
  let jsxtnm37 = XATSCAPP("strmcon_nil", [0])
  // I1CMP:return:jsxtnm37
  return jsxtnm37
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(3856(line=219,offs=1)--3946(line=224,offs=38)))
// LCSRCsome1(precats.dats)@(3864(line=220,offs=1)--3946(line=224,offs=38))
// I1FUNDCL
// XATS2JS_strmcon_cons_3867
  // FJARGdarg($list(I1BNDcons(I1TNM(38);I0Pvar(x1(32));$list(@(x1(32),I1Vtnm(I1TNM(38))))),I1BNDcons(I1TNM(39);I0Pvar(xs(33));$list(@(xs(33),I1Vtnm(I1TNM(39)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_cons);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(3947(line=225,offs=1)--4005(line=226,offs=50)))
let XATS2JS_strmcon_cons = function (arg1, arg2) { // impl
  let jsxtnm40 = arg1
  let jsxtnm41 = arg2
  // I1CMP:start
  let jsxtnm42 = XATSCAPP("strmcon_cons", [1, jsxtnm40, jsxtnm41])
  // I1CMP:return:jsxtnm42
  return jsxtnm42
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(4009(line=228,offs=1)--4099(line=233,offs=38)))
// LCSRCsome1(precats.dats)@(4017(line=229,offs=1)--4099(line=233,offs=38))
// I1FUNDCL
// XATS2JS_strxcon_cons_4020
  // FJARGdarg($list(I1BNDcons(I1TNM(43);I0Pvar(x1(37));$list(@(x1(37),I1Vtnm(I1TNM(43))))),I1BNDcons(I1TNM(44);I0Pvar(xs(38));$list(@(xs(38),I1Vtnm(I1TNM(44)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strxcon_cons);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(4100(line=234,offs=1)--4158(line=235,offs=50)))
let XATS2JS_strxcon_cons = function (arg1, arg2) { // impl
  let jsxtnm45 = arg1
  let jsxtnm46 = arg2
  // I1CMP:start
  let jsxtnm47 = XATSCAPP("strxcon_cons", [0, jsxtnm45, jsxtnm46])
  // I1CMP:return:jsxtnm47
  return jsxtnm47
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(4185(line=239,offs=1)--4261(line=244,offs=32)))
// LCSRCsome1(precats.dats)@(4193(line=240,offs=1)--4261(line=244,offs=32))
// I1FUNDCL
// XATS2JS_strmcon_nilq_4196
  // FJARGdarg($list(I1BNDcons(I1TNM(48);I0Pvar(xs(42));$list(@(xs(42),I1Vtnm(I1TNM(48)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_nilq);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(4262(line=245,offs=1)--4360(line=249,offs=49)))
let XATS2JS_strmcon_nilq = function (arg1) { // impl
  let jsxtnm49 = arg1
  // I1CMP:start
  let jsxtnm52 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(50);I0Pdapp(I0Pcon(strmcon_nil(12));$list());$list()))
    if (XATS000_ctgeq(jsxtnm49, XATSCTAG("strmcon_nil",0))) { // gpt
      let jsxtnm50 = jsxtnm49
      jsxtnm52 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(51);I0Pdap1(I0Pcon(strmcon_cons(13)));$list()))
    if (XATS000_ctgeq(jsxtnm49, XATSCTAG("strmcon_cons",1))) { // gpt
      let jsxtnm51 = jsxtnm49
      jsxtnm52 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm52
  return jsxtnm52
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(4364(line=251,offs=1)--4441(line=256,offs=32)))
// LCSRCsome1(precats.dats)@(4372(line=252,offs=1)--4441(line=256,offs=32))
// I1FUNDCL
// XATS2JS_strmcon_consq_4375
  // FJARGdarg($list(I1BNDcons(I1TNM(53);I0Pvar(xs(45));$list(@(xs(45),I1Vtnm(I1TNM(53)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_consq);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(4442(line=257,offs=1)--4543(line=261,offs=51)))
let XATS2JS_strmcon_consq = function (arg1) { // impl
  let jsxtnm54 = arg1
  // I1CMP:start
  let jsxtnm57 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(55);I0Pdapp(I0Pcon(strmcon_nil(12));$list());$list()))
    if (XATS000_ctgeq(jsxtnm54, XATSCTAG("strmcon_nil",0))) { // gpt
      let jsxtnm55 = jsxtnm54
      jsxtnm57 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(56);I0Pdap1(I0Pcon(strmcon_cons(13)));$list()))
    if (XATS000_ctgeq(jsxtnm54, XATSCTAG("strmcon_cons",1))) { // gpt
      let jsxtnm56 = jsxtnm54
      jsxtnm57 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm57
  return jsxtnm57
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(4570(line=265,offs=1)--4649(line=270,offs=31)))
// LCSRCsome1(precats.dats)@(4578(line=266,offs=1)--4649(line=270,offs=31))
// I1FUNDCL
// XATS2JS_strmcon_head$raw_4581
  // FJARGdarg($list(I1BNDcons(I1TNM(58);I0Pvar(xs(48));$list(@(xs(48),I1Vtnm(I1TNM(58)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_head$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(4650(line=271,offs=1)--4733(line=274,offs=42)))
let XATS2JS_strmcon_head$raw = function (arg1) { // impl
  let jsxtnm59 = arg1
  // I1CMP:start
  let jsxtnm61 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(60);I0Pdapp(I0Pcon(strmcon_cons(13));$list(I0Pvar(x1(50)),I0Pvar(xs(51))));$list(@(x1(50),I1Vp1cn(I0Pcon(strmcon_cons(13));I1Vtnm(I1TNM(60));0)),@(xs(51),I1Vp1cn(I0Pcon(strmcon_cons(13));I1Vtnm(I1TNM(60));1)))))
    if (XATS000_ctgeq(jsxtnm59, XATSCTAG("strmcon_cons",1))) { // gpt
      let jsxtnm60 = jsxtnm59
      jsxtnm61 = XATSP1CN("strmcon_cons", jsxtnm60[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm61
  return jsxtnm61
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(4737(line=276,offs=1)--4820(line=281,offs=35)))
// LCSRCsome1(precats.dats)@(4745(line=277,offs=1)--4820(line=281,offs=35))
// I1FUNDCL
// XATS2JS_strmcon_tail$raw_4748
  // FJARGdarg($list(I1BNDcons(I1TNM(62);I0Pvar(xs(53));$list(@(xs(53),I1Vtnm(I1TNM(62)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_tail$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(4821(line=282,offs=1)--4904(line=285,offs=42)))
let XATS2JS_strmcon_tail$raw = function (arg1) { // impl
  let jsxtnm63 = arg1
  // I1CMP:start
  let jsxtnm65 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(64);I0Pdapp(I0Pcon(strmcon_cons(13));$list(I0Pvar(x1(55)),I0Pvar(xs(56))));$list(@(x1(55),I1Vp1cn(I0Pcon(strmcon_cons(13));I1Vtnm(I1TNM(64));0)),@(xs(56),I1Vp1cn(I0Pcon(strmcon_cons(13));I1Vtnm(I1TNM(64));1)))))
    if (XATS000_ctgeq(jsxtnm63, XATSCTAG("strmcon_cons",1))) { // gpt
      let jsxtnm64 = jsxtnm63
      jsxtnm65 = XATSP1CN("strmcon_cons", jsxtnm64[1+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm65
  return jsxtnm65
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(4931(line=289,offs=1)--5032(line=297,offs=31)))
// LCSRCsome1(precats.dats)@(4939(line=290,offs=1)--5032(line=297,offs=31))
// I1FUNDCL
// XATS2JS_strxcon_head$raw_4964
  // FJARGdarg($list(I1BNDcons(I1TNM(66);I0Pvar(xs(58));$list(@(xs(58),I1Vtnm(I1TNM(66)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strxcon_head$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(5033(line=298,offs=1)--5116(line=301,offs=42)))
let XATS2JS_strxcon_head$raw = function (arg1) { // impl
  let jsxtnm67 = arg1
  // I1CMP:start
  let jsxtnm69 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(68);I0Pdapp(I0Pcon(strxcon_cons(14));$list(I0Pvar(x1(60)),I0Pvar(xs(61))));$list(@(x1(60),I1Vp1cn(I0Pcon(strxcon_cons(14));I1Vtnm(I1TNM(68));0)),@(xs(61),I1Vp1cn(I0Pcon(strxcon_cons(14));I1Vtnm(I1TNM(68));1)))))
    if (XATS000_ctgeq(jsxtnm67, XATSCTAG("strxcon_cons",0))) { // gpt
      let jsxtnm68 = jsxtnm67
      jsxtnm69 = XATSP1CN("strxcon_cons", jsxtnm68[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm69
  return jsxtnm69
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(5120(line=303,offs=1)--5225(line=311,offs=35)))
// LCSRCsome1(precats.dats)@(5128(line=304,offs=1)--5225(line=311,offs=35))
// I1FUNDCL
// XATS2JS_strxcon_tail$raw_5153
  // FJARGdarg($list(I1BNDcons(I1TNM(70);I0Pvar(xs(63));$list(@(xs(63),I1Vtnm(I1TNM(70)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strxcon_tail$raw);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(5226(line=312,offs=1)--5309(line=315,offs=42)))
let XATS2JS_strxcon_tail$raw = function (arg1) { // impl
  let jsxtnm71 = arg1
  // I1CMP:start
  let jsxtnm73 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(72);I0Pdapp(I0Pcon(strxcon_cons(14));$list(I0Pvar(x1(65)),I0Pvar(xs(66))));$list(@(x1(65),I1Vp1cn(I0Pcon(strxcon_cons(14));I1Vtnm(I1TNM(72));0)),@(xs(66),I1Vp1cn(I0Pcon(strxcon_cons(14));I1Vtnm(I1TNM(72));1)))))
    if (XATS000_ctgeq(jsxtnm71, XATSCTAG("strxcon_cons",0))) { // gpt
      let jsxtnm72 = jsxtnm71
      jsxtnm73 = XATSP1CN("strxcon_cons", jsxtnm72[1+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm73
  return jsxtnm73
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(5767(line=352,offs=1)--5845(line=357,offs=32)))
// LCSRCsome1(precats.dats)@(5775(line=353,offs=1)--5845(line=357,offs=32))
// I1FUNDCL
// XATS2JS_optn_vt_nilq1_5778
  // FJARGdarg($list(I1BNDcons(I1TNM(74);I0Pvar(xs(68));$list(@(xs(68),I1Vtnm(I1TNM(74)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_vt_nilq1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(5846(line=358,offs=1)--5942(line=362,offs=46)))
let XATS2JS_optn_vt_nilq1 = function (arg1) { // impl
  let jsxtnm75 = arg1
  // I1CMP:start
  let jsxtnm78 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(76);I0Pdapp(I0Pcon(optn_vt_nil(6));$list());$list()))
    if (XATS000_ctgeq(jsxtnm75, XATSCTAG("optn_vt_nil",0))) { // gpt
      let jsxtnm76 = jsxtnm75
      jsxtnm78 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(77);I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(70))));$list(@(x0(70),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(77));0)))))
    if (XATS000_ctgeq(jsxtnm75, XATSCTAG("optn_vt_cons",1))) { // gpt
      let jsxtnm77 = jsxtnm75
      jsxtnm78 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm78
  return jsxtnm78
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(5946(line=364,offs=1)--6025(line=369,offs=32)))
// LCSRCsome1(precats.dats)@(5954(line=365,offs=1)--6025(line=369,offs=32))
// I1FUNDCL
// XATS2JS_optn_vt_consq1_5957
  // FJARGdarg($list(I1BNDcons(I1TNM(79);I0Pvar(xs(72));$list(@(xs(72),I1Vtnm(I1TNM(79)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_vt_consq1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(6026(line=370,offs=1)--6125(line=374,offs=48)))
let XATS2JS_optn_vt_consq1 = function (arg1) { // impl
  let jsxtnm80 = arg1
  // I1CMP:start
  let jsxtnm83 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(81);I0Pdapp(I0Pcon(optn_vt_nil(6));$list());$list()))
    if (XATS000_ctgeq(jsxtnm80, XATSCTAG("optn_vt_nil",0))) { // gpt
      let jsxtnm81 = jsxtnm80
      jsxtnm83 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(82);I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(74))));$list(@(x0(74),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(82));0)))))
    if (XATS000_ctgeq(jsxtnm80, XATSCTAG("optn_vt_cons",1))) { // gpt
      let jsxtnm82 = jsxtnm80
      jsxtnm83 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm83
  return jsxtnm83
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(6152(line=378,offs=1)--6232(line=383,offs=31)))
// LCSRCsome1(precats.dats)@(6160(line=379,offs=1)--6232(line=383,offs=31))
// I1FUNDCL
// XATS2JS_optn_vt_head$raw0_6163
  // FJARGdarg($list(I1BNDcons(I1TNM(84);I0Pvar(xs(76));$list(@(xs(76),I1Vtnm(I1TNM(84)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_vt_head$raw0);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(6233(line=384,offs=1)--6314(line=387,offs=39)))
let XATS2JS_optn_vt_head$raw0 = function (arg1) { // impl
  let jsxtnm85 = arg1
  // I1CMP:start
  let jsxtnm87 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(86);I0Pfree(I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(78)))));$list(@(x0(78),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(86));0)))))
    if (XATS000_ctgeq(jsxtnm85, XATSCTAG("optn_vt_cons",1))) { // gpt
      let jsxtnm86 = jsxtnm85
      jsxtnm87 = XATSP1CN("optn_vt_cons", jsxtnm86[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm87
  return jsxtnm87
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(6318(line=389,offs=1)--6400(line=394,offs=31)))
// LCSRCsome1(precats.dats)@(6326(line=390,offs=1)--6400(line=394,offs=31))
// I1FUNDCL
// XATS2JS_optn_vt_uncons$raw0_6329
  // FJARGdarg($list(I1BNDcons(I1TNM(88);I0Pvar(xs(80));$list(@(xs(80),I1Vtnm(I1TNM(88)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_optn_vt_uncons$raw0);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(6401(line=395,offs=1)--6484(line=398,offs=39)))
let XATS2JS_optn_vt_uncons$raw0 = function (arg1) { // impl
  let jsxtnm89 = arg1
  // I1CMP:start
  let jsxtnm91 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(90);I0Pfree(I0Pdapp(I0Pcon(optn_vt_cons(7));$list(I0Pvar(x0(82)))));$list(@(x0(82),I1Vp1cn(I0Pcon(optn_vt_cons(7));I1Vtnm(I1TNM(90));0)))))
    if (XATS000_ctgeq(jsxtnm89, XATSCTAG("optn_vt_cons",1))) { // gpt
      let jsxtnm90 = jsxtnm89
      jsxtnm91 = XATSP1CN("optn_vt_cons", jsxtnm90[0+1])
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm91
  return jsxtnm91
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(6903(line=431,offs=1)--6981(line=436,offs=32)))
// LCSRCsome1(precats.dats)@(6911(line=432,offs=1)--6981(line=436,offs=32))
// I1FUNDCL
// XATS2JS_list_vt_nilq1_6914
  // FJARGdarg($list(I1BNDcons(I1TNM(92);I0Pvar(xs(84));$list(@(xs(84),I1Vtnm(I1TNM(92)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_vt_nilq1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(6982(line=437,offs=1)--7078(line=441,offs=46)))
let XATS2JS_list_vt_nilq1 = function (arg1) { // impl
  let jsxtnm93 = arg1
  // I1CMP:start
  let jsxtnm96 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(94);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
    if (XATS000_ctgeq(jsxtnm93, XATSCTAG("list_vt_nil",0))) { // gpt
      let jsxtnm94 = jsxtnm93
      jsxtnm96 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(95);I0Pdap1(I0Pcon(list_vt_cons(11)));$list()))
    if (XATS000_ctgeq(jsxtnm93, XATSCTAG("list_vt_cons",1))) { // gpt
      let jsxtnm95 = jsxtnm93
      jsxtnm96 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm96
  return jsxtnm96
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(7082(line=443,offs=1)--7161(line=448,offs=32)))
// LCSRCsome1(precats.dats)@(7090(line=444,offs=1)--7161(line=448,offs=32))
// I1FUNDCL
// XATS2JS_list_vt_consq1_7093
  // FJARGdarg($list(I1BNDcons(I1TNM(97);I0Pvar(xs(87));$list(@(xs(87),I1Vtnm(I1TNM(97)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_vt_consq1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(7162(line=449,offs=1)--7261(line=453,offs=48)))
let XATS2JS_list_vt_consq1 = function (arg1) { // impl
  let jsxtnm98 = arg1
  // I1CMP:start
  let jsxtnm101 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(99);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
    if (XATS000_ctgeq(jsxtnm98, XATSCTAG("list_vt_nil",0))) { // gpt
      let jsxtnm99 = jsxtnm98
      jsxtnm101 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(100);I0Pdap1(I0Pcon(list_vt_cons(11)));$list()))
    if (XATS000_ctgeq(jsxtnm98, XATSCTAG("list_vt_cons",1))) { // gpt
      let jsxtnm100 = jsxtnm98
      jsxtnm101 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm101
  return jsxtnm101
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(7288(line=457,offs=1)--7368(line=462,offs=31)))
// LCSRCsome1(precats.dats)@(7296(line=458,offs=1)--7368(line=462,offs=31))
// I1FUNDCL
// XATS2JS_list_vt_head$raw1_7299
  // FJARGdarg($list(I1BNDcons(I1TNM(102);I0Pvar(xs(90));$list(@(xs(90),I1Vtnm(I1TNM(102)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_vt_head$raw1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(7369(line=463,offs=1)--7509(line=472,offs=42)))
let XATS2JS_list_vt_head$raw1 = function (arg1) { // impl
  let jsxtnm103 = arg1
  // I1CMP:start
  let jsxtnm109 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(104);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(92)),I0Pvar(xs(93))));$list(@(x1(92),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(104));0)),@(xs(93),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(104));1)))))
    if (XATS000_ctgeq(jsxtnm103, XATSCTAG("list_vt_cons",1))) { // gpt
      let jsxtnm104 = jsxtnm103
      let jsxtnm108 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(precats.dats)@(7459(line=471,offs=1)--7484(line=472,offs=17)))
        // I1VALDCL
        let jsxtnm106
        let jsxtnm105 = XATSCAST("datacopy_1720", [XATSP1CN("list_vt_cons", jsxtnm104[0+1])])
        jsxtnm106 = jsxtnm105
        XATS000_patck(true)
        let jsxtnm107 = XATSCAST("enlinear_1756", [jsxtnm106])
        jsxtnm108 = jsxtnm107
      } // endlet
      jsxtnm109 = jsxtnm108
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm109
  return jsxtnm109
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(7513(line=474,offs=1)--7601(line=479,offs=38)))
// LCSRCsome1(precats.dats)@(7521(line=475,offs=1)--7601(line=479,offs=38))
// I1FUNDCL
// XATS2JS_list_vt_tail$raw0_7524
  // FJARGdarg($list(I1BNDcons(I1TNM(110);I0Pvar(xs(96));$list(@(xs(96),I1Vtnm(I1TNM(110)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_list_vt_tail$raw0);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(7602(line=480,offs=1)--7732(line=487,offs=43)))
let XATS2JS_list_vt_tail$raw0 = function (arg1) { // impl
  let jsxtnm111 = arg1
  // I1CMP:start
  let jsxtnm116 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(112);I0Pfree(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(98)),I0Pvar(xs(99)))));$list(@(x1(98),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(112));0)),@(xs(99),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(112));1)))))
    if (XATS000_ctgeq(jsxtnm111, XATSCTAG("list_vt_cons",1))) { // gpt
      let jsxtnm112 = jsxtnm111
      let jsxtnm115 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(precats.dats)@(7696(line=487,offs=7)--7721(line=487,offs=32)))
        // I1VALDCL
        let jsxtnm114
        let jsxtnm113 = XATSCAST("delinear_1667", [XATSP1CN("list_vt_cons", jsxtnm112[0+1])])
        jsxtnm114 = jsxtnm113
        XATS000_patck(true)
        jsxtnm115 = XATSP1CN("list_vt_cons", jsxtnm112[1+1])
      } // endlet
      jsxtnm116 = jsxtnm115
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm116
  return jsxtnm116
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(7779(line=492,offs=1)--7855(line=497,offs=31)))
// LCSRCsome1(precats.dats)@(7787(line=493,offs=1)--7855(line=497,offs=31))
// I1FUNDCL
// XATS2JS_lazy_vt_eval_7790
  // FJARGdarg($list(I1BNDcons(I1TNM(117);I0Pvar(lz(102));$list(@(lz(102),I1Vtnm(I1TNM(117)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_lazy_vt_eval);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(7856(line=498,offs=1)--7901(line=499,offs=37)))
let XATS2JS_lazy_vt_eval = function (arg1) { // impl
  let jsxtnm118 = arg1
  // I1CMP:start
  let jsxtnm119 = XATS000_dl1az(jsxtnm118)
  // I1CMP:return:jsxtnm119
  return jsxtnm119
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(7905(line=501,offs=1)--7982(line=506,offs=32)))
// LCSRCsome1(precats.dats)@(7913(line=502,offs=1)--7982(line=506,offs=32))
// I1FUNDCL
// XATS2JS_lazy_vt_free_7916
  // FJARGdarg($list(I1BNDcons(I1TNM(120);I0Pvar(lz(105));$list(@(lz(105),I1Vtnm(I1TNM(120)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_lazy_vt_free);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(7983(line=507,offs=1)--8028(line=508,offs=37)))
let XATS2JS_lazy_vt_free = function (arg1) { // impl
  let jsxtnm121 = arg1
  // I1CMP:start
  XATS000_free(jsxtnm121)
  // I1CMP:return:[]
  return []
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(8055(line=512,offs=1)--8139(line=517,offs=35)))
// LCSRCsome1(precats.dats)@(8063(line=513,offs=1)--8139(line=517,offs=35))
// I1FUNDCL
// XATS2JS_lazy_vt_make_f0un_8066
  // FJARGdarg($list(I1BNDcons(I1TNM(122);I0Pvar(f0(108));$list(@(f0(108),I1Vtnm(I1TNM(122)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_lazy_vt_make_f0un);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(8140(line=518,offs=1)--8193(line=519,offs=45)))
let XATS2JS_lazy_vt_make_f0un = function (arg1) { // impl
  let jsxtnm123 = arg1
  // I1CMP:start
  let jsxtnm125 = XATS000_l1azy(function (tlaz) { // l1azy
    // I1CMP:start
    let jsxtnm124 = XATSDAPP(jsxtnm123())
    // I1CMP:return:jsxtnm124
    return jsxtnm124
  }) // endfun(l1azy)
  // I1CMP:return:jsxtnm125
  return jsxtnm125
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(8240(line=524,offs=1)--8316(line=528,offs=35)))
// LCSRCsome1(precats.dats)@(8248(line=525,offs=1)--8316(line=528,offs=35))
// I1FUNDCL
// XATS2JS_strmcon_vt_nil_8251
  // FJARGdarg($list())
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_vt_nil);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(8317(line=529,offs=1)--8369(line=530,offs=44)))
let XATS2JS_strmcon_vt_nil = function () { // impl
  // I1CMP:start
  let jsxtnm126 = XATSCAPP("strmcon_vt_nil", [0])
  // I1CMP:return:jsxtnm126
  return jsxtnm126
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(8373(line=532,offs=1)--8472(line=537,offs=44)))
// LCSRCsome1(precats.dats)@(8381(line=533,offs=1)--8472(line=537,offs=44))
// I1FUNDCL
// XATS2JS_strmcon_vt_cons_8384
  // FJARGdarg($list(I1BNDcons(I1TNM(127);I0Pvar(x1(112));$list(@(x1(112),I1Vtnm(I1TNM(127))))),I1BNDcons(I1TNM(128);I0Pvar(xs(113));$list(@(xs(113),I1Vtnm(I1TNM(128)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_vt_cons);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(8473(line=538,offs=1)--8537(line=539,offs=56)))
let XATS2JS_strmcon_vt_cons = function (arg1, arg2) { // impl
  let jsxtnm129 = arg1
  let jsxtnm130 = arg2
  // I1CMP:start
  let jsxtnm131 = XATSCAPP("strmcon_vt_cons", [1, jsxtnm129, jsxtnm130])
  // I1CMP:return:jsxtnm131
  return jsxtnm131
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(8541(line=541,offs=1)--8640(line=546,offs=44)))
// LCSRCsome1(precats.dats)@(8549(line=542,offs=1)--8640(line=546,offs=44))
// I1FUNDCL
// XATS2JS_strxcon_vt_cons_8552
  // FJARGdarg($list(I1BNDcons(I1TNM(132);I0Pvar(x1(117));$list(@(x1(117),I1Vtnm(I1TNM(132))))),I1BNDcons(I1TNM(133);I0Pvar(xs(118));$list(@(xs(118),I1Vtnm(I1TNM(133)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strxcon_vt_cons);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(8641(line=547,offs=1)--8705(line=548,offs=56)))
let XATS2JS_strxcon_vt_cons = function (arg1, arg2) { // impl
  let jsxtnm134 = arg1
  let jsxtnm135 = arg2
  // I1CMP:start
  let jsxtnm136 = XATSCAPP("strxcon_vt_cons", [0, jsxtnm134, jsxtnm135])
  // I1CMP:return:jsxtnm136
  return jsxtnm136
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(8732(line=552,offs=1)--8816(line=557,offs=35)))
// LCSRCsome1(precats.dats)@(8740(line=553,offs=1)--8816(line=557,offs=35))
// I1FUNDCL
// XATS2JS_strmcon_vt_nilq1_8743
  // FJARGdarg($list(I1BNDcons(I1TNM(137);I0Pvar(xs(122));$list(@(xs(122),I1Vtnm(I1TNM(137)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_vt_nilq1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(8817(line=558,offs=1)--8921(line=562,offs=51)))
let XATS2JS_strmcon_vt_nilq1 = function (arg1) { // impl
  let jsxtnm138 = arg1
  // I1CMP:start
  let jsxtnm141 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(139);I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list());$list()))
    if (XATS000_ctgeq(jsxtnm138, XATSCTAG("strmcon_vt_nil",0))) { // gpt
      let jsxtnm139 = jsxtnm138
      jsxtnm141 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(140);I0Pdap1(I0Pcon(strmcon_vt_cons(16)));$list()))
    if (XATS000_ctgeq(jsxtnm138, XATSCTAG("strmcon_vt_cons",1))) { // gpt
      let jsxtnm140 = jsxtnm138
      jsxtnm141 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm141
  return jsxtnm141
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(8925(line=564,offs=1)--9010(line=569,offs=35)))
// LCSRCsome1(precats.dats)@(8933(line=565,offs=1)--9010(line=569,offs=35))
// I1FUNDCL
// XATS2JS_strmcon_vt_consq1_8936
  // FJARGdarg($list(I1BNDcons(I1TNM(142);I0Pvar(xs(125));$list(@(xs(125),I1Vtnm(I1TNM(142)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_vt_consq1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(9011(line=570,offs=1)--9118(line=574,offs=53)))
let XATS2JS_strmcon_vt_consq1 = function (arg1) { // impl
  let jsxtnm143 = arg1
  // I1CMP:start
  let jsxtnm146 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(144);I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list());$list()))
    if (XATS000_ctgeq(jsxtnm143, XATSCTAG("strmcon_vt_nil",0))) { // gpt
      let jsxtnm144 = jsxtnm143
      jsxtnm146 = XATSBOOL(false)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(145);I0Pdap1(I0Pcon(strmcon_vt_cons(16)));$list()))
    if (XATS000_ctgeq(jsxtnm143, XATSCTAG("strmcon_vt_cons",1))) { // gpt
      let jsxtnm145 = jsxtnm143
      jsxtnm146 = XATSBOOL(true)
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm146
  return jsxtnm146
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(9145(line=578,offs=1)--9232(line=583,offs=34)))
// LCSRCsome1(precats.dats)@(9153(line=579,offs=1)--9232(line=583,offs=34))
// I1FUNDCL
// XATS2JS_strmcon_vt_head$raw1_9156
  // FJARGdarg($list(I1BNDcons(I1TNM(147);I0Pvar(xs(128));$list(@(xs(128),I1Vtnm(I1TNM(147)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_vt_head$raw1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(9233(line=584,offs=1)--9382(line=593,offs=42)))
let XATS2JS_strmcon_vt_head$raw1 = function (arg1) { // impl
  let jsxtnm148 = arg1
  // I1CMP:start
  let jsxtnm154 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(149);I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(130)),I0Pvar(xs(131))));$list(@(x1(130),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(149));0)),@(xs(131),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(149));1)))))
    if (XATS000_ctgeq(jsxtnm148, XATSCTAG("strmcon_vt_cons",1))) { // gpt
      let jsxtnm149 = jsxtnm148
      let jsxtnm153 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(precats.dats)@(9332(line=592,offs=1)--9357(line=593,offs=17)))
        // I1VALDCL
        let jsxtnm151
        let jsxtnm150 = XATSCAST("datacopy_1720", [XATSP1CN("strmcon_vt_cons", jsxtnm149[0+1])])
        jsxtnm151 = jsxtnm150
        XATS000_patck(true)
        let jsxtnm152 = XATSCAST("enlinear_1756", [jsxtnm151])
        jsxtnm153 = jsxtnm152
      } // endlet
      jsxtnm154 = jsxtnm153
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm154
  return jsxtnm154
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(9386(line=595,offs=1)--9480(line=600,offs=41)))
// LCSRCsome1(precats.dats)@(9394(line=596,offs=1)--9480(line=600,offs=41))
// I1FUNDCL
// XATS2JS_strmcon_vt_tail$raw0_9397
  // FJARGdarg($list(I1BNDcons(I1TNM(155);I0Pvar(xs(134));$list(@(xs(134),I1Vtnm(I1TNM(155)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strmcon_vt_tail$raw0);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(9481(line=601,offs=1)--9620(line=608,offs=43)))
let XATS2JS_strmcon_vt_tail$raw0 = function (arg1) { // impl
  let jsxtnm156 = arg1
  // I1CMP:start
  let jsxtnm161 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(157);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(136)),I0Pvar(xs(137)))));$list(@(x1(136),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(157));0)),@(xs(137),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(157));1)))))
    if (XATS000_ctgeq(jsxtnm156, XATSCTAG("strmcon_vt_cons",1))) { // gpt
      let jsxtnm157 = jsxtnm156
      let jsxtnm160 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(precats.dats)@(9584(line=608,offs=7)--9609(line=608,offs=32)))
        // I1VALDCL
        let jsxtnm159
        let jsxtnm158 = XATSCAST("delinear_1667", [XATSP1CN("strmcon_vt_cons", jsxtnm157[0+1])])
        jsxtnm159 = jsxtnm158
        XATS000_patck(true)
        jsxtnm160 = XATSP1CN("strmcon_vt_cons", jsxtnm157[1+1])
      } // endlet
      jsxtnm161 = jsxtnm160
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm161
  return jsxtnm161
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(9669(line=615,offs=1)--9756(line=620,offs=34)))
// LCSRCsome1(precats.dats)@(9677(line=616,offs=1)--9756(line=620,offs=34))
// I1FUNDCL
// XATS2JS_strxcon_vt_head$raw1_9680
  // FJARGdarg($list(I1BNDcons(I1TNM(162);I0Pvar(xs(140));$list(@(xs(140),I1Vtnm(I1TNM(162)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strxcon_vt_head$raw1);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(9757(line=621,offs=1)--9906(line=630,offs=42)))
let XATS2JS_strxcon_vt_head$raw1 = function (arg1) { // impl
  let jsxtnm163 = arg1
  // I1CMP:start
  let jsxtnm169 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(164);I0Pdapp(I0Pcon(strxcon_vt_cons(17));$list(I0Pvar(x1(142)),I0Pvar(xs(143))));$list(@(x1(142),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(164));0)),@(xs(143),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(164));1)))))
    if (XATS000_ctgeq(jsxtnm163, XATSCTAG("strxcon_vt_cons",0))) { // gpt
      let jsxtnm164 = jsxtnm163
      let jsxtnm168 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(precats.dats)@(9856(line=629,offs=1)--9881(line=630,offs=17)))
        // I1VALDCL
        let jsxtnm166
        let jsxtnm165 = XATSCAST("datacopy_1720", [XATSP1CN("strxcon_vt_cons", jsxtnm164[0+1])])
        jsxtnm166 = jsxtnm165
        XATS000_patck(true)
        let jsxtnm167 = XATSCAST("enlinear_1756", [jsxtnm166])
        jsxtnm168 = jsxtnm167
      } // endlet
      jsxtnm169 = jsxtnm168
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm169
  return jsxtnm169
} // endfun(impl)
// I1Dextern(LCSRCsome1(precats.dats)@(9932(line=635,offs=1)--10026(line=640,offs=41)))
// LCSRCsome1(precats.dats)@(9940(line=636,offs=1)--10026(line=640,offs=41))
// I1FUNDCL
// XATS2JS_strxcon_vt_tail$raw0_9943
  // FJARGdarg($list(I1BNDcons(I1TNM(170);I0Pvar(xs(146));$list(@(xs(146),I1Vtnm(I1TNM(170)))))))
  // I1CMP:start
  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strxcon_vt_tail$raw0);G1Nlist($list())) // I1CMP:return
// I1Dimplmnt0(LCSRCsome1(precats.dats)@(10027(line=641,offs=1)--10166(line=648,offs=43)))
let XATS2JS_strxcon_vt_tail$raw0 = function (arg1) { // impl
  let jsxtnm171 = arg1
  // I1CMP:start
  let jsxtnm176 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(172);I0Pfree(I0Pdapp(I0Pcon(strxcon_vt_cons(17));$list(I0Pvar(x1(148)),I0Pvar(xs(149)))));$list(@(x1(148),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(172));0)),@(xs(149),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(172));1)))))
    if (XATS000_ctgeq(jsxtnm171, XATSCTAG("strxcon_vt_cons",0))) { // gpt
      let jsxtnm172 = jsxtnm171
      let jsxtnm175 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(precats.dats)@(10130(line=648,offs=7)--10155(line=648,offs=32)))
        // I1VALDCL
        let jsxtnm174
        let jsxtnm173 = XATSCAST("delinear_1667", [XATSP1CN("strxcon_vt_cons", jsxtnm172[0+1])])
        jsxtnm174 = jsxtnm173
        XATS000_patck(true)
        jsxtnm175 = XATSP1CN("strxcon_vt_cons", jsxtnm172[1+1])
      } // endlet
      jsxtnm176 = jsxtnm175
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:jsxtnm176
  return jsxtnm176
} // endfun(impl)
// LCSRCsome1(precats.dats)@(10422(line=656,offs=1)--10422(line=656,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(precats.dats)@(10422(line=656,offs=1)--10422(line=656,offs=1));D3Cnone0()))
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
// LCSRCsome1(test09_llist00.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
// I1Dinclude(LCSRCsome1(test09_llist00.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
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
// I1Dinclude(LCSRCsome1(test09_llist00.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
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
// I1Dfundclist(LCSRCsome1(test09_llist00.dats)@(323(line=21,offs=1)--437(line=28,offs=36)))
// I1FUNDCL
function length_326(arg1)
{ // fun
  let jsxtnm1 = arg1
  // I1CMP:start
  let jsxtnm14 // cas
  do {
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(2);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
    if (XATS000_ctgeq(jsxtnm1, XATSCTAG("list_vt_nil",0))) { // gpt
      let jsxtnm2 = jsxtnm1
      jsxtnm14 = XATSINT1(0)
      break // cls
    } // gpt
    // } // cls
    // { // cls
    // I1GPTpat(I1BNDcons(I1TNM(3);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pbang(I0Pvar(xs(5206)))));$list(@(xs(5206),I1Vlpcn(LABint(1);I1Vtnm(I1TNM(3)))))))
    if (XATS000_ctgeq(jsxtnm1, XATSCTAG("list_vt_cons",1))) { // gpt
      let jsxtnm3 = jsxtnm1
      // LCSRCsome1(test09_llist00.dats)@(426(line=28,offs=25)--427(line=28,offs=26))
      // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
      // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
      // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
      let jsxtnm10 = function (arg1, arg2) { // timp: sint_add$sint(936)
        let jsxtnm4 = arg1
        let jsxtnm5 = arg2
        // I1CMP:start
        let jsxtnm9 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
          // I1FUNDCL: XATS2JS_sint_add$sint(4922)
          // XATS2JS_sint_add$sint_2778
            // FJARGdarg($list(I1BNDcons(I1TNM(6);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(6))))),I1BNDcons(I1TNM(7);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(7)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
          let jsxtnm8 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm4, jsxtnm5))
          jsxtnm9 = jsxtnm8
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(9))
        return jsxtnm9
      } // endtimp(sint_add$sint(936))
      let jsxtnm11 = XATSFLAT(XATSLPCN(1, jsxtnm3))
      let jsxtnm12 = XATSDAPP(length_326(jsxtnm11))
      let jsxtnm13 = XATSDAPP(jsxtnm10(XATSINT1(1), jsxtnm12))
      jsxtnm14 = jsxtnm13
      break // cls
    } // gpt
    // } // cls
    XATS000_cfail()
  } while (false) // end-of(do)
  // I1CMP:return:I1Vtnm(I1TNM(14))
  return jsxtnm14
} // endfun(length_326)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(484(line=33,offs=1)--523(line=35,offs=18)))
// I1VALDCL
let jsxtnm79
// LCSRCsome1(test09_llist00.dats)@(493(line=34,offs=1)--505(line=34,offs=13))
// I0Etapq(I0Ecst(list_vt_make_nfun(2038)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(3083(line=156,offs=1)--3100(line=156,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(list_vt_make_nfun(2038);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2448(line=120,offs=1)--2509(line=123,offs=23)))
// T1IMPallx(list_vt_make_nfun(2038)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8493],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_make_nfun(2038);$list(@(a[5245],T2Pvar(a[8493])))))))
let jsxtnm75
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2487(line=123,offs=1)--2506(line=123,offs=20))
// I0Etapq(I0Ecst(nint_map$f1un_llist(969)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3824(line=192,offs=1)--3843(line=192,offs=20))));$list(T2JAG($list(T2Pvar(a[8493])))))
// T1IMPallx(nint_map$f1un_llist(969);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7232(line=482,offs=1)--7375(line=492,offs=2)))
// T1IMPallx(nint_map$f1un_llist(969)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map$f1un_llist(969);$list(@(y0[2872],T2Pvar(y0[7247])))))))
let jsxtnm74 = function (arg1, arg2) { // timp: nint_map$f1un_llist(969)
  let jsxtnm15 = arg1
  let jsxtnm16 = arg2
  // I1CMP:start
  let jsxtnm73 // let
  { // let
    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
    // I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Pvar(y0[7247]))))):timp
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7288(line=487,offs=1)--7302(line=487,offs=15))
    // I0Etapq(I0Ecst(nint_map_llist(968)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3756(line=187,offs=1)--3770(line=187,offs=15))));$list(T2JAG($list(T2Pvar(y0[7247])))))
    // T1IMPallx(nint_map_llist(968);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6864(line=449,offs=1)--7193(line=480,offs=2)))
    // T1IMPallx(nint_map_llist(968)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7246],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map_llist(968);$list(@(y0[2870],T2Pvar(y0[7246])))))))
    let jsxtnm71 = function (arg1) { // timp: nint_map_llist(968)
      let jsxtnm19 = arg1
      // I1CMP:start
      let jsxtnm70 // let
      { // let
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6958(line=459,offs=1)--6983(line=460,offs=17))
        // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(ys;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(3;vtbx)));list_vt);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));y0[7246])))))))
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6987(line=462,offs=1)--7009(line=463,offs=19)))
        // I1VALDCL
        let jsxtnm21
        let jsxtnm20 = XATSCAPP("list_vt_nil", [0])
        jsxtnm21 = jsxtnm20
        XATS000_patck(true)
        // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7013(line=465,offs=1)--7188(line=478,offs=2)))
        // I1FUNDCL
        function loop_7016(arg1, arg2)
        { // fun
          let jsxtnm22 = arg1
          let jsxtnm23 = arg2
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7054(line=470,offs=5)--7056(line=470,offs=7))
          // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
          // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
          // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
          let jsxtnm30 = function (arg1, arg2) { // timp: sint_gte$sint(931)
            let jsxtnm24 = arg1
            let jsxtnm25 = arg2
            // I1CMP:start
            let jsxtnm29 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
              // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
              // XATS2JS_sint_gte$sint_2399
                // FJARGdarg($list(I1BNDcons(I1TNM(26);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(26))))),I1BNDcons(I1TNM(27);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(27)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
              let jsxtnm28 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm24, jsxtnm25))
              jsxtnm29 = jsxtnm28
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(29))
            return jsxtnm29
          } // endtimp(sint_gte$sint(931))
          let jsxtnm31 = XATSDAPP(jsxtnm30(jsxtnm22, jsxtnm19))
          let jsxtnm48 // ift
          if (jsxtnm31) // ift
          {
            jsxtnm48 = jsxtnm23
          } else {
            let jsxtnm47 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7078(line=473,offs=1)--7107(line=473,offs=30)))
              // I1VALDCL
              let jsxtnm36
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7087(line=473,offs=10)--7095(line=473,offs=18))
              // I0Etapq(I0Ecst(map$fopr(77)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(4030(line=256,offs=1)--4038(line=256,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Pvar(y0[7246])))))
              // T1IMPallx(map$fopr(77);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
              // T1IMPallx(map$fopr(77)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm34 = function (arg1) { // timp: map$fopr(77)
                let jsxtnm32 = arg1
                // I1CMP:start
                let jsxtnm33 = XATSDAPP(jsxtnm16(jsxtnm32))
                // I1CMP:return:I1Vtnm(I1TNM(33))
                return jsxtnm33
              } // endtimp(map$fopr(77))
              let jsxtnm35 = XATSDAPP(jsxtnm34(jsxtnm22))
              jsxtnm36 = jsxtnm35
              XATS000_patck(true)
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7125(line=476,offs=8)--7126(line=476,offs=9))
              // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
              // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
              // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
              let jsxtnm43 = function (arg1, arg2) { // timp: sint_add$sint(936)
                let jsxtnm37 = arg1
                let jsxtnm38 = arg2
                // I1CMP:start
                let jsxtnm42 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                  // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                  // XATS2JS_sint_add$sint_2778
                    // FJARGdarg($list(I1BNDcons(I1TNM(39);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(39))))),I1BNDcons(I1TNM(40);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(40)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                  let jsxtnm41 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm37, jsxtnm38))
                  jsxtnm42 = jsxtnm41
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(42))
                return jsxtnm42
              } // endtimp(sint_add$sint(936))
              let jsxtnm44 = XATSDAPP(jsxtnm43(jsxtnm22, XATSINT1(1)))
              let jsxtnm45 = XATSCAPP("list_vt_cons", [1, jsxtnm36, jsxtnm23])
              let jsxtnm46 = XATSDAPP(loop_7016(jsxtnm44, jsxtnm45))
              jsxtnm47 = jsxtnm46
            } // endlet
            jsxtnm48 = jsxtnm47
          } // end(if)
          // I1CMP:return:I1Vtnm(I1TNM(48))
          return jsxtnm48
        } // endfun(loop_7016)
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6911(line=454,offs=1)--6927(line=454,offs=17))
        // I0Etapq(I0Ecst(list_vt_reverse0(2046)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4474(line=255,offs=1)--4490(line=255,offs=17))));$list(T2JAG($list(T2Pvar(y0[7246])))))
        // T1IMPallx(list_vt_reverse0(2046);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7033(line=475,offs=1)--7120(line=478,offs=46)))
        // T1IMPallx(list_vt_reverse0(2046)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8528],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_reverse0(2046);$list(@(x0[5264],T2Pvar(a[8528])))))))
        let jsxtnm67 = function (arg1) { // timp: list_vt_reverse0(2046)
          let jsxtnm49 = arg1
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7075(line=478,offs=1)--7092(line=478,offs=18))
          // I0Etapq(I0Ecst(list_vt_rappend00(2049)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4855(line=281,offs=1)--4872(line=281,offs=18))));$list(T2JAG($list(T2Pvar(a[8528])))))
          // T1IMPallx(list_vt_rappend00(2049);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6363(line=426,offs=1)--6772(line=458,offs=2)))
          // T1IMPallx(list_vt_rappend00(2049)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8524],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_rappend00(2049);$list(@(x0[5271],T2Pvar(a[8524])))))))
          let jsxtnm64 = function (arg1, arg2) { // timp: list_vt_rappend00(2049)
            let jsxtnm50 = arg1
            let jsxtnm51 = arg2
            // I1CMP:start
            let jsxtnm63 // let
            { // let
              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6442(line=434,offs=1)--6733(line=456,offs=2)))
              // I1FUNDCL
              function loop_6445(arg1, arg2)
              { // fun
                let jsxtnm52 = arg1
                let jsxtnm53 = arg2
                // I1CMP:start
                let jsxtnm61 // cas
                do {
                  // { // cls
                  // I1GPTpat(I1BNDcons(I1TNM(54);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
                  if (XATS000_ctgeq(jsxtnm52, XATSCTAG("list_vt_nil",0))) { // gpt
                    let jsxtnm54 = jsxtnm52
                    jsxtnm61 = jsxtnm53
                    break // cls
                  } // gpt
                  // } // cls
                  // { // cls
                  // I1GPTpat(I1BNDcons(I1TNM(55);I0Pflat(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pany())));$list()))
                  if (XATS000_ctgeq(jsxtnm52, XATSCTAG("list_vt_cons",1))) { // gpt
                    let jsxtnm55 = jsxtnm52
                    let jsxtnm60 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6616(line=450,offs=3)--6631(line=450,offs=18)))
                      // I1VALDCL
                      let jsxtnm57
                      let jsxtnm56 = XATSPCON(jsxtnm52,1)
                      jsxtnm57 = jsxtnm56
                      XATS000_patck(true)
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6634(line=451,offs=3)--6656(line=451,offs=25)))
                      // I1VALDCL
                      let jsxtnm58
                      XATS000_assgn(XATSLPCN(1, jsxtnm52), jsxtnm53)
                      jsxtnm58 = XATSVOID
                      XATS000_patck(true)
                      XATS000_fold(jsxtnm52)
                      let jsxtnm59 = XATSDAPP(loop_6445(jsxtnm57, jsxtnm52))
                      jsxtnm60 = jsxtnm59
                    } // endlet
                    jsxtnm61 = jsxtnm60
                    break // cls
                  } // gpt
                  // } // cls
                  XATS000_cfail()
                } while (false) // end-of(do)
                // I1CMP:return:I1Vtnm(I1TNM(61))
                return jsxtnm61
              } // endfun(loop_6445)
              let jsxtnm62 = XATSDAPP(loop_6445(jsxtnm50, jsxtnm51))
              jsxtnm63 = jsxtnm62
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(63))
            return jsxtnm63
          } // endtimp(list_vt_rappend00(2049))
          let jsxtnm65 = XATSCAPP("list_vt_nil", [0])
          let jsxtnm66 = XATSDAPP(jsxtnm64(jsxtnm49, jsxtnm65))
          // I1CMP:return:I1Vtnm(I1TNM(66))
          return jsxtnm66
        } // endtimp(list_vt_reverse0(2046))
        let jsxtnm68 = XATSDAPP(loop_7016(XATSINT1(0), jsxtnm21))
        let jsxtnm69 = XATSDAPP(jsxtnm67(jsxtnm68))
        jsxtnm70 = jsxtnm69
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(70))
      return jsxtnm70
    } // endtimp(nint_map_llist(968))
    let jsxtnm72 = XATSDAPP(jsxtnm71(jsxtnm15))
    jsxtnm73 = jsxtnm72
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(73))
  return jsxtnm73
} // endtimp(nint_map$f1un_llist(969))
jsxtnm75 = jsxtnm74
let jsxtnm77 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm76 = arg1
  // I1CMP:start
  // I1CMP:return:I1Vtnm(I1TNM(76))
  return jsxtnm76
} // endfun(lam0)
let jsxtnm78 = XATSDAPP(jsxtnm75(XATSINT1(10), jsxtnm77))
jsxtnm79 = jsxtnm78
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(527(line=37,offs=1)--546(line=37,offs=20)))
// I1VALDCL
let jsxtnm81
let jsxtnm80 = XATSDAPP(length_326(jsxtnm79))
jsxtnm81 = jsxtnm80
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(547(line=38,offs=1)--577(line=39,offs=22)))
// I1VALDCL
let jsxtnm122
// LCSRCsome1(test09_llist00.dats)@(556(line=39,offs=1)--564(line=39,offs=9))
// I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(gs_println_a2(820);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
// T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
let jsxtnm120 = function (arg1, arg2) { // timp: gs_println_a2(820)
  let jsxtnm82 = arg1
  let jsxtnm83 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  // I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  // T1IMPallx(gs_print_a2(807);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  // T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  let jsxtnm111 = function (arg1, arg2) { // timp: gs_print_a2(807)
    let jsxtnm84 = arg1
    let jsxtnm85 = arg2
    // I1CMP:start
    let jsxtnm110 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
      // I1VALDCL
      let jsxtnm89
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
      // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      let jsxtnm87 = function () { // timp: gs_print$beg(802)
        // I1CMP:start
        let jsxtnm86 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(86))
        return jsxtnm86
      } // endtimp(gs_print$beg(802))
      let jsxtnm88 = XATSDAPP(jsxtnm87())
      jsxtnm89 = jsxtnm88
      XATS000_patck(true)
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm95
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm94 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm90 = arg1
        // I1CMP:start
        let jsxtnm93 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(91);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(91)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm92 = XATSDAPP(XATS2JS_strn_print(jsxtnm90))
          jsxtnm93 = jsxtnm92
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(93))
        return jsxtnm93
      } // endtimp(strn_print(1040))
      jsxtnm95 = jsxtnm94
      let jsxtnm96 = XATSDAPP(jsxtnm95(jsxtnm84))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm98 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm97 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(97))
        return jsxtnm97
      } // endtimp(gs_print$sep(803))
      let jsxtnm99 = XATSDAPP(jsxtnm98())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
      let jsxtnm105
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
      // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
      // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
      let jsxtnm104 = function (arg1) { // timp: sint_print(922)
        let jsxtnm100 = arg1
        // I1CMP:start
        let jsxtnm103 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
          // I1FUNDCL: XATS2JS_sint_print(4946)
          // XATS2JS_sint_print_3707
            // FJARGdarg($list(I1BNDcons(I1TNM(101);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(101)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm102 = XATSDAPP(XATS2JS_sint_print(jsxtnm100))
          jsxtnm103 = jsxtnm102
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(103))
        return jsxtnm103
      } // endtimp(sint_print(922))
      jsxtnm105 = jsxtnm104
      let jsxtnm106 = XATSDAPP(jsxtnm105(jsxtnm85))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
      // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      let jsxtnm108 = function () { // timp: gs_print$end(804)
        // I1CMP:start
        let jsxtnm107 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(107))
        return jsxtnm107
      } // endtimp(gs_print$end(804))
      let jsxtnm109 = XATSDAPP(jsxtnm108())
      jsxtnm110 = jsxtnm109
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(110))
    return jsxtnm110
  } // endtimp(gs_print_a2(807))
  let jsxtnm112 = XATSDAPP(jsxtnm111(jsxtnm82, jsxtnm83))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm118
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm117 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm113 = arg1
    // I1CMP:start
    let jsxtnm116 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(114);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(114)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm115 = XATSDAPP(XATS2JS_strn_print(jsxtnm113))
      jsxtnm116 = jsxtnm115
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(116))
    return jsxtnm116
  } // endtimp(strn_print(1040))
  jsxtnm118 = jsxtnm117
  let jsxtnm119 = XATSDAPP(jsxtnm118(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(119))
  return jsxtnm119
} // endtimp(gs_println_a2(820))
let jsxtnm121 = XATSDAPP(jsxtnm120(XATSSTRN("ln = "), jsxtnm81))
jsxtnm122 = jsxtnm121
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(581(line=41,offs=1)--620(line=42,offs=31)))
// I1VALDCL
let jsxtnm166
// LCSRCsome1(test09_llist00.dats)@(590(line=42,offs=1)--598(line=42,offs=9))
// I0Etapq(I0Ecst(list_vt_map0$f1un(2105)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(5135(line=313,offs=1)--5152(line=313,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(list_vt_map0$f1un(2105);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5246(line=321,offs=1)--5385(line=330,offs=2)))
// T1IMPallx(list_vt_map0$f1un(2105)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8570],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8571],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_map0$f1un(2105);$list(@(x0[5350],T2Pvar(x0[8570])),@(y0[5351],T2Pvar(y0[8571])))))))
let jsxtnm154 = function (arg1, arg2) { // timp: list_vt_map0$f1un(2105)
  let jsxtnm123 = arg1
  let jsxtnm124 = arg2
  // I1CMP:start
  let jsxtnm153 // let
  { // let
    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5344(line=329,offs=1)--5383(line=329,offs=40)))
    // I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Pvar(x0[8570])),@(y0[3858],T2Pvar(y0[8571]))))):timp
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5310(line=327,offs=3)--5322(line=327,offs=15))
    // I0Etapq(I0Ecst(list_vt_map0(2103)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(4887(line=297,offs=1)--4899(line=297,offs=13))));$list(T2JAG($list(T2Pvar(x0[8570]))),T2JAG($list(T2Pvar(y0[8571])))))
    // T1IMPallx(list_vt_map0(2103);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(4753(line=281,offs=1)--5205(line=319,offs=4)))
    // T1IMPallx(list_vt_map0(2103)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8567],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8568],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_map0(2103);$list(@(x0[5344],T2Pvar(x0[8567])),@(y0[5345],T2Pvar(y0[8568])))))))
    let jsxtnm151 = function (arg1) { // timp: list_vt_map0(2103)
      let jsxtnm127 = arg1
      // I1CMP:start
      let jsxtnm150 // let
      { // let
        // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(4813(line=287,offs=1)--5104(line=311,offs=2)))
        // I1FUNDCL
        function loop_4816(arg1, arg2)
        { // fun
          let jsxtnm128 = arg1
          let jsxtnm129 = arg2
          // I1CMP:start
          let jsxtnm144 // cas
          do {
            // { // cls
            // I1GPTpat(I1BNDcons(I1TNM(130);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
            if (XATS000_ctgeq(jsxtnm128, XATSCTAG("list_vt_nil",0))) { // gpt
              let jsxtnm130 = jsxtnm128
              let jsxtnm131 = XATSCAPP("list_vt_nil", [0])
              XATS000_assgn(XATSADDR(jsxtnm129), jsxtnm131)
              jsxtnm144 = XATSVOID
              break // cls
            } // gpt
            // } // cls
            // { // cls
            // I1GPTpat(I1BNDcons(I1TNM(132);I0Pfree(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x0(4373)),I0Pvar(xs(4374)))));$list(@(x0(4373),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(132));0)),@(xs(4374),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(132));1)))))
            if (XATS000_ctgeq(jsxtnm128, XATSCTAG("list_vt_cons",1))) { // gpt
              let jsxtnm132 = jsxtnm128
              let jsxtnm143 // let
              { // let
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(4997(line=303,offs=1)--5027(line=304,offs=22)))
                // I1VALDCL
                let jsxtnm137
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5006(line=304,offs=1)--5015(line=304,offs=10))
                // I0Etapq(I0Ecst(map$fopr0(1484)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(5345(line=363,offs=1)--5354(line=363,offs=10))));$list(T2JAG($list(T2Pvar(x0[8567]))),T2JAG($list(T2Pvar(y0[8568])))))
                // T1IMPallx(map$fopr0(1484);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5344(line=329,offs=1)--5383(line=329,offs=40)))
                // T1IMPallx(map$fopr0(1484)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8570],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8571],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[3858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                let jsxtnm135 = function (arg1) { // timp: map$fopr0(1484)
                  let jsxtnm133 = arg1
                  // I1CMP:start
                  let jsxtnm134 = XATSDAPP(jsxtnm124(jsxtnm133))
                  // I1CMP:return:I1Vtnm(I1TNM(134))
                  return jsxtnm134
                } // endtimp(map$fopr0(1484))
                let jsxtnm136 = XATSDAPP(jsxtnm135(XATSP1CN("list_vt_cons", jsxtnm132[0+1])))
                jsxtnm137 = jsxtnm136
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5028(line=305,offs=1)--5064(line=306,offs=28)))
                // I1VALDCL
                let jsxtnm139
                let jsxtnm138 = XATSCAPP("list_vt_cons", [1, jsxtnm137, XATSTOP0])
                XATS000_assgn(XATSADDR(jsxtnm129), jsxtnm138)
                jsxtnm139 = XATSVOID
                XATS000_patck(true)
                let jsxtnm140 = XATSFLAT(jsxtnm129)
                let jsxtnm141 = XATSDAPP(loop_4816(XATSP1CN("list_vt_cons", jsxtnm132[1+1]), XATSLPCN(1, jsxtnm140)))
                let jsxtnm142 = XATSFLAT(jsxtnm129)
                XATS000_fold(jsxtnm142)
                jsxtnm143 = XATSVOID
              } // endlet
              jsxtnm144 = jsxtnm143
              break // cls
            } // gpt
            // } // cls
            XATS000_cfail()
          } while (false) // end-of(do)
          // I1CMP:return:I1Vtnm(I1TNM(144))
          return jsxtnm144
        } // endfun(loop_4816)
        let jsxtnm149 // let
        { // let
          // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5140(line=316,offs=3)--5159(line=316,offs=22)))
          // I1VARDCL
          let jsxtnm145 = XATSVAR0()
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5162(line=317,offs=3)--5183(line=317,offs=24)))
          // I1VALDCL
          let jsxtnm147
          let jsxtnm146 = XATSDAPP(loop_4816(jsxtnm127, XATSADDR(jsxtnm145)))
          jsxtnm147 = jsxtnm146
          XATS000_patck(true)
          let jsxtnm148 = XATSFLAT(jsxtnm145)
          jsxtnm149 = jsxtnm148
        } // endlet
        jsxtnm150 = jsxtnm149
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(150))
      return jsxtnm150
    } // endtimp(list_vt_map0(2103))
    let jsxtnm152 = XATSDAPP(jsxtnm151(jsxtnm123))
    jsxtnm153 = jsxtnm152
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(153))
  return jsxtnm153
} // endtimp(list_vt_map0$f1un(2105))
let jsxtnm164 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm155 = arg1
  // I1CMP:start
  // LCSRCsome1(test09_llist00.dats)@(617(line=42,offs=28)--618(line=42,offs=29))
  // I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(sint_mul$sint(938);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
  // T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
  let jsxtnm162 = function (arg1, arg2) { // timp: sint_mul$sint(938)
    let jsxtnm156 = arg1
    let jsxtnm157 = arg2
    // I1CMP:start
    let jsxtnm161 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3111(line=182,offs=1)--3175(line=184,offs=39))
      // I1FUNDCL: XATS2JS_sint_mul$sint(4932)
      // XATS2JS_sint_mul$sint_3114
        // FJARGdarg($list(I1BNDcons(I1TNM(158);I0Pvar(i1(4933));$list(@(i1(4933),I1Vtnm(I1TNM(158))))),I1BNDcons(I1TNM(159);I0Pvar(i2(4934));$list(@(i2(4934),I1Vtnm(I1TNM(159)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_mul$sint);G1Nlist($list()))// I1CMP:return
      let jsxtnm160 = XATSDAPP(XATS2JS_sint_mul$sint(jsxtnm156, jsxtnm157))
      jsxtnm161 = jsxtnm160
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(161))
    return jsxtnm161
  } // endtimp(sint_mul$sint(938))
  let jsxtnm163 = XATSDAPP(jsxtnm162(jsxtnm155, jsxtnm155))
  // I1CMP:return:I1Vtnm(I1TNM(163))
  return jsxtnm163
} // endfun(lam0)
let jsxtnm165 = XATSDAPP(jsxtnm154(jsxtnm79, jsxtnm164))
jsxtnm166 = jsxtnm165
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(621(line=43,offs=1)--656(line=43,offs=36)))
// I1VALDCL
let jsxtnm472
// LCSRCsome1(test09_llist00.dats)@(630(line=43,offs=10)--637(line=43,offs=17))
// I0Etapq(I0Ecst(gs_print0_a3(1976)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1751(line=73,offs=1)--1763(line=73,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
// T1IMPallx(gs_print0_a3(1976);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1853(line=75,offs=1)--2020(line=84,offs=21)))
// T1IMPallx(gs_print0_a3(1976)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8303],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8304],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[8305],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print0_a3(1976);$list(@(x0[5041],T2Pvar(x0[8303])),@(x1[5042],T2Pvar(x1[8304])),@(x2[5043],T2Pvar(x2[8305])))))))
let jsxtnm470 = function (arg1, arg2, arg3) { // timp: gs_print0_a3(1976)
  let jsxtnm167 = arg1
  let jsxtnm168 = arg2
  let jsxtnm169 = arg3
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1924(line=81,offs=3)--1937(line=81,offs=16))
  // I0Etapq(I0Ecst(gs_print0$beg(1970)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1430(line=43,offs=1)--1443(line=43,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(gs_print0$beg(1970);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1436(line=42,offs=1)--1475(line=44,offs=21)))
  // T1IMPallx(gs_print0$beg(1970)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$beg(1970);$list()))))
  let jsxtnm171 = function () { // timp: gs_print0$beg(1970)
    // I1CMP:start
    let jsxtnm170 = XATSTUP0([])
    // I1CMP:return:I1Vtnm(I1TNM(170))
    return jsxtnm170
  } // endtimp(gs_print0$beg(1970))
  let jsxtnm172 = XATSDAPP(jsxtnm171())
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1945(line=82,offs=3)--1953(line=82,offs=11))
  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[8303])))))
  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  let jsxtnm179
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm178
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm177 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm173 = arg1
    // I1CMP:start
    let jsxtnm176 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(174);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(174)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm175 = XATSDAPP(XATS2JS_strn_print(jsxtnm173))
      jsxtnm176 = jsxtnm175
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(176))
    return jsxtnm176
  } // endtimp(strn_print(1040))
  jsxtnm178 = jsxtnm177
  jsxtnm179 = jsxtnm178
  let jsxtnm180 = XATSDAPP(jsxtnm179(jsxtnm167))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1964(line=83,offs=3)--1972(line=83,offs=11))
  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x1[8304])))))
  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2815(line=148,offs=1)--2899(line=154,offs=2)))
  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8497])))))))))
  let jsxtnm457 = function (arg1) { // timp: g_print0(1411)
    let jsxtnm181 = arg1
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2865(line=153,offs=1)--2876(line=153,offs=12))
    // I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[8497]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[8497])))))
    // T1IMPallx(gseq_print0(1686);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    // T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    let jsxtnm455 = function (arg1) { // timp: gseq_print0(1686)
      let jsxtnm182 = arg1
      // I1CMP:start
      let jsxtnm454 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
        // I1VALDCL
        let jsxtnm191
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm187 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm183 = arg1
          // I1CMP:start
          let jsxtnm186 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(184);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(184)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm185 = XATSDAPP(XATS2JS_strn_print(jsxtnm183))
            jsxtnm186 = jsxtnm185
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(186))
          return jsxtnm186
        } // endtimp(strn_print(1040))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
        // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
        // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8496])))),@(x0[1068],T2Pvar(x0[8496])))))))
        let jsxtnm188 = function () { // timp: gseq$beg(346)
          // I1CMP:start
          // I1CMP:return:I1Vstr(...)
          return XATSSTRN("list_vt(")
        } // endtimp(gseq$beg(346))
        let jsxtnm189 = XATSDAPP(jsxtnm188())
        let jsxtnm190 = XATSDAPP(jsxtnm187(jsxtnm189))
        jsxtnm191 = jsxtnm190
        XATS000_patck(true)
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
        // I1VALDCL
        let jsxtnm444
        let jsxtnm443 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
          // I1VALDCL
          let jsxtnm200
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
          // I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
          // T1IMPallx(gseq$prlen(350);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
          // T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
          let jsxtnm198 = function () { // timp: gseq$prlen(350)
            // I1CMP:start
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
            // I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
            // T1IMPallx(sint_neg(923);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
            // T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
            let jsxtnm196 = function (arg1) { // timp: sint_neg(923)
              let jsxtnm192 = arg1
              // I1CMP:start
              let jsxtnm195 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1514(line=49,offs=1)--1563(line=51,offs=29))
                // I1FUNDCL: XATS2JS_sint_neg(4888)
                // XATS2JS_sint_neg_1517
                  // FJARGdarg($list(I1BNDcons(I1TNM(193);I0Pvar(i1(4889));$list(@(i1(4889),I1Vtnm(I1TNM(193)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_neg);G1Nlist($list()))// I1CMP:return
                let jsxtnm194 = XATSDAPP(XATS2JS_sint_neg(jsxtnm192))
                jsxtnm195 = jsxtnm194
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(195))
              return jsxtnm195
            } // endtimp(sint_neg(923))
            let jsxtnm197 = XATSDAPP(jsxtnm196(XATSINT1(1)))
            // I1CMP:return:I1Vtnm(I1TNM(197))
            return jsxtnm197
          } // endtimp(gseq$prlen(350))
          let jsxtnm199 = XATSDAPP(jsxtnm198())
          jsxtnm200 = jsxtnm199
          XATS000_patck(true)
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
          // I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
          // I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
          // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
          // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
          // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
          let jsxtnm233 = function (arg1, arg2) { // timp: sint_gte$sint(931)
            let jsxtnm227 = arg1
            let jsxtnm228 = arg2
            // I1CMP:start
            let jsxtnm232 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
              // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
              // XATS2JS_sint_gte$sint_2399
                // FJARGdarg($list(I1BNDcons(I1TNM(229);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(229))))),I1BNDcons(I1TNM(230);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(230)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
              let jsxtnm231 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm227, jsxtnm228))
              jsxtnm232 = jsxtnm231
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(232))
            return jsxtnm232
          } // endtimp(sint_gte$sint(931))
          let jsxtnm234 = XATSDAPP(jsxtnm233(jsxtnm200, XATSINT1(0)))
          let jsxtnm442 // ift
          if (jsxtnm234) // ift
          {
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
            // I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
            // T1IMPallx(g_void(22);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
            // T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
            let jsxtnm237 = function (arg1) { // timp: g_void(22)
              let jsxtnm235 = arg1
              // I1CMP:start
              let jsxtnm236 = XATSTUP0([])
              // I1CMP:return:I1Vtnm(I1TNM(236))
              return jsxtnm236
            } // endtimp(g_void(22))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
            // I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
            // T1IMPallx(gseq_iforall0(1735);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
            // T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
            let jsxtnm341 = function (arg1) { // timp: gseq_iforall0(1735)
              let jsxtnm238 = arg1
              // I1CMP:start
              let jsxtnm340 // let
              { // let
                // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
                // I1VARDCL
                // I1CMP:start
                // I1CMP:return:I1Vint(T_INT01(0))
                let jsxtnm239 = XATSVAR1(XATSINT1(0))
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
                // I1VALDCL
                let jsxtnm240
                jsxtnm240 = XATSADDR(jsxtnm239)
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
                // I1VALDCL
                let jsxtnm339
                let jsxtnm338 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                  // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
                  // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
                  // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
                  // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
                  let jsxtnm336
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
                  // I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
                  // T1IMPallx(list_vt_forall0(2062);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
                  // T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8842],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8842])))))))
                  let jsxtnm335 = function (arg1) { // timp: list_vt_forall0(2062)
                    let jsxtnm249 = arg1
                    // I1CMP:start
                    let jsxtnm334 // let
                    { // let
                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
                      // I1FUNDCL
                      function test_2076(arg1)
                      { // fun
                        let jsxtnm250 = arg1
                        // I1CMP:start
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                        // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                        // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                        // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        let jsxtnm326 = function (arg1) { // timp: forall$test0(1422)
                          let jsxtnm251 = arg1
                          // I1CMP:start
                          let jsxtnm325 // let
                          { // let
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                            // I1VALDCL
                            let jsxtnm256
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                            // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                            // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                            let jsxtnm254 = function (arg1) { // timp: p2tr_get(2309)
                              let jsxtnm252 = arg1
                              // I1CMP:start
                              let jsxtnm253 = XATS000_dp2tr(jsxtnm252)
                              // I1CMP:return:I1Vtnm(I1TNM(253))
                              return jsxtnm253
                            } // endtimp(p2tr_get(2309))
                            let jsxtnm255 = XATSDAPP(jsxtnm254(jsxtnm240))
                            jsxtnm256 = jsxtnm255
                            XATS000_patck(true)
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                            // I1VALDCL
                            let jsxtnm312
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                            // I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                            // T1IMPallx(iforall$test0(1432);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                            // T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                            let jsxtnm310 = function (arg1, arg2) { // timp: iforall$test0(1432)
                              let jsxtnm257 = arg1
                              let jsxtnm258 = arg2
                              // I1CMP:start
                              let jsxtnm309 // let
                              { // let
                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                                // I1VALDCL
                                let jsxtnm276
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                                // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                let jsxtnm265 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                  let jsxtnm259 = arg1
                                  let jsxtnm260 = arg2
                                  // I1CMP:start
                                  let jsxtnm264 // let
                                  { // let
                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                    // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                    // XATS2JS_sint_gt$sint_1876
                                      // FJARGdarg($list(I1BNDcons(I1TNM(261);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(261))))),I1BNDcons(I1TNM(262);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(262)))))))
                                      // I1CMP:start
                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                    let jsxtnm263 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm259, jsxtnm260))
                                    jsxtnm264 = jsxtnm263
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(264))
                                  return jsxtnm264
                                } // endtimp(sint_gt$sint(928))
                                let jsxtnm266 = XATSDAPP(jsxtnm265(jsxtnm257, XATSINT1(0)))
                                let jsxtnm275 // ift
                                if (jsxtnm266) // ift
                                {
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                                  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                  let jsxtnm271 = function (arg1) { // timp: strn_print(1040)
                                    let jsxtnm267 = arg1
                                    // I1CMP:start
                                    let jsxtnm270 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                      // I1FUNDCL: XATS2JS_strn_print(5082)
                                      // XATS2JS_strn_print_2202
                                        // FJARGdarg($list(I1BNDcons(I1TNM(268);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(268)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm269 = XATSDAPP(XATS2JS_strn_print(jsxtnm267))
                                      jsxtnm270 = jsxtnm269
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(270))
                                    return jsxtnm270
                                  } // endtimp(strn_print(1040))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                                  // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                  // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                                  // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                                  let jsxtnm272 = function () { // timp: gseq$sep(348)
                                    // I1CMP:start
                                    // I1CMP:return:I1Vstr(...)
                                    return XATSSTRN(",")
                                  } // endtimp(gseq$sep(348))
                                  let jsxtnm273 = XATSDAPP(jsxtnm272())
                                  let jsxtnm274 = XATSDAPP(jsxtnm271(jsxtnm273))
                                  jsxtnm275 = jsxtnm274
                                } else {
                                } // end(if)
                                jsxtnm276 = jsxtnm275
                                XATS000_patck(true)
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                let jsxtnm283 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                  let jsxtnm277 = arg1
                                  let jsxtnm278 = arg2
                                  // I1CMP:start
                                  let jsxtnm282 // let
                                  { // let
                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                    // XATS2JS_sint_gte$sint_2399
                                      // FJARGdarg($list(I1BNDcons(I1TNM(279);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(279))))),I1BNDcons(I1TNM(280);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(280)))))))
                                      // I1CMP:start
                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                    let jsxtnm281 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm277, jsxtnm278))
                                    jsxtnm282 = jsxtnm281
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(282))
                                  return jsxtnm282
                                } // endtimp(sint_gte$sint(931))
                                let jsxtnm284 = XATSDAPP(jsxtnm283(jsxtnm257, jsxtnm200))
                                let jsxtnm308 // ift
                                if (jsxtnm284) // ift
                                {
                                  let jsxtnm299 // let
                                  { // let
                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                                    // I1VALDCL
                                    let jsxtnm289
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                                    // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                    // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                    // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                    let jsxtnm287 = function (arg1) { // timp: g_free(23)
                                      let jsxtnm285 = arg1
                                      // I1CMP:start
                                      let jsxtnm286 = XATSTUP0([])
                                      // I1CMP:return:I1Vtnm(I1TNM(286))
                                      return jsxtnm286
                                    } // endtimp(g_free(23))
                                    let jsxtnm288 = XATSDAPP(jsxtnm287(jsxtnm258))
                                    jsxtnm289 = jsxtnm288
                                    XATS000_patck(true)
                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                                    // I1VALDCL
                                    let jsxtnm298
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                                    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                    let jsxtnm294 = function (arg1) { // timp: strn_print(1040)
                                      let jsxtnm290 = arg1
                                      // I1CMP:start
                                      let jsxtnm293 // let
                                      { // let
                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                        // I1FUNDCL: XATS2JS_strn_print(5082)
                                        // XATS2JS_strn_print_2202
                                          // FJARGdarg($list(I1BNDcons(I1TNM(291);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(291)))))))
                                          // I1CMP:start
                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                        let jsxtnm292 = XATSDAPP(XATS2JS_strn_print(jsxtnm290))
                                        jsxtnm293 = jsxtnm292
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(293))
                                      return jsxtnm293
                                    } // endtimp(strn_print(1040))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                                    // I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                    // T1IMPallx(gseq$rst(349);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                                    // T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                                    let jsxtnm295 = function () { // timp: gseq$rst(349)
                                      // I1CMP:start
                                      // I1CMP:return:I1Vstr(...)
                                      return XATSSTRN("...")
                                    } // endtimp(gseq$rst(349))
                                    let jsxtnm296 = XATSDAPP(jsxtnm295())
                                    let jsxtnm297 = XATSDAPP(jsxtnm294(jsxtnm296))
                                    jsxtnm298 = jsxtnm297
                                    XATS000_patck(true)
                                    jsxtnm299 = XATSBOOL(false)
                                  } // endlet
                                  jsxtnm308 = jsxtnm299
                                } else {
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                                  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                                  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                                  let jsxtnm306
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                                  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                                  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                  let jsxtnm305
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                  // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                  // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                  // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                  let jsxtnm304 = function (arg1) { // timp: sint_print(922)
                                    let jsxtnm300 = arg1
                                    // I1CMP:start
                                    let jsxtnm303 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                      // I1FUNDCL: XATS2JS_sint_print(4946)
                                      // XATS2JS_sint_print_3707
                                        // FJARGdarg($list(I1BNDcons(I1TNM(301);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(301)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm302 = XATSDAPP(XATS2JS_sint_print(jsxtnm300))
                                      jsxtnm303 = jsxtnm302
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(303))
                                    return jsxtnm303
                                  } // endtimp(sint_print(922))
                                  jsxtnm305 = jsxtnm304
                                  jsxtnm306 = jsxtnm305
                                  let jsxtnm307 = XATSDAPP(jsxtnm306(jsxtnm258))
                                  jsxtnm308 = XATSBOOL(true)
                                } // end(if)
                                jsxtnm309 = jsxtnm308
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(309))
                              return jsxtnm309
                            } // endtimp(iforall$test0(1432))
                            let jsxtnm311 = XATSDAPP(jsxtnm310(jsxtnm256, jsxtnm251))
                            jsxtnm312 = jsxtnm311
                            XATS000_patck(true)
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                            // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                            // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                            let jsxtnm315 = function (arg1, arg2) { // timp: p2tr_set(2310)
                              let jsxtnm313 = arg1
                              let jsxtnm314 = arg2
                              // I1CMP:start
                              XATS000_assgn(jsxtnm313, jsxtnm314)
                              // I1CMP:return:I1V000()
                              return XATSVOID
                            } // endtimp(p2tr_set(2310))
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                            let jsxtnm322 = function (arg1, arg2) { // timp: sint_add$sint(936)
                              let jsxtnm316 = arg1
                              let jsxtnm317 = arg2
                              // I1CMP:start
                              let jsxtnm321 // let
                              { // let
                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                // XATS2JS_sint_add$sint_2778
                                  // FJARGdarg($list(I1BNDcons(I1TNM(318);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(318))))),I1BNDcons(I1TNM(319);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(319)))))))
                                  // I1CMP:start
                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                let jsxtnm320 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm316, jsxtnm317))
                                jsxtnm321 = jsxtnm320
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(321))
                              return jsxtnm321
                            } // endtimp(sint_add$sint(936))
                            let jsxtnm323 = XATSDAPP(jsxtnm322(jsxtnm256, XATSINT1(1)))
                            let jsxtnm324 = XATSDAPP(jsxtnm315(jsxtnm240, jsxtnm323))
                            jsxtnm325 = jsxtnm312
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(325))
                          return jsxtnm325
                        } // endtimp(forall$test0(1422))
                        let jsxtnm327 = XATSDAPP(jsxtnm326(jsxtnm250))
                        // I1CMP:return:I1Vtnm(I1TNM(327))
                        return jsxtnm327
                      } // endfun(test_2076)
                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
                      // I1FUNDCL
                      function free_2128(arg1)
                      { // fun
                        let jsxtnm328 = arg1
                        // I1CMP:start
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                        // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                        // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                        // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                        let jsxtnm331 = function (arg1) { // timp: g_free(23)
                          let jsxtnm329 = arg1
                          // I1CMP:start
                          let jsxtnm330 = XATSTUP0([])
                          // I1CMP:return:I1Vtnm(I1TNM(330))
                          return jsxtnm330
                        } // endtimp(g_free(23))
                        let jsxtnm332 = XATSDAPP(jsxtnm331(jsxtnm328))
                        // I1CMP:return:I1Vtnm(I1TNM(332))
                        return jsxtnm332
                      } // endfun(free_2128)
                      let jsxtnm333 = XATSDAPP(XATS2JS_list_vt_forall0$f1un(jsxtnm249, test_2076, free_2128))
                      jsxtnm334 = jsxtnm333
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(334))
                    return jsxtnm334
                  } // endtimp(list_vt_forall0(2062))
                  jsxtnm336 = jsxtnm335
                  let jsxtnm337 = XATSDAPP(jsxtnm336(jsxtnm238))
                  jsxtnm338 = jsxtnm337
                } // endlet
                jsxtnm339 = jsxtnm338
                XATS000_patck(true)
                jsxtnm340 = jsxtnm339
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(340))
              return jsxtnm340
            } // endtimp(gseq_iforall0(1735))
            let jsxtnm342 = XATSDAPP(jsxtnm341(jsxtnm182))
            let jsxtnm343 = XATSDAPP(jsxtnm237(jsxtnm342))
            jsxtnm442 = jsxtnm343
          } else {
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
            // I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
            // T1IMPallx(gseq_iforitm0(1759);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
            // T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
            let jsxtnm440 = function (arg1) { // timp: gseq_iforitm0(1759)
              let jsxtnm344 = arg1
              // I1CMP:start
              let jsxtnm439 // let
              { // let
                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                // I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
                let jsxtnm438 // let
                { // let
                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
                  // I1VALDCL
                  let jsxtnm437
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
                  // I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
                  // T1IMPallx(gseq_iforall0(1735);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
                  // T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
                  let jsxtnm435 = function (arg1) { // timp: gseq_iforall0(1735)
                    let jsxtnm350 = arg1
                    // I1CMP:start
                    let jsxtnm434 // let
                    { // let
                      // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
                      // I1VARDCL
                      // I1CMP:start
                      // I1CMP:return:I1Vint(T_INT01(0))
                      let jsxtnm351 = XATSVAR1(XATSINT1(0))
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
                      // I1VALDCL
                      let jsxtnm352
                      jsxtnm352 = XATSADDR(jsxtnm351)
                      XATS000_patck(true)
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
                      // I1VALDCL
                      let jsxtnm433
                      let jsxtnm432 // let
                      { // let
                        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                        // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
                        // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
                        // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
                        // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
                        let jsxtnm430
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
                        // I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
                        // T1IMPallx(list_vt_forall0(2062);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
                        // T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8842],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8842])))))))
                        let jsxtnm429 = function (arg1) { // timp: list_vt_forall0(2062)
                          let jsxtnm361 = arg1
                          // I1CMP:start
                          let jsxtnm428 // let
                          { // let
                            // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
                            // I1FUNDCL
                            function test_2076(arg1)
                            { // fun
                              let jsxtnm362 = arg1
                              // I1CMP:start
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                              // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                              // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                              // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                              let jsxtnm420 = function (arg1) { // timp: forall$test0(1422)
                                let jsxtnm363 = arg1
                                // I1CMP:start
                                let jsxtnm419 // let
                                { // let
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                                  // I1VALDCL
                                  let jsxtnm368
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                                  // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                  // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                  let jsxtnm366 = function (arg1) { // timp: p2tr_get(2309)
                                    let jsxtnm364 = arg1
                                    // I1CMP:start
                                    let jsxtnm365 = XATS000_dp2tr(jsxtnm364)
                                    // I1CMP:return:I1Vtnm(I1TNM(365))
                                    return jsxtnm365
                                  } // endtimp(p2tr_get(2309))
                                  let jsxtnm367 = XATSDAPP(jsxtnm366(jsxtnm352))
                                  jsxtnm368 = jsxtnm367
                                  XATS000_patck(true)
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                                  // I1VALDCL
                                  let jsxtnm406
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                                  // I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                                  // T1IMPallx(iforall$test0(1432);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                                  // T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                  let jsxtnm404 = function (arg1, arg2) { // timp: iforall$test0(1432)
                                    let jsxtnm369 = arg1
                                    let jsxtnm370 = arg2
                                    // I1CMP:start
                                    let jsxtnm403 // let
                                    { // let
                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                                      // I1VALDCL
                                      let jsxtnm402
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                                      // I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                                      // T1IMPallx(iforitm$work0(1448);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                                      // T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                      let jsxtnm400 = function (arg1, arg2) { // timp: iforitm$work0(1448)
                                        let jsxtnm371 = arg1
                                        let jsxtnm372 = arg2
                                        // I1CMP:start
                                        let jsxtnm399 // let
                                        { // let
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                                          // I1VALDCL
                                          let jsxtnm390
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                                          // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                          // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                          // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                          let jsxtnm379 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                            let jsxtnm373 = arg1
                                            let jsxtnm374 = arg2
                                            // I1CMP:start
                                            let jsxtnm378 // let
                                            { // let
                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                              // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                              // XATS2JS_sint_gt$sint_1876
                                                // FJARGdarg($list(I1BNDcons(I1TNM(375);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(375))))),I1BNDcons(I1TNM(376);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(376)))))))
                                                // I1CMP:start
                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                              let jsxtnm377 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm373, jsxtnm374))
                                              jsxtnm378 = jsxtnm377
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(378))
                                            return jsxtnm378
                                          } // endtimp(sint_gt$sint(928))
                                          let jsxtnm380 = XATSDAPP(jsxtnm379(jsxtnm371, XATSINT1(0)))
                                          let jsxtnm389 // ift
                                          if (jsxtnm380) // ift
                                          {
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                                            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                            let jsxtnm385 = function (arg1) { // timp: strn_print(1040)
                                              let jsxtnm381 = arg1
                                              // I1CMP:start
                                              let jsxtnm384 // let
                                              { // let
                                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                // I1FUNDCL: XATS2JS_strn_print(5082)
                                                // XATS2JS_strn_print_2202
                                                  // FJARGdarg($list(I1BNDcons(I1TNM(382);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(382)))))))
                                                  // I1CMP:start
                                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                let jsxtnm383 = XATSDAPP(XATS2JS_strn_print(jsxtnm381))
                                                jsxtnm384 = jsxtnm383
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(384))
                                              return jsxtnm384
                                            } // endtimp(strn_print(1040))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                                            // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                            // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                                            // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                                            let jsxtnm386 = function () { // timp: gseq$sep(348)
                                              // I1CMP:start
                                              // I1CMP:return:I1Vstr(...)
                                              return XATSSTRN(",")
                                            } // endtimp(gseq$sep(348))
                                            let jsxtnm387 = XATSDAPP(jsxtnm386())
                                            let jsxtnm388 = XATSDAPP(jsxtnm385(jsxtnm387))
                                            jsxtnm389 = jsxtnm388
                                          } else {
                                          } // end(if)
                                          jsxtnm390 = jsxtnm389
                                          XATS000_patck(true)
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                                          // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                          // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                                          // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                                          let jsxtnm397
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                                          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                                          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                          let jsxtnm396
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                          // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                          // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                          // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                          let jsxtnm395 = function (arg1) { // timp: sint_print(922)
                                            let jsxtnm391 = arg1
                                            // I1CMP:start
                                            let jsxtnm394 // let
                                            { // let
                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                              // I1FUNDCL: XATS2JS_sint_print(4946)
                                              // XATS2JS_sint_print_3707
                                                // FJARGdarg($list(I1BNDcons(I1TNM(392);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(392)))))))
                                                // I1CMP:start
                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                              let jsxtnm393 = XATSDAPP(XATS2JS_sint_print(jsxtnm391))
                                              jsxtnm394 = jsxtnm393
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(394))
                                            return jsxtnm394
                                          } // endtimp(sint_print(922))
                                          jsxtnm396 = jsxtnm395
                                          jsxtnm397 = jsxtnm396
                                          let jsxtnm398 = XATSDAPP(jsxtnm397(jsxtnm372))
                                          jsxtnm399 = jsxtnm398
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(399))
                                        return jsxtnm399
                                      } // endtimp(iforitm$work0(1448))
                                      let jsxtnm401 = XATSDAPP(jsxtnm400(jsxtnm369, jsxtnm370))
                                      jsxtnm402 = jsxtnm401
                                      XATS000_patck(true)
                                      jsxtnm403 = XATSBOOL(true)
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(403))
                                    return jsxtnm403
                                  } // endtimp(iforall$test0(1432))
                                  let jsxtnm405 = XATSDAPP(jsxtnm404(jsxtnm368, jsxtnm363))
                                  jsxtnm406 = jsxtnm405
                                  XATS000_patck(true)
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                                  // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                  // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                  let jsxtnm409 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                    let jsxtnm407 = arg1
                                    let jsxtnm408 = arg2
                                    // I1CMP:start
                                    XATS000_assgn(jsxtnm407, jsxtnm408)
                                    // I1CMP:return:I1V000()
                                    return XATSVOID
                                  } // endtimp(p2tr_set(2310))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                                  // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                  // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                  // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                  let jsxtnm416 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                    let jsxtnm410 = arg1
                                    let jsxtnm411 = arg2
                                    // I1CMP:start
                                    let jsxtnm415 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                      // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                      // XATS2JS_sint_add$sint_2778
                                        // FJARGdarg($list(I1BNDcons(I1TNM(412);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(412))))),I1BNDcons(I1TNM(413);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(413)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm414 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm410, jsxtnm411))
                                      jsxtnm415 = jsxtnm414
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(415))
                                    return jsxtnm415
                                  } // endtimp(sint_add$sint(936))
                                  let jsxtnm417 = XATSDAPP(jsxtnm416(jsxtnm368, XATSINT1(1)))
                                  let jsxtnm418 = XATSDAPP(jsxtnm409(jsxtnm352, jsxtnm417))
                                  jsxtnm419 = jsxtnm406
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(419))
                                return jsxtnm419
                              } // endtimp(forall$test0(1422))
                              let jsxtnm421 = XATSDAPP(jsxtnm420(jsxtnm362))
                              // I1CMP:return:I1Vtnm(I1TNM(421))
                              return jsxtnm421
                            } // endfun(test_2076)
                            // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
                            // I1FUNDCL
                            function free_2128(arg1)
                            { // fun
                              let jsxtnm422 = arg1
                              // I1CMP:start
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                              // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                              // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                              // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                              let jsxtnm425 = function (arg1) { // timp: g_free(23)
                                let jsxtnm423 = arg1
                                // I1CMP:start
                                let jsxtnm424 = XATSTUP0([])
                                // I1CMP:return:I1Vtnm(I1TNM(424))
                                return jsxtnm424
                              } // endtimp(g_free(23))
                              let jsxtnm426 = XATSDAPP(jsxtnm425(jsxtnm422))
                              // I1CMP:return:I1Vtnm(I1TNM(426))
                              return jsxtnm426
                            } // endfun(free_2128)
                            let jsxtnm427 = XATSDAPP(XATS2JS_list_vt_forall0$f1un(jsxtnm361, test_2076, free_2128))
                            jsxtnm428 = jsxtnm427
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(428))
                          return jsxtnm428
                        } // endtimp(list_vt_forall0(2062))
                        jsxtnm430 = jsxtnm429
                        let jsxtnm431 = XATSDAPP(jsxtnm430(jsxtnm350))
                        jsxtnm432 = jsxtnm431
                      } // endlet
                      jsxtnm433 = jsxtnm432
                      XATS000_patck(true)
                      jsxtnm434 = jsxtnm433
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(434))
                    return jsxtnm434
                  } // endtimp(gseq_iforall0(1735))
                  let jsxtnm436 = XATSDAPP(jsxtnm435(jsxtnm344))
                  jsxtnm437 = jsxtnm436
                  XATS000_patck(true)
                  jsxtnm438 = XATSVOID
                } // endlet
                jsxtnm439 = jsxtnm438
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(439))
              return jsxtnm439
            } // endtimp(gseq_iforitm0(1759))
            let jsxtnm441 = XATSDAPP(jsxtnm440(jsxtnm182))
            jsxtnm442 = jsxtnm441
          } // end(if)
          jsxtnm443 = jsxtnm442
        } // endlet
        jsxtnm444 = jsxtnm443
        XATS000_patck(true)
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
        // I1VALDCL
        let jsxtnm453
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm449 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm445 = arg1
          // I1CMP:start
          let jsxtnm448 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(446);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(446)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm447 = XATSDAPP(XATS2JS_strn_print(jsxtnm445))
            jsxtnm448 = jsxtnm447
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(448))
          return jsxtnm448
        } // endtimp(strn_print(1040))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
        // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
        // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8495])))),@(x0[1070],T2Pvar(x0[8495])))))))
        let jsxtnm450 = function () { // timp: gseq$end(347)
          // I1CMP:start
          // I1CMP:return:I1Vstr(...)
          return XATSSTRN(")")
        } // endtimp(gseq$end(347))
        let jsxtnm451 = XATSDAPP(jsxtnm450())
        let jsxtnm452 = XATSDAPP(jsxtnm449(jsxtnm451))
        jsxtnm453 = jsxtnm452
        XATS000_patck(true)
        jsxtnm454 = XATSVOID
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(454))
      return jsxtnm454
    } // endtimp(gseq_print0(1686))
    let jsxtnm456 = XATSDAPP(jsxtnm455(jsxtnm181))
    // I1CMP:return:I1Vtnm(I1TNM(456))
    return jsxtnm456
  } // endtimp(g_print0(1411))
  let jsxtnm458 = XATSDAPP(jsxtnm457(jsxtnm168))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1982(line=83,offs=21)--1990(line=83,offs=29))
  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x2[8305])))))
  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  let jsxtnm465
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm464
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm463 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm459 = arg1
    // I1CMP:start
    let jsxtnm462 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(460);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(460)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm461 = XATSDAPP(XATS2JS_strn_print(jsxtnm459))
      jsxtnm462 = jsxtnm461
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(462))
    return jsxtnm462
  } // endtimp(strn_print(1040))
  jsxtnm464 = jsxtnm463
  jsxtnm465 = jsxtnm464
  let jsxtnm466 = XATSDAPP(jsxtnm465(jsxtnm169))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(2002(line=84,offs=3)--2015(line=84,offs=16))
  // I0Etapq(I0Ecst(gs_print0$end(1971)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1466(line=46,offs=1)--1479(line=46,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(gs_print0$end(1971);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1479(line=46,offs=1)--1518(line=48,offs=21)))
  // T1IMPallx(gs_print0$end(1971)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$end(1971);$list()))))
  let jsxtnm468 = function () { // timp: gs_print0$end(1971)
    // I1CMP:start
    let jsxtnm467 = XATSTUP0([])
    // I1CMP:return:I1Vtnm(I1TNM(467))
    return jsxtnm467
  } // endtimp(gs_print0$end(1971))
  let jsxtnm469 = XATSDAPP(jsxtnm468())
  // I1CMP:return:I1Vtnm(I1TNM(469))
  return jsxtnm469
} // endtimp(gs_print0_a3(1976))
let jsxtnm471 = XATSDAPP(jsxtnm470(XATSSTRN("ns = "), jsxtnm166, XATSSTRN("\n")))
jsxtnm472 = jsxtnm471
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(703(line=48,offs=1)--742(line=50,offs=18)))
// I1VALDCL
let jsxtnm537
// LCSRCsome1(test09_llist00.dats)@(712(line=49,offs=1)--724(line=49,offs=13))
// I0Etapq(I0Ecst(list_vt_make_nfun(2038)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(3083(line=156,offs=1)--3100(line=156,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(list_vt_make_nfun(2038);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2448(line=120,offs=1)--2509(line=123,offs=23)))
// T1IMPallx(list_vt_make_nfun(2038)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8493],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_make_nfun(2038);$list(@(a[5245],T2Pvar(a[8493])))))))
let jsxtnm533
// LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2487(line=123,offs=1)--2506(line=123,offs=20))
// I0Etapq(I0Ecst(nint_map$f1un_llist(969)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3824(line=192,offs=1)--3843(line=192,offs=20))));$list(T2JAG($list(T2Pvar(a[8493])))))
// T1IMPallx(nint_map$f1un_llist(969);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7232(line=482,offs=1)--7375(line=492,offs=2)))
// T1IMPallx(nint_map$f1un_llist(969)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map$f1un_llist(969);$list(@(y0[2872],T2Pvar(y0[7247])))))))
let jsxtnm532 = function (arg1, arg2) { // timp: nint_map$f1un_llist(969)
  let jsxtnm473 = arg1
  let jsxtnm474 = arg2
  // I1CMP:start
  let jsxtnm531 // let
  { // let
    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
    // I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Pvar(y0[7247]))))):timp
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7288(line=487,offs=1)--7302(line=487,offs=15))
    // I0Etapq(I0Ecst(nint_map_llist(968)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3756(line=187,offs=1)--3770(line=187,offs=15))));$list(T2JAG($list(T2Pvar(y0[7247])))))
    // T1IMPallx(nint_map_llist(968);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6864(line=449,offs=1)--7193(line=480,offs=2)))
    // T1IMPallx(nint_map_llist(968)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7246],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map_llist(968);$list(@(y0[2870],T2Pvar(y0[7246])))))))
    let jsxtnm529 = function (arg1) { // timp: nint_map_llist(968)
      let jsxtnm477 = arg1
      // I1CMP:start
      let jsxtnm528 // let
      { // let
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6958(line=459,offs=1)--6983(line=460,offs=17))
        // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(ys;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(3;vtbx)));list_vt);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));y0[7246])))))))
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6987(line=462,offs=1)--7009(line=463,offs=19)))
        // I1VALDCL
        let jsxtnm479
        let jsxtnm478 = XATSCAPP("list_vt_nil", [0])
        jsxtnm479 = jsxtnm478
        XATS000_patck(true)
        // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7013(line=465,offs=1)--7188(line=478,offs=2)))
        // I1FUNDCL
        function loop_7016(arg1, arg2)
        { // fun
          let jsxtnm480 = arg1
          let jsxtnm481 = arg2
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7054(line=470,offs=5)--7056(line=470,offs=7))
          // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
          // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
          // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
          let jsxtnm488 = function (arg1, arg2) { // timp: sint_gte$sint(931)
            let jsxtnm482 = arg1
            let jsxtnm483 = arg2
            // I1CMP:start
            let jsxtnm487 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
              // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
              // XATS2JS_sint_gte$sint_2399
                // FJARGdarg($list(I1BNDcons(I1TNM(484);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(484))))),I1BNDcons(I1TNM(485);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(485)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
              let jsxtnm486 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm482, jsxtnm483))
              jsxtnm487 = jsxtnm486
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(487))
            return jsxtnm487
          } // endtimp(sint_gte$sint(931))
          let jsxtnm489 = XATSDAPP(jsxtnm488(jsxtnm480, jsxtnm477))
          let jsxtnm506 // ift
          if (jsxtnm489) // ift
          {
            jsxtnm506 = jsxtnm481
          } else {
            let jsxtnm505 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7078(line=473,offs=1)--7107(line=473,offs=30)))
              // I1VALDCL
              let jsxtnm494
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7087(line=473,offs=10)--7095(line=473,offs=18))
              // I0Etapq(I0Ecst(map$fopr(77)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(4030(line=256,offs=1)--4038(line=256,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Pvar(y0[7246])))))
              // T1IMPallx(map$fopr(77);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
              // T1IMPallx(map$fopr(77)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm492 = function (arg1) { // timp: map$fopr(77)
                let jsxtnm490 = arg1
                // I1CMP:start
                let jsxtnm491 = XATSDAPP(jsxtnm474(jsxtnm490))
                // I1CMP:return:I1Vtnm(I1TNM(491))
                return jsxtnm491
              } // endtimp(map$fopr(77))
              let jsxtnm493 = XATSDAPP(jsxtnm492(jsxtnm480))
              jsxtnm494 = jsxtnm493
              XATS000_patck(true)
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7125(line=476,offs=8)--7126(line=476,offs=9))
              // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
              // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
              // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
              let jsxtnm501 = function (arg1, arg2) { // timp: sint_add$sint(936)
                let jsxtnm495 = arg1
                let jsxtnm496 = arg2
                // I1CMP:start
                let jsxtnm500 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                  // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                  // XATS2JS_sint_add$sint_2778
                    // FJARGdarg($list(I1BNDcons(I1TNM(497);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(497))))),I1BNDcons(I1TNM(498);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(498)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                  let jsxtnm499 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm495, jsxtnm496))
                  jsxtnm500 = jsxtnm499
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(500))
                return jsxtnm500
              } // endtimp(sint_add$sint(936))
              let jsxtnm502 = XATSDAPP(jsxtnm501(jsxtnm480, XATSINT1(1)))
              let jsxtnm503 = XATSCAPP("list_vt_cons", [1, jsxtnm494, jsxtnm481])
              let jsxtnm504 = XATSDAPP(loop_7016(jsxtnm502, jsxtnm503))
              jsxtnm505 = jsxtnm504
            } // endlet
            jsxtnm506 = jsxtnm505
          } // end(if)
          // I1CMP:return:I1Vtnm(I1TNM(506))
          return jsxtnm506
        } // endfun(loop_7016)
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6911(line=454,offs=1)--6927(line=454,offs=17))
        // I0Etapq(I0Ecst(list_vt_reverse0(2046)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4474(line=255,offs=1)--4490(line=255,offs=17))));$list(T2JAG($list(T2Pvar(y0[7246])))))
        // T1IMPallx(list_vt_reverse0(2046);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7033(line=475,offs=1)--7120(line=478,offs=46)))
        // T1IMPallx(list_vt_reverse0(2046)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8528],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_reverse0(2046);$list(@(x0[5264],T2Pvar(a[8528])))))))
        let jsxtnm525 = function (arg1) { // timp: list_vt_reverse0(2046)
          let jsxtnm507 = arg1
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7075(line=478,offs=1)--7092(line=478,offs=18))
          // I0Etapq(I0Ecst(list_vt_rappend00(2049)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4855(line=281,offs=1)--4872(line=281,offs=18))));$list(T2JAG($list(T2Pvar(a[8528])))))
          // T1IMPallx(list_vt_rappend00(2049);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6363(line=426,offs=1)--6772(line=458,offs=2)))
          // T1IMPallx(list_vt_rappend00(2049)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8524],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_rappend00(2049);$list(@(x0[5271],T2Pvar(a[8524])))))))
          let jsxtnm522 = function (arg1, arg2) { // timp: list_vt_rappend00(2049)
            let jsxtnm508 = arg1
            let jsxtnm509 = arg2
            // I1CMP:start
            let jsxtnm521 // let
            { // let
              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6442(line=434,offs=1)--6733(line=456,offs=2)))
              // I1FUNDCL
              function loop_6445(arg1, arg2)
              { // fun
                let jsxtnm510 = arg1
                let jsxtnm511 = arg2
                // I1CMP:start
                let jsxtnm519 // cas
                do {
                  // { // cls
                  // I1GPTpat(I1BNDcons(I1TNM(512);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
                  if (XATS000_ctgeq(jsxtnm510, XATSCTAG("list_vt_nil",0))) { // gpt
                    let jsxtnm512 = jsxtnm510
                    jsxtnm519 = jsxtnm511
                    break // cls
                  } // gpt
                  // } // cls
                  // { // cls
                  // I1GPTpat(I1BNDcons(I1TNM(513);I0Pflat(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pany())));$list()))
                  if (XATS000_ctgeq(jsxtnm510, XATSCTAG("list_vt_cons",1))) { // gpt
                    let jsxtnm513 = jsxtnm510
                    let jsxtnm518 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6616(line=450,offs=3)--6631(line=450,offs=18)))
                      // I1VALDCL
                      let jsxtnm515
                      let jsxtnm514 = XATSPCON(jsxtnm510,1)
                      jsxtnm515 = jsxtnm514
                      XATS000_patck(true)
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6634(line=451,offs=3)--6656(line=451,offs=25)))
                      // I1VALDCL
                      let jsxtnm516
                      XATS000_assgn(XATSLPCN(1, jsxtnm510), jsxtnm511)
                      jsxtnm516 = XATSVOID
                      XATS000_patck(true)
                      XATS000_fold(jsxtnm510)
                      let jsxtnm517 = XATSDAPP(loop_6445(jsxtnm515, jsxtnm510))
                      jsxtnm518 = jsxtnm517
                    } // endlet
                    jsxtnm519 = jsxtnm518
                    break // cls
                  } // gpt
                  // } // cls
                  XATS000_cfail()
                } while (false) // end-of(do)
                // I1CMP:return:I1Vtnm(I1TNM(519))
                return jsxtnm519
              } // endfun(loop_6445)
              let jsxtnm520 = XATSDAPP(loop_6445(jsxtnm508, jsxtnm509))
              jsxtnm521 = jsxtnm520
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(521))
            return jsxtnm521
          } // endtimp(list_vt_rappend00(2049))
          let jsxtnm523 = XATSCAPP("list_vt_nil", [0])
          let jsxtnm524 = XATSDAPP(jsxtnm522(jsxtnm507, jsxtnm523))
          // I1CMP:return:I1Vtnm(I1TNM(524))
          return jsxtnm524
        } // endtimp(list_vt_reverse0(2046))
        let jsxtnm526 = XATSDAPP(loop_7016(XATSINT1(0), jsxtnm479))
        let jsxtnm527 = XATSDAPP(jsxtnm525(jsxtnm526))
        jsxtnm528 = jsxtnm527
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(528))
      return jsxtnm528
    } // endtimp(nint_map_llist(968))
    let jsxtnm530 = XATSDAPP(jsxtnm529(jsxtnm473))
    jsxtnm531 = jsxtnm530
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(531))
  return jsxtnm531
} // endtimp(nint_map$f1un_llist(969))
jsxtnm533 = jsxtnm532
let jsxtnm535 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm534 = arg1
  // I1CMP:start
  // I1CMP:return:I1Vtnm(I1TNM(534))
  return jsxtnm534
} // endfun(lam0)
let jsxtnm536 = XATSDAPP(jsxtnm533(XATSINT1(10), jsxtnm535))
jsxtnm537 = jsxtnm536
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(743(line=51,offs=1)--785(line=52,offs=34)))
// I1VALDCL
let jsxtnm576
// LCSRCsome1(test09_llist00.dats)@(752(line=52,offs=1)--763(line=52,offs=12))
// I0Etapq(I0Ecst(list_vt_maprev0$f1un(2109)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(5822(line=357,offs=1)--5842(line=357,offs=21))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(list_vt_maprev0$f1un(2109);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5904(line=371,offs=1)--6049(line=380,offs=2)))
// T1IMPallx(list_vt_maprev0$f1un(2109)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8576],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8577],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_maprev0$f1un(2109);$list(@(x0[5362],T2Pvar(x0[8576])),@(y0[5363],T2Pvar(y0[8577])))))))
let jsxtnm564 = function (arg1, arg2) { // timp: list_vt_maprev0$f1un(2109)
  let jsxtnm538 = arg1
  let jsxtnm539 = arg2
  // I1CMP:start
  let jsxtnm563 // let
  { // let
    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(6008(line=379,offs=1)--6047(line=379,offs=40)))
    // I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Pvar(x0[8576])),@(y0[3858],T2Pvar(y0[8577]))))):timp
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5971(line=377,offs=3)--5986(line=377,offs=18))
    // I0Etapq(I0Ecst(list_vt_maprev0(2107)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(5556(line=341,offs=1)--5571(line=341,offs=16))));$list(T2JAG($list(T2Pvar(x0[8576]))),T2JAG($list(T2Pvar(y0[8577])))))
    // T1IMPallx(list_vt_maprev0(2107);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5474(line=335,offs=1)--5860(line=369,offs=2)))
    // T1IMPallx(list_vt_maprev0(2107)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8572],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8573],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_maprev0(2107);$list(@(x0[5356],T2Pvar(x0[8572])),@(y0[5357],T2Pvar(y0[8573])))))))
    let jsxtnm561 = function (arg1) { // timp: list_vt_maprev0(2107)
      let jsxtnm542 = arg1
      // I1CMP:start
      let jsxtnm560 // let
      { // let
        // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5586(line=347,offs=1)--5855(line=367,offs=2)))
        // I1FUNDCL
        function loop_5589(arg1, arg2)
        { // fun
          let jsxtnm543 = arg1
          let jsxtnm544 = arg2
          // I1CMP:start
          let jsxtnm555 // cas
          do {
            // { // cls
            // I1GPTpat(I1BNDcons(I1TNM(545);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
            if (XATS000_ctgeq(jsxtnm543, XATSCTAG("list_vt_nil",0))) { // gpt
              let jsxtnm545 = jsxtnm543
              jsxtnm555 = jsxtnm544
              break // cls
            } // gpt
            // } // cls
            // { // cls
            // I1GPTpat(I1BNDcons(I1TNM(546);I0Pfree(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x0(4384)),I0Pvar(xs(4385)))));$list(@(x0(4384),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(546));0)),@(xs(4385),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(546));1)))))
            if (XATS000_ctgeq(jsxtnm543, XATSCTAG("list_vt_cons",1))) { // gpt
              let jsxtnm546 = jsxtnm543
              let jsxtnm554 // let
              { // let
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5748(line=362,offs=3)--5780(line=363,offs=24)))
                // I1VALDCL
                let jsxtnm551
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5759(line=363,offs=3)--5768(line=363,offs=12))
                // I0Etapq(I0Ecst(map$fopr0(1484)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(5345(line=363,offs=1)--5354(line=363,offs=10))));$list(T2JAG($list(T2Pvar(x0[8572]))),T2JAG($list(T2Pvar(y0[8573])))))
                // T1IMPallx(map$fopr0(1484);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(6008(line=379,offs=1)--6047(line=379,offs=40)))
                // T1IMPallx(map$fopr0(1484)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8576],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8577],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[3858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                let jsxtnm549 = function (arg1) { // timp: map$fopr0(1484)
                  let jsxtnm547 = arg1
                  // I1CMP:start
                  let jsxtnm548 = XATSDAPP(jsxtnm539(jsxtnm547))
                  // I1CMP:return:I1Vtnm(I1TNM(548))
                  return jsxtnm548
                } // endtimp(map$fopr0(1484))
                let jsxtnm550 = XATSDAPP(jsxtnm549(XATSP1CN("list_vt_cons", jsxtnm546[0+1])))
                jsxtnm551 = jsxtnm550
                XATS000_patck(true)
                let jsxtnm552 = XATSCAPP("list_vt_cons", [1, jsxtnm551, jsxtnm544])
                let jsxtnm553 = XATSDAPP(loop_5589(XATSP1CN("list_vt_cons", jsxtnm546[1+1]), jsxtnm552))
                jsxtnm554 = jsxtnm553
              } // endlet
              jsxtnm555 = jsxtnm554
              break // cls
            } // gpt
            // } // cls
            XATS000_cfail()
          } while (false) // end-of(do)
          // I1CMP:return:I1Vtnm(I1TNM(555))
          return jsxtnm555
        } // endfun(loop_5589)
        let jsxtnm559 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5525(line=341,offs=1)--5547(line=342,offs=14)))
          // I1VALDCL
          let jsxtnm557
          let jsxtnm556 = XATSCAPP("list_vt_nil", [0])
          jsxtnm557 = jsxtnm556
          XATS000_patck(true)
          let jsxtnm558 = XATSDAPP(loop_5589(jsxtnm542, jsxtnm557))
          jsxtnm559 = jsxtnm558
        } // endlet
        jsxtnm560 = jsxtnm559
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(560))
      return jsxtnm560
    } // endtimp(list_vt_maprev0(2107))
    let jsxtnm562 = XATSDAPP(jsxtnm561(jsxtnm538))
    jsxtnm563 = jsxtnm562
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(563))
  return jsxtnm563
} // endtimp(list_vt_maprev0$f1un(2109))
let jsxtnm574 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm565 = arg1
  // I1CMP:start
  // LCSRCsome1(test09_llist00.dats)@(782(line=52,offs=31)--783(line=52,offs=32))
  // I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(sint_mul$sint(938);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
  // T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
  let jsxtnm572 = function (arg1, arg2) { // timp: sint_mul$sint(938)
    let jsxtnm566 = arg1
    let jsxtnm567 = arg2
    // I1CMP:start
    let jsxtnm571 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3111(line=182,offs=1)--3175(line=184,offs=39))
      // I1FUNDCL: XATS2JS_sint_mul$sint(4932)
      // XATS2JS_sint_mul$sint_3114
        // FJARGdarg($list(I1BNDcons(I1TNM(568);I0Pvar(i1(4933));$list(@(i1(4933),I1Vtnm(I1TNM(568))))),I1BNDcons(I1TNM(569);I0Pvar(i2(4934));$list(@(i2(4934),I1Vtnm(I1TNM(569)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_mul$sint);G1Nlist($list()))// I1CMP:return
      let jsxtnm570 = XATSDAPP(XATS2JS_sint_mul$sint(jsxtnm566, jsxtnm567))
      jsxtnm571 = jsxtnm570
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(571))
    return jsxtnm571
  } // endtimp(sint_mul$sint(938))
  let jsxtnm573 = XATSDAPP(jsxtnm572(jsxtnm565, jsxtnm565))
  // I1CMP:return:I1Vtnm(I1TNM(573))
  return jsxtnm573
} // endfun(lam0)
let jsxtnm575 = XATSDAPP(jsxtnm564(jsxtnm537, jsxtnm574))
jsxtnm576 = jsxtnm575
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(786(line=53,offs=1)--821(line=53,offs=36)))
// I1VALDCL
let jsxtnm882
// LCSRCsome1(test09_llist00.dats)@(795(line=53,offs=10)--802(line=53,offs=17))
// I0Etapq(I0Ecst(gs_print0_a3(1976)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1751(line=73,offs=1)--1763(line=73,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
// T1IMPallx(gs_print0_a3(1976);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1853(line=75,offs=1)--2020(line=84,offs=21)))
// T1IMPallx(gs_print0_a3(1976)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8303],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8304],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[8305],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print0_a3(1976);$list(@(x0[5041],T2Pvar(x0[8303])),@(x1[5042],T2Pvar(x1[8304])),@(x2[5043],T2Pvar(x2[8305])))))))
let jsxtnm880 = function (arg1, arg2, arg3) { // timp: gs_print0_a3(1976)
  let jsxtnm577 = arg1
  let jsxtnm578 = arg2
  let jsxtnm579 = arg3
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1924(line=81,offs=3)--1937(line=81,offs=16))
  // I0Etapq(I0Ecst(gs_print0$beg(1970)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1430(line=43,offs=1)--1443(line=43,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(gs_print0$beg(1970);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1436(line=42,offs=1)--1475(line=44,offs=21)))
  // T1IMPallx(gs_print0$beg(1970)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$beg(1970);$list()))))
  let jsxtnm581 = function () { // timp: gs_print0$beg(1970)
    // I1CMP:start
    let jsxtnm580 = XATSTUP0([])
    // I1CMP:return:I1Vtnm(I1TNM(580))
    return jsxtnm580
  } // endtimp(gs_print0$beg(1970))
  let jsxtnm582 = XATSDAPP(jsxtnm581())
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1945(line=82,offs=3)--1953(line=82,offs=11))
  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[8303])))))
  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  let jsxtnm589
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm588
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm587 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm583 = arg1
    // I1CMP:start
    let jsxtnm586 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(584);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(584)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm585 = XATSDAPP(XATS2JS_strn_print(jsxtnm583))
      jsxtnm586 = jsxtnm585
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(586))
    return jsxtnm586
  } // endtimp(strn_print(1040))
  jsxtnm588 = jsxtnm587
  jsxtnm589 = jsxtnm588
  let jsxtnm590 = XATSDAPP(jsxtnm589(jsxtnm577))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1964(line=83,offs=3)--1972(line=83,offs=11))
  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x1[8304])))))
  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2815(line=148,offs=1)--2899(line=154,offs=2)))
  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8497])))))))))
  let jsxtnm867 = function (arg1) { // timp: g_print0(1411)
    let jsxtnm591 = arg1
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2865(line=153,offs=1)--2876(line=153,offs=12))
    // I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[8497]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[8497])))))
    // T1IMPallx(gseq_print0(1686);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    // T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    let jsxtnm865 = function (arg1) { // timp: gseq_print0(1686)
      let jsxtnm592 = arg1
      // I1CMP:start
      let jsxtnm864 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
        // I1VALDCL
        let jsxtnm601
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm597 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm593 = arg1
          // I1CMP:start
          let jsxtnm596 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(594);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(594)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm595 = XATSDAPP(XATS2JS_strn_print(jsxtnm593))
            jsxtnm596 = jsxtnm595
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(596))
          return jsxtnm596
        } // endtimp(strn_print(1040))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
        // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
        // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8496])))),@(x0[1068],T2Pvar(x0[8496])))))))
        let jsxtnm598 = function () { // timp: gseq$beg(346)
          // I1CMP:start
          // I1CMP:return:I1Vstr(...)
          return XATSSTRN("list_vt(")
        } // endtimp(gseq$beg(346))
        let jsxtnm599 = XATSDAPP(jsxtnm598())
        let jsxtnm600 = XATSDAPP(jsxtnm597(jsxtnm599))
        jsxtnm601 = jsxtnm600
        XATS000_patck(true)
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
        // I1VALDCL
        let jsxtnm854
        let jsxtnm853 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
          // I1VALDCL
          let jsxtnm610
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
          // I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
          // T1IMPallx(gseq$prlen(350);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
          // T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
          let jsxtnm608 = function () { // timp: gseq$prlen(350)
            // I1CMP:start
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
            // I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
            // T1IMPallx(sint_neg(923);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
            // T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
            let jsxtnm606 = function (arg1) { // timp: sint_neg(923)
              let jsxtnm602 = arg1
              // I1CMP:start
              let jsxtnm605 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1514(line=49,offs=1)--1563(line=51,offs=29))
                // I1FUNDCL: XATS2JS_sint_neg(4888)
                // XATS2JS_sint_neg_1517
                  // FJARGdarg($list(I1BNDcons(I1TNM(603);I0Pvar(i1(4889));$list(@(i1(4889),I1Vtnm(I1TNM(603)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_neg);G1Nlist($list()))// I1CMP:return
                let jsxtnm604 = XATSDAPP(XATS2JS_sint_neg(jsxtnm602))
                jsxtnm605 = jsxtnm604
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(605))
              return jsxtnm605
            } // endtimp(sint_neg(923))
            let jsxtnm607 = XATSDAPP(jsxtnm606(XATSINT1(1)))
            // I1CMP:return:I1Vtnm(I1TNM(607))
            return jsxtnm607
          } // endtimp(gseq$prlen(350))
          let jsxtnm609 = XATSDAPP(jsxtnm608())
          jsxtnm610 = jsxtnm609
          XATS000_patck(true)
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
          // I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
          // I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
          // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
          // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
          // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
          let jsxtnm643 = function (arg1, arg2) { // timp: sint_gte$sint(931)
            let jsxtnm637 = arg1
            let jsxtnm638 = arg2
            // I1CMP:start
            let jsxtnm642 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
              // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
              // XATS2JS_sint_gte$sint_2399
                // FJARGdarg($list(I1BNDcons(I1TNM(639);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(639))))),I1BNDcons(I1TNM(640);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(640)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
              let jsxtnm641 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm637, jsxtnm638))
              jsxtnm642 = jsxtnm641
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(642))
            return jsxtnm642
          } // endtimp(sint_gte$sint(931))
          let jsxtnm644 = XATSDAPP(jsxtnm643(jsxtnm610, XATSINT1(0)))
          let jsxtnm852 // ift
          if (jsxtnm644) // ift
          {
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
            // I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
            // T1IMPallx(g_void(22);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
            // T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
            let jsxtnm647 = function (arg1) { // timp: g_void(22)
              let jsxtnm645 = arg1
              // I1CMP:start
              let jsxtnm646 = XATSTUP0([])
              // I1CMP:return:I1Vtnm(I1TNM(646))
              return jsxtnm646
            } // endtimp(g_void(22))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
            // I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
            // T1IMPallx(gseq_iforall0(1735);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
            // T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
            let jsxtnm751 = function (arg1) { // timp: gseq_iforall0(1735)
              let jsxtnm648 = arg1
              // I1CMP:start
              let jsxtnm750 // let
              { // let
                // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
                // I1VARDCL
                // I1CMP:start
                // I1CMP:return:I1Vint(T_INT01(0))
                let jsxtnm649 = XATSVAR1(XATSINT1(0))
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
                // I1VALDCL
                let jsxtnm650
                jsxtnm650 = XATSADDR(jsxtnm649)
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
                // I1VALDCL
                let jsxtnm749
                let jsxtnm748 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                  // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
                  // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
                  // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
                  // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
                  let jsxtnm746
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
                  // I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
                  // T1IMPallx(list_vt_forall0(2062);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
                  // T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8842],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8842])))))))
                  let jsxtnm745 = function (arg1) { // timp: list_vt_forall0(2062)
                    let jsxtnm659 = arg1
                    // I1CMP:start
                    let jsxtnm744 // let
                    { // let
                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
                      // I1FUNDCL
                      function test_2076(arg1)
                      { // fun
                        let jsxtnm660 = arg1
                        // I1CMP:start
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                        // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                        // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                        // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        let jsxtnm736 = function (arg1) { // timp: forall$test0(1422)
                          let jsxtnm661 = arg1
                          // I1CMP:start
                          let jsxtnm735 // let
                          { // let
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                            // I1VALDCL
                            let jsxtnm666
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                            // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                            // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                            let jsxtnm664 = function (arg1) { // timp: p2tr_get(2309)
                              let jsxtnm662 = arg1
                              // I1CMP:start
                              let jsxtnm663 = XATS000_dp2tr(jsxtnm662)
                              // I1CMP:return:I1Vtnm(I1TNM(663))
                              return jsxtnm663
                            } // endtimp(p2tr_get(2309))
                            let jsxtnm665 = XATSDAPP(jsxtnm664(jsxtnm650))
                            jsxtnm666 = jsxtnm665
                            XATS000_patck(true)
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                            // I1VALDCL
                            let jsxtnm722
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                            // I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                            // T1IMPallx(iforall$test0(1432);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                            // T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                            let jsxtnm720 = function (arg1, arg2) { // timp: iforall$test0(1432)
                              let jsxtnm667 = arg1
                              let jsxtnm668 = arg2
                              // I1CMP:start
                              let jsxtnm719 // let
                              { // let
                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                                // I1VALDCL
                                let jsxtnm686
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                                // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                let jsxtnm675 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                  let jsxtnm669 = arg1
                                  let jsxtnm670 = arg2
                                  // I1CMP:start
                                  let jsxtnm674 // let
                                  { // let
                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                    // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                    // XATS2JS_sint_gt$sint_1876
                                      // FJARGdarg($list(I1BNDcons(I1TNM(671);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(671))))),I1BNDcons(I1TNM(672);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(672)))))))
                                      // I1CMP:start
                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                    let jsxtnm673 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm669, jsxtnm670))
                                    jsxtnm674 = jsxtnm673
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(674))
                                  return jsxtnm674
                                } // endtimp(sint_gt$sint(928))
                                let jsxtnm676 = XATSDAPP(jsxtnm675(jsxtnm667, XATSINT1(0)))
                                let jsxtnm685 // ift
                                if (jsxtnm676) // ift
                                {
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                                  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                  let jsxtnm681 = function (arg1) { // timp: strn_print(1040)
                                    let jsxtnm677 = arg1
                                    // I1CMP:start
                                    let jsxtnm680 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                      // I1FUNDCL: XATS2JS_strn_print(5082)
                                      // XATS2JS_strn_print_2202
                                        // FJARGdarg($list(I1BNDcons(I1TNM(678);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(678)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm679 = XATSDAPP(XATS2JS_strn_print(jsxtnm677))
                                      jsxtnm680 = jsxtnm679
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(680))
                                    return jsxtnm680
                                  } // endtimp(strn_print(1040))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                                  // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                  // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                                  // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                                  let jsxtnm682 = function () { // timp: gseq$sep(348)
                                    // I1CMP:start
                                    // I1CMP:return:I1Vstr(...)
                                    return XATSSTRN(",")
                                  } // endtimp(gseq$sep(348))
                                  let jsxtnm683 = XATSDAPP(jsxtnm682())
                                  let jsxtnm684 = XATSDAPP(jsxtnm681(jsxtnm683))
                                  jsxtnm685 = jsxtnm684
                                } else {
                                } // end(if)
                                jsxtnm686 = jsxtnm685
                                XATS000_patck(true)
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                let jsxtnm693 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                  let jsxtnm687 = arg1
                                  let jsxtnm688 = arg2
                                  // I1CMP:start
                                  let jsxtnm692 // let
                                  { // let
                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                    // XATS2JS_sint_gte$sint_2399
                                      // FJARGdarg($list(I1BNDcons(I1TNM(689);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(689))))),I1BNDcons(I1TNM(690);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(690)))))))
                                      // I1CMP:start
                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                    let jsxtnm691 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm687, jsxtnm688))
                                    jsxtnm692 = jsxtnm691
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(692))
                                  return jsxtnm692
                                } // endtimp(sint_gte$sint(931))
                                let jsxtnm694 = XATSDAPP(jsxtnm693(jsxtnm667, jsxtnm610))
                                let jsxtnm718 // ift
                                if (jsxtnm694) // ift
                                {
                                  let jsxtnm709 // let
                                  { // let
                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                                    // I1VALDCL
                                    let jsxtnm699
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                                    // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                    // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                    // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                    let jsxtnm697 = function (arg1) { // timp: g_free(23)
                                      let jsxtnm695 = arg1
                                      // I1CMP:start
                                      let jsxtnm696 = XATSTUP0([])
                                      // I1CMP:return:I1Vtnm(I1TNM(696))
                                      return jsxtnm696
                                    } // endtimp(g_free(23))
                                    let jsxtnm698 = XATSDAPP(jsxtnm697(jsxtnm668))
                                    jsxtnm699 = jsxtnm698
                                    XATS000_patck(true)
                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                                    // I1VALDCL
                                    let jsxtnm708
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                                    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                    let jsxtnm704 = function (arg1) { // timp: strn_print(1040)
                                      let jsxtnm700 = arg1
                                      // I1CMP:start
                                      let jsxtnm703 // let
                                      { // let
                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                        // I1FUNDCL: XATS2JS_strn_print(5082)
                                        // XATS2JS_strn_print_2202
                                          // FJARGdarg($list(I1BNDcons(I1TNM(701);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(701)))))))
                                          // I1CMP:start
                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                        let jsxtnm702 = XATSDAPP(XATS2JS_strn_print(jsxtnm700))
                                        jsxtnm703 = jsxtnm702
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(703))
                                      return jsxtnm703
                                    } // endtimp(strn_print(1040))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                                    // I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                    // T1IMPallx(gseq$rst(349);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                                    // T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                                    let jsxtnm705 = function () { // timp: gseq$rst(349)
                                      // I1CMP:start
                                      // I1CMP:return:I1Vstr(...)
                                      return XATSSTRN("...")
                                    } // endtimp(gseq$rst(349))
                                    let jsxtnm706 = XATSDAPP(jsxtnm705())
                                    let jsxtnm707 = XATSDAPP(jsxtnm704(jsxtnm706))
                                    jsxtnm708 = jsxtnm707
                                    XATS000_patck(true)
                                    jsxtnm709 = XATSBOOL(false)
                                  } // endlet
                                  jsxtnm718 = jsxtnm709
                                } else {
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                                  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                                  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                                  let jsxtnm716
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                                  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                                  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                  let jsxtnm715
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                  // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                  // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                  // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                  let jsxtnm714 = function (arg1) { // timp: sint_print(922)
                                    let jsxtnm710 = arg1
                                    // I1CMP:start
                                    let jsxtnm713 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                      // I1FUNDCL: XATS2JS_sint_print(4946)
                                      // XATS2JS_sint_print_3707
                                        // FJARGdarg($list(I1BNDcons(I1TNM(711);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(711)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm712 = XATSDAPP(XATS2JS_sint_print(jsxtnm710))
                                      jsxtnm713 = jsxtnm712
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(713))
                                    return jsxtnm713
                                  } // endtimp(sint_print(922))
                                  jsxtnm715 = jsxtnm714
                                  jsxtnm716 = jsxtnm715
                                  let jsxtnm717 = XATSDAPP(jsxtnm716(jsxtnm668))
                                  jsxtnm718 = XATSBOOL(true)
                                } // end(if)
                                jsxtnm719 = jsxtnm718
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(719))
                              return jsxtnm719
                            } // endtimp(iforall$test0(1432))
                            let jsxtnm721 = XATSDAPP(jsxtnm720(jsxtnm666, jsxtnm661))
                            jsxtnm722 = jsxtnm721
                            XATS000_patck(true)
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                            // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                            // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                            // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                            let jsxtnm725 = function (arg1, arg2) { // timp: p2tr_set(2310)
                              let jsxtnm723 = arg1
                              let jsxtnm724 = arg2
                              // I1CMP:start
                              XATS000_assgn(jsxtnm723, jsxtnm724)
                              // I1CMP:return:I1V000()
                              return XATSVOID
                            } // endtimp(p2tr_set(2310))
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                            let jsxtnm732 = function (arg1, arg2) { // timp: sint_add$sint(936)
                              let jsxtnm726 = arg1
                              let jsxtnm727 = arg2
                              // I1CMP:start
                              let jsxtnm731 // let
                              { // let
                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                // XATS2JS_sint_add$sint_2778
                                  // FJARGdarg($list(I1BNDcons(I1TNM(728);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(728))))),I1BNDcons(I1TNM(729);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(729)))))))
                                  // I1CMP:start
                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                let jsxtnm730 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm726, jsxtnm727))
                                jsxtnm731 = jsxtnm730
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(731))
                              return jsxtnm731
                            } // endtimp(sint_add$sint(936))
                            let jsxtnm733 = XATSDAPP(jsxtnm732(jsxtnm666, XATSINT1(1)))
                            let jsxtnm734 = XATSDAPP(jsxtnm725(jsxtnm650, jsxtnm733))
                            jsxtnm735 = jsxtnm722
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(735))
                          return jsxtnm735
                        } // endtimp(forall$test0(1422))
                        let jsxtnm737 = XATSDAPP(jsxtnm736(jsxtnm660))
                        // I1CMP:return:I1Vtnm(I1TNM(737))
                        return jsxtnm737
                      } // endfun(test_2076)
                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
                      // I1FUNDCL
                      function free_2128(arg1)
                      { // fun
                        let jsxtnm738 = arg1
                        // I1CMP:start
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                        // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                        // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                        // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                        let jsxtnm741 = function (arg1) { // timp: g_free(23)
                          let jsxtnm739 = arg1
                          // I1CMP:start
                          let jsxtnm740 = XATSTUP0([])
                          // I1CMP:return:I1Vtnm(I1TNM(740))
                          return jsxtnm740
                        } // endtimp(g_free(23))
                        let jsxtnm742 = XATSDAPP(jsxtnm741(jsxtnm738))
                        // I1CMP:return:I1Vtnm(I1TNM(742))
                        return jsxtnm742
                      } // endfun(free_2128)
                      let jsxtnm743 = XATSDAPP(XATS2JS_list_vt_forall0$f1un(jsxtnm659, test_2076, free_2128))
                      jsxtnm744 = jsxtnm743
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(744))
                    return jsxtnm744
                  } // endtimp(list_vt_forall0(2062))
                  jsxtnm746 = jsxtnm745
                  let jsxtnm747 = XATSDAPP(jsxtnm746(jsxtnm648))
                  jsxtnm748 = jsxtnm747
                } // endlet
                jsxtnm749 = jsxtnm748
                XATS000_patck(true)
                jsxtnm750 = jsxtnm749
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(750))
              return jsxtnm750
            } // endtimp(gseq_iforall0(1735))
            let jsxtnm752 = XATSDAPP(jsxtnm751(jsxtnm592))
            let jsxtnm753 = XATSDAPP(jsxtnm647(jsxtnm752))
            jsxtnm852 = jsxtnm753
          } else {
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
            // I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
            // T1IMPallx(gseq_iforitm0(1759);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
            // T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
            let jsxtnm850 = function (arg1) { // timp: gseq_iforitm0(1759)
              let jsxtnm754 = arg1
              // I1CMP:start
              let jsxtnm849 // let
              { // let
                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                // I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
                let jsxtnm848 // let
                { // let
                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
                  // I1VALDCL
                  let jsxtnm847
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
                  // I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
                  // T1IMPallx(gseq_iforall0(1735);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
                  // T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
                  let jsxtnm845 = function (arg1) { // timp: gseq_iforall0(1735)
                    let jsxtnm760 = arg1
                    // I1CMP:start
                    let jsxtnm844 // let
                    { // let
                      // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
                      // I1VARDCL
                      // I1CMP:start
                      // I1CMP:return:I1Vint(T_INT01(0))
                      let jsxtnm761 = XATSVAR1(XATSINT1(0))
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
                      // I1VALDCL
                      let jsxtnm762
                      jsxtnm762 = XATSADDR(jsxtnm761)
                      XATS000_patck(true)
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
                      // I1VALDCL
                      let jsxtnm843
                      let jsxtnm842 // let
                      { // let
                        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                        // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
                        // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
                        // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
                        // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
                        let jsxtnm840
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
                        // I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
                        // T1IMPallx(list_vt_forall0(2062);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
                        // T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8842],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8842])))))))
                        let jsxtnm839 = function (arg1) { // timp: list_vt_forall0(2062)
                          let jsxtnm771 = arg1
                          // I1CMP:start
                          let jsxtnm838 // let
                          { // let
                            // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
                            // I1FUNDCL
                            function test_2076(arg1)
                            { // fun
                              let jsxtnm772 = arg1
                              // I1CMP:start
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                              // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                              // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                              // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                              let jsxtnm830 = function (arg1) { // timp: forall$test0(1422)
                                let jsxtnm773 = arg1
                                // I1CMP:start
                                let jsxtnm829 // let
                                { // let
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                                  // I1VALDCL
                                  let jsxtnm778
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                                  // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                  // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                  let jsxtnm776 = function (arg1) { // timp: p2tr_get(2309)
                                    let jsxtnm774 = arg1
                                    // I1CMP:start
                                    let jsxtnm775 = XATS000_dp2tr(jsxtnm774)
                                    // I1CMP:return:I1Vtnm(I1TNM(775))
                                    return jsxtnm775
                                  } // endtimp(p2tr_get(2309))
                                  let jsxtnm777 = XATSDAPP(jsxtnm776(jsxtnm762))
                                  jsxtnm778 = jsxtnm777
                                  XATS000_patck(true)
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                                  // I1VALDCL
                                  let jsxtnm816
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                                  // I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                                  // T1IMPallx(iforall$test0(1432);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                                  // T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                  let jsxtnm814 = function (arg1, arg2) { // timp: iforall$test0(1432)
                                    let jsxtnm779 = arg1
                                    let jsxtnm780 = arg2
                                    // I1CMP:start
                                    let jsxtnm813 // let
                                    { // let
                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                                      // I1VALDCL
                                      let jsxtnm812
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                                      // I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                                      // T1IMPallx(iforitm$work0(1448);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                                      // T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                      let jsxtnm810 = function (arg1, arg2) { // timp: iforitm$work0(1448)
                                        let jsxtnm781 = arg1
                                        let jsxtnm782 = arg2
                                        // I1CMP:start
                                        let jsxtnm809 // let
                                        { // let
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                                          // I1VALDCL
                                          let jsxtnm800
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                                          // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                          // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                          // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                          let jsxtnm789 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                            let jsxtnm783 = arg1
                                            let jsxtnm784 = arg2
                                            // I1CMP:start
                                            let jsxtnm788 // let
                                            { // let
                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                              // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                              // XATS2JS_sint_gt$sint_1876
                                                // FJARGdarg($list(I1BNDcons(I1TNM(785);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(785))))),I1BNDcons(I1TNM(786);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(786)))))))
                                                // I1CMP:start
                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                              let jsxtnm787 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm783, jsxtnm784))
                                              jsxtnm788 = jsxtnm787
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(788))
                                            return jsxtnm788
                                          } // endtimp(sint_gt$sint(928))
                                          let jsxtnm790 = XATSDAPP(jsxtnm789(jsxtnm781, XATSINT1(0)))
                                          let jsxtnm799 // ift
                                          if (jsxtnm790) // ift
                                          {
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                                            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                            let jsxtnm795 = function (arg1) { // timp: strn_print(1040)
                                              let jsxtnm791 = arg1
                                              // I1CMP:start
                                              let jsxtnm794 // let
                                              { // let
                                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                // I1FUNDCL: XATS2JS_strn_print(5082)
                                                // XATS2JS_strn_print_2202
                                                  // FJARGdarg($list(I1BNDcons(I1TNM(792);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(792)))))))
                                                  // I1CMP:start
                                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                let jsxtnm793 = XATSDAPP(XATS2JS_strn_print(jsxtnm791))
                                                jsxtnm794 = jsxtnm793
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(794))
                                              return jsxtnm794
                                            } // endtimp(strn_print(1040))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                                            // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                                            // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                                            // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                                            let jsxtnm796 = function () { // timp: gseq$sep(348)
                                              // I1CMP:start
                                              // I1CMP:return:I1Vstr(...)
                                              return XATSSTRN(",")
                                            } // endtimp(gseq$sep(348))
                                            let jsxtnm797 = XATSDAPP(jsxtnm796())
                                            let jsxtnm798 = XATSDAPP(jsxtnm795(jsxtnm797))
                                            jsxtnm799 = jsxtnm798
                                          } else {
                                          } // end(if)
                                          jsxtnm800 = jsxtnm799
                                          XATS000_patck(true)
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                                          // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                                          // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                                          // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                                          let jsxtnm807
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                                          // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                                          // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                          // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                          let jsxtnm806
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                          // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                          // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                          // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                          let jsxtnm805 = function (arg1) { // timp: sint_print(922)
                                            let jsxtnm801 = arg1
                                            // I1CMP:start
                                            let jsxtnm804 // let
                                            { // let
                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                              // I1FUNDCL: XATS2JS_sint_print(4946)
                                              // XATS2JS_sint_print_3707
                                                // FJARGdarg($list(I1BNDcons(I1TNM(802);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(802)))))))
                                                // I1CMP:start
                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                              let jsxtnm803 = XATSDAPP(XATS2JS_sint_print(jsxtnm801))
                                              jsxtnm804 = jsxtnm803
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(804))
                                            return jsxtnm804
                                          } // endtimp(sint_print(922))
                                          jsxtnm806 = jsxtnm805
                                          jsxtnm807 = jsxtnm806
                                          let jsxtnm808 = XATSDAPP(jsxtnm807(jsxtnm782))
                                          jsxtnm809 = jsxtnm808
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(809))
                                        return jsxtnm809
                                      } // endtimp(iforitm$work0(1448))
                                      let jsxtnm811 = XATSDAPP(jsxtnm810(jsxtnm779, jsxtnm780))
                                      jsxtnm812 = jsxtnm811
                                      XATS000_patck(true)
                                      jsxtnm813 = XATSBOOL(true)
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(813))
                                    return jsxtnm813
                                  } // endtimp(iforall$test0(1432))
                                  let jsxtnm815 = XATSDAPP(jsxtnm814(jsxtnm778, jsxtnm773))
                                  jsxtnm816 = jsxtnm815
                                  XATS000_patck(true)
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                                  // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                  // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                  let jsxtnm819 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                    let jsxtnm817 = arg1
                                    let jsxtnm818 = arg2
                                    // I1CMP:start
                                    XATS000_assgn(jsxtnm817, jsxtnm818)
                                    // I1CMP:return:I1V000()
                                    return XATSVOID
                                  } // endtimp(p2tr_set(2310))
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                                  // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                  // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                  // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                  let jsxtnm826 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                    let jsxtnm820 = arg1
                                    let jsxtnm821 = arg2
                                    // I1CMP:start
                                    let jsxtnm825 // let
                                    { // let
                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                      // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                      // XATS2JS_sint_add$sint_2778
                                        // FJARGdarg($list(I1BNDcons(I1TNM(822);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(822))))),I1BNDcons(I1TNM(823);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(823)))))))
                                        // I1CMP:start
                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                      let jsxtnm824 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm820, jsxtnm821))
                                      jsxtnm825 = jsxtnm824
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(825))
                                    return jsxtnm825
                                  } // endtimp(sint_add$sint(936))
                                  let jsxtnm827 = XATSDAPP(jsxtnm826(jsxtnm778, XATSINT1(1)))
                                  let jsxtnm828 = XATSDAPP(jsxtnm819(jsxtnm762, jsxtnm827))
                                  jsxtnm829 = jsxtnm816
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(829))
                                return jsxtnm829
                              } // endtimp(forall$test0(1422))
                              let jsxtnm831 = XATSDAPP(jsxtnm830(jsxtnm772))
                              // I1CMP:return:I1Vtnm(I1TNM(831))
                              return jsxtnm831
                            } // endfun(test_2076)
                            // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
                            // I1FUNDCL
                            function free_2128(arg1)
                            { // fun
                              let jsxtnm832 = arg1
                              // I1CMP:start
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                              // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8842])))))
                              // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                              // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                              let jsxtnm835 = function (arg1) { // timp: g_free(23)
                                let jsxtnm833 = arg1
                                // I1CMP:start
                                let jsxtnm834 = XATSTUP0([])
                                // I1CMP:return:I1Vtnm(I1TNM(834))
                                return jsxtnm834
                              } // endtimp(g_free(23))
                              let jsxtnm836 = XATSDAPP(jsxtnm835(jsxtnm832))
                              // I1CMP:return:I1Vtnm(I1TNM(836))
                              return jsxtnm836
                            } // endfun(free_2128)
                            let jsxtnm837 = XATSDAPP(XATS2JS_list_vt_forall0$f1un(jsxtnm771, test_2076, free_2128))
                            jsxtnm838 = jsxtnm837
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(838))
                          return jsxtnm838
                        } // endtimp(list_vt_forall0(2062))
                        jsxtnm840 = jsxtnm839
                        let jsxtnm841 = XATSDAPP(jsxtnm840(jsxtnm760))
                        jsxtnm842 = jsxtnm841
                      } // endlet
                      jsxtnm843 = jsxtnm842
                      XATS000_patck(true)
                      jsxtnm844 = jsxtnm843
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(844))
                    return jsxtnm844
                  } // endtimp(gseq_iforall0(1735))
                  let jsxtnm846 = XATSDAPP(jsxtnm845(jsxtnm754))
                  jsxtnm847 = jsxtnm846
                  XATS000_patck(true)
                  jsxtnm848 = XATSVOID
                } // endlet
                jsxtnm849 = jsxtnm848
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(849))
              return jsxtnm849
            } // endtimp(gseq_iforitm0(1759))
            let jsxtnm851 = XATSDAPP(jsxtnm850(jsxtnm592))
            jsxtnm852 = jsxtnm851
          } // end(if)
          jsxtnm853 = jsxtnm852
        } // endlet
        jsxtnm854 = jsxtnm853
        XATS000_patck(true)
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
        // I1VALDCL
        let jsxtnm863
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm859 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm855 = arg1
          // I1CMP:start
          let jsxtnm858 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(856);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(856)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm857 = XATSDAPP(XATS2JS_strn_print(jsxtnm855))
            jsxtnm858 = jsxtnm857
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(858))
          return jsxtnm858
        } // endtimp(strn_print(1040))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
        // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
        // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8495])))),@(x0[1070],T2Pvar(x0[8495])))))))
        let jsxtnm860 = function () { // timp: gseq$end(347)
          // I1CMP:start
          // I1CMP:return:I1Vstr(...)
          return XATSSTRN(")")
        } // endtimp(gseq$end(347))
        let jsxtnm861 = XATSDAPP(jsxtnm860())
        let jsxtnm862 = XATSDAPP(jsxtnm859(jsxtnm861))
        jsxtnm863 = jsxtnm862
        XATS000_patck(true)
        jsxtnm864 = XATSVOID
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(864))
      return jsxtnm864
    } // endtimp(gseq_print0(1686))
    let jsxtnm866 = XATSDAPP(jsxtnm865(jsxtnm591))
    // I1CMP:return:I1Vtnm(I1TNM(866))
    return jsxtnm866
  } // endtimp(g_print0(1411))
  let jsxtnm868 = XATSDAPP(jsxtnm867(jsxtnm578))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1982(line=83,offs=21)--1990(line=83,offs=29))
  // I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x2[8305])))))
  // T1IMPallx(g_print0(1411);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  // T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  let jsxtnm875
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm874
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm873 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm869 = arg1
    // I1CMP:start
    let jsxtnm872 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(870);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(870)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm871 = XATSDAPP(XATS2JS_strn_print(jsxtnm869))
      jsxtnm872 = jsxtnm871
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(872))
    return jsxtnm872
  } // endtimp(strn_print(1040))
  jsxtnm874 = jsxtnm873
  jsxtnm875 = jsxtnm874
  let jsxtnm876 = XATSDAPP(jsxtnm875(jsxtnm579))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(2002(line=84,offs=3)--2015(line=84,offs=16))
  // I0Etapq(I0Ecst(gs_print0$end(1971)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1466(line=46,offs=1)--1479(line=46,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(gs_print0$end(1971);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1479(line=46,offs=1)--1518(line=48,offs=21)))
  // T1IMPallx(gs_print0$end(1971)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$end(1971);$list()))))
  let jsxtnm878 = function () { // timp: gs_print0$end(1971)
    // I1CMP:start
    let jsxtnm877 = XATSTUP0([])
    // I1CMP:return:I1Vtnm(I1TNM(877))
    return jsxtnm877
  } // endtimp(gs_print0$end(1971))
  let jsxtnm879 = XATSDAPP(jsxtnm878())
  // I1CMP:return:I1Vtnm(I1TNM(879))
  return jsxtnm879
} // endtimp(gs_print0_a3(1976))
let jsxtnm881 = XATSDAPP(jsxtnm880(XATSSTRN("ns = "), jsxtnm576, XATSSTRN("\n")))
jsxtnm882 = jsxtnm881
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(868(line=58,offs=1)--923(line=58,offs=56)))
// I1VALDCL
let jsxtnm893
// LCSRCsome1(test09_llist00.dats)@(877(line=58,offs=10)--888(line=58,offs=21))
// I0Etapq(I0Ecst(console_log(2594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1544(line=50,offs=1)--1555(line=50,offs=12))));$list(T2JAG($list())))
// T1IMPallx(console_log(2594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1581(line=53,offs=1)--1730(line=65,offs=2)))
// T1IMPallx(console_log(2594)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(console_log(2594);$list()))))
let jsxtnm887 = function (arg1) { // timp: console_log(2594)
  let jsxtnm883 = arg1
  // I1CMP:start
  let jsxtnm886 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1663(line=61,offs=1)--1728(line=64,offs=34)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1671(line=62,offs=1)--1728(line=64,offs=34))
    // I1FUNDCL: XATS2JS_console_log(4774)
    // XATS2JS_console_log_1674
      // FJARGdarg($list(I1BNDcons(I1TNM(884);I0Pvar(x0(4775));$list(@(x0(4775),I1Vtnm(I1TNM(884)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_console_log);G1Nlist($list()))// I1CMP:return
    let jsxtnm885 = XATSDAPP(XATS2JS_console_log(jsxtnm883))
    jsxtnm886 = jsxtnm885
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(886))
  return jsxtnm886
} // endtimp(console_log(2594))
// LCSRCsome1(test09_llist00.dats)@(889(line=58,offs=22)--910(line=58,offs=43))
// I0Etapq(I0Ecst(the_print_store_flush(2597)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1836(line=76,offs=1)--1857(line=76,offs=22))));$list(T2JAG($list())))
// T1IMPallx(the_print_store_flush(2597);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1998(line=87,offs=1)--2171(line=98,offs=2)))
// T1IMPallx(the_print_store_flush(2597)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(the_print_store_flush(2597);$list()))))
let jsxtnm890 = function () { // timp: the_print_store_flush(2597)
  // I1CMP:start
  let jsxtnm889 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2108(line=95,offs=1)--2169(line=97,offs=50)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2116(line=96,offs=1)--2169(line=97,offs=50))
    // I1FUNDCL: XATS2JS_the_print_store_flush(4778)
    // XATS2JS_the_print_store_flush_2119
      // FJARGdarg($list())
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_the_print_store_flush);G1Nlist($list()))// I1CMP:return
    let jsxtnm888 = XATSDAPP(XATS2JS_the_print_store_flush())
    jsxtnm889 = jsxtnm888
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(889))
  return jsxtnm889
} // endtimp(the_print_store_flush(2597))
let jsxtnm891 = XATSDAPP(jsxtnm890())
let jsxtnm892 = XATSDAPP(jsxtnm887(jsxtnm891))
jsxtnm893 = jsxtnm892
XATS000_patck(true)
// LCSRCsome1(test09_llist00.dats)@(1186(line=66,offs=1)--1186(line=66,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(test09_llist00.dats)@(1186(line=66,offs=1)--1186(line=66,offs=1));D3Cnone0()))
