// Sun Aug 16 12:15:27 PM EDT 2026
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
// LCSRCsome1(test02_a1rf000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
// LCSRCsome1(test02_a1rf000.dats)@(187(line=12,offs=1)--221(line=13,offs=26))
// I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csymload(T_SRP_SYMLOAD();array;D2PTMsome(0;D2ITMcst($list(a1rf_make_ncpy(1104))))))))
// LCSRCsome1(test02_a1rf000.dats)@(222(line=14,offs=1)--256(line=15,offs=26))
// I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csymload(T_SRP_SYMLOAD();array;D2PTMsome(0;D2ITMcst($list(a1rf_make_nfun(1105))))))))
// I1Dinclude(LCSRCsome1(test02_a1rf000.dats)@(297(line=18,offs=1)--338(line=19,offs=33)))
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
// I1Dinclude(LCSRCsome1(test02_a1rf000.dats)@(359(line=21,offs=1)--403(line=22,offs=36)))
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
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(520(line=31,offs=1)--541(line=32,offs=13)))
// I1VALDCL
let jsxtnm9
// LCSRCsome1(test02_a1rf000.dats)@(529(line=32,offs=1)--534(line=32,offs=6))
// I0Etapq(I0Ecst(a1rf_make_ncpy(1104)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3640(line=183,offs=1)--3654(line=183,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(a1rf_make_ncpy(1104);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2725(line=148,offs=1)--2890(line=160,offs=2)))
// T1IMPallx(a1rf_make_ncpy(1104)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8867],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_make_ncpy(1104);$list(@(a[2969],T2Pvar(a[8867])))))))
let jsxtnm7 = function (arg1, arg2) { // timp: a1rf_make_ncpy(1104)
  let jsxtnm1 = arg1
  let jsxtnm2 = arg2
  // I1CMP:start
  let jsxtnm6 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2813(line=156,offs=1)--2888(line=159,offs=41)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2821(line=157,offs=1)--2888(line=159,offs=41))
    // I1FUNDCL: XATS2JS_a1rf_make_ncpy(5163)
    // XATS2JS_a1rf_make_ncpy_2824
      // FJARGdarg($list(I1BNDcons(I1TNM(3);I0Pvar(n(5164));$list(@(n(5164),I1Vtnm(I1TNM(3))))),I1BNDcons(I1TNM(4);I0Pvar(x(5165));$list(@(x(5165),I1Vtnm(I1TNM(4)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1rf_make_ncpy);G1Nlist($list()))// I1CMP:return
    let jsxtnm5 = XATSDAPP(XATS2JS_a1rf_make_ncpy(jsxtnm1, jsxtnm2))
    jsxtnm6 = jsxtnm5
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(6))
  return jsxtnm6
} // endtimp(a1rf_make_ncpy(1104))
let jsxtnm8 = XATSDAPP(jsxtnm7(XATSINT1(10), XATSINT1(1)))
jsxtnm9 = jsxtnm8
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(542(line=33,offs=1)--645(line=41,offs=29)))
// I1VALDCL
let jsxtnm246
let jsxtnm245 // let
{ // let
  // I1Dimplmnt0(LCSRCsome1(test02_a1rf000.dats)@(586(line=38,offs=1)--643(line=41,offs=27)))
  // I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8891])))),@(x0[1875],T2Pvar(x0[8891]))))):timp
  // LCSRCsome1(test02_a1rf000.dats)@(555(line=35,offs=3)--563(line=35,offs=11))
  // I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
  // T1IMPallx(gs_println_a2(820);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
  // T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
  let jsxtnm243 = function (arg1, arg2) { // timp: gs_println_a2(820)
    let jsxtnm11 = arg1
    let jsxtnm12 = arg2
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
    // I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
    // T1IMPallx(gs_print_a2(807);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
    // T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
    let jsxtnm234 = function (arg1, arg2) { // timp: gs_print_a2(807)
      let jsxtnm13 = arg1
      let jsxtnm14 = arg2
      // I1CMP:start
      let jsxtnm233 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
        // I1VALDCL
        let jsxtnm18
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
        // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
        // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
        let jsxtnm16 = function () { // timp: gs_print$beg(802)
          // I1CMP:start
          let jsxtnm15 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(15))
          return jsxtnm15
        } // endtimp(gs_print$beg(802))
        let jsxtnm17 = XATSDAPP(jsxtnm16())
        jsxtnm18 = jsxtnm17
        XATS000_patck(true)
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm24
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm23 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm19 = arg1
          // I1CMP:start
          let jsxtnm22 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(20);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(20)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm21 = XATSDAPP(XATS2JS_strn_print(jsxtnm19))
            jsxtnm22 = jsxtnm21
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(22))
          return jsxtnm22
        } // endtimp(strn_print(1040))
        jsxtnm24 = jsxtnm23
        let jsxtnm25 = XATSDAPP(jsxtnm24(jsxtnm13))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
        // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
        // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
        let jsxtnm27 = function () { // timp: gs_print$sep(803)
          // I1CMP:start
          let jsxtnm26 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(26))
          return jsxtnm26
        } // endtimp(gs_print$sep(803))
        let jsxtnm28 = XATSDAPP(jsxtnm27())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2186(line=97,offs=1)--2419(line=115,offs=4)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7263])))))))))
        let jsxtnm228 = function (arg1) { // timp: g_print(39)
          let jsxtnm29 = arg1
          // I1CMP:start
          let jsxtnm227 // let
          { // let
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2244(line=104,offs=1)--2266(line=104,offs=23))
            // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1rf);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7263])))))))
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
            // I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7263]))))):timp
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
            // I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7263]))))):timp
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
            // I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7263]))))):timp
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2388(line=114,offs=3)--2399(line=114,offs=14))
            // I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7263]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7263])))))
            // T1IMPallx(gseq_print1(1687);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
            // T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
            let jsxtnm225 = function (arg1) { // timp: gseq_print1(1687)
              let jsxtnm30 = arg1
              // I1CMP:start
              let jsxtnm224 // let
              { // let
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
                // I1VALDCL
                let jsxtnm39
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
                // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                let jsxtnm35 = function (arg1) { // timp: strn_print(1040)
                  let jsxtnm31 = arg1
                  // I1CMP:start
                  let jsxtnm34 // let
                  { // let
                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                    // I1FUNDCL: XATS2JS_strn_print(5082)
                    // XATS2JS_strn_print_2202
                      // FJARGdarg($list(I1BNDcons(I1TNM(32);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(32)))))))
                      // I1CMP:start
                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                    let jsxtnm33 = XATSDAPP(XATS2JS_strn_print(jsxtnm31))
                    jsxtnm34 = jsxtnm33
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(34))
                  return jsxtnm34
                } // endtimp(strn_print(1040))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
                // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
                // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                let jsxtnm36 = function () { // timp: gseq$beg(346)
                  // I1CMP:start
                  // I1CMP:return:I1Vstr(...)
                  return XATSSTRN("a1rf(")
                } // endtimp(gseq$beg(346))
                let jsxtnm37 = XATSDAPP(jsxtnm36())
                let jsxtnm38 = XATSDAPP(jsxtnm35(jsxtnm37))
                jsxtnm39 = jsxtnm38
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
                // I1VALDCL
                let jsxtnm214
                let jsxtnm213 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                  // I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
                  // I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                  // T1IMPallx(gseq_iforitm1(1760);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
                  // T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
                  let jsxtnm211 = function (arg1) { // timp: gseq_iforitm1(1760)
                    let jsxtnm49 = arg1
                    // I1CMP:start
                    let jsxtnm210 // let
                    { // let
                      // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                      // I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
                      let jsxtnm209 // let
                      { // let
                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
                        // I1VALDCL
                        let jsxtnm208
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
                        // I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
                        // T1IMPallx(gseq_iforall1(1736);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
                        // T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
                        let jsxtnm206 = function (arg1) { // timp: gseq_iforall1(1736)
                          let jsxtnm55 = arg1
                          // I1CMP:start
                          let jsxtnm205 // let
                          { // let
                            // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
                            // I1VARDCL
                            // I1CMP:start
                            // I1CMP:return:I1Vint(T_INT01(0))
                            let jsxtnm56 = XATSVAR1(XATSINT1(0))
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
                            // I1VALDCL
                            let jsxtnm57
                            jsxtnm57 = XATSADDR(jsxtnm56)
                            XATS000_patck(true)
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
                            // I1VALDCL
                            let jsxtnm204
                            let jsxtnm203 // let
                            { // let
                              // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                              // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
                              // I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
                              // T1IMPallx(gseq_forall1(1720);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
                              // T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
                              let jsxtnm201 = function (arg1) { // timp: gseq_forall1(1720)
                                let jsxtnm66 = arg1
                                // I1CMP:start
                                let jsxtnm200 // let
                                { // let
                                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                  // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
                                  // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
                                  // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2740(line=141,offs=1)--2882(line=152,offs=2)))
                                  // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7287])))),@(x0[1168],T2Pvar(x0[7287])))))))
                                  let jsxtnm198 = function (arg1) { // timp: gseq_forall(386)
                                    let jsxtnm67 = arg1
                                    // I1CMP:start
                                    let jsxtnm197 // let
                                    { // let
                                      // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                                      // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7287]))))):timp
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2798(line=147,offs=1)--2809(line=147,offs=12))
                                      // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7287]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7287])))))
                                      // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                                      // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                                      let jsxtnm195 = function (arg1) { // timp: gasq_forall(609)
                                        let jsxtnm68 = arg1
                                        // I1CMP:start
                                        let jsxtnm194 // let
                                        { // let
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                          // I1VALDCL
                                          let jsxtnm72
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                          // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                          // T1IMPallx(gasq_length(594);LCSRCsome1(test02_a1rf000.dats)@(586(line=38,offs=1)--643(line=41,offs=27)))
                                          // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8891],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8891],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8891])))),@(x0[1875],T2Pvar(x0[8891])))))))
                                          let jsxtnm70 = function (arg1) { // timp: gasq_length(594)
                                            let jsxtnm69 = arg1
                                            // I1CMP:start
                                            // I1CMP:return:I1Vint(T_INT01(10))
                                            return XATSINT1(10)
                                          } // endtimp(gasq_length(594))
                                          let jsxtnm71 = XATSDAPP(jsxtnm70(jsxtnm68))
                                          jsxtnm72 = jsxtnm71
                                          XATS000_patck(true)
                                          let jsxtnm193 // let
                                          { // let
                                            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                            // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                            // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                            // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                            // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                            let jsxtnm191 = function (arg1) { // timp: nint_forall(958)
                                              let jsxtnm82 = arg1
                                              // I1CMP:start
                                              let jsxtnm190 // let
                                              { // let
                                                // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                                // I1FUNDCL
                                                function loop_2862(arg1, arg2)
                                                { // fun
                                                  let jsxtnm83 = arg1
                                                  let jsxtnm84 = arg2
                                                  // I1CMP:start
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                                  // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                                  // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                                  // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                                  let jsxtnm91 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                                    let jsxtnm85 = arg1
                                                    let jsxtnm86 = arg2
                                                    // I1CMP:start
                                                    let jsxtnm90 // let
                                                    { // let
                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                                      // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                                      // XATS2JS_sint_gte$sint_2399
                                                        // FJARGdarg($list(I1BNDcons(I1TNM(87);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(87))))),I1BNDcons(I1TNM(88);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(88)))))))
                                                        // I1CMP:start
                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                                      let jsxtnm89 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm85, jsxtnm86))
                                                      jsxtnm90 = jsxtnm89
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(90))
                                                    return jsxtnm90
                                                  } // endtimp(sint_gte$sint(931))
                                                  let jsxtnm92 = XATSDAPP(jsxtnm91(jsxtnm84, jsxtnm83))
                                                  let jsxtnm188 // ift
                                                  if (jsxtnm92) // ift
                                                  {
                                                    jsxtnm188 = XATSBOOL(true)
                                                  } else {
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                                    // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                    // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                                    // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                                    let jsxtnm176 = function (arg1) { // timp: forall$test(47)
                                                      let jsxtnm93 = arg1
                                                      // I1CMP:start
                                                      let jsxtnm175 // let
                                                      { // let
                                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                                        // I1VALDCL
                                                        let jsxtnm106
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                                        // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                                        // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4092(line=227,offs=1)--4187(line=231,offs=35)))
                                                        // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7276])))),@(x0[5735],T2Pvar(x0[7276])))))))
                                                        let jsxtnm104 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                          let jsxtnm94 = arg1
                                                          let jsxtnm95 = arg2
                                                          // I1CMP:start
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4165(line=231,offs=13)--4177(line=231,offs=25))
                                                          // I0Etapq(I0Ecst(a1rf_lget$at(1111)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(4779(line=262,offs=1)--4791(line=262,offs=13))));$list(T2JAG($list(T2Pvar(x0[7276])))))
                                                          // T1IMPallx(a1rf_lget$at(1111);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2306(line=112,offs=1)--2483(line=127,offs=2)))
                                                          // T1IMPallx(a1rf_lget$at(1111)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8863],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_lget$at(1111);$list(@(a[2983],T2Pvar(a[8863])))))))
                                                          let jsxtnm102 = function (arg1, arg2) { // timp: a1rf_lget$at(1111)
                                                            let jsxtnm96 = arg1
                                                            let jsxtnm97 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm101 // let
                                                            { // let
                                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2390(line=120,offs=1)--2481(line=126,offs=38)))
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2398(line=121,offs=1)--2481(line=126,offs=38))
                                                              // I1FUNDCL: XATS2JS_a1rf_lget$at(5149)
                                                              // XATS2JS_a1rf_lget$at_2401
                                                                // FJARGdarg($list(I1BNDcons(I1TNM(98);I0Pvar(A(5150));$list(@(A(5150),I1Vtnm(I1TNM(98))))),I1BNDcons(I1TNM(99);I0Pvar(i(5151));$list(@(i(5151),I1Vtnm(I1TNM(99)))))))
                                                                // I1CMP:start
                                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1rf_lget$at);G1Nlist($list()))// I1CMP:return
                                                              let jsxtnm100 = XATSDAPP(XATS2JS_a1rf_lget$at(jsxtnm96, jsxtnm97))
                                                              jsxtnm101 = jsxtnm100
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(101))
                                                            return jsxtnm101
                                                          } // endtimp(a1rf_lget$at(1111))
                                                          let jsxtnm103 = XATSDAPP(jsxtnm102(jsxtnm94, jsxtnm95))
                                                          // I1CMP:return:I1Vtnm(I1TNM(103))
                                                          return jsxtnm103
                                                        } // endtimp(gasq_lget$at$raw(2326))
                                                        let jsxtnm105 = XATSDAPP(jsxtnm104(jsxtnm68, jsxtnm93))
                                                        jsxtnm106 = jsxtnm105
                                                        XATS000_patck(true)
                                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                                        // I1VALDCL
                                                        let jsxtnm168
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                                        // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                        // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                                                        // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm166
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2865(line=151,offs=20)--2876(line=151,offs=31))
                                                        // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7287])))))
                                                        // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                                        // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm165
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                                                        // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                                                        // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                                                        // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm164 = function (arg1) { // timp: forall$test1(1423)
                                                          let jsxtnm107 = arg1
                                                          // I1CMP:start
                                                          let jsxtnm163 // let
                                                          { // let
                                                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                                                            // I1VALDCL
                                                            let jsxtnm112
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                                                            // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                            // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                            // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                            let jsxtnm110 = function (arg1) { // timp: p2tr_get(2309)
                                                              let jsxtnm108 = arg1
                                                              // I1CMP:start
                                                              let jsxtnm109 = XATS000_dp2tr(jsxtnm108)
                                                              // I1CMP:return:I1Vtnm(I1TNM(109))
                                                              return jsxtnm109
                                                            } // endtimp(p2tr_get(2309))
                                                            let jsxtnm111 = XATSDAPP(jsxtnm110(jsxtnm57))
                                                            jsxtnm112 = jsxtnm111
                                                            XATS000_patck(true)
                                                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                                                            // I1VALDCL
                                                            let jsxtnm150
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                                                            // I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                                                            // T1IMPallx(iforall$test1(1433);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                                                            // T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                            let jsxtnm148 = function (arg1, arg2) { // timp: iforall$test1(1433)
                                                              let jsxtnm113 = arg1
                                                              let jsxtnm114 = arg2
                                                              // I1CMP:start
                                                              let jsxtnm147 // let
                                                              { // let
                                                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                                                                // I1VALDCL
                                                                let jsxtnm146
                                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                                                                // I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                                                                // T1IMPallx(iforitm$work1(1449);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                                                                // T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                let jsxtnm144 = function (arg1, arg2) { // timp: iforitm$work1(1449)
                                                                  let jsxtnm115 = arg1
                                                                  let jsxtnm116 = arg2
                                                                  // I1CMP:start
                                                                  let jsxtnm143 // let
                                                                  { // let
                                                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                                                    // I1VALDCL
                                                                    let jsxtnm134
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                                                    // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                                                    // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                                                    // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                                                    let jsxtnm123 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                                                      let jsxtnm117 = arg1
                                                                      let jsxtnm118 = arg2
                                                                      // I1CMP:start
                                                                      let jsxtnm122 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                                                        // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                                                        // XATS2JS_sint_gt$sint_1876
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(119);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(119))))),I1BNDcons(I1TNM(120);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(120)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm121 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm117, jsxtnm118))
                                                                        jsxtnm122 = jsxtnm121
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(122))
                                                                      return jsxtnm122
                                                                    } // endtimp(sint_gt$sint(928))
                                                                    let jsxtnm124 = XATSDAPP(jsxtnm123(jsxtnm115, XATSINT1(0)))
                                                                    let jsxtnm133 // ift
                                                                    if (jsxtnm124) // ift
                                                                    {
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                                                      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                                                      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                                                      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                                                      let jsxtnm129 = function (arg1) { // timp: strn_print(1040)
                                                                        let jsxtnm125 = arg1
                                                                        // I1CMP:start
                                                                        let jsxtnm128 // let
                                                                        { // let
                                                                          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                                          // I1FUNDCL: XATS2JS_strn_print(5082)
                                                                          // XATS2JS_strn_print_2202
                                                                            // FJARGdarg($list(I1BNDcons(I1TNM(126);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(126)))))))
                                                                            // I1CMP:start
                                                                            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                                          let jsxtnm127 = XATSDAPP(XATS2JS_strn_print(jsxtnm125))
                                                                          jsxtnm128 = jsxtnm127
                                                                        } // endlet
                                                                        // I1CMP:return:I1Vtnm(I1TNM(128))
                                                                        return jsxtnm128
                                                                      } // endtimp(strn_print(1040))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                                                      // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                                                      // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
                                                                      // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                      let jsxtnm130 = function () { // timp: gseq$sep(348)
                                                                        // I1CMP:start
                                                                        // I1CMP:return:I1Vstr(...)
                                                                        return XATSSTRN(",")
                                                                      } // endtimp(gseq$sep(348))
                                                                      let jsxtnm131 = XATSDAPP(jsxtnm130())
                                                                      let jsxtnm132 = XATSDAPP(jsxtnm129(jsxtnm131))
                                                                      jsxtnm133 = jsxtnm132
                                                                    } else {
                                                                    } // end(if)
                                                                    jsxtnm134 = jsxtnm133
                                                                    XATS000_patck(true)
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                                                    // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                                                    // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                                                    // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                                                    let jsxtnm141
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                                                    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                                                    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                                                    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                                                    let jsxtnm140
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                                                    // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                                                    // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                                                    // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                                                    let jsxtnm139 = function (arg1) { // timp: sint_print(922)
                                                                      let jsxtnm135 = arg1
                                                                      // I1CMP:start
                                                                      let jsxtnm138 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                                                        // I1FUNDCL: XATS2JS_sint_print(4946)
                                                                        // XATS2JS_sint_print_3707
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(136);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(136)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm137 = XATSDAPP(XATS2JS_sint_print(jsxtnm135))
                                                                        jsxtnm138 = jsxtnm137
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(138))
                                                                      return jsxtnm138
                                                                    } // endtimp(sint_print(922))
                                                                    jsxtnm140 = jsxtnm139
                                                                    jsxtnm141 = jsxtnm140
                                                                    let jsxtnm142 = XATSDAPP(jsxtnm141(jsxtnm116))
                                                                    jsxtnm143 = jsxtnm142
                                                                  } // endlet
                                                                  // I1CMP:return:I1Vtnm(I1TNM(143))
                                                                  return jsxtnm143
                                                                } // endtimp(iforitm$work1(1449))
                                                                let jsxtnm145 = XATSDAPP(jsxtnm144(jsxtnm113, jsxtnm114))
                                                                jsxtnm146 = jsxtnm145
                                                                XATS000_patck(true)
                                                                jsxtnm147 = XATSBOOL(true)
                                                              } // endlet
                                                              // I1CMP:return:I1Vtnm(I1TNM(147))
                                                              return jsxtnm147
                                                            } // endtimp(iforall$test1(1433))
                                                            let jsxtnm149 = XATSDAPP(jsxtnm148(jsxtnm112, jsxtnm107))
                                                            jsxtnm150 = jsxtnm149
                                                            XATS000_patck(true)
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                                                            // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                            // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                                            // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                                            let jsxtnm153 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                                              let jsxtnm151 = arg1
                                                              let jsxtnm152 = arg2
                                                              // I1CMP:start
                                                              XATS000_assgn(jsxtnm151, jsxtnm152)
                                                              // I1CMP:return:I1V000()
                                                              return XATSVOID
                                                            } // endtimp(p2tr_set(2310))
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                                                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                            let jsxtnm160 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                              let jsxtnm154 = arg1
                                                              let jsxtnm155 = arg2
                                                              // I1CMP:start
                                                              let jsxtnm159 // let
                                                              { // let
                                                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                                // XATS2JS_sint_add$sint_2778
                                                                  // FJARGdarg($list(I1BNDcons(I1TNM(156);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(156))))),I1BNDcons(I1TNM(157);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(157)))))))
                                                                  // I1CMP:start
                                                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                                let jsxtnm158 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm154, jsxtnm155))
                                                                jsxtnm159 = jsxtnm158
                                                              } // endlet
                                                              // I1CMP:return:I1Vtnm(I1TNM(159))
                                                              return jsxtnm159
                                                            } // endtimp(sint_add$sint(936))
                                                            let jsxtnm161 = XATSDAPP(jsxtnm160(jsxtnm112, XATSINT1(1)))
                                                            let jsxtnm162 = XATSDAPP(jsxtnm153(jsxtnm57, jsxtnm161))
                                                            jsxtnm163 = jsxtnm150
                                                          } // endlet
                                                          // I1CMP:return:I1Vtnm(I1TNM(163))
                                                          return jsxtnm163
                                                        } // endtimp(forall$test1(1423))
                                                        jsxtnm165 = jsxtnm164
                                                        jsxtnm166 = jsxtnm165
                                                        let jsxtnm167 = XATSDAPP(jsxtnm166(jsxtnm106))
                                                        jsxtnm168 = jsxtnm167
                                                        XATS000_patck(true)
                                                        // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                                        // I1VALDCL
                                                        // I1BNDcons(I1TNM(170);I0Ptup0($list());$list())
                                                        // I1CMP:start
                                                        // I1LETnew1(I1TNM(169);...)
                                                          // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(106))))
                                                        // I1CMP(ival):I1Vtnm(I1TNM(169))// I1CMP:return
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                                        // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                        // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                                        // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                                        let jsxtnm173 = function (arg1) { // timp: g_free(23)
                                                          let jsxtnm171 = arg1
                                                          // I1CMP:start
                                                          let jsxtnm172 = XATSTUP0([])
                                                          // I1CMP:return:I1Vtnm(I1TNM(172))
                                                          return jsxtnm172
                                                        } // endtimp(g_free(23))
                                                        let jsxtnm174 = XATSDAPP(jsxtnm173(jsxtnm106))
                                                        jsxtnm175 = jsxtnm168
                                                      } // endlet
                                                      // I1CMP:return:I1Vtnm(I1TNM(175))
                                                      return jsxtnm175
                                                    } // endtimp(forall$test(47))
                                                    let jsxtnm177 = XATSDAPP(jsxtnm176(jsxtnm84))
                                                    let jsxtnm187 // ift
                                                    if (jsxtnm177) // ift
                                                    {
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                                      // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                      // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                      // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                      let jsxtnm184 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                        let jsxtnm178 = arg1
                                                        let jsxtnm179 = arg2
                                                        // I1CMP:start
                                                        let jsxtnm183 // let
                                                        { // let
                                                          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                          // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                          // XATS2JS_sint_add$sint_2778
                                                            // FJARGdarg($list(I1BNDcons(I1TNM(180);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(180))))),I1BNDcons(I1TNM(181);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(181)))))))
                                                            // I1CMP:start
                                                            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                          let jsxtnm182 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm178, jsxtnm179))
                                                          jsxtnm183 = jsxtnm182
                                                        } // endlet
                                                        // I1CMP:return:I1Vtnm(I1TNM(183))
                                                        return jsxtnm183
                                                      } // endtimp(sint_add$sint(936))
                                                      let jsxtnm185 = XATSDAPP(jsxtnm184(jsxtnm84, XATSINT1(1)))
                                                      let jsxtnm186 = XATSDAPP(loop_2862(jsxtnm83, jsxtnm185))
                                                      jsxtnm187 = jsxtnm186
                                                    } else {
                                                      jsxtnm187 = XATSBOOL(false)
                                                    } // end(if)
                                                    jsxtnm188 = jsxtnm187
                                                  } // end(if)
                                                  // I1CMP:return:I1Vtnm(I1TNM(188))
                                                  return jsxtnm188
                                                } // endfun(loop_2862)
                                                let jsxtnm189 = XATSDAPP(loop_2862(jsxtnm82, XATSINT1(0)))
                                                jsxtnm190 = jsxtnm189
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(190))
                                              return jsxtnm190
                                            } // endtimp(nint_forall(958))
                                            let jsxtnm192 = XATSDAPP(jsxtnm191(jsxtnm72))
                                            jsxtnm193 = jsxtnm192
                                          } // endlet
                                          jsxtnm194 = jsxtnm193
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(194))
                                        return jsxtnm194
                                      } // endtimp(gasq_forall(609))
                                      let jsxtnm196 = XATSDAPP(jsxtnm195(jsxtnm67))
                                      jsxtnm197 = jsxtnm196
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(197))
                                    return jsxtnm197
                                  } // endtimp(gseq_forall(386))
                                  let jsxtnm199 = XATSDAPP(jsxtnm198(jsxtnm66))
                                  jsxtnm200 = jsxtnm199
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(200))
                                return jsxtnm200
                              } // endtimp(gseq_forall1(1720))
                              let jsxtnm202 = XATSDAPP(jsxtnm201(jsxtnm55))
                              jsxtnm203 = jsxtnm202
                            } // endlet
                            jsxtnm204 = jsxtnm203
                            XATS000_patck(true)
                            jsxtnm205 = jsxtnm204
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(205))
                          return jsxtnm205
                        } // endtimp(gseq_iforall1(1736))
                        let jsxtnm207 = XATSDAPP(jsxtnm206(jsxtnm49))
                        jsxtnm208 = jsxtnm207
                        XATS000_patck(true)
                        jsxtnm209 = XATSVOID
                      } // endlet
                      jsxtnm210 = jsxtnm209
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(210))
                    return jsxtnm210
                  } // endtimp(gseq_iforitm1(1760))
                  let jsxtnm212 = XATSDAPP(jsxtnm211(jsxtnm30))
                  jsxtnm213 = jsxtnm212
                } // endlet
                jsxtnm214 = jsxtnm213
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
                // I1VALDCL
                let jsxtnm223
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
                // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                let jsxtnm219 = function (arg1) { // timp: strn_print(1040)
                  let jsxtnm215 = arg1
                  // I1CMP:start
                  let jsxtnm218 // let
                  { // let
                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                    // I1FUNDCL: XATS2JS_strn_print(5082)
                    // XATS2JS_strn_print_2202
                      // FJARGdarg($list(I1BNDcons(I1TNM(216);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(216)))))))
                      // I1CMP:start
                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                    let jsxtnm217 = XATSDAPP(XATS2JS_strn_print(jsxtnm215))
                    jsxtnm218 = jsxtnm217
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(218))
                  return jsxtnm218
                } // endtimp(strn_print(1040))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
                // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
                // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                let jsxtnm220 = function () { // timp: gseq$end(347)
                  // I1CMP:start
                  // I1CMP:return:I1Vstr(...)
                  return XATSSTRN(")")
                } // endtimp(gseq$end(347))
                let jsxtnm221 = XATSDAPP(jsxtnm220())
                let jsxtnm222 = XATSDAPP(jsxtnm219(jsxtnm221))
                jsxtnm223 = jsxtnm222
                XATS000_patck(true)
                jsxtnm224 = XATSVOID
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(224))
              return jsxtnm224
            } // endtimp(gseq_print1(1687))
            let jsxtnm226 = XATSDAPP(jsxtnm225(jsxtnm29))
            jsxtnm227 = jsxtnm226
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(227))
          return jsxtnm227
        } // endtimp(g_print(39))
        let jsxtnm229 = XATSDAPP(jsxtnm228(jsxtnm14))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
        // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
        // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
        let jsxtnm231 = function () { // timp: gs_print$end(804)
          // I1CMP:start
          let jsxtnm230 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(230))
          return jsxtnm230
        } // endtimp(gs_print$end(804))
        let jsxtnm232 = XATSDAPP(jsxtnm231())
        jsxtnm233 = jsxtnm232
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(233))
      return jsxtnm233
    } // endtimp(gs_print_a2(807))
    let jsxtnm235 = XATSDAPP(jsxtnm234(jsxtnm11, jsxtnm12))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm241
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm240 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm236 = arg1
      // I1CMP:start
      let jsxtnm239 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(237);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(237)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm238 = XATSDAPP(XATS2JS_strn_print(jsxtnm236))
        jsxtnm239 = jsxtnm238
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(239))
      return jsxtnm239
    } // endtimp(strn_print(1040))
    jsxtnm241 = jsxtnm240
    let jsxtnm242 = XATSDAPP(jsxtnm241(XATSSTRN("\n")))
    // I1CMP:return:I1Vtnm(I1TNM(242))
    return jsxtnm242
  } // endtimp(gs_println_a2(820))
  let jsxtnm244 = XATSDAPP(jsxtnm243(XATSSTRN("A0 = "), jsxtnm9))
  jsxtnm245 = jsxtnm244
} // endlet
jsxtnm246 = jsxtnm245
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(692(line=46,offs=1)--702(line=46,offs=11)))
// I1VALDCL
let jsxtnm247
jsxtnm247 = XATSINT1(10)
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(703(line=47,offs=1)--743(line=49,offs=26)))
// I1VALDCL
let jsxtnm266
// LCSRCsome1(test02_a1rf000.dats)@(712(line=48,offs=1)--717(line=48,offs=6))
// I0Etapq(I0Ecst(a1rf_make_nfun(1105)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3712(line=189,offs=1)--3726(line=189,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(a1rf_make_nfun(1105);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2917(line=164,offs=1)--3093(line=177,offs=2)))
// T1IMPallx(a1rf_make_nfun(1105)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_make_nfun(1105);$list(@(a[2971],T2Pvar(a[8869])))))))
let jsxtnm254 = function (arg1, arg2) { // timp: a1rf_make_nfun(1105)
  let jsxtnm248 = arg1
  let jsxtnm249 = arg2
  // I1CMP:start
  let jsxtnm253 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(3005(line=172,offs=1)--3091(line=176,offs=45)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(3013(line=173,offs=1)--3091(line=176,offs=45))
    // I1FUNDCL: XATS2JS_a1rf_make_nfun(5168)
    // XATS2JS_a1rf_make_nfun_3016
      // FJARGdarg($list(I1BNDcons(I1TNM(250);I0Pvar(n(5169));$list(@(n(5169),I1Vtnm(I1TNM(250))))),I1BNDcons(I1TNM(251);I0Pvar(f(5170));$list(@(f(5170),I1Vtnm(I1TNM(251)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1rf_make_nfun);G1Nlist($list()))// I1CMP:return
    let jsxtnm252 = XATSDAPP(XATS2JS_a1rf_make_nfun(jsxtnm248, jsxtnm249))
    jsxtnm253 = jsxtnm252
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(253))
  return jsxtnm253
} // endtimp(a1rf_make_nfun(1105))
let jsxtnm264 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm255 = arg1
  // I1CMP:start
  // LCSRCsome1(test02_a1rf000.dats)@(739(line=49,offs=22)--740(line=49,offs=23))
  // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
  // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
  let jsxtnm262 = function (arg1, arg2) { // timp: sint_add$sint(936)
    let jsxtnm256 = arg1
    let jsxtnm257 = arg2
    // I1CMP:start
    let jsxtnm261 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
      // I1FUNDCL: XATS2JS_sint_add$sint(4922)
      // XATS2JS_sint_add$sint_2778
        // FJARGdarg($list(I1BNDcons(I1TNM(258);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(258))))),I1BNDcons(I1TNM(259);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(259)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
      let jsxtnm260 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm256, jsxtnm257))
      jsxtnm261 = jsxtnm260
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(261))
    return jsxtnm261
  } // endtimp(sint_add$sint(936))
  let jsxtnm263 = XATSDAPP(jsxtnm262(jsxtnm255, XATSINT1(1)))
  // I1CMP:return:I1Vtnm(I1TNM(263))
  return jsxtnm263
} // endfun(lam0)
let jsxtnm265 = XATSDAPP(jsxtnm254(jsxtnm247, jsxtnm264))
jsxtnm266 = jsxtnm265
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(744(line=50,offs=1)--856(line=58,offs=2)))
// I1VALDCL
let jsxtnm564
let jsxtnm563 // let
{ // let
  // I1Dimplmnt0(LCSRCsome1(test02_a1rf000.dats)@(800(line=55,offs=1)--854(line=57,offs=36)))
  // I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8892])))),@(x0[1875],T2Pvar(x0[8892]))))):timp
  // LCSRCsome1(test02_a1rf000.dats)@(753(line=51,offs=1)--761(line=51,offs=9))
  // I0Etapq(I0Ecst(gs_println_a4(822)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13918(line=908,offs=1)--13931(line=908,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
  // T1IMPallx(gs_println_a4(822);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26458(line=1604,offs=1)--26602(line=1613,offs=59)))
  // T1IMPallx(gs_println_a4(822)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7101],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7102],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7103],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7104],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a4(822);$list(@(x0[2570],T2Pvar(x0[7101])),@(x1[2571],T2Pvar(x1[7102])),@(x2[2572],T2Pvar(x2[7103])),@(x3[2573],T2Pvar(x3[7104])))))))
  let jsxtnm556 = function (arg1, arg2, arg3, arg4) { // timp: gs_println_a4(822)
    let jsxtnm268 = arg1
    let jsxtnm269 = arg2
    let jsxtnm270 = arg3
    let jsxtnm271 = arg4
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26546(line=1613,offs=3)--26557(line=1613,offs=14))
    // I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Pvar(x0[7101]))),T2JAG($list(T2Pvar(x1[7102]))),T2JAG($list(T2Pvar(x2[7103]))),T2JAG($list(T2Pvar(x3[7104])))))
    // T1IMPallx(gs_print_a4(809);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
    // T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
    let jsxtnm547 = function (arg1, arg2, arg3, arg4) { // timp: gs_print_a4(809)
      let jsxtnm272 = arg1
      let jsxtnm273 = arg2
      let jsxtnm274 = arg3
      let jsxtnm275 = arg4
      // I1CMP:start
      let jsxtnm546 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
        // I1VALDCL
        let jsxtnm279
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
        // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
        // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
        let jsxtnm277 = function () { // timp: gs_print$beg(802)
          // I1CMP:start
          let jsxtnm276 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(276))
          return jsxtnm276
        } // endtimp(gs_print$beg(802))
        let jsxtnm278 = XATSDAPP(jsxtnm277())
        jsxtnm279 = jsxtnm278
        XATS000_patck(true)
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm285
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm284 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm280 = arg1
          // I1CMP:start
          let jsxtnm283 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(281);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(281)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm282 = XATSDAPP(XATS2JS_strn_print(jsxtnm280))
            jsxtnm283 = jsxtnm282
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(283))
          return jsxtnm283
        } // endtimp(strn_print(1040))
        jsxtnm285 = jsxtnm284
        let jsxtnm286 = XATSDAPP(jsxtnm285(jsxtnm272))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
        // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
        // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
        let jsxtnm288 = function () { // timp: gs_print$sep(803)
          // I1CMP:start
          let jsxtnm287 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(287))
          return jsxtnm287
        } // endtimp(gs_print$sep(803))
        let jsxtnm289 = XATSDAPP(jsxtnm288())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
        let jsxtnm327 = function (arg1) { // timp: g_print(39)
          let jsxtnm290 = arg1
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
          // I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
          // T1IMPallx(g_ptype(202);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1618(line=53,offs=1)--1720(line=60,offs=32)))
          // T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(vt[7260],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(a1rf);$list(T2Pvar(vt[7260])))))))))
          let jsxtnm311 = function () { // timp: g_ptype(202)
            // I1CMP:start
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1673(line=59,offs=1)--1678(line=59,offs=6))
            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            let jsxtnm295 = function (arg1) { // timp: strn_print(1040)
              let jsxtnm291 = arg1
              // I1CMP:start
              let jsxtnm294 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                // I1FUNDCL: XATS2JS_strn_print(5082)
                // XATS2JS_strn_print_2202
                  // FJARGdarg($list(I1BNDcons(I1TNM(292);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(292)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                let jsxtnm293 = XATSDAPP(XATS2JS_strn_print(jsxtnm291))
                jsxtnm294 = jsxtnm293
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(294))
              return jsxtnm294
            } // endtimp(strn_print(1040))
            let jsxtnm296 = XATSDAPP(jsxtnm295(XATSSTRN("a1rf(")))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1689(line=60,offs=1)--1696(line=60,offs=8))
            // I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vt[7260])))))
            // T1IMPallx(g_ptype(202);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
            // T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
            let jsxtnm303 = function () { // timp: g_ptype(202)
              // I1CMP:start
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm301 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm297 = arg1
                // I1CMP:start
                let jsxtnm300 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(298);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(298)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm299 = XATSDAPP(XATS2JS_strn_print(jsxtnm297))
                  jsxtnm300 = jsxtnm299
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(300))
                return jsxtnm300
              } // endtimp(strn_print(1040))
              let jsxtnm302 = XATSDAPP(jsxtnm301(XATSSTRN("sint")))
              // I1CMP:return:I1Vtnm(I1TNM(302))
              return jsxtnm302
            } // endtimp(g_ptype(202))
            let jsxtnm304 = XATSDAPP(jsxtnm303())
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(1709(line=60,offs=21)--1714(line=60,offs=26))
            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            let jsxtnm309 = function (arg1) { // timp: strn_print(1040)
              let jsxtnm305 = arg1
              // I1CMP:start
              let jsxtnm308 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                // I1FUNDCL: XATS2JS_strn_print(5082)
                // XATS2JS_strn_print_2202
                  // FJARGdarg($list(I1BNDcons(I1TNM(306);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(306)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                let jsxtnm307 = XATSDAPP(XATS2JS_strn_print(jsxtnm305))
                jsxtnm308 = jsxtnm307
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(308))
              return jsxtnm308
            } // endtimp(strn_print(1040))
            let jsxtnm310 = XATSDAPP(jsxtnm309(XATSSTRN(")")))
            // I1CMP:return:I1Vtnm(I1TNM(310))
            return jsxtnm310
          } // endtimp(g_ptype(202))
          let jsxtnm312 = XATSDAPP(jsxtnm311())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm317 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm313 = arg1
            // I1CMP:start
            let jsxtnm316 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(314);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(314)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm315 = XATSDAPP(XATS2JS_strn_print(jsxtnm313))
              jsxtnm316 = jsxtnm315
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(316))
            return jsxtnm316
          } // endtimp(strn_print(1040))
          let jsxtnm318 = XATSDAPP(jsxtnm317(XATSSTRN(":")))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
          // I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
          // T1IMPallx(g_psort(201);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1831(line=74,offs=1)--1885(line=78,offs=22)))
          // T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(tx[5755],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(tx[5755])))))))
          let jsxtnm325 = function () { // timp: g_psort(201)
            // I1CMP:start
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1866(line=78,offs=3)--1876(line=78,offs=13))
            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            let jsxtnm323 = function (arg1) { // timp: strn_print(1040)
              let jsxtnm319 = arg1
              // I1CMP:start
              let jsxtnm322 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                // I1FUNDCL: XATS2JS_strn_print(5082)
                // XATS2JS_strn_print_2202
                  // FJARGdarg($list(I1BNDcons(I1TNM(320);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(320)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                let jsxtnm321 = XATSDAPP(XATS2JS_strn_print(jsxtnm319))
                jsxtnm322 = jsxtnm321
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(322))
              return jsxtnm322
            } // endtimp(strn_print(1040))
            let jsxtnm324 = XATSDAPP(jsxtnm323(XATSSTRN("tbox")))
            // I1CMP:return:I1Vtnm(I1TNM(324))
            return jsxtnm324
          } // endtimp(g_psort(201))
          let jsxtnm326 = XATSDAPP(jsxtnm325())
          // I1CMP:return:I1Vtnm(I1TNM(326))
          return jsxtnm326
        } // endtimp(g_print(39))
        let jsxtnm328 = XATSDAPP(jsxtnm327(jsxtnm273))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
        // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
        // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
        let jsxtnm330 = function () { // timp: gs_print$sep(803)
          // I1CMP:start
          let jsxtnm329 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(329))
          return jsxtnm329
        } // endtimp(gs_print$sep(803))
        let jsxtnm331 = XATSDAPP(jsxtnm330())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
        let jsxtnm337
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm336 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm332 = arg1
          // I1CMP:start
          let jsxtnm335 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(333);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(333)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm334 = XATSDAPP(XATS2JS_strn_print(jsxtnm332))
            jsxtnm335 = jsxtnm334
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(335))
          return jsxtnm335
        } // endtimp(strn_print(1040))
        jsxtnm337 = jsxtnm336
        let jsxtnm338 = XATSDAPP(jsxtnm337(jsxtnm274))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
        // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
        // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
        let jsxtnm340 = function () { // timp: gs_print$sep(803)
          // I1CMP:start
          let jsxtnm339 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(339))
          return jsxtnm339
        } // endtimp(gs_print$sep(803))
        let jsxtnm341 = XATSDAPP(jsxtnm340())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
        // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
        // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2186(line=97,offs=1)--2419(line=115,offs=4)))
        // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7263])))))))))
        let jsxtnm541 = function (arg1) { // timp: g_print(39)
          let jsxtnm342 = arg1
          // I1CMP:start
          let jsxtnm540 // let
          { // let
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2244(line=104,offs=1)--2266(line=104,offs=23))
            // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1rf);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7263])))))))
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
            // I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7263]))))):timp
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
            // I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7263]))))):timp
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
            // I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7263]))))):timp
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2388(line=114,offs=3)--2399(line=114,offs=14))
            // I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7263]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7263])))))
            // T1IMPallx(gseq_print1(1687);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
            // T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
            let jsxtnm538 = function (arg1) { // timp: gseq_print1(1687)
              let jsxtnm343 = arg1
              // I1CMP:start
              let jsxtnm537 // let
              { // let
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
                // I1VALDCL
                let jsxtnm352
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
                // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                let jsxtnm348 = function (arg1) { // timp: strn_print(1040)
                  let jsxtnm344 = arg1
                  // I1CMP:start
                  let jsxtnm347 // let
                  { // let
                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                    // I1FUNDCL: XATS2JS_strn_print(5082)
                    // XATS2JS_strn_print_2202
                      // FJARGdarg($list(I1BNDcons(I1TNM(345);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(345)))))))
                      // I1CMP:start
                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                    let jsxtnm346 = XATSDAPP(XATS2JS_strn_print(jsxtnm344))
                    jsxtnm347 = jsxtnm346
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(347))
                  return jsxtnm347
                } // endtimp(strn_print(1040))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
                // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2338(line=110,offs=1)--2375(line=111,offs=29)))
                // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                let jsxtnm349 = function () { // timp: gseq$beg(346)
                  // I1CMP:start
                  // I1CMP:return:I1Vstr(...)
                  return XATSSTRN("a1rf(")
                } // endtimp(gseq$beg(346))
                let jsxtnm350 = XATSDAPP(jsxtnm349())
                let jsxtnm351 = XATSDAPP(jsxtnm348(jsxtnm350))
                jsxtnm352 = jsxtnm351
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
                // I1VALDCL
                let jsxtnm527
                let jsxtnm526 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                  // I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
                  // I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                  // T1IMPallx(gseq_iforitm1(1760);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
                  // T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
                  let jsxtnm524 = function (arg1) { // timp: gseq_iforitm1(1760)
                    let jsxtnm362 = arg1
                    // I1CMP:start
                    let jsxtnm523 // let
                    { // let
                      // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                      // I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
                      let jsxtnm522 // let
                      { // let
                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
                        // I1VALDCL
                        let jsxtnm521
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
                        // I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
                        // T1IMPallx(gseq_iforall1(1736);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
                        // T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
                        let jsxtnm519 = function (arg1) { // timp: gseq_iforall1(1736)
                          let jsxtnm368 = arg1
                          // I1CMP:start
                          let jsxtnm518 // let
                          { // let
                            // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
                            // I1VARDCL
                            // I1CMP:start
                            // I1CMP:return:I1Vint(T_INT01(0))
                            let jsxtnm369 = XATSVAR1(XATSINT1(0))
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
                            // I1VALDCL
                            let jsxtnm370
                            jsxtnm370 = XATSADDR(jsxtnm369)
                            XATS000_patck(true)
                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
                            // I1VALDCL
                            let jsxtnm517
                            let jsxtnm516 // let
                            { // let
                              // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                              // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
                              // I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
                              // T1IMPallx(gseq_forall1(1720);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
                              // T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
                              let jsxtnm514 = function (arg1) { // timp: gseq_forall1(1720)
                                let jsxtnm379 = arg1
                                // I1CMP:start
                                let jsxtnm513 // let
                                { // let
                                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                  // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
                                  // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
                                  // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2740(line=141,offs=1)--2882(line=152,offs=2)))
                                  // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7287])))),@(x0[1168],T2Pvar(x0[7287])))))))
                                  let jsxtnm511 = function (arg1) { // timp: gseq_forall(386)
                                    let jsxtnm380 = arg1
                                    // I1CMP:start
                                    let jsxtnm510 // let
                                    { // let
                                      // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                                      // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7287]))))):timp
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2798(line=147,offs=1)--2809(line=147,offs=12))
                                      // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7287]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7287])))))
                                      // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                                      // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                                      let jsxtnm508 = function (arg1) { // timp: gasq_forall(609)
                                        let jsxtnm381 = arg1
                                        // I1CMP:start
                                        let jsxtnm507 // let
                                        { // let
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                          // I1VALDCL
                                          let jsxtnm385
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                          // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                          // T1IMPallx(gasq_length(594);LCSRCsome1(test02_a1rf000.dats)@(800(line=55,offs=1)--854(line=57,offs=36)))
                                          // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8892])))),@(x0[1875],T2Pvar(x0[8892])))))))
                                          let jsxtnm383 = function (arg1) { // timp: gasq_length(594)
                                            let jsxtnm382 = arg1
                                            // I1CMP:start
                                            // I1CMP:return:I1Vtnm(I1TNM(247))
                                            return jsxtnm247
                                          } // endtimp(gasq_length(594))
                                          let jsxtnm384 = XATSDAPP(jsxtnm383(jsxtnm381))
                                          jsxtnm385 = jsxtnm384
                                          XATS000_patck(true)
                                          let jsxtnm506 // let
                                          { // let
                                            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                            // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                            // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                            // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                            // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                            let jsxtnm504 = function (arg1) { // timp: nint_forall(958)
                                              let jsxtnm395 = arg1
                                              // I1CMP:start
                                              let jsxtnm503 // let
                                              { // let
                                                // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                                // I1FUNDCL
                                                function loop_2862(arg1, arg2)
                                                { // fun
                                                  let jsxtnm396 = arg1
                                                  let jsxtnm397 = arg2
                                                  // I1CMP:start
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                                  // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                                  // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                                  // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                                  let jsxtnm404 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                                    let jsxtnm398 = arg1
                                                    let jsxtnm399 = arg2
                                                    // I1CMP:start
                                                    let jsxtnm403 // let
                                                    { // let
                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                                      // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                                      // XATS2JS_sint_gte$sint_2399
                                                        // FJARGdarg($list(I1BNDcons(I1TNM(400);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(400))))),I1BNDcons(I1TNM(401);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(401)))))))
                                                        // I1CMP:start
                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                                      let jsxtnm402 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm398, jsxtnm399))
                                                      jsxtnm403 = jsxtnm402
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(403))
                                                    return jsxtnm403
                                                  } // endtimp(sint_gte$sint(931))
                                                  let jsxtnm405 = XATSDAPP(jsxtnm404(jsxtnm397, jsxtnm396))
                                                  let jsxtnm501 // ift
                                                  if (jsxtnm405) // ift
                                                  {
                                                    jsxtnm501 = XATSBOOL(true)
                                                  } else {
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                                    // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                    // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                                    // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                                    let jsxtnm489 = function (arg1) { // timp: forall$test(47)
                                                      let jsxtnm406 = arg1
                                                      // I1CMP:start
                                                      let jsxtnm488 // let
                                                      { // let
                                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                                        // I1VALDCL
                                                        let jsxtnm419
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                                        // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                                        // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4092(line=227,offs=1)--4187(line=231,offs=35)))
                                                        // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7276])))),@(x0[5735],T2Pvar(x0[7276])))))))
                                                        let jsxtnm417 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                          let jsxtnm407 = arg1
                                                          let jsxtnm408 = arg2
                                                          // I1CMP:start
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4165(line=231,offs=13)--4177(line=231,offs=25))
                                                          // I0Etapq(I0Ecst(a1rf_lget$at(1111)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(4779(line=262,offs=1)--4791(line=262,offs=13))));$list(T2JAG($list(T2Pvar(x0[7276])))))
                                                          // T1IMPallx(a1rf_lget$at(1111);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2306(line=112,offs=1)--2483(line=127,offs=2)))
                                                          // T1IMPallx(a1rf_lget$at(1111)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8863],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_lget$at(1111);$list(@(a[2983],T2Pvar(a[8863])))))))
                                                          let jsxtnm415 = function (arg1, arg2) { // timp: a1rf_lget$at(1111)
                                                            let jsxtnm409 = arg1
                                                            let jsxtnm410 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm414 // let
                                                            { // let
                                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2390(line=120,offs=1)--2481(line=126,offs=38)))
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2398(line=121,offs=1)--2481(line=126,offs=38))
                                                              // I1FUNDCL: XATS2JS_a1rf_lget$at(5149)
                                                              // XATS2JS_a1rf_lget$at_2401
                                                                // FJARGdarg($list(I1BNDcons(I1TNM(411);I0Pvar(A(5150));$list(@(A(5150),I1Vtnm(I1TNM(411))))),I1BNDcons(I1TNM(412);I0Pvar(i(5151));$list(@(i(5151),I1Vtnm(I1TNM(412)))))))
                                                                // I1CMP:start
                                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1rf_lget$at);G1Nlist($list()))// I1CMP:return
                                                              let jsxtnm413 = XATSDAPP(XATS2JS_a1rf_lget$at(jsxtnm409, jsxtnm410))
                                                              jsxtnm414 = jsxtnm413
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(414))
                                                            return jsxtnm414
                                                          } // endtimp(a1rf_lget$at(1111))
                                                          let jsxtnm416 = XATSDAPP(jsxtnm415(jsxtnm407, jsxtnm408))
                                                          // I1CMP:return:I1Vtnm(I1TNM(416))
                                                          return jsxtnm416
                                                        } // endtimp(gasq_lget$at$raw(2326))
                                                        let jsxtnm418 = XATSDAPP(jsxtnm417(jsxtnm381, jsxtnm406))
                                                        jsxtnm419 = jsxtnm418
                                                        XATS000_patck(true)
                                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                                        // I1VALDCL
                                                        let jsxtnm481
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                                        // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                        // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                                                        // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm479
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2865(line=151,offs=20)--2876(line=151,offs=31))
                                                        // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7287])))))
                                                        // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                                        // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm478
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                                                        // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                                                        // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                                                        // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm477 = function (arg1) { // timp: forall$test1(1423)
                                                          let jsxtnm420 = arg1
                                                          // I1CMP:start
                                                          let jsxtnm476 // let
                                                          { // let
                                                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                                                            // I1VALDCL
                                                            let jsxtnm425
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                                                            // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                            // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                            // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                            let jsxtnm423 = function (arg1) { // timp: p2tr_get(2309)
                                                              let jsxtnm421 = arg1
                                                              // I1CMP:start
                                                              let jsxtnm422 = XATS000_dp2tr(jsxtnm421)
                                                              // I1CMP:return:I1Vtnm(I1TNM(422))
                                                              return jsxtnm422
                                                            } // endtimp(p2tr_get(2309))
                                                            let jsxtnm424 = XATSDAPP(jsxtnm423(jsxtnm370))
                                                            jsxtnm425 = jsxtnm424
                                                            XATS000_patck(true)
                                                            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                                                            // I1VALDCL
                                                            let jsxtnm463
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                                                            // I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                                                            // T1IMPallx(iforall$test1(1433);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                                                            // T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                            let jsxtnm461 = function (arg1, arg2) { // timp: iforall$test1(1433)
                                                              let jsxtnm426 = arg1
                                                              let jsxtnm427 = arg2
                                                              // I1CMP:start
                                                              let jsxtnm460 // let
                                                              { // let
                                                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                                                                // I1VALDCL
                                                                let jsxtnm459
                                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                                                                // I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                                                                // T1IMPallx(iforitm$work1(1449);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                                                                // T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                let jsxtnm457 = function (arg1, arg2) { // timp: iforitm$work1(1449)
                                                                  let jsxtnm428 = arg1
                                                                  let jsxtnm429 = arg2
                                                                  // I1CMP:start
                                                                  let jsxtnm456 // let
                                                                  { // let
                                                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                                                    // I1VALDCL
                                                                    let jsxtnm447
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                                                    // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                                                    // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                                                    // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                                                    let jsxtnm436 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                                                      let jsxtnm430 = arg1
                                                                      let jsxtnm431 = arg2
                                                                      // I1CMP:start
                                                                      let jsxtnm435 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                                                        // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                                                        // XATS2JS_sint_gt$sint_1876
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(432);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(432))))),I1BNDcons(I1TNM(433);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(433)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm434 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm430, jsxtnm431))
                                                                        jsxtnm435 = jsxtnm434
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(435))
                                                                      return jsxtnm435
                                                                    } // endtimp(sint_gt$sint(928))
                                                                    let jsxtnm437 = XATSDAPP(jsxtnm436(jsxtnm428, XATSINT1(0)))
                                                                    let jsxtnm446 // ift
                                                                    if (jsxtnm437) // ift
                                                                    {
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                                                      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                                                      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                                                      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                                                      let jsxtnm442 = function (arg1) { // timp: strn_print(1040)
                                                                        let jsxtnm438 = arg1
                                                                        // I1CMP:start
                                                                        let jsxtnm441 // let
                                                                        { // let
                                                                          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                                          // I1FUNDCL: XATS2JS_strn_print(5082)
                                                                          // XATS2JS_strn_print_2202
                                                                            // FJARGdarg($list(I1BNDcons(I1TNM(439);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(439)))))))
                                                                            // I1CMP:start
                                                                            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                                          let jsxtnm440 = XATSDAPP(XATS2JS_strn_print(jsxtnm438))
                                                                          jsxtnm441 = jsxtnm440
                                                                        } // endlet
                                                                        // I1CMP:return:I1Vtnm(I1TNM(441))
                                                                        return jsxtnm441
                                                                      } // endtimp(strn_print(1040))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                                                      // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                                                      // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2270(line=106,offs=1)--2303(line=107,offs=25)))
                                                                      // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                      let jsxtnm443 = function () { // timp: gseq$sep(348)
                                                                        // I1CMP:start
                                                                        // I1CMP:return:I1Vstr(...)
                                                                        return XATSSTRN(",")
                                                                      } // endtimp(gseq$sep(348))
                                                                      let jsxtnm444 = XATSDAPP(jsxtnm443())
                                                                      let jsxtnm445 = XATSDAPP(jsxtnm442(jsxtnm444))
                                                                      jsxtnm446 = jsxtnm445
                                                                    } else {
                                                                    } // end(if)
                                                                    jsxtnm447 = jsxtnm446
                                                                    XATS000_patck(true)
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                                                    // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                                                    // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                                                    // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                                                    let jsxtnm454
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                                                    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                                                    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                                                    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                                                    let jsxtnm453
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                                                    // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                                                    // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                                                    // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                                                    let jsxtnm452 = function (arg1) { // timp: sint_print(922)
                                                                      let jsxtnm448 = arg1
                                                                      // I1CMP:start
                                                                      let jsxtnm451 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                                                        // I1FUNDCL: XATS2JS_sint_print(4946)
                                                                        // XATS2JS_sint_print_3707
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(449);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(449)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm450 = XATSDAPP(XATS2JS_sint_print(jsxtnm448))
                                                                        jsxtnm451 = jsxtnm450
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(451))
                                                                      return jsxtnm451
                                                                    } // endtimp(sint_print(922))
                                                                    jsxtnm453 = jsxtnm452
                                                                    jsxtnm454 = jsxtnm453
                                                                    let jsxtnm455 = XATSDAPP(jsxtnm454(jsxtnm429))
                                                                    jsxtnm456 = jsxtnm455
                                                                  } // endlet
                                                                  // I1CMP:return:I1Vtnm(I1TNM(456))
                                                                  return jsxtnm456
                                                                } // endtimp(iforitm$work1(1449))
                                                                let jsxtnm458 = XATSDAPP(jsxtnm457(jsxtnm426, jsxtnm427))
                                                                jsxtnm459 = jsxtnm458
                                                                XATS000_patck(true)
                                                                jsxtnm460 = XATSBOOL(true)
                                                              } // endlet
                                                              // I1CMP:return:I1Vtnm(I1TNM(460))
                                                              return jsxtnm460
                                                            } // endtimp(iforall$test1(1433))
                                                            let jsxtnm462 = XATSDAPP(jsxtnm461(jsxtnm425, jsxtnm420))
                                                            jsxtnm463 = jsxtnm462
                                                            XATS000_patck(true)
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                                                            // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                            // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                                            // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                                            let jsxtnm466 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                                              let jsxtnm464 = arg1
                                                              let jsxtnm465 = arg2
                                                              // I1CMP:start
                                                              XATS000_assgn(jsxtnm464, jsxtnm465)
                                                              // I1CMP:return:I1V000()
                                                              return XATSVOID
                                                            } // endtimp(p2tr_set(2310))
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                                                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                            let jsxtnm473 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                              let jsxtnm467 = arg1
                                                              let jsxtnm468 = arg2
                                                              // I1CMP:start
                                                              let jsxtnm472 // let
                                                              { // let
                                                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                                // XATS2JS_sint_add$sint_2778
                                                                  // FJARGdarg($list(I1BNDcons(I1TNM(469);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(469))))),I1BNDcons(I1TNM(470);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(470)))))))
                                                                  // I1CMP:start
                                                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                                let jsxtnm471 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm467, jsxtnm468))
                                                                jsxtnm472 = jsxtnm471
                                                              } // endlet
                                                              // I1CMP:return:I1Vtnm(I1TNM(472))
                                                              return jsxtnm472
                                                            } // endtimp(sint_add$sint(936))
                                                            let jsxtnm474 = XATSDAPP(jsxtnm473(jsxtnm425, XATSINT1(1)))
                                                            let jsxtnm475 = XATSDAPP(jsxtnm466(jsxtnm370, jsxtnm474))
                                                            jsxtnm476 = jsxtnm463
                                                          } // endlet
                                                          // I1CMP:return:I1Vtnm(I1TNM(476))
                                                          return jsxtnm476
                                                        } // endtimp(forall$test1(1423))
                                                        jsxtnm478 = jsxtnm477
                                                        jsxtnm479 = jsxtnm478
                                                        let jsxtnm480 = XATSDAPP(jsxtnm479(jsxtnm419))
                                                        jsxtnm481 = jsxtnm480
                                                        XATS000_patck(true)
                                                        // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                                        // I1VALDCL
                                                        // I1BNDcons(I1TNM(483);I0Ptup0($list());$list())
                                                        // I1CMP:start
                                                        // I1LETnew1(I1TNM(482);...)
                                                          // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(419))))
                                                        // I1CMP(ival):I1Vtnm(I1TNM(482))// I1CMP:return
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                                        // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                        // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                                        // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                                        let jsxtnm486 = function (arg1) { // timp: g_free(23)
                                                          let jsxtnm484 = arg1
                                                          // I1CMP:start
                                                          let jsxtnm485 = XATSTUP0([])
                                                          // I1CMP:return:I1Vtnm(I1TNM(485))
                                                          return jsxtnm485
                                                        } // endtimp(g_free(23))
                                                        let jsxtnm487 = XATSDAPP(jsxtnm486(jsxtnm419))
                                                        jsxtnm488 = jsxtnm481
                                                      } // endlet
                                                      // I1CMP:return:I1Vtnm(I1TNM(488))
                                                      return jsxtnm488
                                                    } // endtimp(forall$test(47))
                                                    let jsxtnm490 = XATSDAPP(jsxtnm489(jsxtnm397))
                                                    let jsxtnm500 // ift
                                                    if (jsxtnm490) // ift
                                                    {
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                                      // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                      // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                      // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                      let jsxtnm497 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                        let jsxtnm491 = arg1
                                                        let jsxtnm492 = arg2
                                                        // I1CMP:start
                                                        let jsxtnm496 // let
                                                        { // let
                                                          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                          // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                          // XATS2JS_sint_add$sint_2778
                                                            // FJARGdarg($list(I1BNDcons(I1TNM(493);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(493))))),I1BNDcons(I1TNM(494);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(494)))))))
                                                            // I1CMP:start
                                                            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                          let jsxtnm495 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm491, jsxtnm492))
                                                          jsxtnm496 = jsxtnm495
                                                        } // endlet
                                                        // I1CMP:return:I1Vtnm(I1TNM(496))
                                                        return jsxtnm496
                                                      } // endtimp(sint_add$sint(936))
                                                      let jsxtnm498 = XATSDAPP(jsxtnm497(jsxtnm397, XATSINT1(1)))
                                                      let jsxtnm499 = XATSDAPP(loop_2862(jsxtnm396, jsxtnm498))
                                                      jsxtnm500 = jsxtnm499
                                                    } else {
                                                      jsxtnm500 = XATSBOOL(false)
                                                    } // end(if)
                                                    jsxtnm501 = jsxtnm500
                                                  } // end(if)
                                                  // I1CMP:return:I1Vtnm(I1TNM(501))
                                                  return jsxtnm501
                                                } // endfun(loop_2862)
                                                let jsxtnm502 = XATSDAPP(loop_2862(jsxtnm395, XATSINT1(0)))
                                                jsxtnm503 = jsxtnm502
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(503))
                                              return jsxtnm503
                                            } // endtimp(nint_forall(958))
                                            let jsxtnm505 = XATSDAPP(jsxtnm504(jsxtnm385))
                                            jsxtnm506 = jsxtnm505
                                          } // endlet
                                          jsxtnm507 = jsxtnm506
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(507))
                                        return jsxtnm507
                                      } // endtimp(gasq_forall(609))
                                      let jsxtnm509 = XATSDAPP(jsxtnm508(jsxtnm380))
                                      jsxtnm510 = jsxtnm509
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(510))
                                    return jsxtnm510
                                  } // endtimp(gseq_forall(386))
                                  let jsxtnm512 = XATSDAPP(jsxtnm511(jsxtnm379))
                                  jsxtnm513 = jsxtnm512
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(513))
                                return jsxtnm513
                              } // endtimp(gseq_forall1(1720))
                              let jsxtnm515 = XATSDAPP(jsxtnm514(jsxtnm368))
                              jsxtnm516 = jsxtnm515
                            } // endlet
                            jsxtnm517 = jsxtnm516
                            XATS000_patck(true)
                            jsxtnm518 = jsxtnm517
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(518))
                          return jsxtnm518
                        } // endtimp(gseq_iforall1(1736))
                        let jsxtnm520 = XATSDAPP(jsxtnm519(jsxtnm362))
                        jsxtnm521 = jsxtnm520
                        XATS000_patck(true)
                        jsxtnm522 = XATSVOID
                      } // endlet
                      jsxtnm523 = jsxtnm522
                    } // endlet
                    // I1CMP:return:I1Vtnm(I1TNM(523))
                    return jsxtnm523
                  } // endtimp(gseq_iforitm1(1760))
                  let jsxtnm525 = XATSDAPP(jsxtnm524(jsxtnm343))
                  jsxtnm526 = jsxtnm525
                } // endlet
                jsxtnm527 = jsxtnm526
                XATS000_patck(true)
                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
                // I1VALDCL
                let jsxtnm536
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
                // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                let jsxtnm532 = function (arg1) { // timp: strn_print(1040)
                  let jsxtnm528 = arg1
                  // I1CMP:start
                  let jsxtnm531 // let
                  { // let
                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                    // I1FUNDCL: XATS2JS_strn_print(5082)
                    // XATS2JS_strn_print_2202
                      // FJARGdarg($list(I1BNDcons(I1TNM(529);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(529)))))))
                      // I1CMP:start
                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                    let jsxtnm530 = XATSDAPP(XATS2JS_strn_print(jsxtnm528))
                    jsxtnm531 = jsxtnm530
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(531))
                  return jsxtnm531
                } // endtimp(strn_print(1040))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
                // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(2304(line=108,offs=1)--2337(line=109,offs=25)))
                // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7263],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1rf);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                let jsxtnm533 = function () { // timp: gseq$end(347)
                  // I1CMP:start
                  // I1CMP:return:I1Vstr(...)
                  return XATSSTRN(")")
                } // endtimp(gseq$end(347))
                let jsxtnm534 = XATSDAPP(jsxtnm533())
                let jsxtnm535 = XATSDAPP(jsxtnm532(jsxtnm534))
                jsxtnm536 = jsxtnm535
                XATS000_patck(true)
                jsxtnm537 = XATSVOID
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(537))
              return jsxtnm537
            } // endtimp(gseq_print1(1687))
            let jsxtnm539 = XATSDAPP(jsxtnm538(jsxtnm342))
            jsxtnm540 = jsxtnm539
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(540))
          return jsxtnm540
        } // endtimp(g_print(39))
        let jsxtnm542 = XATSDAPP(jsxtnm541(jsxtnm275))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
        // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
        // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
        // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
        let jsxtnm544 = function () { // timp: gs_print$end(804)
          // I1CMP:start
          let jsxtnm543 = XATSTUP0([])
          // I1CMP:return:I1Vtnm(I1TNM(543))
          return jsxtnm543
        } // endtimp(gs_print$end(804))
        let jsxtnm545 = XATSDAPP(jsxtnm544())
        jsxtnm546 = jsxtnm545
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(546))
      return jsxtnm546
    } // endtimp(gs_print_a4(809))
    let jsxtnm548 = XATSDAPP(jsxtnm547(jsxtnm268, jsxtnm269, jsxtnm270, jsxtnm271))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26588(line=1613,offs=45)--26595(line=1613,offs=52))
    // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
    // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    let jsxtnm554
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    let jsxtnm553 = function (arg1) { // timp: strn_print(1040)
      let jsxtnm549 = arg1
      // I1CMP:start
      let jsxtnm552 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
        // I1FUNDCL: XATS2JS_strn_print(5082)
        // XATS2JS_strn_print_2202
          // FJARGdarg($list(I1BNDcons(I1TNM(550);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(550)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
        let jsxtnm551 = XATSDAPP(XATS2JS_strn_print(jsxtnm549))
        jsxtnm552 = jsxtnm551
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(552))
      return jsxtnm552
    } // endtimp(strn_print(1040))
    jsxtnm554 = jsxtnm553
    let jsxtnm555 = XATSDAPP(jsxtnm554(XATSSTRN("\n")))
    // I1CMP:return:I1Vtnm(I1TNM(555))
    return jsxtnm555
  } // endtimp(gs_println_a4(822))
  // LCSRCsome1(test02_a1rf000.dats)@(770(line=52,offs=9)--774(line=52,offs=13))
  // I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
  // T1IMPallx(g_type(196);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
  // T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
  let jsxtnm560 = function (arg1) { // timp: g_type(196)
    let jsxtnm557 = arg1
    // I1CMP:start
    let jsxtnm558 = XATSCAPP("unit", [0])
    let jsxtnm559 = XATSCAST("castxy_1839", [jsxtnm558])
    // I1CMP:return:I1Vtnm(I1TNM(559))
    return jsxtnm559
  } // endtimp(g_type(196))
  let jsxtnm561 = XATSDAPP(jsxtnm560(jsxtnm266))
  let jsxtnm562 = XATSDAPP(jsxtnm556(XATSSTRN("A1("), jsxtnm561, XATSSTRN(") = "), jsxtnm266))
  jsxtnm563 = jsxtnm562
} // endlet
jsxtnm564 = jsxtnm563
XATS000_patck(true)
// I1Dfundclist(LCSRCsome1(test02_a1rf000.dats)@(883(line=62,offs=1)--1009(line=72,offs=35)))
// I1FUNDCL
function fact_886(arg1)
{ // fun
  let jsxtnm565 = arg1
  // I1CMP:start
  let jsxtnm742 // let
  { // let
    // I1Dimplmnt0(LCSRCsome1(test02_a1rf000.dats)@(956(line=70,offs=1)--1007(line=72,offs=33)))
    // I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8893])))),@(x0[1875],T2Pvar(x0[8893]))))):timp
    // LCSRCsome1(test02_a1rf000.dats)@(940(line=67,offs=25)--947(line=67,offs=32))
    // I0Etapq(I0Ecst(GSEQ_prod(249)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2953(line=150,offs=1)--2962(line=150,offs=10))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
    // T1IMPallx(GSEQ_prod(249);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2187(line=101,offs=1)--2283(line=108,offs=35)))
    // T1IMPallx(GSEQ_prod(249)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6659],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6660],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_prod(249);$list(@(xs[825],T2Pvar(xs[6659])),@(x0[826],T2Pvar(x0[6660])))))))
    let jsxtnm721 = function (arg1) { // timp: GSEQ_prod(249)
      let jsxtnm567 = arg1
      // I1CMP:start
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2239(line=107,offs=1)--2248(line=107,offs=10))
      // I0Etapq(I0Ecst(gseq_prod(345)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2064(line=105,offs=1)--2073(line=105,offs=10))));$list(T2JAG($list(T2Pvar(xs[6659]))),T2JAG($list(T2Pvar(x0[6660])))))
      // T1IMPallx(gseq_prod(345);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2634(line=144,offs=1)--2693(line=147,offs=31)))
      // T1IMPallx(gseq_prod(345)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6050],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6051],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_prod(345);$list(@(xs[1065],T2Pvar(xs[6050])),@(x0[1066],T2Pvar(x0[6051])))))))
      let jsxtnm715
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2675(line=147,offs=13)--2685(line=147,offs=23))
      // I0Etapq(I0Ecst(gseq_prod0(1667)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(2132(line=108,offs=1)--2142(line=108,offs=11))));$list(T2JAG($list(T2Pvar(xs[6050]))),T2JAG($list(T2Pvar(x0[6051])))))
      // T1IMPallx(gseq_prod0(1667);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(1943(line=75,offs=1)--2120(line=87,offs=4)))
      // T1IMPallx(gseq_prod0(1667)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7891],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_prod0(1667);$list(@(xs[4181],T2Pvar(xs[7891])),@(x0[4182],T2Pvar(x0[7892])))))))
      let jsxtnm714 = function (arg1) { // timp: gseq_prod0(1667)
        let jsxtnm568 = arg1
        // I1CMP:start
        let jsxtnm713 // let
        { // let
          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(1993(line=80,offs=1)--2011(line=80,offs=19)))
          // I1VALDCL
          let jsxtnm571
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2002(line=80,offs=10)--2005(line=80,offs=13))
          // I0Etapq(I0Ecst(g_1(211)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gnum000.sats)@(1457(line=46,offs=1)--1460(line=46,offs=4))));$list(T2JAG($list(T2Pvar(x0[7892])))))
          // T1IMPallx(g_1(211);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(1619(line=51,offs=1)--1645(line=52,offs=18)))
          // T1IMPallx(g_1(211)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_1(211);$list(@(a[779],T2Pcst(si)))))))
          let jsxtnm569 = function () { // timp: g_1(211)
            // I1CMP:start
            // I1CMP:return:I1Vint(T_INT01(1))
            return XATSINT1(1)
          } // endtimp(g_1(211))
          let jsxtnm570 = XATSDAPP(jsxtnm569())
          jsxtnm571 = jsxtnm570
          XATS000_patck(true)
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2012(line=81,offs=1)--2074(line=84,offs=31)))
          // I1Dimplmnt0(DIMPLone2(folditm$fopr0(1454);$list(@(x0[3797],T2Pvar(x0[7892])),@(r0[3798],T2Pvar(x0[7892]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2083(line=86,offs=1)--2096(line=86,offs=14))
          // I0Etapq(I0Ecst(gseq_folditm0(1767)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(12340(line=666,offs=1)--12353(line=666,offs=14))));$list(T2JAG($list(T2Pvar(xs[7891]))),T2JAG($list(T2Pvar(x0[7892]))),T2JAG($list(T2Pvar(x0[7892])))))
          // T1IMPallx(gseq_folditm0(1767);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11599(line=792,offs=1)--11911(line=818,offs=2)))
          // T1IMPallx(gseq_folditm0(1767)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8054],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8055],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[8056],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_folditm0(1767);$list(@(xs[4418],T2Pvar(xs[8054])),@(x0[4419],T2Pvar(x0[8055])),@(r0[4420],T2Pvar(r0[8056])))))))
          let jsxtnm711 = function (arg1, arg2) { // timp: gseq_folditm0(1767)
            let jsxtnm575 = arg1
            let jsxtnm576 = arg2
            // I1CMP:start
            let jsxtnm710 // let
            { // let
              // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11679(line=800,offs=1)--11694(line=800,offs=16)))
              // I1VARDCL
              // I1CMP:start
              // I1CMP:return:I1Vtnm(I1TNM(576))
              let jsxtnm577 = XATSVAR1(jsxtnm576)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11698(line=802,offs=1)--11716(line=802,offs=19)))
              // I1VALDCL
              let jsxtnm578
              jsxtnm578 = XATSADDR(jsxtnm577)
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11720(line=804,offs=1)--11906(line=816,offs=41)))
              // I1VALDCL
              let jsxtnm708
              let jsxtnm707 // let
              { // let
                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11766(line=809,offs=1)--11905(line=816,offs=40)))
                // I1Dimplmnt0(DIMPLone2(foritm$work0(1442);$list(@(x0[3785],T2Pvar(x0[8055]))))):timp
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11731(line=806,offs=1)--11743(line=806,offs=13))
                // I0Etapq(I0Ecst(gseq_foritm0(1751)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(9424(line=503,offs=1)--9436(line=503,offs=13))));$list(T2JAG($list(T2Pvar(xs[8054]))),T2JAG($list(T2Pvar(x0[8055])))))
                // T1IMPallx(gseq_foritm0(1751);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8019(line=527,offs=1)--8210(line=544,offs=2)))
                // T1IMPallx(gseq_foritm0(1751)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8022],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8023],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm0(1751);$list(@(xs[4386],T2Pvar(xs[8022])),@(x0[4387],T2Pvar(x0[8023])))))))
                let jsxtnm705 = function (arg1) { // timp: gseq_foritm0(1751)
                  let jsxtnm586 = arg1
                  // I1CMP:start
                  let jsxtnm704 // let
                  { // let
                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8131(line=539,offs=1)--8208(line=543,offs=33)))
                    // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8023]))))):timp
                    let jsxtnm703 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8078(line=534,offs=1)--8111(line=536,offs=13)))
                      // I1VALDCL
                      let jsxtnm702
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8086(line=535,offs=1)--8098(line=535,offs=13))
                      // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8022]))),T2JAG($list(T2Pvar(x0[8023])))))
                      // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
                      // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
                      let jsxtnm700 = function (arg1) { // timp: gseq_forall0(1719)
                        let jsxtnm591 = arg1
                        // I1CMP:start
                        let jsxtnm699 // let
                        { // let
                          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                          // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
                          // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
                          // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2740(line=141,offs=1)--2882(line=152,offs=2)))
                          // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7287])))),@(x0[1168],T2Pvar(x0[7287])))))))
                          let jsxtnm697 = function (arg1) { // timp: gseq_forall(386)
                            let jsxtnm592 = arg1
                            // I1CMP:start
                            let jsxtnm696 // let
                            { // let
                              // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                              // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7287]))))):timp
                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2798(line=147,offs=1)--2809(line=147,offs=12))
                              // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Pvar(x0[7287]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7287])))))
                              // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                              // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                              let jsxtnm694 = function (arg1) { // timp: gasq_forall(609)
                                let jsxtnm593 = arg1
                                // I1CMP:start
                                let jsxtnm693 // let
                                { // let
                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                  // I1VALDCL
                                  let jsxtnm597
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                  // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                  // T1IMPallx(gasq_length(594);LCSRCsome1(test02_a1rf000.dats)@(956(line=70,offs=1)--1007(line=72,offs=33)))
                                  // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8893],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8893],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[8893])))),@(x0[1875],T2Pvar(x0[8893])))))))
                                  let jsxtnm595 = function (arg1) { // timp: gasq_length(594)
                                    let jsxtnm594 = arg1
                                    // I1CMP:start
                                    // I1CMP:return:I1Vtnm(I1TNM(565))
                                    return jsxtnm565
                                  } // endtimp(gasq_length(594))
                                  let jsxtnm596 = XATSDAPP(jsxtnm595(jsxtnm593))
                                  jsxtnm597 = jsxtnm596
                                  XATS000_patck(true)
                                  let jsxtnm692 // let
                                  { // let
                                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                    // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                    // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                    // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                    // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                    let jsxtnm690 = function (arg1) { // timp: nint_forall(958)
                                      let jsxtnm607 = arg1
                                      // I1CMP:start
                                      let jsxtnm689 // let
                                      { // let
                                        // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                        // I1FUNDCL
                                        function loop_2862(arg1, arg2)
                                        { // fun
                                          let jsxtnm608 = arg1
                                          let jsxtnm609 = arg2
                                          // I1CMP:start
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                          // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                          // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                          // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                          let jsxtnm616 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                            let jsxtnm610 = arg1
                                            let jsxtnm611 = arg2
                                            // I1CMP:start
                                            let jsxtnm615 // let
                                            { // let
                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                              // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                              // XATS2JS_sint_gte$sint_2399
                                                // FJARGdarg($list(I1BNDcons(I1TNM(612);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(612))))),I1BNDcons(I1TNM(613);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(613)))))))
                                                // I1CMP:start
                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                              let jsxtnm614 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm610, jsxtnm611))
                                              jsxtnm615 = jsxtnm614
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(615))
                                            return jsxtnm615
                                          } // endtimp(sint_gte$sint(931))
                                          let jsxtnm617 = XATSDAPP(jsxtnm616(jsxtnm609, jsxtnm608))
                                          let jsxtnm687 // ift
                                          if (jsxtnm617) // ift
                                          {
                                            jsxtnm687 = XATSBOOL(true)
                                          } else {
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                            // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                            // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                            // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                            let jsxtnm675 = function (arg1) { // timp: forall$test(47)
                                              let jsxtnm618 = arg1
                                              // I1CMP:start
                                              let jsxtnm674 // let
                                              { // let
                                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                                // I1VALDCL
                                                let jsxtnm631
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                                // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                                // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4092(line=227,offs=1)--4187(line=231,offs=35)))
                                                // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7276],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1rf);$list(T2Pvar(x0[7276])))),@(x0[5735],T2Pvar(x0[7276])))))))
                                                let jsxtnm629 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                  let jsxtnm619 = arg1
                                                  let jsxtnm620 = arg2
                                                  // I1CMP:start
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf000.dats)@(4165(line=231,offs=13)--4177(line=231,offs=25))
                                                  // I0Etapq(I0Ecst(a1rf_lget$at(1111)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(4779(line=262,offs=1)--4791(line=262,offs=13))));$list(T2JAG($list(T2Pvar(x0[7276])))))
                                                  // T1IMPallx(a1rf_lget$at(1111);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2306(line=112,offs=1)--2483(line=127,offs=2)))
                                                  // T1IMPallx(a1rf_lget$at(1111)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8863],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_lget$at(1111);$list(@(a[2983],T2Pvar(a[8863])))))))
                                                  let jsxtnm627 = function (arg1, arg2) { // timp: a1rf_lget$at(1111)
                                                    let jsxtnm621 = arg1
                                                    let jsxtnm622 = arg2
                                                    // I1CMP:start
                                                    let jsxtnm626 // let
                                                    { // let
                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2390(line=120,offs=1)--2481(line=126,offs=38)))
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2398(line=121,offs=1)--2481(line=126,offs=38))
                                                      // I1FUNDCL: XATS2JS_a1rf_lget$at(5149)
                                                      // XATS2JS_a1rf_lget$at_2401
                                                        // FJARGdarg($list(I1BNDcons(I1TNM(623);I0Pvar(A(5150));$list(@(A(5150),I1Vtnm(I1TNM(623))))),I1BNDcons(I1TNM(624);I0Pvar(i(5151));$list(@(i(5151),I1Vtnm(I1TNM(624)))))))
                                                        // I1CMP:start
                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1rf_lget$at);G1Nlist($list()))// I1CMP:return
                                                      let jsxtnm625 = XATSDAPP(XATS2JS_a1rf_lget$at(jsxtnm621, jsxtnm622))
                                                      jsxtnm626 = jsxtnm625
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(626))
                                                    return jsxtnm626
                                                  } // endtimp(a1rf_lget$at(1111))
                                                  let jsxtnm628 = XATSDAPP(jsxtnm627(jsxtnm619, jsxtnm620))
                                                  // I1CMP:return:I1Vtnm(I1TNM(628))
                                                  return jsxtnm628
                                                } // endtimp(gasq_lget$at$raw(2326))
                                                let jsxtnm630 = XATSDAPP(jsxtnm629(jsxtnm593, jsxtnm618))
                                                jsxtnm631 = jsxtnm630
                                                XATS000_patck(true)
                                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                                // I1VALDCL
                                                let jsxtnm667
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                                // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2837(line=150,offs=1)--2880(line=151,offs=35)))
                                                // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7287],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                let jsxtnm665
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axrf001.dats)@(2865(line=151,offs=20)--2876(line=151,offs=31))
                                                // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7287])))))
                                                // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                                                // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                let jsxtnm664
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                                                // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                                                // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8131(line=539,offs=1)--8208(line=543,offs=33)))
                                                // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8022],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8023],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                let jsxtnm663 = function (arg1) { // timp: forall$test0(1422)
                                                  let jsxtnm632 = arg1
                                                  // I1CMP:start
                                                  let jsxtnm662 // let
                                                  { // let
                                                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8167(line=542,offs=1)--8196(line=543,offs=21)))
                                                    // I1VALDCL
                                                    let jsxtnm661
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8176(line=543,offs=1)--8188(line=543,offs=13))
                                                    // I0Etapq(I0Ecst(foritm$work0(1442)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3042(line=183,offs=1)--3054(line=183,offs=13))));$list(T2JAG($list(T2Pvar(x0[8023])))))
                                                    // T1IMPallx(foritm$work0(1442);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11766(line=809,offs=1)--11905(line=816,offs=40)))
                                                    // T1IMPallx(foritm$work0(1442)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8054],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8055],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[8056],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work0(1442);$list(@(x0[3785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                    let jsxtnm659 = function (arg1) { // timp: foritm$work0(1442)
                                                      let jsxtnm633 = arg1
                                                      // I1CMP:start
                                                      let jsxtnm658 // let
                                                      { // let
                                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11836(line=815,offs=1)--11865(line=815,offs=30)))
                                                        // I1VALDCL
                                                        let jsxtnm638
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11849(line=815,offs=14)--11857(line=815,offs=22))
                                                        // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Pvar(r0[8056])))))
                                                        // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                        // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                        let jsxtnm636 = function (arg1) { // timp: p2tr_get(2309)
                                                          let jsxtnm634 = arg1
                                                          // I1CMP:start
                                                          let jsxtnm635 = XATS000_dp2tr(jsxtnm634)
                                                          // I1CMP:return:I1Vtnm(I1TNM(635))
                                                          return jsxtnm635
                                                        } // endtimp(p2tr_get(2309))
                                                        let jsxtnm637 = XATSDAPP(jsxtnm636(jsxtnm578))
                                                        jsxtnm638 = jsxtnm637
                                                        XATS000_patck(true)
                                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11866(line=816,offs=1)--11904(line=816,offs=39)))
                                                        // I1VALDCL
                                                        let jsxtnm653
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11875(line=816,offs=10)--11888(line=816,offs=23))
                                                        // I0Etapq(I0Ecst(folditm$fopr0(1454)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3581(line=226,offs=1)--3594(line=226,offs=14))));$list(T2JAG($list(T2Pvar(x0[8055]))),T2JAG($list(T2Pvar(r0[8056])))))
                                                        // T1IMPallx(folditm$fopr0(1454);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2012(line=81,offs=1)--2074(line=84,offs=31)))
                                                        // T1IMPallx(folditm$fopr0(1454)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7891],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(folditm$fopr0(1454);$list(@(x0[3797],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[3798],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                        let jsxtnm651 = function (arg1, arg2) { // timp: folditm$fopr0(1454)
                                                          let jsxtnm639 = arg1
                                                          let jsxtnm640 = arg2
                                                          // I1CMP:start
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2055(line=84,offs=12)--2062(line=84,offs=19))
                                                          // I0Etapq(I0Ecst(g_mul00(1586)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gnum000_vt.sats)@(2005(line=95,offs=1)--2012(line=95,offs=8))));$list(T2JAG($list(T2Pvar(x0[7892])))))
                                                          // T1IMPallx(g_mul00(1586);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats)@(1874(line=76,offs=1)--1916(line=78,offs=24)))
                                                          // T1IMPallx(g_mul00(1586)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7800],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_mul00(1586);$list(@(x0[4047],T2Pvar(x0[7800])))))))
                                                          let jsxtnm649
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats)@(1907(line=78,offs=15)--1912(line=78,offs=20))
                                                          // I0Etapq(I0Ecst(g_mul(223)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gnum000.sats)@(2025(line=99,offs=1)--2030(line=99,offs=6))));$list(T2JAG($list(T2Pvar(x0[7800])))))
                                                          // T1IMPallx(g_mul(223);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2166(line=88,offs=1)--2202(line=89,offs=28)))
                                                          // T1IMPallx(g_mul(223)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_mul(223);$list(@(x0[791],T2Pcst(si)))))))
                                                          let jsxtnm648
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2187(line=89,offs=13)--2200(line=89,offs=26))
                                                          // I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
                                                          // T1IMPallx(sint_mul$sint(938);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
                                                          // T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
                                                          let jsxtnm647 = function (arg1, arg2) { // timp: sint_mul$sint(938)
                                                            let jsxtnm641 = arg1
                                                            let jsxtnm642 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm646 // let
                                                            { // let
                                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3111(line=182,offs=1)--3175(line=184,offs=39))
                                                              // I1FUNDCL: XATS2JS_sint_mul$sint(4932)
                                                              // XATS2JS_sint_mul$sint_3114
                                                                // FJARGdarg($list(I1BNDcons(I1TNM(643);I0Pvar(i1(4933));$list(@(i1(4933),I1Vtnm(I1TNM(643))))),I1BNDcons(I1TNM(644);I0Pvar(i2(4934));$list(@(i2(4934),I1Vtnm(I1TNM(644)))))))
                                                                // I1CMP:start
                                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_mul$sint);G1Nlist($list()))// I1CMP:return
                                                              let jsxtnm645 = XATSDAPP(XATS2JS_sint_mul$sint(jsxtnm641, jsxtnm642))
                                                              jsxtnm646 = jsxtnm645
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(646))
                                                            return jsxtnm646
                                                          } // endtimp(sint_mul$sint(938))
                                                          jsxtnm648 = jsxtnm647
                                                          jsxtnm649 = jsxtnm648
                                                          let jsxtnm650 = XATSDAPP(jsxtnm649(jsxtnm639, jsxtnm640))
                                                          // I1CMP:return:I1Vtnm(I1TNM(650))
                                                          return jsxtnm650
                                                        } // endtimp(folditm$fopr0(1454))
                                                        let jsxtnm652 = XATSDAPP(jsxtnm651(jsxtnm638, jsxtnm633))
                                                        jsxtnm653 = jsxtnm652
                                                        XATS000_patck(true)
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11806(line=812,offs=7)--11814(line=812,offs=15))
                                                        // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Pvar(r0[8056])))))
                                                        // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                                        // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                                        let jsxtnm656 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                                          let jsxtnm654 = arg1
                                                          let jsxtnm655 = arg2
                                                          // I1CMP:start
                                                          XATS000_assgn(jsxtnm654, jsxtnm655)
                                                          // I1CMP:return:I1V000()
                                                          return XATSVOID
                                                        } // endtimp(p2tr_set(2310))
                                                        let jsxtnm657 = XATSDAPP(jsxtnm656(jsxtnm578, jsxtnm653))
                                                        jsxtnm658 = jsxtnm657
                                                      } // endlet
                                                      // I1CMP:return:I1Vtnm(I1TNM(658))
                                                      return jsxtnm658
                                                    } // endtimp(foritm$work0(1442))
                                                    let jsxtnm660 = XATSDAPP(jsxtnm659(jsxtnm632))
                                                    jsxtnm661 = jsxtnm660
                                                    XATS000_patck(true)
                                                    jsxtnm662 = XATSBOOL(true)
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(662))
                                                  return jsxtnm662
                                                } // endtimp(forall$test0(1422))
                                                jsxtnm664 = jsxtnm663
                                                jsxtnm665 = jsxtnm664
                                                let jsxtnm666 = XATSDAPP(jsxtnm665(jsxtnm631))
                                                jsxtnm667 = jsxtnm666
                                                XATS000_patck(true)
                                                // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                                // I1VALDCL
                                                // I1BNDcons(I1TNM(669);I0Ptup0($list());$list())
                                                // I1CMP:start
                                                // I1LETnew1(I1TNM(668);...)
                                                  // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(631))))
                                                // I1CMP(ival):I1Vtnm(I1TNM(668))// I1CMP:return
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                                // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                                // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                                let jsxtnm672 = function (arg1) { // timp: g_free(23)
                                                  let jsxtnm670 = arg1
                                                  // I1CMP:start
                                                  let jsxtnm671 = XATSTUP0([])
                                                  // I1CMP:return:I1Vtnm(I1TNM(671))
                                                  return jsxtnm671
                                                } // endtimp(g_free(23))
                                                let jsxtnm673 = XATSDAPP(jsxtnm672(jsxtnm631))
                                                jsxtnm674 = jsxtnm667
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(674))
                                              return jsxtnm674
                                            } // endtimp(forall$test(47))
                                            let jsxtnm676 = XATSDAPP(jsxtnm675(jsxtnm609))
                                            let jsxtnm686 // ift
                                            if (jsxtnm676) // ift
                                            {
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                              // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                              // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                              // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                              let jsxtnm683 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                let jsxtnm677 = arg1
                                                let jsxtnm678 = arg2
                                                // I1CMP:start
                                                let jsxtnm682 // let
                                                { // let
                                                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                  // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                  // XATS2JS_sint_add$sint_2778
                                                    // FJARGdarg($list(I1BNDcons(I1TNM(679);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(679))))),I1BNDcons(I1TNM(680);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(680)))))))
                                                    // I1CMP:start
                                                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                  let jsxtnm681 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm677, jsxtnm678))
                                                  jsxtnm682 = jsxtnm681
                                                } // endlet
                                                // I1CMP:return:I1Vtnm(I1TNM(682))
                                                return jsxtnm682
                                              } // endtimp(sint_add$sint(936))
                                              let jsxtnm684 = XATSDAPP(jsxtnm683(jsxtnm609, XATSINT1(1)))
                                              let jsxtnm685 = XATSDAPP(loop_2862(jsxtnm608, jsxtnm684))
                                              jsxtnm686 = jsxtnm685
                                            } else {
                                              jsxtnm686 = XATSBOOL(false)
                                            } // end(if)
                                            jsxtnm687 = jsxtnm686
                                          } // end(if)
                                          // I1CMP:return:I1Vtnm(I1TNM(687))
                                          return jsxtnm687
                                        } // endfun(loop_2862)
                                        let jsxtnm688 = XATSDAPP(loop_2862(jsxtnm607, XATSINT1(0)))
                                        jsxtnm689 = jsxtnm688
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(689))
                                      return jsxtnm689
                                    } // endtimp(nint_forall(958))
                                    let jsxtnm691 = XATSDAPP(jsxtnm690(jsxtnm597))
                                    jsxtnm692 = jsxtnm691
                                  } // endlet
                                  jsxtnm693 = jsxtnm692
                                } // endlet
                                // I1CMP:return:I1Vtnm(I1TNM(693))
                                return jsxtnm693
                              } // endtimp(gasq_forall(609))
                              let jsxtnm695 = XATSDAPP(jsxtnm694(jsxtnm592))
                              jsxtnm696 = jsxtnm695
                            } // endlet
                            // I1CMP:return:I1Vtnm(I1TNM(696))
                            return jsxtnm696
                          } // endtimp(gseq_forall(386))
                          let jsxtnm698 = XATSDAPP(jsxtnm697(jsxtnm591))
                          jsxtnm699 = jsxtnm698
                        } // endlet
                        // I1CMP:return:I1Vtnm(I1TNM(699))
                        return jsxtnm699
                      } // endtimp(gseq_forall0(1719))
                      let jsxtnm701 = XATSDAPP(jsxtnm700(jsxtnm586))
                      jsxtnm702 = jsxtnm701
                      XATS000_patck(true)
                      jsxtnm703 = XATSVOID
                    } // endlet
                    jsxtnm704 = jsxtnm703
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(704))
                  return jsxtnm704
                } // endtimp(gseq_foritm0(1751))
                let jsxtnm706 = XATSDAPP(jsxtnm705(jsxtnm575))
                jsxtnm707 = jsxtnm706
              } // endlet
              jsxtnm708 = jsxtnm707
              XATS000_patck(true)
              let jsxtnm709 = XATSFLAT(jsxtnm577)
              jsxtnm710 = jsxtnm709
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(710))
            return jsxtnm710
          } // endtimp(gseq_folditm0(1767))
          let jsxtnm712 = XATSDAPP(jsxtnm711(jsxtnm568, jsxtnm571))
          jsxtnm713 = jsxtnm712
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(713))
        return jsxtnm713
      } // endtimp(gseq_prod0(1667))
      jsxtnm715 = jsxtnm714
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2258(line=108,offs=10)--2267(line=108,offs=19))
      // I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6659]))),T2JAG($list(T2Pvar(x0[6660])))))
      // T1IMPallx(GSEQ_unmk(245);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
      // T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(a1rf_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
      let jsxtnm718 = function (arg1) { // timp: GSEQ_unmk(245)
        let jsxtnm716 = arg1
        // I1CMP:start
        let jsxtnm717 = XATSCAST("castxy_1839", [jsxtnm716])
        // I1CMP:return:I1Vtnm(I1TNM(717))
        return jsxtnm717
      } // endtimp(GSEQ_unmk(245))
      let jsxtnm719 = XATSDAPP(jsxtnm718(jsxtnm567))
      let jsxtnm720 = XATSDAPP(jsxtnm715(jsxtnm719))
      // I1CMP:return:I1Vtnm(I1TNM(720))
      return jsxtnm720
    } // endtimp(GSEQ_prod(249))
    // LCSRCsome1(test02_a1rf000.dats)@(910(line=66,offs=1)--915(line=66,offs=6))
    // I0Etapq(I0Ecst(a1rf_make_nfun(1105)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axrf000.sats)@(3712(line=189,offs=1)--3726(line=189,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
    // T1IMPallx(a1rf_make_nfun(1105);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(2917(line=164,offs=1)--3093(line=177,offs=2)))
    // T1IMPallx(a1rf_make_nfun(1105)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8869],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1rf_make_nfun(1105);$list(@(a[2971],T2Pvar(a[8869])))))))
    let jsxtnm728 = function (arg1, arg2) { // timp: a1rf_make_nfun(1105)
      let jsxtnm722 = arg1
      let jsxtnm723 = arg2
      // I1CMP:start
      let jsxtnm727 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(3005(line=172,offs=1)--3091(line=176,offs=45)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axrf000.dats)@(3013(line=173,offs=1)--3091(line=176,offs=45))
        // I1FUNDCL: XATS2JS_a1rf_make_nfun(5168)
        // XATS2JS_a1rf_make_nfun_3016
          // FJARGdarg($list(I1BNDcons(I1TNM(724);I0Pvar(n(5169));$list(@(n(5169),I1Vtnm(I1TNM(724))))),I1BNDcons(I1TNM(725);I0Pvar(f(5170));$list(@(f(5170),I1Vtnm(I1TNM(725)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1rf_make_nfun);G1Nlist($list()))// I1CMP:return
        let jsxtnm726 = XATSDAPP(XATS2JS_a1rf_make_nfun(jsxtnm722, jsxtnm723))
        jsxtnm727 = jsxtnm726
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(727))
      return jsxtnm727
    } // endtimp(a1rf_make_nfun(1105))
    let jsxtnm738 = function (arg1) { // lam0(T_LAM(0))
      let jsxtnm729 = arg1
      // I1CMP:start
      // LCSRCsome1(test02_a1rf000.dats)@(936(line=67,offs=21)--937(line=67,offs=22))
      // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
      // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
      // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
      let jsxtnm736 = function (arg1, arg2) { // timp: sint_add$sint(936)
        let jsxtnm730 = arg1
        let jsxtnm731 = arg2
        // I1CMP:start
        let jsxtnm735 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
          // I1FUNDCL: XATS2JS_sint_add$sint(4922)
          // XATS2JS_sint_add$sint_2778
            // FJARGdarg($list(I1BNDcons(I1TNM(732);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(732))))),I1BNDcons(I1TNM(733);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(733)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
          let jsxtnm734 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm730, jsxtnm731))
          jsxtnm735 = jsxtnm734
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(735))
        return jsxtnm735
      } // endtimp(sint_add$sint(936))
      let jsxtnm737 = XATSDAPP(jsxtnm736(jsxtnm729, XATSINT1(1)))
      // I1CMP:return:I1Vtnm(I1TNM(737))
      return jsxtnm737
    } // endfun(lam0)
    let jsxtnm739 = XATSDAPP(jsxtnm728(jsxtnm565, jsxtnm738))
    let jsxtnm740 = XATSCAST("GSEQ_make_a1rf_5120", [jsxtnm739])
    let jsxtnm741 = XATSDAPP(jsxtnm721(jsxtnm740))
    jsxtnm742 = jsxtnm741
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(742))
  return jsxtnm742
} // endfun(fact_886)
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(1013(line=74,offs=1)--1060(line=76,offs=37)))
// I1VALDCL
let jsxtnm784
// LCSRCsome1(test02_a1rf000.dats)@(1026(line=76,offs=3)--1034(line=76,offs=11))
// I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(gs_println_a2(820);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
// T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
let jsxtnm781 = function (arg1, arg2) { // timp: gs_println_a2(820)
  let jsxtnm743 = arg1
  let jsxtnm744 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  // I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  // T1IMPallx(gs_print_a2(807);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  // T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  let jsxtnm772 = function (arg1, arg2) { // timp: gs_print_a2(807)
    let jsxtnm745 = arg1
    let jsxtnm746 = arg2
    // I1CMP:start
    let jsxtnm771 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
      // I1VALDCL
      let jsxtnm750
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
      // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      let jsxtnm748 = function () { // timp: gs_print$beg(802)
        // I1CMP:start
        let jsxtnm747 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(747))
        return jsxtnm747
      } // endtimp(gs_print$beg(802))
      let jsxtnm749 = XATSDAPP(jsxtnm748())
      jsxtnm750 = jsxtnm749
      XATS000_patck(true)
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm756
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm755 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm751 = arg1
        // I1CMP:start
        let jsxtnm754 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(752);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(752)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm753 = XATSDAPP(XATS2JS_strn_print(jsxtnm751))
          jsxtnm754 = jsxtnm753
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(754))
        return jsxtnm754
      } // endtimp(strn_print(1040))
      jsxtnm756 = jsxtnm755
      let jsxtnm757 = XATSDAPP(jsxtnm756(jsxtnm745))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm759 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm758 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(758))
        return jsxtnm758
      } // endtimp(gs_print$sep(803))
      let jsxtnm760 = XATSDAPP(jsxtnm759())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
      let jsxtnm766
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
      // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
      // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
      let jsxtnm765 = function (arg1) { // timp: sint_print(922)
        let jsxtnm761 = arg1
        // I1CMP:start
        let jsxtnm764 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
          // I1FUNDCL: XATS2JS_sint_print(4946)
          // XATS2JS_sint_print_3707
            // FJARGdarg($list(I1BNDcons(I1TNM(762);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(762)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm763 = XATSDAPP(XATS2JS_sint_print(jsxtnm761))
          jsxtnm764 = jsxtnm763
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(764))
        return jsxtnm764
      } // endtimp(sint_print(922))
      jsxtnm766 = jsxtnm765
      let jsxtnm767 = XATSDAPP(jsxtnm766(jsxtnm746))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
      // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      let jsxtnm769 = function () { // timp: gs_print$end(804)
        // I1CMP:start
        let jsxtnm768 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(768))
        return jsxtnm768
      } // endtimp(gs_print$end(804))
      let jsxtnm770 = XATSDAPP(jsxtnm769())
      jsxtnm771 = jsxtnm770
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(771))
    return jsxtnm771
  } // endtimp(gs_print_a2(807))
  let jsxtnm773 = XATSDAPP(jsxtnm772(jsxtnm743, jsxtnm744))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm779
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm778 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm774 = arg1
    // I1CMP:start
    let jsxtnm777 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(775);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(775)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm776 = XATSDAPP(XATS2JS_strn_print(jsxtnm774))
      jsxtnm777 = jsxtnm776
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(777))
    return jsxtnm777
  } // endtimp(strn_print(1040))
  jsxtnm779 = jsxtnm778
  let jsxtnm780 = XATSDAPP(jsxtnm779(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(780))
  return jsxtnm780
} // endtimp(gs_println_a2(820))
let jsxtnm782 = XATSDAPP(fact_886(XATSINT1(10)))
let jsxtnm783 = XATSDAPP(jsxtnm781(XATSSTRN("fact(10) = "), jsxtnm782))
jsxtnm784 = jsxtnm783
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test02_a1rf000.dats)@(1107(line=81,offs=1)--1152(line=81,offs=46)))
// I1VALDCL
let jsxtnm795
// LCSRCsome1(test02_a1rf000.dats)@(1116(line=81,offs=10)--1127(line=81,offs=21))
// I0Etapq(I0Ecst(console_log(2594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1544(line=50,offs=1)--1555(line=50,offs=12))));$list(T2JAG($list())))
// T1IMPallx(console_log(2594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1581(line=53,offs=1)--1730(line=65,offs=2)))
// T1IMPallx(console_log(2594)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(console_log(2594);$list()))))
let jsxtnm789 = function (arg1) { // timp: console_log(2594)
  let jsxtnm785 = arg1
  // I1CMP:start
  let jsxtnm788 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1663(line=61,offs=1)--1728(line=64,offs=34)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1671(line=62,offs=1)--1728(line=64,offs=34))
    // I1FUNDCL: XATS2JS_console_log(4774)
    // XATS2JS_console_log_1674
      // FJARGdarg($list(I1BNDcons(I1TNM(786);I0Pvar(x0(4775));$list(@(x0(4775),I1Vtnm(I1TNM(786)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_console_log);G1Nlist($list()))// I1CMP:return
    let jsxtnm787 = XATSDAPP(XATS2JS_console_log(jsxtnm785))
    jsxtnm788 = jsxtnm787
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(788))
  return jsxtnm788
} // endtimp(console_log(2594))
// LCSRCsome1(test02_a1rf000.dats)@(1128(line=81,offs=22)--1149(line=81,offs=43))
// I0Etapq(I0Ecst(the_print_store_flush(2597)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1836(line=76,offs=1)--1857(line=76,offs=22))));$list(T2JAG($list())))
// T1IMPallx(the_print_store_flush(2597);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1998(line=87,offs=1)--2171(line=98,offs=2)))
// T1IMPallx(the_print_store_flush(2597)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(the_print_store_flush(2597);$list()))))
let jsxtnm792 = function () { // timp: the_print_store_flush(2597)
  // I1CMP:start
  let jsxtnm791 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2108(line=95,offs=1)--2169(line=97,offs=50)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2116(line=96,offs=1)--2169(line=97,offs=50))
    // I1FUNDCL: XATS2JS_the_print_store_flush(4778)
    // XATS2JS_the_print_store_flush_2119
      // FJARGdarg($list())
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_the_print_store_flush);G1Nlist($list()))// I1CMP:return
    let jsxtnm790 = XATSDAPP(XATS2JS_the_print_store_flush())
    jsxtnm791 = jsxtnm790
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(791))
  return jsxtnm791
} // endtimp(the_print_store_flush(2597))
let jsxtnm793 = XATSDAPP(jsxtnm792())
let jsxtnm794 = XATSDAPP(jsxtnm789(jsxtnm793))
jsxtnm795 = jsxtnm794
XATS000_patck(true)
// LCSRCsome1(test02_a1rf000.dats)@(1415(line=89,offs=1)--1415(line=89,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(test02_a1rf000.dats)@(1415(line=89,offs=1)--1415(line=89,offs=1));D3Cnone0()))
