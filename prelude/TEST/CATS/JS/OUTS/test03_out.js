// Sun Aug 16 12:15:37 PM EDT 2026
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
// LCSRCsome1(test03_a1sz000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
// I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
// I1Dinclude(LCSRCsome1(test03_a1sz000.dats)@(187(line=12,offs=1)--228(line=13,offs=33)))
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
// I1Dinclude(LCSRCsome1(test03_a1sz000.dats)@(249(line=15,offs=1)--293(line=16,offs=36)))
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
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(337(line=20,offs=1)--358(line=21,offs=13)))
// I1VALDCL
let jsxtnm9
// LCSRCsome1(test03_a1sz000.dats)@(346(line=21,offs=1)--351(line=21,offs=6))
// I0Etapq(I0Ecst(a1sz_make_ncpy(1120)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(2325(line=103,offs=1)--2339(line=103,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(a1sz_make_ncpy(1120);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2511(line=128,offs=1)--2676(line=140,offs=2)))
// T1IMPallx(a1sz_make_ncpy(1120)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8885],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_make_ncpy(1120);$list(@(a[3028],T2Pvar(a[8885])))))))
let jsxtnm7 = function (arg1, arg2) { // timp: a1sz_make_ncpy(1120)
  let jsxtnm1 = arg1
  let jsxtnm2 = arg2
  // I1CMP:start
  let jsxtnm6 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2599(line=136,offs=1)--2674(line=139,offs=41)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2607(line=137,offs=1)--2674(line=139,offs=41))
    // I1FUNDCL: XATS2JS_a1sz_make_ncpy(5193)
    // XATS2JS_a1sz_make_ncpy_2610
      // FJARGdarg($list(I1BNDcons(I1TNM(3);I0Pvar(n(5194));$list(@(n(5194),I1Vtnm(I1TNM(3))))),I1BNDcons(I1TNM(4);I0Pvar(x(5195));$list(@(x(5195),I1Vtnm(I1TNM(4)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_make_ncpy);G1Nlist($list()))// I1CMP:return
    let jsxtnm5 = XATSDAPP(XATS2JS_a1sz_make_ncpy(jsxtnm1, jsxtnm2))
    jsxtnm6 = jsxtnm5
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(6))
  return jsxtnm6
} // endtimp(a1sz_make_ncpy(1120))
let jsxtnm8 = XATSDAPP(jsxtnm7(XATSINT1(10), XATSINT1(1)))
jsxtnm9 = jsxtnm8
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(359(line=22,offs=1)--394(line=24,offs=25)))
// I1VALDCL
let jsxtnm249
// LCSRCsome1(test03_a1sz000.dats)@(372(line=24,offs=3)--380(line=24,offs=11))
// I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
// T1IMPallx(gs_println_a2(820);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
// T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
let jsxtnm247 = function (arg1, arg2) { // timp: gs_println_a2(820)
  let jsxtnm10 = arg1
  let jsxtnm11 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  // I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  // T1IMPallx(gs_print_a2(807);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  // T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  let jsxtnm238 = function (arg1, arg2) { // timp: gs_print_a2(807)
    let jsxtnm12 = arg1
    let jsxtnm13 = arg2
    // I1CMP:start
    let jsxtnm237 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
      // I1VALDCL
      let jsxtnm17
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
      // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      let jsxtnm15 = function () { // timp: gs_print$beg(802)
        // I1CMP:start
        let jsxtnm14 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(14))
        return jsxtnm14
      } // endtimp(gs_print$beg(802))
      let jsxtnm16 = XATSDAPP(jsxtnm15())
      jsxtnm17 = jsxtnm16
      XATS000_patck(true)
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm23
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm22 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm18 = arg1
        // I1CMP:start
        let jsxtnm21 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(19);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(19)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm20 = XATSDAPP(XATS2JS_strn_print(jsxtnm18))
          jsxtnm21 = jsxtnm20
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(21))
        return jsxtnm21
      } // endtimp(strn_print(1040))
      jsxtnm23 = jsxtnm22
      let jsxtnm24 = XATSDAPP(jsxtnm23(jsxtnm12))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm26 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm25 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(25))
        return jsxtnm25
      } // endtimp(gs_print$sep(803))
      let jsxtnm27 = XATSDAPP(jsxtnm26())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1767(line=65,offs=1)--2003(line=84,offs=4)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7295])))))))))
      let jsxtnm232 = function (arg1) { // timp: g_print(39)
        let jsxtnm28 = arg1
        // I1CMP:start
        let jsxtnm231 // let
        { // let
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1825(line=72,offs=1)--1847(line=72,offs=23))
          // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1sz);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7295])))))))
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1851(line=74,offs=1)--1884(line=75,offs=25)))
          // I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7295]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1885(line=76,offs=1)--1918(line=77,offs=25)))
          // I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7295]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1919(line=78,offs=1)--1956(line=79,offs=29)))
          // I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7295]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1972(line=83,offs=3)--1983(line=83,offs=14))
          // I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7295]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7295])))))
          // T1IMPallx(gseq_print1(1687);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
          // T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
          let jsxtnm229 = function (arg1) { // timp: gseq_print1(1687)
            let jsxtnm29 = arg1
            // I1CMP:start
            let jsxtnm228 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
              // I1VALDCL
              let jsxtnm38
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm34 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm30 = arg1
                // I1CMP:start
                let jsxtnm33 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(31);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(31)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm32 = XATSDAPP(XATS2JS_strn_print(jsxtnm30))
                  jsxtnm33 = jsxtnm32
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(33))
                return jsxtnm33
              } // endtimp(strn_print(1040))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
              // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
              // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1919(line=78,offs=1)--1956(line=79,offs=29)))
              // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm35 = function () { // timp: gseq$beg(346)
                // I1CMP:start
                // I1CMP:return:I1Vstr(...)
                return XATSSTRN("a1sz(")
              } // endtimp(gseq$beg(346))
              let jsxtnm36 = XATSDAPP(jsxtnm35())
              let jsxtnm37 = XATSDAPP(jsxtnm34(jsxtnm36))
              jsxtnm38 = jsxtnm37
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
              // I1VALDCL
              let jsxtnm218
              let jsxtnm217 // let
              { // let
                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                // I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
                // I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq_iforitm1(1760);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
                // T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
                let jsxtnm215 = function (arg1) { // timp: gseq_iforitm1(1760)
                  let jsxtnm48 = arg1
                  // I1CMP:start
                  let jsxtnm214 // let
                  { // let
                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                    // I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
                    let jsxtnm213 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
                      // I1VALDCL
                      let jsxtnm212
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
                      // I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
                      // T1IMPallx(gseq_iforall1(1736);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
                      // T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
                      let jsxtnm210 = function (arg1) { // timp: gseq_iforall1(1736)
                        let jsxtnm54 = arg1
                        // I1CMP:start
                        let jsxtnm209 // let
                        { // let
                          // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
                          // I1VARDCL
                          // I1CMP:start
                          // I1CMP:return:I1Vint(T_INT01(0))
                          let jsxtnm55 = XATSVAR1(XATSINT1(0))
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
                          // I1VALDCL
                          let jsxtnm56
                          jsxtnm56 = XATSADDR(jsxtnm55)
                          XATS000_patck(true)
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
                          // I1VALDCL
                          let jsxtnm208
                          let jsxtnm207 // let
                          { // let
                            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                            // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
                            // I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
                            // T1IMPallx(gseq_forall1(1720);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
                            // T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
                            let jsxtnm205 = function (arg1) { // timp: gseq_forall1(1720)
                              let jsxtnm65 = arg1
                              // I1CMP:start
                              let jsxtnm204 // let
                              { // let
                                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
                                // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
                                // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2214(line=93,offs=1)--2345(line=103,offs=2)))
                                // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7314])))),@(x0[1168],T2Pvar(x0[7314])))))))
                                let jsxtnm202 = function (arg1) { // timp: gseq_forall(386)
                                  let jsxtnm66 = arg1
                                  // I1CMP:start
                                  let jsxtnm201 // let
                                  { // let
                                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                    // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7314]))))):timp
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2272(line=99,offs=1)--2283(line=99,offs=12))
                                    // I0Etapq(I0Ecst(a1sz_forall(1140)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz001.sats)@(1643(line=55,offs=1)--1654(line=55,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                    // T1IMPallx(a1sz_forall(1140);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(1999(line=78,offs=1)--2057(line=81,offs=26)))
                                    // T1IMPallx(a1sz_forall(1140)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7312],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_forall(1140);$list(@(a[3064],T2Pvar(x0[7312])))))))
                                    let jsxtnm199
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2032(line=81,offs=1)--2043(line=81,offs=12))
                                    // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7312]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7312])))))
                                    // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                                    // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                                    let jsxtnm198 = function (arg1) { // timp: gasq_forall(609)
                                      let jsxtnm67 = arg1
                                      // I1CMP:start
                                      let jsxtnm197 // let
                                      { // let
                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                        // I1VALDCL
                                        let jsxtnm75
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                        // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                        // T1IMPallx(gasq_length(594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2083(line=89,offs=1)--2146(line=92,offs=33)))
                                        // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7296])))),@(x0[1875],T2Pvar(x0[7296])))))))
                                        let jsxtnm73
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2131(line=92,offs=18)--2142(line=92,offs=29))
                                        // I0Etapq(I0Ecst(a1sz_length(1125)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3102(line=157,offs=1)--3113(line=157,offs=12))));$list(T2JAG($list(T2Pvar(x0[7296])))))
                                        // T1IMPallx(a1sz_length(1125);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1594(line=50,offs=1)--1768(line=64,offs=2)))
                                        // T1IMPallx(a1sz_length(1125)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8875],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_length(1125);$list(@(a[3038],T2Pvar(a[8875])))))))
                                        let jsxtnm72 = function (arg1) { // timp: a1sz_length(1125)
                                          let jsxtnm68 = arg1
                                          // I1CMP:start
                                          let jsxtnm71 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1684(line=58,offs=1)--1766(line=63,offs=37)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1692(line=59,offs=1)--1766(line=63,offs=37))
                                            // I1FUNDCL: XATS2JS_a1sz_length(5172)
                                            // XATS2JS_a1sz_length_1695
                                              // FJARGdarg($list(I1BNDcons(I1TNM(69);I0Pvar(A(5173));$list(@(A(5173),I1Vtnm(I1TNM(69)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_length);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm70 = XATSDAPP(XATS2JS_a1sz_length(jsxtnm68))
                                            jsxtnm71 = jsxtnm70
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(71))
                                          return jsxtnm71
                                        } // endtimp(a1sz_length(1125))
                                        jsxtnm73 = jsxtnm72
                                        let jsxtnm74 = XATSDAPP(jsxtnm73(jsxtnm67))
                                        jsxtnm75 = jsxtnm74
                                        XATS000_patck(true)
                                        let jsxtnm196 // let
                                        { // let
                                          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                          // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                          // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                          // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                          // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                          let jsxtnm194 = function (arg1) { // timp: nint_forall(958)
                                            let jsxtnm85 = arg1
                                            // I1CMP:start
                                            let jsxtnm193 // let
                                            { // let
                                              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                              // I1FUNDCL
                                              function loop_2862(arg1, arg2)
                                              { // fun
                                                let jsxtnm86 = arg1
                                                let jsxtnm87 = arg2
                                                // I1CMP:start
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                                let jsxtnm94 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                                  let jsxtnm88 = arg1
                                                  let jsxtnm89 = arg2
                                                  // I1CMP:start
                                                  let jsxtnm93 // let
                                                  { // let
                                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                                    // XATS2JS_sint_gte$sint_2399
                                                      // FJARGdarg($list(I1BNDcons(I1TNM(90);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(90))))),I1BNDcons(I1TNM(91);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(91)))))))
                                                      // I1CMP:start
                                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                                    let jsxtnm92 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm88, jsxtnm89))
                                                    jsxtnm93 = jsxtnm92
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(93))
                                                  return jsxtnm93
                                                } // endtimp(sint_gte$sint(931))
                                                let jsxtnm95 = XATSDAPP(jsxtnm94(jsxtnm87, jsxtnm86))
                                                let jsxtnm191 // ift
                                                if (jsxtnm95) // ift
                                                {
                                                  jsxtnm191 = XATSBOOL(true)
                                                } else {
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                                  // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                  // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                                  // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                                  let jsxtnm179 = function (arg1) { // timp: forall$test(47)
                                                    let jsxtnm96 = arg1
                                                    // I1CMP:start
                                                    let jsxtnm178 // let
                                                    { // let
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                                      // I1VALDCL
                                                      let jsxtnm109
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                                      // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2517(line=119,offs=1)--2612(line=123,offs=35)))
                                                      // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7301])))),@(x0[5735],T2Pvar(x0[7301])))))))
                                                      let jsxtnm107 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                        let jsxtnm97 = arg1
                                                        let jsxtnm98 = arg2
                                                        // I1CMP:start
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2590(line=123,offs=13)--2602(line=123,offs=25))
                                                        // I0Etapq(I0Ecst(a1sz_lget$at(1130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3888(line=213,offs=1)--3900(line=213,offs=13))));$list(T2JAG($list(T2Pvar(x0[7301])))))
                                                        // T1IMPallx(a1sz_lget$at(1130);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1815(line=69,offs=1)--1992(line=84,offs=2)))
                                                        // T1IMPallx(a1sz_lget$at(1130)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8879],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_lget$at(1130);$list(@(a[3048],T2Pvar(a[8879])))))))
                                                        let jsxtnm105 = function (arg1, arg2) { // timp: a1sz_lget$at(1130)
                                                          let jsxtnm99 = arg1
                                                          let jsxtnm100 = arg2
                                                          // I1CMP:start
                                                          let jsxtnm104 // let
                                                          { // let
                                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1899(line=77,offs=1)--1990(line=83,offs=38)))
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1907(line=78,offs=1)--1990(line=83,offs=38))
                                                            // I1FUNDCL: XATS2JS_a1sz_lget$at(5176)
                                                            // XATS2JS_a1sz_lget$at_1910
                                                              // FJARGdarg($list(I1BNDcons(I1TNM(101);I0Pvar(A(5177));$list(@(A(5177),I1Vtnm(I1TNM(101))))),I1BNDcons(I1TNM(102);I0Pvar(i(5178));$list(@(i(5178),I1Vtnm(I1TNM(102)))))))
                                                              // I1CMP:start
                                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_lget$at);G1Nlist($list()))// I1CMP:return
                                                            let jsxtnm103 = XATSDAPP(XATS2JS_a1sz_lget$at(jsxtnm99, jsxtnm100))
                                                            jsxtnm104 = jsxtnm103
                                                          } // endlet
                                                          // I1CMP:return:I1Vtnm(I1TNM(104))
                                                          return jsxtnm104
                                                        } // endtimp(a1sz_lget$at(1130))
                                                        let jsxtnm106 = XATSDAPP(jsxtnm105(jsxtnm97, jsxtnm98))
                                                        // I1CMP:return:I1Vtnm(I1TNM(106))
                                                        return jsxtnm106
                                                      } // endtimp(gasq_lget$at$raw(2326))
                                                      let jsxtnm108 = XATSDAPP(jsxtnm107(jsxtnm67, jsxtnm96))
                                                      jsxtnm109 = jsxtnm108
                                                      XATS000_patck(true)
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                                      // I1VALDCL
                                                      let jsxtnm171
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm169
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2328(line=102,offs=20)--2339(line=102,offs=31))
                                                      // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                                      // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                                      // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm168
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm167 = function (arg1) { // timp: forall$test1(1423)
                                                        let jsxtnm110 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm166 // let
                                                        { // let
                                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                                                          // I1VALDCL
                                                          let jsxtnm115
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                                                          // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                          // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                          // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                          let jsxtnm113 = function (arg1) { // timp: p2tr_get(2309)
                                                            let jsxtnm111 = arg1
                                                            // I1CMP:start
                                                            let jsxtnm112 = XATS000_dp2tr(jsxtnm111)
                                                            // I1CMP:return:I1Vtnm(I1TNM(112))
                                                            return jsxtnm112
                                                          } // endtimp(p2tr_get(2309))
                                                          let jsxtnm114 = XATSDAPP(jsxtnm113(jsxtnm56))
                                                          jsxtnm115 = jsxtnm114
                                                          XATS000_patck(true)
                                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                                                          // I1VALDCL
                                                          let jsxtnm153
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                                                          // I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                                                          // T1IMPallx(iforall$test1(1433);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                                                          // T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                          let jsxtnm151 = function (arg1, arg2) { // timp: iforall$test1(1433)
                                                            let jsxtnm116 = arg1
                                                            let jsxtnm117 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm150 // let
                                                            { // let
                                                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                                                              // I1VALDCL
                                                              let jsxtnm149
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                                                              // I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                                                              // T1IMPallx(iforitm$work1(1449);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                                                              // T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                              let jsxtnm147 = function (arg1, arg2) { // timp: iforitm$work1(1449)
                                                                let jsxtnm118 = arg1
                                                                let jsxtnm119 = arg2
                                                                // I1CMP:start
                                                                let jsxtnm146 // let
                                                                { // let
                                                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                                                  // I1VALDCL
                                                                  let jsxtnm137
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                                                  // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                                                  // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                                                  // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                                                  let jsxtnm126 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                                                    let jsxtnm120 = arg1
                                                                    let jsxtnm121 = arg2
                                                                    // I1CMP:start
                                                                    let jsxtnm125 // let
                                                                    { // let
                                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                                                      // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                                                      // XATS2JS_sint_gt$sint_1876
                                                                        // FJARGdarg($list(I1BNDcons(I1TNM(122);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(122))))),I1BNDcons(I1TNM(123);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(123)))))))
                                                                        // I1CMP:start
                                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                                                      let jsxtnm124 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm120, jsxtnm121))
                                                                      jsxtnm125 = jsxtnm124
                                                                    } // endlet
                                                                    // I1CMP:return:I1Vtnm(I1TNM(125))
                                                                    return jsxtnm125
                                                                  } // endtimp(sint_gt$sint(928))
                                                                  let jsxtnm127 = XATSDAPP(jsxtnm126(jsxtnm118, XATSINT1(0)))
                                                                  let jsxtnm136 // ift
                                                                  if (jsxtnm127) // ift
                                                                  {
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                                                    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                                                    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                                                    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                                                    let jsxtnm132 = function (arg1) { // timp: strn_print(1040)
                                                                      let jsxtnm128 = arg1
                                                                      // I1CMP:start
                                                                      let jsxtnm131 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                                        // I1FUNDCL: XATS2JS_strn_print(5082)
                                                                        // XATS2JS_strn_print_2202
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(129);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(129)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm130 = XATSDAPP(XATS2JS_strn_print(jsxtnm128))
                                                                        jsxtnm131 = jsxtnm130
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(131))
                                                                      return jsxtnm131
                                                                    } // endtimp(strn_print(1040))
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                                                    // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                                                    // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1851(line=74,offs=1)--1884(line=75,offs=25)))
                                                                    // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                    let jsxtnm133 = function () { // timp: gseq$sep(348)
                                                                      // I1CMP:start
                                                                      // I1CMP:return:I1Vstr(...)
                                                                      return XATSSTRN(",")
                                                                    } // endtimp(gseq$sep(348))
                                                                    let jsxtnm134 = XATSDAPP(jsxtnm133())
                                                                    let jsxtnm135 = XATSDAPP(jsxtnm132(jsxtnm134))
                                                                    jsxtnm136 = jsxtnm135
                                                                  } else {
                                                                  } // end(if)
                                                                  jsxtnm137 = jsxtnm136
                                                                  XATS000_patck(true)
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                                                  // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                                                  // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                                                  // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                                                  let jsxtnm144
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                                                  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                                                  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                                                  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                                                  let jsxtnm143
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                                                  // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                                                  // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                                                  // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                                                  let jsxtnm142 = function (arg1) { // timp: sint_print(922)
                                                                    let jsxtnm138 = arg1
                                                                    // I1CMP:start
                                                                    let jsxtnm141 // let
                                                                    { // let
                                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                                                      // I1FUNDCL: XATS2JS_sint_print(4946)
                                                                      // XATS2JS_sint_print_3707
                                                                        // FJARGdarg($list(I1BNDcons(I1TNM(139);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(139)))))))
                                                                        // I1CMP:start
                                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                                                      let jsxtnm140 = XATSDAPP(XATS2JS_sint_print(jsxtnm138))
                                                                      jsxtnm141 = jsxtnm140
                                                                    } // endlet
                                                                    // I1CMP:return:I1Vtnm(I1TNM(141))
                                                                    return jsxtnm141
                                                                  } // endtimp(sint_print(922))
                                                                  jsxtnm143 = jsxtnm142
                                                                  jsxtnm144 = jsxtnm143
                                                                  let jsxtnm145 = XATSDAPP(jsxtnm144(jsxtnm119))
                                                                  jsxtnm146 = jsxtnm145
                                                                } // endlet
                                                                // I1CMP:return:I1Vtnm(I1TNM(146))
                                                                return jsxtnm146
                                                              } // endtimp(iforitm$work1(1449))
                                                              let jsxtnm148 = XATSDAPP(jsxtnm147(jsxtnm116, jsxtnm117))
                                                              jsxtnm149 = jsxtnm148
                                                              XATS000_patck(true)
                                                              jsxtnm150 = XATSBOOL(true)
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(150))
                                                            return jsxtnm150
                                                          } // endtimp(iforall$test1(1433))
                                                          let jsxtnm152 = XATSDAPP(jsxtnm151(jsxtnm115, jsxtnm110))
                                                          jsxtnm153 = jsxtnm152
                                                          XATS000_patck(true)
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
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
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
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
                                                          let jsxtnm164 = XATSDAPP(jsxtnm163(jsxtnm115, XATSINT1(1)))
                                                          let jsxtnm165 = XATSDAPP(jsxtnm156(jsxtnm56, jsxtnm164))
                                                          jsxtnm166 = jsxtnm153
                                                        } // endlet
                                                        // I1CMP:return:I1Vtnm(I1TNM(166))
                                                        return jsxtnm166
                                                      } // endtimp(forall$test1(1423))
                                                      jsxtnm168 = jsxtnm167
                                                      jsxtnm169 = jsxtnm168
                                                      let jsxtnm170 = XATSDAPP(jsxtnm169(jsxtnm109))
                                                      jsxtnm171 = jsxtnm170
                                                      XATS000_patck(true)
                                                      // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                                      // I1VALDCL
                                                      // I1BNDcons(I1TNM(173);I0Ptup0($list());$list())
                                                      // I1CMP:start
                                                      // I1LETnew1(I1TNM(172);...)
                                                        // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(109))))
                                                      // I1CMP(ival):I1Vtnm(I1TNM(172))// I1CMP:return
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                                      // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                                      // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                                      let jsxtnm176 = function (arg1) { // timp: g_free(23)
                                                        let jsxtnm174 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm175 = XATSTUP0([])
                                                        // I1CMP:return:I1Vtnm(I1TNM(175))
                                                        return jsxtnm175
                                                      } // endtimp(g_free(23))
                                                      let jsxtnm177 = XATSDAPP(jsxtnm176(jsxtnm109))
                                                      jsxtnm178 = jsxtnm171
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(178))
                                                    return jsxtnm178
                                                  } // endtimp(forall$test(47))
                                                  let jsxtnm180 = XATSDAPP(jsxtnm179(jsxtnm87))
                                                  let jsxtnm190 // ift
                                                  if (jsxtnm180) // ift
                                                  {
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                                    // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                    // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                    // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                    let jsxtnm187 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                      let jsxtnm181 = arg1
                                                      let jsxtnm182 = arg2
                                                      // I1CMP:start
                                                      let jsxtnm186 // let
                                                      { // let
                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                        // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                        // XATS2JS_sint_add$sint_2778
                                                          // FJARGdarg($list(I1BNDcons(I1TNM(183);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(183))))),I1BNDcons(I1TNM(184);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(184)))))))
                                                          // I1CMP:start
                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                        let jsxtnm185 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm181, jsxtnm182))
                                                        jsxtnm186 = jsxtnm185
                                                      } // endlet
                                                      // I1CMP:return:I1Vtnm(I1TNM(186))
                                                      return jsxtnm186
                                                    } // endtimp(sint_add$sint(936))
                                                    let jsxtnm188 = XATSDAPP(jsxtnm187(jsxtnm87, XATSINT1(1)))
                                                    let jsxtnm189 = XATSDAPP(loop_2862(jsxtnm86, jsxtnm188))
                                                    jsxtnm190 = jsxtnm189
                                                  } else {
                                                    jsxtnm190 = XATSBOOL(false)
                                                  } // end(if)
                                                  jsxtnm191 = jsxtnm190
                                                } // end(if)
                                                // I1CMP:return:I1Vtnm(I1TNM(191))
                                                return jsxtnm191
                                              } // endfun(loop_2862)
                                              let jsxtnm192 = XATSDAPP(loop_2862(jsxtnm85, XATSINT1(0)))
                                              jsxtnm193 = jsxtnm192
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(193))
                                            return jsxtnm193
                                          } // endtimp(nint_forall(958))
                                          let jsxtnm195 = XATSDAPP(jsxtnm194(jsxtnm75))
                                          jsxtnm196 = jsxtnm195
                                        } // endlet
                                        jsxtnm197 = jsxtnm196
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(197))
                                      return jsxtnm197
                                    } // endtimp(gasq_forall(609))
                                    jsxtnm199 = jsxtnm198
                                    let jsxtnm200 = XATSDAPP(jsxtnm199(jsxtnm66))
                                    jsxtnm201 = jsxtnm200
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(201))
                                  return jsxtnm201
                                } // endtimp(gseq_forall(386))
                                let jsxtnm203 = XATSDAPP(jsxtnm202(jsxtnm65))
                                jsxtnm204 = jsxtnm203
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(204))
                              return jsxtnm204
                            } // endtimp(gseq_forall1(1720))
                            let jsxtnm206 = XATSDAPP(jsxtnm205(jsxtnm54))
                            jsxtnm207 = jsxtnm206
                          } // endlet
                          jsxtnm208 = jsxtnm207
                          XATS000_patck(true)
                          jsxtnm209 = jsxtnm208
                        } // endlet
                        // I1CMP:return:I1Vtnm(I1TNM(209))
                        return jsxtnm209
                      } // endtimp(gseq_iforall1(1736))
                      let jsxtnm211 = XATSDAPP(jsxtnm210(jsxtnm48))
                      jsxtnm212 = jsxtnm211
                      XATS000_patck(true)
                      jsxtnm213 = XATSVOID
                    } // endlet
                    jsxtnm214 = jsxtnm213
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(214))
                  return jsxtnm214
                } // endtimp(gseq_iforitm1(1760))
                let jsxtnm216 = XATSDAPP(jsxtnm215(jsxtnm29))
                jsxtnm217 = jsxtnm216
              } // endlet
              jsxtnm218 = jsxtnm217
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
              // I1VALDCL
              let jsxtnm227
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm223 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm219 = arg1
                // I1CMP:start
                let jsxtnm222 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(220);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(220)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm221 = XATSDAPP(XATS2JS_strn_print(jsxtnm219))
                  jsxtnm222 = jsxtnm221
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(222))
                return jsxtnm222
              } // endtimp(strn_print(1040))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
              // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
              // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1885(line=76,offs=1)--1918(line=77,offs=25)))
              // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm224 = function () { // timp: gseq$end(347)
                // I1CMP:start
                // I1CMP:return:I1Vstr(...)
                return XATSSTRN(")")
              } // endtimp(gseq$end(347))
              let jsxtnm225 = XATSDAPP(jsxtnm224())
              let jsxtnm226 = XATSDAPP(jsxtnm223(jsxtnm225))
              jsxtnm227 = jsxtnm226
              XATS000_patck(true)
              jsxtnm228 = XATSVOID
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(228))
            return jsxtnm228
          } // endtimp(gseq_print1(1687))
          let jsxtnm230 = XATSDAPP(jsxtnm229(jsxtnm28))
          jsxtnm231 = jsxtnm230
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(231))
        return jsxtnm231
      } // endtimp(g_print(39))
      let jsxtnm233 = XATSDAPP(jsxtnm232(jsxtnm13))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
      // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      let jsxtnm235 = function () { // timp: gs_print$end(804)
        // I1CMP:start
        let jsxtnm234 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(234))
        return jsxtnm234
      } // endtimp(gs_print$end(804))
      let jsxtnm236 = XATSDAPP(jsxtnm235())
      jsxtnm237 = jsxtnm236
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(237))
    return jsxtnm237
  } // endtimp(gs_print_a2(807))
  let jsxtnm239 = XATSDAPP(jsxtnm238(jsxtnm10, jsxtnm11))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm245
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm244 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm240 = arg1
    // I1CMP:start
    let jsxtnm243 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(241);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(241)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm242 = XATSDAPP(XATS2JS_strn_print(jsxtnm240))
      jsxtnm243 = jsxtnm242
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(243))
    return jsxtnm243
  } // endtimp(strn_print(1040))
  jsxtnm245 = jsxtnm244
  let jsxtnm246 = XATSDAPP(jsxtnm245(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(246))
  return jsxtnm246
} // endtimp(gs_println_a2(820))
let jsxtnm248 = XATSDAPP(jsxtnm247(XATSSTRN("A0 = "), jsxtnm9))
jsxtnm249 = jsxtnm248
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(421(line=28,offs=1)--431(line=28,offs=11)))
// I1VALDCL
let jsxtnm250
jsxtnm250 = XATSINT1(10)
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(432(line=29,offs=1)--472(line=31,offs=26)))
// I1VALDCL
let jsxtnm269
// LCSRCsome1(test03_a1sz000.dats)@(441(line=30,offs=1)--446(line=30,offs=6))
// I0Etapq(I0Ecst(a1sz_make_nfun(1121)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(2396(line=109,offs=1)--2410(line=109,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(a1sz_make_nfun(1121);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2703(line=144,offs=1)--2879(line=157,offs=2)))
// T1IMPallx(a1sz_make_nfun(1121)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8887],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_make_nfun(1121);$list(@(a[3030],T2Pvar(a[8887])))))))
let jsxtnm257 = function (arg1, arg2) { // timp: a1sz_make_nfun(1121)
  let jsxtnm251 = arg1
  let jsxtnm252 = arg2
  // I1CMP:start
  let jsxtnm256 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2791(line=152,offs=1)--2877(line=156,offs=45)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2799(line=153,offs=1)--2877(line=156,offs=45))
    // I1FUNDCL: XATS2JS_a1sz_make_nfun(5198)
    // XATS2JS_a1sz_make_nfun_2802
      // FJARGdarg($list(I1BNDcons(I1TNM(253);I0Pvar(n(5199));$list(@(n(5199),I1Vtnm(I1TNM(253))))),I1BNDcons(I1TNM(254);I0Pvar(f(5200));$list(@(f(5200),I1Vtnm(I1TNM(254)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_make_nfun);G1Nlist($list()))// I1CMP:return
    let jsxtnm255 = XATSDAPP(XATS2JS_a1sz_make_nfun(jsxtnm251, jsxtnm252))
    jsxtnm256 = jsxtnm255
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(256))
  return jsxtnm256
} // endtimp(a1sz_make_nfun(1121))
let jsxtnm267 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm258 = arg1
  // I1CMP:start
  // LCSRCsome1(test03_a1sz000.dats)@(468(line=31,offs=22)--469(line=31,offs=23))
  // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
  // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
  let jsxtnm265 = function (arg1, arg2) { // timp: sint_add$sint(936)
    let jsxtnm259 = arg1
    let jsxtnm260 = arg2
    // I1CMP:start
    let jsxtnm264 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
      // I1FUNDCL: XATS2JS_sint_add$sint(4922)
      // XATS2JS_sint_add$sint_2778
        // FJARGdarg($list(I1BNDcons(I1TNM(261);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(261))))),I1BNDcons(I1TNM(262);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(262)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
      let jsxtnm263 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm259, jsxtnm260))
      jsxtnm264 = jsxtnm263
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(264))
    return jsxtnm264
  } // endtimp(sint_add$sint(936))
  let jsxtnm266 = XATSDAPP(jsxtnm265(jsxtnm258, XATSINT1(1)))
  // I1CMP:return:I1Vtnm(I1TNM(266))
  return jsxtnm266
} // endfun(lam0)
let jsxtnm268 = XATSDAPP(jsxtnm257(jsxtnm250, jsxtnm267))
jsxtnm269 = jsxtnm268
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(473(line=32,offs=1)--520(line=34,offs=30)))
// I1VALDCL
let jsxtnm570
// LCSRCsome1(test03_a1sz000.dats)@(482(line=33,offs=1)--490(line=33,offs=9))
// I0Etapq(I0Ecst(gs_println_a4(822)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13918(line=908,offs=1)--13931(line=908,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
// T1IMPallx(gs_println_a4(822);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26458(line=1604,offs=1)--26602(line=1613,offs=59)))
// T1IMPallx(gs_println_a4(822)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7101],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7102],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7103],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7104],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a4(822);$list(@(x0[2570],T2Pvar(x0[7101])),@(x1[2571],T2Pvar(x1[7102])),@(x2[2572],T2Pvar(x2[7103])),@(x3[2573],T2Pvar(x3[7104])))))))
let jsxtnm563 = function (arg1, arg2, arg3, arg4) { // timp: gs_println_a4(822)
  let jsxtnm270 = arg1
  let jsxtnm271 = arg2
  let jsxtnm272 = arg3
  let jsxtnm273 = arg4
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26546(line=1613,offs=3)--26557(line=1613,offs=14))
  // I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Pvar(x0[7101]))),T2JAG($list(T2Pvar(x1[7102]))),T2JAG($list(T2Pvar(x2[7103]))),T2JAG($list(T2Pvar(x3[7104])))))
  // T1IMPallx(gs_print_a4(809);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
  // T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
  let jsxtnm554 = function (arg1, arg2, arg3, arg4) { // timp: gs_print_a4(809)
    let jsxtnm274 = arg1
    let jsxtnm275 = arg2
    let jsxtnm276 = arg3
    let jsxtnm277 = arg4
    // I1CMP:start
    let jsxtnm553 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
      // I1VALDCL
      let jsxtnm281
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
      // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      let jsxtnm279 = function () { // timp: gs_print$beg(802)
        // I1CMP:start
        let jsxtnm278 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(278))
        return jsxtnm278
      } // endtimp(gs_print$beg(802))
      let jsxtnm280 = XATSDAPP(jsxtnm279())
      jsxtnm281 = jsxtnm280
      XATS000_patck(true)
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm287
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm286 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm282 = arg1
        // I1CMP:start
        let jsxtnm285 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(283);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(283)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm284 = XATSDAPP(XATS2JS_strn_print(jsxtnm282))
          jsxtnm285 = jsxtnm284
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(285))
        return jsxtnm285
      } // endtimp(strn_print(1040))
      jsxtnm287 = jsxtnm286
      let jsxtnm288 = XATSDAPP(jsxtnm287(jsxtnm274))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm290 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm289 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(289))
        return jsxtnm289
      } // endtimp(gs_print$sep(803))
      let jsxtnm291 = XATSDAPP(jsxtnm290())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
      let jsxtnm329 = function (arg1) { // timp: g_print(39)
        let jsxtnm292 = arg1
        // I1CMP:start
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
        // I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
        // T1IMPallx(g_ptype(202);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1512(line=44,offs=1)--1614(line=51,offs=32)))
        // T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(vt[7293],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(a1sz);$list(T2Pvar(vt[7293])))))))))
        let jsxtnm313 = function () { // timp: g_ptype(202)
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1567(line=50,offs=1)--1572(line=50,offs=6))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm297 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm293 = arg1
            // I1CMP:start
            let jsxtnm296 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(294);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(294)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm295 = XATSDAPP(XATS2JS_strn_print(jsxtnm293))
              jsxtnm296 = jsxtnm295
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(296))
            return jsxtnm296
          } // endtimp(strn_print(1040))
          let jsxtnm298 = XATSDAPP(jsxtnm297(XATSSTRN("a1sz(")))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1583(line=51,offs=1)--1590(line=51,offs=8))
          // I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vt[7293])))))
          // T1IMPallx(g_ptype(202);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          // T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          let jsxtnm305 = function () { // timp: g_ptype(202)
            // I1CMP:start
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            let jsxtnm303 = function (arg1) { // timp: strn_print(1040)
              let jsxtnm299 = arg1
              // I1CMP:start
              let jsxtnm302 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                // I1FUNDCL: XATS2JS_strn_print(5082)
                // XATS2JS_strn_print_2202
                  // FJARGdarg($list(I1BNDcons(I1TNM(300);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(300)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                let jsxtnm301 = XATSDAPP(XATS2JS_strn_print(jsxtnm299))
                jsxtnm302 = jsxtnm301
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(302))
              return jsxtnm302
            } // endtimp(strn_print(1040))
            let jsxtnm304 = XATSDAPP(jsxtnm303(XATSSTRN("sint")))
            // I1CMP:return:I1Vtnm(I1TNM(304))
            return jsxtnm304
          } // endtimp(g_ptype(202))
          let jsxtnm306 = XATSDAPP(jsxtnm305())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1603(line=51,offs=21)--1608(line=51,offs=26))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm311 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm307 = arg1
            // I1CMP:start
            let jsxtnm310 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(308);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(308)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm309 = XATSDAPP(XATS2JS_strn_print(jsxtnm307))
              jsxtnm310 = jsxtnm309
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(310))
            return jsxtnm310
          } // endtimp(strn_print(1040))
          let jsxtnm312 = XATSDAPP(jsxtnm311(XATSSTRN(")")))
          // I1CMP:return:I1Vtnm(I1TNM(312))
          return jsxtnm312
        } // endtimp(g_ptype(202))
        let jsxtnm314 = XATSDAPP(jsxtnm313())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm319 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm315 = arg1
          // I1CMP:start
          let jsxtnm318 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(316);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(316)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm317 = XATSDAPP(XATS2JS_strn_print(jsxtnm315))
            jsxtnm318 = jsxtnm317
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(318))
          return jsxtnm318
        } // endtimp(strn_print(1040))
        let jsxtnm320 = XATSDAPP(jsxtnm319(XATSSTRN(":")))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
        // I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
        // T1IMPallx(g_psort(201);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1831(line=74,offs=1)--1885(line=78,offs=22)))
        // T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(tx[5755],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(tx[5755])))))))
        let jsxtnm327 = function () { // timp: g_psort(201)
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1866(line=78,offs=3)--1876(line=78,offs=13))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm325 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm321 = arg1
            // I1CMP:start
            let jsxtnm324 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(322);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(322)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm323 = XATSDAPP(XATS2JS_strn_print(jsxtnm321))
              jsxtnm324 = jsxtnm323
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(324))
            return jsxtnm324
          } // endtimp(strn_print(1040))
          let jsxtnm326 = XATSDAPP(jsxtnm325(XATSSTRN("tbox")))
          // I1CMP:return:I1Vtnm(I1TNM(326))
          return jsxtnm326
        } // endtimp(g_psort(201))
        let jsxtnm328 = XATSDAPP(jsxtnm327())
        // I1CMP:return:I1Vtnm(I1TNM(328))
        return jsxtnm328
      } // endtimp(g_print(39))
      let jsxtnm330 = XATSDAPP(jsxtnm329(jsxtnm275))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm332 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm331 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(331))
        return jsxtnm331
      } // endtimp(gs_print$sep(803))
      let jsxtnm333 = XATSDAPP(jsxtnm332())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm339
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm338 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm334 = arg1
        // I1CMP:start
        let jsxtnm337 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(335);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(335)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm336 = XATSDAPP(XATS2JS_strn_print(jsxtnm334))
          jsxtnm337 = jsxtnm336
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(337))
        return jsxtnm337
      } // endtimp(strn_print(1040))
      jsxtnm339 = jsxtnm338
      let jsxtnm340 = XATSDAPP(jsxtnm339(jsxtnm276))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm342 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm341 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(341))
        return jsxtnm341
      } // endtimp(gs_print$sep(803))
      let jsxtnm343 = XATSDAPP(jsxtnm342())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1767(line=65,offs=1)--2003(line=84,offs=4)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7295])))))))))
      let jsxtnm548 = function (arg1) { // timp: g_print(39)
        let jsxtnm344 = arg1
        // I1CMP:start
        let jsxtnm547 // let
        { // let
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1825(line=72,offs=1)--1847(line=72,offs=23))
          // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1sz);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7295])))))))
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1851(line=74,offs=1)--1884(line=75,offs=25)))
          // I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7295]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1885(line=76,offs=1)--1918(line=77,offs=25)))
          // I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7295]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1919(line=78,offs=1)--1956(line=79,offs=29)))
          // I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7295]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1972(line=83,offs=3)--1983(line=83,offs=14))
          // I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7295]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7295])))))
          // T1IMPallx(gseq_print1(1687);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
          // T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
          let jsxtnm545 = function (arg1) { // timp: gseq_print1(1687)
            let jsxtnm345 = arg1
            // I1CMP:start
            let jsxtnm544 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
              // I1VALDCL
              let jsxtnm354
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm350 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm346 = arg1
                // I1CMP:start
                let jsxtnm349 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(347);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(347)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm348 = XATSDAPP(XATS2JS_strn_print(jsxtnm346))
                  jsxtnm349 = jsxtnm348
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(349))
                return jsxtnm349
              } // endtimp(strn_print(1040))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
              // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
              // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1919(line=78,offs=1)--1956(line=79,offs=29)))
              // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm351 = function () { // timp: gseq$beg(346)
                // I1CMP:start
                // I1CMP:return:I1Vstr(...)
                return XATSSTRN("a1sz(")
              } // endtimp(gseq$beg(346))
              let jsxtnm352 = XATSDAPP(jsxtnm351())
              let jsxtnm353 = XATSDAPP(jsxtnm350(jsxtnm352))
              jsxtnm354 = jsxtnm353
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
              // I1VALDCL
              let jsxtnm534
              let jsxtnm533 // let
              { // let
                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                // I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
                // I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq_iforitm1(1760);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
                // T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
                let jsxtnm531 = function (arg1) { // timp: gseq_iforitm1(1760)
                  let jsxtnm364 = arg1
                  // I1CMP:start
                  let jsxtnm530 // let
                  { // let
                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                    // I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
                    let jsxtnm529 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
                      // I1VALDCL
                      let jsxtnm528
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
                      // I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
                      // T1IMPallx(gseq_iforall1(1736);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
                      // T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
                      let jsxtnm526 = function (arg1) { // timp: gseq_iforall1(1736)
                        let jsxtnm370 = arg1
                        // I1CMP:start
                        let jsxtnm525 // let
                        { // let
                          // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
                          // I1VARDCL
                          // I1CMP:start
                          // I1CMP:return:I1Vint(T_INT01(0))
                          let jsxtnm371 = XATSVAR1(XATSINT1(0))
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
                          // I1VALDCL
                          let jsxtnm372
                          jsxtnm372 = XATSADDR(jsxtnm371)
                          XATS000_patck(true)
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
                          // I1VALDCL
                          let jsxtnm524
                          let jsxtnm523 // let
                          { // let
                            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                            // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
                            // I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
                            // T1IMPallx(gseq_forall1(1720);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
                            // T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
                            let jsxtnm521 = function (arg1) { // timp: gseq_forall1(1720)
                              let jsxtnm381 = arg1
                              // I1CMP:start
                              let jsxtnm520 // let
                              { // let
                                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
                                // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
                                // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2214(line=93,offs=1)--2345(line=103,offs=2)))
                                // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7314])))),@(x0[1168],T2Pvar(x0[7314])))))))
                                let jsxtnm518 = function (arg1) { // timp: gseq_forall(386)
                                  let jsxtnm382 = arg1
                                  // I1CMP:start
                                  let jsxtnm517 // let
                                  { // let
                                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                    // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7314]))))):timp
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2272(line=99,offs=1)--2283(line=99,offs=12))
                                    // I0Etapq(I0Ecst(a1sz_forall(1140)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz001.sats)@(1643(line=55,offs=1)--1654(line=55,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                    // T1IMPallx(a1sz_forall(1140);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(1999(line=78,offs=1)--2057(line=81,offs=26)))
                                    // T1IMPallx(a1sz_forall(1140)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7312],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_forall(1140);$list(@(a[3064],T2Pvar(x0[7312])))))))
                                    let jsxtnm515
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2032(line=81,offs=1)--2043(line=81,offs=12))
                                    // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7312]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7312])))))
                                    // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                                    // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                                    let jsxtnm514 = function (arg1) { // timp: gasq_forall(609)
                                      let jsxtnm383 = arg1
                                      // I1CMP:start
                                      let jsxtnm513 // let
                                      { // let
                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                        // I1VALDCL
                                        let jsxtnm391
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                        // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                        // T1IMPallx(gasq_length(594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2083(line=89,offs=1)--2146(line=92,offs=33)))
                                        // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7296])))),@(x0[1875],T2Pvar(x0[7296])))))))
                                        let jsxtnm389
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2131(line=92,offs=18)--2142(line=92,offs=29))
                                        // I0Etapq(I0Ecst(a1sz_length(1125)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3102(line=157,offs=1)--3113(line=157,offs=12))));$list(T2JAG($list(T2Pvar(x0[7296])))))
                                        // T1IMPallx(a1sz_length(1125);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1594(line=50,offs=1)--1768(line=64,offs=2)))
                                        // T1IMPallx(a1sz_length(1125)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8875],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_length(1125);$list(@(a[3038],T2Pvar(a[8875])))))))
                                        let jsxtnm388 = function (arg1) { // timp: a1sz_length(1125)
                                          let jsxtnm384 = arg1
                                          // I1CMP:start
                                          let jsxtnm387 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1684(line=58,offs=1)--1766(line=63,offs=37)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1692(line=59,offs=1)--1766(line=63,offs=37))
                                            // I1FUNDCL: XATS2JS_a1sz_length(5172)
                                            // XATS2JS_a1sz_length_1695
                                              // FJARGdarg($list(I1BNDcons(I1TNM(385);I0Pvar(A(5173));$list(@(A(5173),I1Vtnm(I1TNM(385)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_length);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm386 = XATSDAPP(XATS2JS_a1sz_length(jsxtnm384))
                                            jsxtnm387 = jsxtnm386
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(387))
                                          return jsxtnm387
                                        } // endtimp(a1sz_length(1125))
                                        jsxtnm389 = jsxtnm388
                                        let jsxtnm390 = XATSDAPP(jsxtnm389(jsxtnm383))
                                        jsxtnm391 = jsxtnm390
                                        XATS000_patck(true)
                                        let jsxtnm512 // let
                                        { // let
                                          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                          // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                          // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                          // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                          // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                          let jsxtnm510 = function (arg1) { // timp: nint_forall(958)
                                            let jsxtnm401 = arg1
                                            // I1CMP:start
                                            let jsxtnm509 // let
                                            { // let
                                              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                              // I1FUNDCL
                                              function loop_2862(arg1, arg2)
                                              { // fun
                                                let jsxtnm402 = arg1
                                                let jsxtnm403 = arg2
                                                // I1CMP:start
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                                let jsxtnm410 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                                  let jsxtnm404 = arg1
                                                  let jsxtnm405 = arg2
                                                  // I1CMP:start
                                                  let jsxtnm409 // let
                                                  { // let
                                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                                    // XATS2JS_sint_gte$sint_2399
                                                      // FJARGdarg($list(I1BNDcons(I1TNM(406);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(406))))),I1BNDcons(I1TNM(407);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(407)))))))
                                                      // I1CMP:start
                                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                                    let jsxtnm408 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm404, jsxtnm405))
                                                    jsxtnm409 = jsxtnm408
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(409))
                                                  return jsxtnm409
                                                } // endtimp(sint_gte$sint(931))
                                                let jsxtnm411 = XATSDAPP(jsxtnm410(jsxtnm403, jsxtnm402))
                                                let jsxtnm507 // ift
                                                if (jsxtnm411) // ift
                                                {
                                                  jsxtnm507 = XATSBOOL(true)
                                                } else {
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                                  // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                  // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                                  // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                                  let jsxtnm495 = function (arg1) { // timp: forall$test(47)
                                                    let jsxtnm412 = arg1
                                                    // I1CMP:start
                                                    let jsxtnm494 // let
                                                    { // let
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                                      // I1VALDCL
                                                      let jsxtnm425
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                                      // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2517(line=119,offs=1)--2612(line=123,offs=35)))
                                                      // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7301])))),@(x0[5735],T2Pvar(x0[7301])))))))
                                                      let jsxtnm423 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                        let jsxtnm413 = arg1
                                                        let jsxtnm414 = arg2
                                                        // I1CMP:start
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2590(line=123,offs=13)--2602(line=123,offs=25))
                                                        // I0Etapq(I0Ecst(a1sz_lget$at(1130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3888(line=213,offs=1)--3900(line=213,offs=13))));$list(T2JAG($list(T2Pvar(x0[7301])))))
                                                        // T1IMPallx(a1sz_lget$at(1130);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1815(line=69,offs=1)--1992(line=84,offs=2)))
                                                        // T1IMPallx(a1sz_lget$at(1130)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8879],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_lget$at(1130);$list(@(a[3048],T2Pvar(a[8879])))))))
                                                        let jsxtnm421 = function (arg1, arg2) { // timp: a1sz_lget$at(1130)
                                                          let jsxtnm415 = arg1
                                                          let jsxtnm416 = arg2
                                                          // I1CMP:start
                                                          let jsxtnm420 // let
                                                          { // let
                                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1899(line=77,offs=1)--1990(line=83,offs=38)))
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1907(line=78,offs=1)--1990(line=83,offs=38))
                                                            // I1FUNDCL: XATS2JS_a1sz_lget$at(5176)
                                                            // XATS2JS_a1sz_lget$at_1910
                                                              // FJARGdarg($list(I1BNDcons(I1TNM(417);I0Pvar(A(5177));$list(@(A(5177),I1Vtnm(I1TNM(417))))),I1BNDcons(I1TNM(418);I0Pvar(i(5178));$list(@(i(5178),I1Vtnm(I1TNM(418)))))))
                                                              // I1CMP:start
                                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_lget$at);G1Nlist($list()))// I1CMP:return
                                                            let jsxtnm419 = XATSDAPP(XATS2JS_a1sz_lget$at(jsxtnm415, jsxtnm416))
                                                            jsxtnm420 = jsxtnm419
                                                          } // endlet
                                                          // I1CMP:return:I1Vtnm(I1TNM(420))
                                                          return jsxtnm420
                                                        } // endtimp(a1sz_lget$at(1130))
                                                        let jsxtnm422 = XATSDAPP(jsxtnm421(jsxtnm413, jsxtnm414))
                                                        // I1CMP:return:I1Vtnm(I1TNM(422))
                                                        return jsxtnm422
                                                      } // endtimp(gasq_lget$at$raw(2326))
                                                      let jsxtnm424 = XATSDAPP(jsxtnm423(jsxtnm383, jsxtnm412))
                                                      jsxtnm425 = jsxtnm424
                                                      XATS000_patck(true)
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                                      // I1VALDCL
                                                      let jsxtnm487
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm485
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2328(line=102,offs=20)--2339(line=102,offs=31))
                                                      // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                                      // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                                      // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm484
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm483 = function (arg1) { // timp: forall$test1(1423)
                                                        let jsxtnm426 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm482 // let
                                                        { // let
                                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                                                          // I1VALDCL
                                                          let jsxtnm431
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                                                          // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                          // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                          // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                          let jsxtnm429 = function (arg1) { // timp: p2tr_get(2309)
                                                            let jsxtnm427 = arg1
                                                            // I1CMP:start
                                                            let jsxtnm428 = XATS000_dp2tr(jsxtnm427)
                                                            // I1CMP:return:I1Vtnm(I1TNM(428))
                                                            return jsxtnm428
                                                          } // endtimp(p2tr_get(2309))
                                                          let jsxtnm430 = XATSDAPP(jsxtnm429(jsxtnm372))
                                                          jsxtnm431 = jsxtnm430
                                                          XATS000_patck(true)
                                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                                                          // I1VALDCL
                                                          let jsxtnm469
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                                                          // I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                                                          // T1IMPallx(iforall$test1(1433);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                                                          // T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                          let jsxtnm467 = function (arg1, arg2) { // timp: iforall$test1(1433)
                                                            let jsxtnm432 = arg1
                                                            let jsxtnm433 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm466 // let
                                                            { // let
                                                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                                                              // I1VALDCL
                                                              let jsxtnm465
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                                                              // I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                                                              // T1IMPallx(iforitm$work1(1449);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                                                              // T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                              let jsxtnm463 = function (arg1, arg2) { // timp: iforitm$work1(1449)
                                                                let jsxtnm434 = arg1
                                                                let jsxtnm435 = arg2
                                                                // I1CMP:start
                                                                let jsxtnm462 // let
                                                                { // let
                                                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                                                  // I1VALDCL
                                                                  let jsxtnm453
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                                                  // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                                                  // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                                                  // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                                                  let jsxtnm442 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                                                    let jsxtnm436 = arg1
                                                                    let jsxtnm437 = arg2
                                                                    // I1CMP:start
                                                                    let jsxtnm441 // let
                                                                    { // let
                                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                                                      // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                                                      // XATS2JS_sint_gt$sint_1876
                                                                        // FJARGdarg($list(I1BNDcons(I1TNM(438);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(438))))),I1BNDcons(I1TNM(439);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(439)))))))
                                                                        // I1CMP:start
                                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                                                      let jsxtnm440 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm436, jsxtnm437))
                                                                      jsxtnm441 = jsxtnm440
                                                                    } // endlet
                                                                    // I1CMP:return:I1Vtnm(I1TNM(441))
                                                                    return jsxtnm441
                                                                  } // endtimp(sint_gt$sint(928))
                                                                  let jsxtnm443 = XATSDAPP(jsxtnm442(jsxtnm434, XATSINT1(0)))
                                                                  let jsxtnm452 // ift
                                                                  if (jsxtnm443) // ift
                                                                  {
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                                                    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                                                    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                                                    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                                                    let jsxtnm448 = function (arg1) { // timp: strn_print(1040)
                                                                      let jsxtnm444 = arg1
                                                                      // I1CMP:start
                                                                      let jsxtnm447 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                                        // I1FUNDCL: XATS2JS_strn_print(5082)
                                                                        // XATS2JS_strn_print_2202
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(445);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(445)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm446 = XATSDAPP(XATS2JS_strn_print(jsxtnm444))
                                                                        jsxtnm447 = jsxtnm446
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(447))
                                                                      return jsxtnm447
                                                                    } // endtimp(strn_print(1040))
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                                                    // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                                                    // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1851(line=74,offs=1)--1884(line=75,offs=25)))
                                                                    // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                    let jsxtnm449 = function () { // timp: gseq$sep(348)
                                                                      // I1CMP:start
                                                                      // I1CMP:return:I1Vstr(...)
                                                                      return XATSSTRN(",")
                                                                    } // endtimp(gseq$sep(348))
                                                                    let jsxtnm450 = XATSDAPP(jsxtnm449())
                                                                    let jsxtnm451 = XATSDAPP(jsxtnm448(jsxtnm450))
                                                                    jsxtnm452 = jsxtnm451
                                                                  } else {
                                                                  } // end(if)
                                                                  jsxtnm453 = jsxtnm452
                                                                  XATS000_patck(true)
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                                                  // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                                                  // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                                                  // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                                                  let jsxtnm460
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                                                  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                                                  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                                                  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                                                  let jsxtnm459
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                                                  // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                                                  // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                                                  // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                                                  let jsxtnm458 = function (arg1) { // timp: sint_print(922)
                                                                    let jsxtnm454 = arg1
                                                                    // I1CMP:start
                                                                    let jsxtnm457 // let
                                                                    { // let
                                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                                                      // I1FUNDCL: XATS2JS_sint_print(4946)
                                                                      // XATS2JS_sint_print_3707
                                                                        // FJARGdarg($list(I1BNDcons(I1TNM(455);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(455)))))))
                                                                        // I1CMP:start
                                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                                                      let jsxtnm456 = XATSDAPP(XATS2JS_sint_print(jsxtnm454))
                                                                      jsxtnm457 = jsxtnm456
                                                                    } // endlet
                                                                    // I1CMP:return:I1Vtnm(I1TNM(457))
                                                                    return jsxtnm457
                                                                  } // endtimp(sint_print(922))
                                                                  jsxtnm459 = jsxtnm458
                                                                  jsxtnm460 = jsxtnm459
                                                                  let jsxtnm461 = XATSDAPP(jsxtnm460(jsxtnm435))
                                                                  jsxtnm462 = jsxtnm461
                                                                } // endlet
                                                                // I1CMP:return:I1Vtnm(I1TNM(462))
                                                                return jsxtnm462
                                                              } // endtimp(iforitm$work1(1449))
                                                              let jsxtnm464 = XATSDAPP(jsxtnm463(jsxtnm432, jsxtnm433))
                                                              jsxtnm465 = jsxtnm464
                                                              XATS000_patck(true)
                                                              jsxtnm466 = XATSBOOL(true)
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(466))
                                                            return jsxtnm466
                                                          } // endtimp(iforall$test1(1433))
                                                          let jsxtnm468 = XATSDAPP(jsxtnm467(jsxtnm431, jsxtnm426))
                                                          jsxtnm469 = jsxtnm468
                                                          XATS000_patck(true)
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                                                          // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                          // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                                          // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                                          let jsxtnm472 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                                            let jsxtnm470 = arg1
                                                            let jsxtnm471 = arg2
                                                            // I1CMP:start
                                                            XATS000_assgn(jsxtnm470, jsxtnm471)
                                                            // I1CMP:return:I1V000()
                                                            return XATSVOID
                                                          } // endtimp(p2tr_set(2310))
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                                                          // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                          // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                          // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                          let jsxtnm479 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                            let jsxtnm473 = arg1
                                                            let jsxtnm474 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm478 // let
                                                            { // let
                                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                              // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                              // XATS2JS_sint_add$sint_2778
                                                                // FJARGdarg($list(I1BNDcons(I1TNM(475);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(475))))),I1BNDcons(I1TNM(476);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(476)))))))
                                                                // I1CMP:start
                                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                              let jsxtnm477 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm473, jsxtnm474))
                                                              jsxtnm478 = jsxtnm477
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(478))
                                                            return jsxtnm478
                                                          } // endtimp(sint_add$sint(936))
                                                          let jsxtnm480 = XATSDAPP(jsxtnm479(jsxtnm431, XATSINT1(1)))
                                                          let jsxtnm481 = XATSDAPP(jsxtnm472(jsxtnm372, jsxtnm480))
                                                          jsxtnm482 = jsxtnm469
                                                        } // endlet
                                                        // I1CMP:return:I1Vtnm(I1TNM(482))
                                                        return jsxtnm482
                                                      } // endtimp(forall$test1(1423))
                                                      jsxtnm484 = jsxtnm483
                                                      jsxtnm485 = jsxtnm484
                                                      let jsxtnm486 = XATSDAPP(jsxtnm485(jsxtnm425))
                                                      jsxtnm487 = jsxtnm486
                                                      XATS000_patck(true)
                                                      // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                                      // I1VALDCL
                                                      // I1BNDcons(I1TNM(489);I0Ptup0($list());$list())
                                                      // I1CMP:start
                                                      // I1LETnew1(I1TNM(488);...)
                                                        // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(425))))
                                                      // I1CMP(ival):I1Vtnm(I1TNM(488))// I1CMP:return
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                                      // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                                      // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                                      let jsxtnm492 = function (arg1) { // timp: g_free(23)
                                                        let jsxtnm490 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm491 = XATSTUP0([])
                                                        // I1CMP:return:I1Vtnm(I1TNM(491))
                                                        return jsxtnm491
                                                      } // endtimp(g_free(23))
                                                      let jsxtnm493 = XATSDAPP(jsxtnm492(jsxtnm425))
                                                      jsxtnm494 = jsxtnm487
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(494))
                                                    return jsxtnm494
                                                  } // endtimp(forall$test(47))
                                                  let jsxtnm496 = XATSDAPP(jsxtnm495(jsxtnm403))
                                                  let jsxtnm506 // ift
                                                  if (jsxtnm496) // ift
                                                  {
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                                    // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                    // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                    // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                    let jsxtnm503 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                      let jsxtnm497 = arg1
                                                      let jsxtnm498 = arg2
                                                      // I1CMP:start
                                                      let jsxtnm502 // let
                                                      { // let
                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                        // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                        // XATS2JS_sint_add$sint_2778
                                                          // FJARGdarg($list(I1BNDcons(I1TNM(499);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(499))))),I1BNDcons(I1TNM(500);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(500)))))))
                                                          // I1CMP:start
                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                        let jsxtnm501 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm497, jsxtnm498))
                                                        jsxtnm502 = jsxtnm501
                                                      } // endlet
                                                      // I1CMP:return:I1Vtnm(I1TNM(502))
                                                      return jsxtnm502
                                                    } // endtimp(sint_add$sint(936))
                                                    let jsxtnm504 = XATSDAPP(jsxtnm503(jsxtnm403, XATSINT1(1)))
                                                    let jsxtnm505 = XATSDAPP(loop_2862(jsxtnm402, jsxtnm504))
                                                    jsxtnm506 = jsxtnm505
                                                  } else {
                                                    jsxtnm506 = XATSBOOL(false)
                                                  } // end(if)
                                                  jsxtnm507 = jsxtnm506
                                                } // end(if)
                                                // I1CMP:return:I1Vtnm(I1TNM(507))
                                                return jsxtnm507
                                              } // endfun(loop_2862)
                                              let jsxtnm508 = XATSDAPP(loop_2862(jsxtnm401, XATSINT1(0)))
                                              jsxtnm509 = jsxtnm508
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(509))
                                            return jsxtnm509
                                          } // endtimp(nint_forall(958))
                                          let jsxtnm511 = XATSDAPP(jsxtnm510(jsxtnm391))
                                          jsxtnm512 = jsxtnm511
                                        } // endlet
                                        jsxtnm513 = jsxtnm512
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(513))
                                      return jsxtnm513
                                    } // endtimp(gasq_forall(609))
                                    jsxtnm515 = jsxtnm514
                                    let jsxtnm516 = XATSDAPP(jsxtnm515(jsxtnm382))
                                    jsxtnm517 = jsxtnm516
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(517))
                                  return jsxtnm517
                                } // endtimp(gseq_forall(386))
                                let jsxtnm519 = XATSDAPP(jsxtnm518(jsxtnm381))
                                jsxtnm520 = jsxtnm519
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(520))
                              return jsxtnm520
                            } // endtimp(gseq_forall1(1720))
                            let jsxtnm522 = XATSDAPP(jsxtnm521(jsxtnm370))
                            jsxtnm523 = jsxtnm522
                          } // endlet
                          jsxtnm524 = jsxtnm523
                          XATS000_patck(true)
                          jsxtnm525 = jsxtnm524
                        } // endlet
                        // I1CMP:return:I1Vtnm(I1TNM(525))
                        return jsxtnm525
                      } // endtimp(gseq_iforall1(1736))
                      let jsxtnm527 = XATSDAPP(jsxtnm526(jsxtnm364))
                      jsxtnm528 = jsxtnm527
                      XATS000_patck(true)
                      jsxtnm529 = XATSVOID
                    } // endlet
                    jsxtnm530 = jsxtnm529
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(530))
                  return jsxtnm530
                } // endtimp(gseq_iforitm1(1760))
                let jsxtnm532 = XATSDAPP(jsxtnm531(jsxtnm345))
                jsxtnm533 = jsxtnm532
              } // endlet
              jsxtnm534 = jsxtnm533
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
              // I1VALDCL
              let jsxtnm543
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm539 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm535 = arg1
                // I1CMP:start
                let jsxtnm538 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(536);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(536)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm537 = XATSDAPP(XATS2JS_strn_print(jsxtnm535))
                  jsxtnm538 = jsxtnm537
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(538))
                return jsxtnm538
              } // endtimp(strn_print(1040))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
              // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
              // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1885(line=76,offs=1)--1918(line=77,offs=25)))
              // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm540 = function () { // timp: gseq$end(347)
                // I1CMP:start
                // I1CMP:return:I1Vstr(...)
                return XATSSTRN(")")
              } // endtimp(gseq$end(347))
              let jsxtnm541 = XATSDAPP(jsxtnm540())
              let jsxtnm542 = XATSDAPP(jsxtnm539(jsxtnm541))
              jsxtnm543 = jsxtnm542
              XATS000_patck(true)
              jsxtnm544 = XATSVOID
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(544))
            return jsxtnm544
          } // endtimp(gseq_print1(1687))
          let jsxtnm546 = XATSDAPP(jsxtnm545(jsxtnm344))
          jsxtnm547 = jsxtnm546
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(547))
        return jsxtnm547
      } // endtimp(g_print(39))
      let jsxtnm549 = XATSDAPP(jsxtnm548(jsxtnm277))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
      // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      let jsxtnm551 = function () { // timp: gs_print$end(804)
        // I1CMP:start
        let jsxtnm550 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(550))
        return jsxtnm550
      } // endtimp(gs_print$end(804))
      let jsxtnm552 = XATSDAPP(jsxtnm551())
      jsxtnm553 = jsxtnm552
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(553))
    return jsxtnm553
  } // endtimp(gs_print_a4(809))
  let jsxtnm555 = XATSDAPP(jsxtnm554(jsxtnm270, jsxtnm271, jsxtnm272, jsxtnm273))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26588(line=1613,offs=45)--26595(line=1613,offs=52))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm561
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm560 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm556 = arg1
    // I1CMP:start
    let jsxtnm559 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(557);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(557)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm558 = XATSDAPP(XATS2JS_strn_print(jsxtnm556))
      jsxtnm559 = jsxtnm558
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(559))
    return jsxtnm559
  } // endtimp(strn_print(1040))
  jsxtnm561 = jsxtnm560
  let jsxtnm562 = XATSDAPP(jsxtnm561(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(562))
  return jsxtnm562
} // endtimp(gs_println_a4(822))
// LCSRCsome1(test03_a1sz000.dats)@(499(line=34,offs=9)--503(line=34,offs=13))
// I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
// T1IMPallx(g_type(196);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
// T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
let jsxtnm567 = function (arg1) { // timp: g_type(196)
  let jsxtnm564 = arg1
  // I1CMP:start
  let jsxtnm565 = XATSCAPP("unit", [0])
  let jsxtnm566 = XATSCAST("castxy_1839", [jsxtnm565])
  // I1CMP:return:I1Vtnm(I1TNM(566))
  return jsxtnm566
} // endtimp(g_type(196))
let jsxtnm568 = XATSDAPP(jsxtnm567(jsxtnm269))
let jsxtnm569 = XATSDAPP(jsxtnm563(XATSSTRN("A0("), jsxtnm568, XATSSTRN(") = "), jsxtnm269))
jsxtnm570 = jsxtnm569
XATS000_patck(true)
// I1Dfundclist(LCSRCsome1(test03_a1sz000.dats)@(567(line=39,offs=1)--631(line=44,offs=32)))
// I1FUNDCL
function fact_570(arg1)
{ // fun
  let jsxtnm571 = arg1
  // I1CMP:start
  // LCSRCsome1(test03_a1sz000.dats)@(624(line=44,offs=25)--631(line=44,offs=32))
  // I0Etapq(I0Ecst(GSEQ_prod(249)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2953(line=150,offs=1)--2962(line=150,offs=10))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  // T1IMPallx(GSEQ_prod(249);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2187(line=101,offs=1)--2283(line=108,offs=35)))
  // T1IMPallx(GSEQ_prod(249)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6659],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6660],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_prod(249);$list(@(xs[825],T2Pvar(xs[6659])),@(x0[826],T2Pvar(x0[6660])))))))
  let jsxtnm731 = function (arg1) { // timp: GSEQ_prod(249)
    let jsxtnm572 = arg1
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2239(line=107,offs=1)--2248(line=107,offs=10))
    // I0Etapq(I0Ecst(gseq_prod(345)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2064(line=105,offs=1)--2073(line=105,offs=10))));$list(T2JAG($list(T2Pvar(xs[6659]))),T2JAG($list(T2Pvar(x0[6660])))))
    // T1IMPallx(gseq_prod(345);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2634(line=144,offs=1)--2693(line=147,offs=31)))
    // T1IMPallx(gseq_prod(345)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6050],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6051],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_prod(345);$list(@(xs[1065],T2Pvar(xs[6050])),@(x0[1066],T2Pvar(x0[6051])))))))
    let jsxtnm725
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2675(line=147,offs=13)--2685(line=147,offs=23))
    // I0Etapq(I0Ecst(gseq_prod0(1667)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(2132(line=108,offs=1)--2142(line=108,offs=11))));$list(T2JAG($list(T2Pvar(xs[6050]))),T2JAG($list(T2Pvar(x0[6051])))))
    // T1IMPallx(gseq_prod0(1667);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(1943(line=75,offs=1)--2120(line=87,offs=4)))
    // T1IMPallx(gseq_prod0(1667)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7891],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_prod0(1667);$list(@(xs[4181],T2Pvar(xs[7891])),@(x0[4182],T2Pvar(x0[7892])))))))
    let jsxtnm724 = function (arg1) { // timp: gseq_prod0(1667)
      let jsxtnm573 = arg1
      // I1CMP:start
      let jsxtnm723 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(1993(line=80,offs=1)--2011(line=80,offs=19)))
        // I1VALDCL
        let jsxtnm576
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2002(line=80,offs=10)--2005(line=80,offs=13))
        // I0Etapq(I0Ecst(g_1(211)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gnum000.sats)@(1457(line=46,offs=1)--1460(line=46,offs=4))));$list(T2JAG($list(T2Pvar(x0[7892])))))
        // T1IMPallx(g_1(211);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(1619(line=51,offs=1)--1645(line=52,offs=18)))
        // T1IMPallx(g_1(211)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_1(211);$list(@(a[779],T2Pcst(si)))))))
        let jsxtnm574 = function () { // timp: g_1(211)
          // I1CMP:start
          // I1CMP:return:I1Vint(T_INT01(1))
          return XATSINT1(1)
        } // endtimp(g_1(211))
        let jsxtnm575 = XATSDAPP(jsxtnm574())
        jsxtnm576 = jsxtnm575
        XATS000_patck(true)
        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2012(line=81,offs=1)--2074(line=84,offs=31)))
        // I1Dimplmnt0(DIMPLone2(folditm$fopr0(1454);$list(@(x0[3797],T2Pvar(x0[7892])),@(r0[3798],T2Pvar(x0[7892]))))):timp
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2083(line=86,offs=1)--2096(line=86,offs=14))
        // I0Etapq(I0Ecst(gseq_folditm0(1767)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(12340(line=666,offs=1)--12353(line=666,offs=14))));$list(T2JAG($list(T2Pvar(xs[7891]))),T2JAG($list(T2Pvar(x0[7892]))),T2JAG($list(T2Pvar(x0[7892])))))
        // T1IMPallx(gseq_folditm0(1767);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11599(line=792,offs=1)--11911(line=818,offs=2)))
        // T1IMPallx(gseq_folditm0(1767)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8054],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8055],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[8056],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_folditm0(1767);$list(@(xs[4418],T2Pvar(xs[8054])),@(x0[4419],T2Pvar(x0[8055])),@(r0[4420],T2Pvar(r0[8056])))))))
        let jsxtnm721 = function (arg1, arg2) { // timp: gseq_folditm0(1767)
          let jsxtnm580 = arg1
          let jsxtnm581 = arg2
          // I1CMP:start
          let jsxtnm720 // let
          { // let
            // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11679(line=800,offs=1)--11694(line=800,offs=16)))
            // I1VARDCL
            // I1CMP:start
            // I1CMP:return:I1Vtnm(I1TNM(581))
            let jsxtnm582 = XATSVAR1(jsxtnm581)
            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11698(line=802,offs=1)--11716(line=802,offs=19)))
            // I1VALDCL
            let jsxtnm583
            jsxtnm583 = XATSADDR(jsxtnm582)
            XATS000_patck(true)
            // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11720(line=804,offs=1)--11906(line=816,offs=41)))
            // I1VALDCL
            let jsxtnm718
            let jsxtnm717 // let
            { // let
              // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11766(line=809,offs=1)--11905(line=816,offs=40)))
              // I1Dimplmnt0(DIMPLone2(foritm$work0(1442);$list(@(x0[3785],T2Pvar(x0[8055]))))):timp
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11731(line=806,offs=1)--11743(line=806,offs=13))
              // I0Etapq(I0Ecst(gseq_foritm0(1751)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(9424(line=503,offs=1)--9436(line=503,offs=13))));$list(T2JAG($list(T2Pvar(xs[8054]))),T2JAG($list(T2Pvar(x0[8055])))))
              // T1IMPallx(gseq_foritm0(1751);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8019(line=527,offs=1)--8210(line=544,offs=2)))
              // T1IMPallx(gseq_foritm0(1751)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8022],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8023],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm0(1751);$list(@(xs[4386],T2Pvar(xs[8022])),@(x0[4387],T2Pvar(x0[8023])))))))
              let jsxtnm715 = function (arg1) { // timp: gseq_foritm0(1751)
                let jsxtnm591 = arg1
                // I1CMP:start
                let jsxtnm714 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8131(line=539,offs=1)--8208(line=543,offs=33)))
                  // I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8023]))))):timp
                  let jsxtnm713 // let
                  { // let
                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8078(line=534,offs=1)--8111(line=536,offs=13)))
                    // I1VALDCL
                    let jsxtnm712
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8086(line=535,offs=1)--8098(line=535,offs=13))
                    // I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8022]))),T2JAG($list(T2Pvar(x0[8023])))))
                    // T1IMPallx(gseq_forall0(1719);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
                    // T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
                    let jsxtnm710 = function (arg1) { // timp: gseq_forall0(1719)
                      let jsxtnm596 = arg1
                      // I1CMP:start
                      let jsxtnm709 // let
                      { // let
                        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                        // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
                        // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
                        // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2214(line=93,offs=1)--2345(line=103,offs=2)))
                        // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7314])))),@(x0[1168],T2Pvar(x0[7314])))))))
                        let jsxtnm707 = function (arg1) { // timp: gseq_forall(386)
                          let jsxtnm597 = arg1
                          // I1CMP:start
                          let jsxtnm706 // let
                          { // let
                            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                            // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7314]))))):timp
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2272(line=99,offs=1)--2283(line=99,offs=12))
                            // I0Etapq(I0Ecst(a1sz_forall(1140)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz001.sats)@(1643(line=55,offs=1)--1654(line=55,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                            // T1IMPallx(a1sz_forall(1140);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(1999(line=78,offs=1)--2057(line=81,offs=26)))
                            // T1IMPallx(a1sz_forall(1140)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7312],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_forall(1140);$list(@(a[3064],T2Pvar(x0[7312])))))))
                            let jsxtnm704
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2032(line=81,offs=1)--2043(line=81,offs=12))
                            // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7312]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7312])))))
                            // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                            // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                            let jsxtnm703 = function (arg1) { // timp: gasq_forall(609)
                              let jsxtnm598 = arg1
                              // I1CMP:start
                              let jsxtnm702 // let
                              { // let
                                // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                // I1VALDCL
                                let jsxtnm606
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                // T1IMPallx(gasq_length(594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2083(line=89,offs=1)--2146(line=92,offs=33)))
                                // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7296])))),@(x0[1875],T2Pvar(x0[7296])))))))
                                let jsxtnm604
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2131(line=92,offs=18)--2142(line=92,offs=29))
                                // I0Etapq(I0Ecst(a1sz_length(1125)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3102(line=157,offs=1)--3113(line=157,offs=12))));$list(T2JAG($list(T2Pvar(x0[7296])))))
                                // T1IMPallx(a1sz_length(1125);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1594(line=50,offs=1)--1768(line=64,offs=2)))
                                // T1IMPallx(a1sz_length(1125)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8875],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_length(1125);$list(@(a[3038],T2Pvar(a[8875])))))))
                                let jsxtnm603 = function (arg1) { // timp: a1sz_length(1125)
                                  let jsxtnm599 = arg1
                                  // I1CMP:start
                                  let jsxtnm602 // let
                                  { // let
                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1684(line=58,offs=1)--1766(line=63,offs=37)))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1692(line=59,offs=1)--1766(line=63,offs=37))
                                    // I1FUNDCL: XATS2JS_a1sz_length(5172)
                                    // XATS2JS_a1sz_length_1695
                                      // FJARGdarg($list(I1BNDcons(I1TNM(600);I0Pvar(A(5173));$list(@(A(5173),I1Vtnm(I1TNM(600)))))))
                                      // I1CMP:start
                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_length);G1Nlist($list()))// I1CMP:return
                                    let jsxtnm601 = XATSDAPP(XATS2JS_a1sz_length(jsxtnm599))
                                    jsxtnm602 = jsxtnm601
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(602))
                                  return jsxtnm602
                                } // endtimp(a1sz_length(1125))
                                jsxtnm604 = jsxtnm603
                                let jsxtnm605 = XATSDAPP(jsxtnm604(jsxtnm598))
                                jsxtnm606 = jsxtnm605
                                XATS000_patck(true)
                                let jsxtnm701 // let
                                { // let
                                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                  // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                  // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                  // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                  // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                  let jsxtnm699 = function (arg1) { // timp: nint_forall(958)
                                    let jsxtnm616 = arg1
                                    // I1CMP:start
                                    let jsxtnm698 // let
                                    { // let
                                      // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                      // I1FUNDCL
                                      function loop_2862(arg1, arg2)
                                      { // fun
                                        let jsxtnm617 = arg1
                                        let jsxtnm618 = arg2
                                        // I1CMP:start
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                        // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                        // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                        // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                        let jsxtnm625 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                          let jsxtnm619 = arg1
                                          let jsxtnm620 = arg2
                                          // I1CMP:start
                                          let jsxtnm624 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                            // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                            // XATS2JS_sint_gte$sint_2399
                                              // FJARGdarg($list(I1BNDcons(I1TNM(621);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(621))))),I1BNDcons(I1TNM(622);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(622)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm623 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm619, jsxtnm620))
                                            jsxtnm624 = jsxtnm623
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(624))
                                          return jsxtnm624
                                        } // endtimp(sint_gte$sint(931))
                                        let jsxtnm626 = XATSDAPP(jsxtnm625(jsxtnm618, jsxtnm617))
                                        let jsxtnm696 // ift
                                        if (jsxtnm626) // ift
                                        {
                                          jsxtnm696 = XATSBOOL(true)
                                        } else {
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                          // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                          // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                          // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                          let jsxtnm684 = function (arg1) { // timp: forall$test(47)
                                            let jsxtnm627 = arg1
                                            // I1CMP:start
                                            let jsxtnm683 // let
                                            { // let
                                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                              // I1VALDCL
                                              let jsxtnm640
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                              // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                              // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2517(line=119,offs=1)--2612(line=123,offs=35)))
                                              // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7301])))),@(x0[5735],T2Pvar(x0[7301])))))))
                                              let jsxtnm638 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                let jsxtnm628 = arg1
                                                let jsxtnm629 = arg2
                                                // I1CMP:start
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2590(line=123,offs=13)--2602(line=123,offs=25))
                                                // I0Etapq(I0Ecst(a1sz_lget$at(1130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3888(line=213,offs=1)--3900(line=213,offs=13))));$list(T2JAG($list(T2Pvar(x0[7301])))))
                                                // T1IMPallx(a1sz_lget$at(1130);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1815(line=69,offs=1)--1992(line=84,offs=2)))
                                                // T1IMPallx(a1sz_lget$at(1130)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8879],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_lget$at(1130);$list(@(a[3048],T2Pvar(a[8879])))))))
                                                let jsxtnm636 = function (arg1, arg2) { // timp: a1sz_lget$at(1130)
                                                  let jsxtnm630 = arg1
                                                  let jsxtnm631 = arg2
                                                  // I1CMP:start
                                                  let jsxtnm635 // let
                                                  { // let
                                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1899(line=77,offs=1)--1990(line=83,offs=38)))
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1907(line=78,offs=1)--1990(line=83,offs=38))
                                                    // I1FUNDCL: XATS2JS_a1sz_lget$at(5176)
                                                    // XATS2JS_a1sz_lget$at_1910
                                                      // FJARGdarg($list(I1BNDcons(I1TNM(632);I0Pvar(A(5177));$list(@(A(5177),I1Vtnm(I1TNM(632))))),I1BNDcons(I1TNM(633);I0Pvar(i(5178));$list(@(i(5178),I1Vtnm(I1TNM(633)))))))
                                                      // I1CMP:start
                                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_lget$at);G1Nlist($list()))// I1CMP:return
                                                    let jsxtnm634 = XATSDAPP(XATS2JS_a1sz_lget$at(jsxtnm630, jsxtnm631))
                                                    jsxtnm635 = jsxtnm634
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(635))
                                                  return jsxtnm635
                                                } // endtimp(a1sz_lget$at(1130))
                                                let jsxtnm637 = XATSDAPP(jsxtnm636(jsxtnm628, jsxtnm629))
                                                // I1CMP:return:I1Vtnm(I1TNM(637))
                                                return jsxtnm637
                                              } // endtimp(gasq_lget$at$raw(2326))
                                              let jsxtnm639 = XATSDAPP(jsxtnm638(jsxtnm598, jsxtnm627))
                                              jsxtnm640 = jsxtnm639
                                              XATS000_patck(true)
                                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                              // I1VALDCL
                                              let jsxtnm676
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                              // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                              // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                              // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                              let jsxtnm674
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2328(line=102,offs=20)--2339(line=102,offs=31))
                                              // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                              // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                                              // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                              let jsxtnm673
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                                              // I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                                              // T1IMPallx(forall$test0(1422);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8131(line=539,offs=1)--8208(line=543,offs=33)))
                                              // T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8022],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8023],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                              let jsxtnm672 = function (arg1) { // timp: forall$test0(1422)
                                                let jsxtnm641 = arg1
                                                // I1CMP:start
                                                let jsxtnm671 // let
                                                { // let
                                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8167(line=542,offs=1)--8196(line=543,offs=21)))
                                                  // I1VALDCL
                                                  let jsxtnm670
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8176(line=543,offs=1)--8188(line=543,offs=13))
                                                  // I0Etapq(I0Ecst(foritm$work0(1442)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3042(line=183,offs=1)--3054(line=183,offs=13))));$list(T2JAG($list(T2Pvar(x0[8023])))))
                                                  // T1IMPallx(foritm$work0(1442);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11766(line=809,offs=1)--11905(line=816,offs=40)))
                                                  // T1IMPallx(foritm$work0(1442)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8054],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8055],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[8056],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work0(1442);$list(@(x0[3785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                  let jsxtnm668 = function (arg1) { // timp: foritm$work0(1442)
                                                    let jsxtnm642 = arg1
                                                    // I1CMP:start
                                                    let jsxtnm667 // let
                                                    { // let
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11836(line=815,offs=1)--11865(line=815,offs=30)))
                                                      // I1VALDCL
                                                      let jsxtnm647
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11849(line=815,offs=14)--11857(line=815,offs=22))
                                                      // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Pvar(r0[8056])))))
                                                      // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                      // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                      let jsxtnm645 = function (arg1) { // timp: p2tr_get(2309)
                                                        let jsxtnm643 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm644 = XATS000_dp2tr(jsxtnm643)
                                                        // I1CMP:return:I1Vtnm(I1TNM(644))
                                                        return jsxtnm644
                                                      } // endtimp(p2tr_get(2309))
                                                      let jsxtnm646 = XATSDAPP(jsxtnm645(jsxtnm583))
                                                      jsxtnm647 = jsxtnm646
                                                      XATS000_patck(true)
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11866(line=816,offs=1)--11904(line=816,offs=39)))
                                                      // I1VALDCL
                                                      let jsxtnm662
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11875(line=816,offs=10)--11888(line=816,offs=23))
                                                      // I0Etapq(I0Ecst(folditm$fopr0(1454)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3581(line=226,offs=1)--3594(line=226,offs=14))));$list(T2JAG($list(T2Pvar(x0[8055]))),T2JAG($list(T2Pvar(r0[8056])))))
                                                      // T1IMPallx(folditm$fopr0(1454);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2012(line=81,offs=1)--2074(line=84,offs=31)))
                                                      // T1IMPallx(folditm$fopr0(1454)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7891],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7892],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(folditm$fopr0(1454);$list(@(x0[3797],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(r0[3798],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm660 = function (arg1, arg2) { // timp: folditm$fopr0(1454)
                                                        let jsxtnm648 = arg1
                                                        let jsxtnm649 = arg2
                                                        // I1CMP:start
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(2055(line=84,offs=12)--2062(line=84,offs=19))
                                                        // I0Etapq(I0Ecst(g_mul00(1586)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gnum000_vt.sats)@(2005(line=95,offs=1)--2012(line=95,offs=8))));$list(T2JAG($list(T2Pvar(x0[7892])))))
                                                        // T1IMPallx(g_mul00(1586);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats)@(1874(line=76,offs=1)--1916(line=78,offs=24)))
                                                        // T1IMPallx(g_mul00(1586)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7800],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_mul00(1586);$list(@(x0[4047],T2Pvar(x0[7800])))))))
                                                        let jsxtnm658
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gnum000_vt.dats)@(1907(line=78,offs=15)--1912(line=78,offs=20))
                                                        // I0Etapq(I0Ecst(g_mul(223)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gnum000.sats)@(2025(line=99,offs=1)--2030(line=99,offs=6))));$list(T2JAG($list(T2Pvar(x0[7800])))))
                                                        // T1IMPallx(g_mul(223);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2166(line=88,offs=1)--2202(line=89,offs=28)))
                                                        // T1IMPallx(g_mul(223)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_mul(223);$list(@(x0[791],T2Pcst(si)))))))
                                                        let jsxtnm657
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2187(line=89,offs=13)--2200(line=89,offs=26))
                                                        // I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
                                                        // T1IMPallx(sint_mul$sint(938);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
                                                        // T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
                                                        let jsxtnm656 = function (arg1, arg2) { // timp: sint_mul$sint(938)
                                                          let jsxtnm650 = arg1
                                                          let jsxtnm651 = arg2
                                                          // I1CMP:start
                                                          let jsxtnm655 // let
                                                          { // let
                                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3111(line=182,offs=1)--3175(line=184,offs=39))
                                                            // I1FUNDCL: XATS2JS_sint_mul$sint(4932)
                                                            // XATS2JS_sint_mul$sint_3114
                                                              // FJARGdarg($list(I1BNDcons(I1TNM(652);I0Pvar(i1(4933));$list(@(i1(4933),I1Vtnm(I1TNM(652))))),I1BNDcons(I1TNM(653);I0Pvar(i2(4934));$list(@(i2(4934),I1Vtnm(I1TNM(653)))))))
                                                              // I1CMP:start
                                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_mul$sint);G1Nlist($list()))// I1CMP:return
                                                            let jsxtnm654 = XATSDAPP(XATS2JS_sint_mul$sint(jsxtnm650, jsxtnm651))
                                                            jsxtnm655 = jsxtnm654
                                                          } // endlet
                                                          // I1CMP:return:I1Vtnm(I1TNM(655))
                                                          return jsxtnm655
                                                        } // endtimp(sint_mul$sint(938))
                                                        jsxtnm657 = jsxtnm656
                                                        jsxtnm658 = jsxtnm657
                                                        let jsxtnm659 = XATSDAPP(jsxtnm658(jsxtnm648, jsxtnm649))
                                                        // I1CMP:return:I1Vtnm(I1TNM(659))
                                                        return jsxtnm659
                                                      } // endtimp(folditm$fopr0(1454))
                                                      let jsxtnm661 = XATSDAPP(jsxtnm660(jsxtnm647, jsxtnm642))
                                                      jsxtnm662 = jsxtnm661
                                                      XATS000_patck(true)
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(11806(line=812,offs=7)--11814(line=812,offs=15))
                                                      // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Pvar(r0[8056])))))
                                                      // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                                      // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                                      let jsxtnm665 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                                        let jsxtnm663 = arg1
                                                        let jsxtnm664 = arg2
                                                        // I1CMP:start
                                                        XATS000_assgn(jsxtnm663, jsxtnm664)
                                                        // I1CMP:return:I1V000()
                                                        return XATSVOID
                                                      } // endtimp(p2tr_set(2310))
                                                      let jsxtnm666 = XATSDAPP(jsxtnm665(jsxtnm583, jsxtnm662))
                                                      jsxtnm667 = jsxtnm666
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(667))
                                                    return jsxtnm667
                                                  } // endtimp(foritm$work0(1442))
                                                  let jsxtnm669 = XATSDAPP(jsxtnm668(jsxtnm641))
                                                  jsxtnm670 = jsxtnm669
                                                  XATS000_patck(true)
                                                  jsxtnm671 = XATSBOOL(true)
                                                } // endlet
                                                // I1CMP:return:I1Vtnm(I1TNM(671))
                                                return jsxtnm671
                                              } // endtimp(forall$test0(1422))
                                              jsxtnm673 = jsxtnm672
                                              jsxtnm674 = jsxtnm673
                                              let jsxtnm675 = XATSDAPP(jsxtnm674(jsxtnm640))
                                              jsxtnm676 = jsxtnm675
                                              XATS000_patck(true)
                                              // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                              // I1VALDCL
                                              // I1BNDcons(I1TNM(678);I0Ptup0($list());$list())
                                              // I1CMP:start
                                              // I1LETnew1(I1TNM(677);...)
                                                // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(640))))
                                              // I1CMP(ival):I1Vtnm(I1TNM(677))// I1CMP:return
                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                              // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                              // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                              // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                              let jsxtnm681 = function (arg1) { // timp: g_free(23)
                                                let jsxtnm679 = arg1
                                                // I1CMP:start
                                                let jsxtnm680 = XATSTUP0([])
                                                // I1CMP:return:I1Vtnm(I1TNM(680))
                                                return jsxtnm680
                                              } // endtimp(g_free(23))
                                              let jsxtnm682 = XATSDAPP(jsxtnm681(jsxtnm640))
                                              jsxtnm683 = jsxtnm676
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(683))
                                            return jsxtnm683
                                          } // endtimp(forall$test(47))
                                          let jsxtnm685 = XATSDAPP(jsxtnm684(jsxtnm618))
                                          let jsxtnm695 // ift
                                          if (jsxtnm685) // ift
                                          {
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                            // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                            // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                            // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                            let jsxtnm692 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                              let jsxtnm686 = arg1
                                              let jsxtnm687 = arg2
                                              // I1CMP:start
                                              let jsxtnm691 // let
                                              { // let
                                                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                // XATS2JS_sint_add$sint_2778
                                                  // FJARGdarg($list(I1BNDcons(I1TNM(688);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(688))))),I1BNDcons(I1TNM(689);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(689)))))))
                                                  // I1CMP:start
                                                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                let jsxtnm690 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm686, jsxtnm687))
                                                jsxtnm691 = jsxtnm690
                                              } // endlet
                                              // I1CMP:return:I1Vtnm(I1TNM(691))
                                              return jsxtnm691
                                            } // endtimp(sint_add$sint(936))
                                            let jsxtnm693 = XATSDAPP(jsxtnm692(jsxtnm618, XATSINT1(1)))
                                            let jsxtnm694 = XATSDAPP(loop_2862(jsxtnm617, jsxtnm693))
                                            jsxtnm695 = jsxtnm694
                                          } else {
                                            jsxtnm695 = XATSBOOL(false)
                                          } // end(if)
                                          jsxtnm696 = jsxtnm695
                                        } // end(if)
                                        // I1CMP:return:I1Vtnm(I1TNM(696))
                                        return jsxtnm696
                                      } // endfun(loop_2862)
                                      let jsxtnm697 = XATSDAPP(loop_2862(jsxtnm616, XATSINT1(0)))
                                      jsxtnm698 = jsxtnm697
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(698))
                                    return jsxtnm698
                                  } // endtimp(nint_forall(958))
                                  let jsxtnm700 = XATSDAPP(jsxtnm699(jsxtnm606))
                                  jsxtnm701 = jsxtnm700
                                } // endlet
                                jsxtnm702 = jsxtnm701
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(702))
                              return jsxtnm702
                            } // endtimp(gasq_forall(609))
                            jsxtnm704 = jsxtnm703
                            let jsxtnm705 = XATSDAPP(jsxtnm704(jsxtnm597))
                            jsxtnm706 = jsxtnm705
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(706))
                          return jsxtnm706
                        } // endtimp(gseq_forall(386))
                        let jsxtnm708 = XATSDAPP(jsxtnm707(jsxtnm596))
                        jsxtnm709 = jsxtnm708
                      } // endlet
                      // I1CMP:return:I1Vtnm(I1TNM(709))
                      return jsxtnm709
                    } // endtimp(gseq_forall0(1719))
                    let jsxtnm711 = XATSDAPP(jsxtnm710(jsxtnm591))
                    jsxtnm712 = jsxtnm711
                    XATS000_patck(true)
                    jsxtnm713 = XATSVOID
                  } // endlet
                  jsxtnm714 = jsxtnm713
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(714))
                return jsxtnm714
              } // endtimp(gseq_foritm0(1751))
              let jsxtnm716 = XATSDAPP(jsxtnm715(jsxtnm580))
              jsxtnm717 = jsxtnm716
            } // endlet
            jsxtnm718 = jsxtnm717
            XATS000_patck(true)
            let jsxtnm719 = XATSFLAT(jsxtnm582)
            jsxtnm720 = jsxtnm719
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(720))
          return jsxtnm720
        } // endtimp(gseq_folditm0(1767))
        let jsxtnm722 = XATSDAPP(jsxtnm721(jsxtnm573, jsxtnm576))
        jsxtnm723 = jsxtnm722
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(723))
      return jsxtnm723
    } // endtimp(gseq_prod0(1667))
    jsxtnm725 = jsxtnm724
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2258(line=108,offs=10)--2267(line=108,offs=19))
    // I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6659]))),T2JAG($list(T2Pvar(x0[6660])))))
    // T1IMPallx(GSEQ_unmk(245);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
    // T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
    let jsxtnm728 = function (arg1) { // timp: GSEQ_unmk(245)
      let jsxtnm726 = arg1
      // I1CMP:start
      let jsxtnm727 = XATSCAST("castxy_1839", [jsxtnm726])
      // I1CMP:return:I1Vtnm(I1TNM(727))
      return jsxtnm727
    } // endtimp(GSEQ_unmk(245))
    let jsxtnm729 = XATSDAPP(jsxtnm728(jsxtnm572))
    let jsxtnm730 = XATSDAPP(jsxtnm725(jsxtnm729))
    // I1CMP:return:I1Vtnm(I1TNM(730))
    return jsxtnm730
  } // endtimp(GSEQ_prod(249))
  // LCSRCsome1(test03_a1sz000.dats)@(594(line=43,offs=1)--599(line=43,offs=6))
  // I0Etapq(I0Ecst(a1sz_make_nfun(1121)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(2396(line=109,offs=1)--2410(line=109,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  // T1IMPallx(a1sz_make_nfun(1121);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2703(line=144,offs=1)--2879(line=157,offs=2)))
  // T1IMPallx(a1sz_make_nfun(1121)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8887],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_make_nfun(1121);$list(@(a[3030],T2Pvar(a[8887])))))))
  let jsxtnm738 = function (arg1, arg2) { // timp: a1sz_make_nfun(1121)
    let jsxtnm732 = arg1
    let jsxtnm733 = arg2
    // I1CMP:start
    let jsxtnm737 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2791(line=152,offs=1)--2877(line=156,offs=45)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2799(line=153,offs=1)--2877(line=156,offs=45))
      // I1FUNDCL: XATS2JS_a1sz_make_nfun(5198)
      // XATS2JS_a1sz_make_nfun_2802
        // FJARGdarg($list(I1BNDcons(I1TNM(734);I0Pvar(n(5199));$list(@(n(5199),I1Vtnm(I1TNM(734))))),I1BNDcons(I1TNM(735);I0Pvar(f(5200));$list(@(f(5200),I1Vtnm(I1TNM(735)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_make_nfun);G1Nlist($list()))// I1CMP:return
      let jsxtnm736 = XATSDAPP(XATS2JS_a1sz_make_nfun(jsxtnm732, jsxtnm733))
      jsxtnm737 = jsxtnm736
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(737))
    return jsxtnm737
  } // endtimp(a1sz_make_nfun(1121))
  let jsxtnm748 = function (arg1) { // lam0(T_LAM(0))
    let jsxtnm739 = arg1
    // I1CMP:start
    // LCSRCsome1(test03_a1sz000.dats)@(620(line=44,offs=21)--621(line=44,offs=22))
    // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
    // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
    // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
    let jsxtnm746 = function (arg1, arg2) { // timp: sint_add$sint(936)
      let jsxtnm740 = arg1
      let jsxtnm741 = arg2
      // I1CMP:start
      let jsxtnm745 // let
      { // let
        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
        // I1FUNDCL: XATS2JS_sint_add$sint(4922)
        // XATS2JS_sint_add$sint_2778
          // FJARGdarg($list(I1BNDcons(I1TNM(742);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(742))))),I1BNDcons(I1TNM(743);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(743)))))))
          // I1CMP:start
          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
        let jsxtnm744 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm740, jsxtnm741))
        jsxtnm745 = jsxtnm744
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(745))
      return jsxtnm745
    } // endtimp(sint_add$sint(936))
    let jsxtnm747 = XATSDAPP(jsxtnm746(jsxtnm739, XATSINT1(1)))
    // I1CMP:return:I1Vtnm(I1TNM(747))
    return jsxtnm747
  } // endfun(lam0)
  let jsxtnm749 = XATSDAPP(jsxtnm738(jsxtnm571, jsxtnm748))
  let jsxtnm750 = XATSCAST("GSEQ_make_a1sz_4560", [jsxtnm749])
  let jsxtnm751 = XATSDAPP(jsxtnm731(jsxtnm750))
  // I1CMP:return:I1Vtnm(I1TNM(751))
  return jsxtnm751
} // endfun(fact_570)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(635(line=46,offs=1)--677(line=47,offs=34)))
// I1VALDCL
let jsxtnm793
// LCSRCsome1(test03_a1sz000.dats)@(644(line=47,offs=1)--652(line=47,offs=9))
// I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(gs_println_a2(820);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
// T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
let jsxtnm790 = function (arg1, arg2) { // timp: gs_println_a2(820)
  let jsxtnm752 = arg1
  let jsxtnm753 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  // I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  // T1IMPallx(gs_print_a2(807);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  // T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  let jsxtnm781 = function (arg1, arg2) { // timp: gs_print_a2(807)
    let jsxtnm754 = arg1
    let jsxtnm755 = arg2
    // I1CMP:start
    let jsxtnm780 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
      // I1VALDCL
      let jsxtnm759
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
      // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      let jsxtnm757 = function () { // timp: gs_print$beg(802)
        // I1CMP:start
        let jsxtnm756 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(756))
        return jsxtnm756
      } // endtimp(gs_print$beg(802))
      let jsxtnm758 = XATSDAPP(jsxtnm757())
      jsxtnm759 = jsxtnm758
      XATS000_patck(true)
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm765
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm764 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm760 = arg1
        // I1CMP:start
        let jsxtnm763 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(761);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(761)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm762 = XATSDAPP(XATS2JS_strn_print(jsxtnm760))
          jsxtnm763 = jsxtnm762
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(763))
        return jsxtnm763
      } // endtimp(strn_print(1040))
      jsxtnm765 = jsxtnm764
      let jsxtnm766 = XATSDAPP(jsxtnm765(jsxtnm754))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm768 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm767 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(767))
        return jsxtnm767
      } // endtimp(gs_print$sep(803))
      let jsxtnm769 = XATSDAPP(jsxtnm768())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
      let jsxtnm775
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
      // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
      // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
      let jsxtnm774 = function (arg1) { // timp: sint_print(922)
        let jsxtnm770 = arg1
        // I1CMP:start
        let jsxtnm773 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
          // I1FUNDCL: XATS2JS_sint_print(4946)
          // XATS2JS_sint_print_3707
            // FJARGdarg($list(I1BNDcons(I1TNM(771);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(771)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm772 = XATSDAPP(XATS2JS_sint_print(jsxtnm770))
          jsxtnm773 = jsxtnm772
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(773))
        return jsxtnm773
      } // endtimp(sint_print(922))
      jsxtnm775 = jsxtnm774
      let jsxtnm776 = XATSDAPP(jsxtnm775(jsxtnm755))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
      // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      let jsxtnm778 = function () { // timp: gs_print$end(804)
        // I1CMP:start
        let jsxtnm777 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(777))
        return jsxtnm777
      } // endtimp(gs_print$end(804))
      let jsxtnm779 = XATSDAPP(jsxtnm778())
      jsxtnm780 = jsxtnm779
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(780))
    return jsxtnm780
  } // endtimp(gs_print_a2(807))
  let jsxtnm782 = XATSDAPP(jsxtnm781(jsxtnm752, jsxtnm753))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm788
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm787 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm783 = arg1
    // I1CMP:start
    let jsxtnm786 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(784);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(784)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm785 = XATSDAPP(XATS2JS_strn_print(jsxtnm783))
      jsxtnm786 = jsxtnm785
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(786))
    return jsxtnm786
  } // endtimp(strn_print(1040))
  jsxtnm788 = jsxtnm787
  let jsxtnm789 = XATSDAPP(jsxtnm788(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(789))
  return jsxtnm789
} // endtimp(gs_println_a2(820))
let jsxtnm791 = XATSDAPP(fact_570(XATSINT1(10)))
let jsxtnm792 = XATSDAPP(jsxtnm790(XATSSTRN("fact(10) = "), jsxtnm791))
jsxtnm793 = jsxtnm792
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(724(line=52,offs=1)--762(line=54,offs=25)))
// I1VALDCL
let jsxtnm911
// LCSRCsome1(test03_a1sz000.dats)@(733(line=53,offs=1)--737(line=53,offs=5))
// I0Etapq(I0Ecst(list_make_nfun(1185)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list000.sats)@(3040(line=167,offs=1)--3054(line=167,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(list_make_nfun(1185);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(8859(line=616,offs=1)--8996(line=624,offs=28)))
// T1IMPallx(list_make_nfun(1185)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7459],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_make_nfun(1185);$list(@(a[3348],T2Pvar(x0[7459])))))))
let jsxtnm899 = function (arg1, arg2) { // timp: list_make_nfun(1185)
  let jsxtnm794 = arg1
  let jsxtnm795 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(8906(line=620,offs=1)--8921(line=620,offs=16))
  // I0Etapq(I0Ecst(list_make_fwork(1257)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(7777(line=362,offs=1)--7792(line=362,offs=16))));$list(T2JAG($list(T2Pvar(x0[7459])))))
  // T1IMPallx(list_make_fwork(1257);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9695(line=651,offs=1)--9956(line=675,offs=4)))
  // T1IMPallx(list_make_fwork(1257)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7532],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_make_fwork(1257);$list(@(x0[3465],T2Pvar(x0[7532])))))))
  let jsxtnm837 = function (arg1) { // timp: list_make_fwork(1257)
    let jsxtnm796 = arg1
    // I1CMP:start
    let jsxtnm836 // let
    { // let
      // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9746(line=656,offs=1)--9787(line=659,offs=18)))
      // I1VARDCL
      // I1CMP:start
      let jsxtnm797 = XATSCAPP("list_vt_nil", [0])
      // I1CMP:return:I1Vtnm(I1TNM(797))
      let jsxtnm798 = XATSVAR1(jsxtnm797)
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9788(line=660,offs=1)--9806(line=660,offs=19)))
      // I1VALDCL
      let jsxtnm799
      jsxtnm799 = XATSADDR(jsxtnm798)
      XATS000_patck(true)
      let jsxtnm835 // let
      { // let
        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9868(line=668,offs=1)--9950(line=673,offs=42)))
        // I1VALDCL
        let jsxtnm812
        let jsxtnm810 = function (arg1) { // lam0(T_LAM(0))
          let jsxtnm800 = arg1
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9900(line=672,offs=5)--9908(line=672,offs=13))
          // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[7532]),T2Pnone0()))))))
          // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
          // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
          let jsxtnm803 = function (arg1, arg2) { // timp: p2tr_set(2310)
            let jsxtnm801 = arg1
            let jsxtnm802 = arg2
            // I1CMP:start
            XATS000_assgn(jsxtnm801, jsxtnm802)
            // I1CMP:return:I1V000()
            return XATSVOID
          } // endtimp(p2tr_set(2310))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9934(line=673,offs=26)--9942(line=673,offs=34))
          // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[7532]),T2Pnone0()))))))
          // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
          // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
          let jsxtnm806 = function (arg1) { // timp: p2tr_get(2309)
            let jsxtnm804 = arg1
            // I1CMP:start
            let jsxtnm805 = XATS000_dp2tr(jsxtnm804)
            // I1CMP:return:I1Vtnm(I1TNM(805))
            return jsxtnm805
          } // endtimp(p2tr_get(2309))
          let jsxtnm807 = XATSDAPP(jsxtnm806(jsxtnm799))
          let jsxtnm808 = XATSCAPP("list_vt_cons", [1, jsxtnm800, jsxtnm807])
          let jsxtnm809 = XATSDAPP(jsxtnm803(jsxtnm799, jsxtnm808))
          // I1CMP:return:I1Vtnm(I1TNM(809))
          return jsxtnm809
        } // endfun(lam0)
        let jsxtnm811 = XATSDAPP(jsxtnm796(jsxtnm810))
        jsxtnm812 = jsxtnm811
        XATS000_patck(true)
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(9833(line=665,offs=1)--9849(line=665,offs=17))
        // I0Etapq(I0Ecst(list_vt_reverse0(2046)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4474(line=255,offs=1)--4490(line=255,offs=17))));$list(T2JAG($list(T2Pvar(x0[7532])))))
        // T1IMPallx(list_vt_reverse0(2046);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7033(line=475,offs=1)--7120(line=478,offs=46)))
        // T1IMPallx(list_vt_reverse0(2046)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8528],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_reverse0(2046);$list(@(x0[5264],T2Pvar(a[8528])))))))
        let jsxtnm831 = function (arg1) { // timp: list_vt_reverse0(2046)
          let jsxtnm813 = arg1
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7075(line=478,offs=1)--7092(line=478,offs=18))
          // I0Etapq(I0Ecst(list_vt_rappend00(2049)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4855(line=281,offs=1)--4872(line=281,offs=18))));$list(T2JAG($list(T2Pvar(a[8528])))))
          // T1IMPallx(list_vt_rappend00(2049);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6363(line=426,offs=1)--6772(line=458,offs=2)))
          // T1IMPallx(list_vt_rappend00(2049)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8524],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_rappend00(2049);$list(@(x0[5271],T2Pvar(a[8524])))))))
          let jsxtnm828 = function (arg1, arg2) { // timp: list_vt_rappend00(2049)
            let jsxtnm814 = arg1
            let jsxtnm815 = arg2
            // I1CMP:start
            let jsxtnm827 // let
            { // let
              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6442(line=434,offs=1)--6733(line=456,offs=2)))
              // I1FUNDCL
              function loop_6445(arg1, arg2)
              { // fun
                let jsxtnm816 = arg1
                let jsxtnm817 = arg2
                // I1CMP:start
                let jsxtnm825 // cas
                do {
                  // { // cls
                  // I1GPTpat(I1BNDcons(I1TNM(818);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
                  if (XATS000_ctgeq(jsxtnm816, XATSCTAG("list_vt_nil",0))) { // gpt
                    let jsxtnm818 = jsxtnm816
                    jsxtnm825 = jsxtnm817
                    break // cls
                  } // gpt
                  // } // cls
                  // { // cls
                  // I1GPTpat(I1BNDcons(I1TNM(819);I0Pflat(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pany())));$list()))
                  if (XATS000_ctgeq(jsxtnm816, XATSCTAG("list_vt_cons",1))) { // gpt
                    let jsxtnm819 = jsxtnm816
                    let jsxtnm824 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6616(line=450,offs=3)--6631(line=450,offs=18)))
                      // I1VALDCL
                      let jsxtnm821
                      let jsxtnm820 = XATSPCON(jsxtnm816,1)
                      jsxtnm821 = jsxtnm820
                      XATS000_patck(true)
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6634(line=451,offs=3)--6656(line=451,offs=25)))
                      // I1VALDCL
                      let jsxtnm822
                      XATS000_assgn(XATSLPCN(1, jsxtnm816), jsxtnm817)
                      jsxtnm822 = XATSVOID
                      XATS000_patck(true)
                      XATS000_fold(jsxtnm816)
                      let jsxtnm823 = XATSDAPP(loop_6445(jsxtnm821, jsxtnm816))
                      jsxtnm824 = jsxtnm823
                    } // endlet
                    jsxtnm825 = jsxtnm824
                    break // cls
                  } // gpt
                  // } // cls
                  XATS000_cfail()
                } while (false) // end-of(do)
                // I1CMP:return:I1Vtnm(I1TNM(825))
                return jsxtnm825
              } // endfun(loop_6445)
              let jsxtnm826 = XATSDAPP(loop_6445(jsxtnm814, jsxtnm815))
              jsxtnm827 = jsxtnm826
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(827))
            return jsxtnm827
          } // endtimp(list_vt_rappend00(2049))
          let jsxtnm829 = XATSCAPP("list_vt_nil", [0])
          let jsxtnm830 = XATSDAPP(jsxtnm828(jsxtnm813, jsxtnm829))
          // I1CMP:return:I1Vtnm(I1TNM(830))
          return jsxtnm830
        } // endtimp(list_vt_reverse0(2046))
        let jsxtnm832 = XATSFLAT(jsxtnm798)
        let jsxtnm833 = XATSDAPP(jsxtnm831(jsxtnm832))
        let jsxtnm834 = XATSCAST("list_vt2t_17913", [jsxtnm833])
        jsxtnm835 = jsxtnm834
      } // endlet
      jsxtnm836 = jsxtnm835
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(836))
    return jsxtnm836
  } // endtimp(list_make_fwork(1257))
  let jsxtnm897 = function (arg1) { // lam0(T_LAM(0))
    let jsxtnm838 = arg1
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(8939(line=623,offs=1)--8945(line=623,offs=7))
    // I0Etapq(I0Ecst(nint_foritm$f1un(964)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3054(line=146,offs=1)--3070(line=146,offs=17))));$list(T2JAG($list())))
    // T1IMPallx(nint_foritm$f1un(964);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4008(line=237,offs=1)--4137(line=246,offs=2)))
    // T1IMPallx(nint_foritm$f1un(964)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_foritm$f1un(964);$list()))))
    let jsxtnm891 = function (arg1, arg2) { // timp: nint_foritm$f1un(964)
      let jsxtnm839 = arg1
      let jsxtnm840 = arg2
      // I1CMP:start
      let jsxtnm890 // let
      { // let
        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4090(line=244,offs=1)--4135(line=245,offs=37)))
        // I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(ni))))):timp
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4063(line=242,offs=3)--4074(line=242,offs=14))
        // I0Etapq(I0Ecst(nint_foritm(962)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(2701(line=122,offs=1)--2712(line=122,offs=12))));$list(T2JAG($list())))
        // T1IMPallx(nint_foritm(962);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3945(line=233,offs=1)--3999(line=236,offs=22)))
        // T1IMPallx(nint_foritm(962)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_foritm(962);$list()))))
        let jsxtnm888
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3978(line=236,offs=1)--3989(line=236,offs=12))
        // I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
        // T1IMPallx(gseq_foritm(402);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
        // T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
        let jsxtnm887 = function (arg1) { // timp: gseq_foritm(402)
          let jsxtnm843 = arg1
          // I1CMP:start
          let jsxtnm886 // let
          { // let
            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
            // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
            let jsxtnm885 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
              // I1VALDCL
              let jsxtnm884
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
              // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
              // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3103(line=172,offs=1)--3149(line=173,offs=38)))
              // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Pcst(nint)),@(x0[1168],T2Pcst(ni)))))))
              let jsxtnm882
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(3136(line=173,offs=25)--3147(line=173,offs=36))
              // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
              // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
              // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
              let jsxtnm881 = function (arg1) { // timp: nint_forall(958)
                let jsxtnm848 = arg1
                // I1CMP:start
                let jsxtnm880 // let
                { // let
                  // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                  // I1FUNDCL
                  function loop_2862(arg1, arg2)
                  { // fun
                    let jsxtnm849 = arg1
                    let jsxtnm850 = arg2
                    // I1CMP:start
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                    // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                    // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                    // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                    let jsxtnm857 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                      let jsxtnm851 = arg1
                      let jsxtnm852 = arg2
                      // I1CMP:start
                      let jsxtnm856 // let
                      { // let
                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                        // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                        // XATS2JS_sint_gte$sint_2399
                          // FJARGdarg($list(I1BNDcons(I1TNM(853);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(853))))),I1BNDcons(I1TNM(854);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(854)))))))
                          // I1CMP:start
                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                        let jsxtnm855 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm851, jsxtnm852))
                        jsxtnm856 = jsxtnm855
                      } // endlet
                      // I1CMP:return:I1Vtnm(I1TNM(856))
                      return jsxtnm856
                    } // endtimp(sint_gte$sint(931))
                    let jsxtnm858 = XATSDAPP(jsxtnm857(jsxtnm850, jsxtnm849))
                    let jsxtnm878 // ift
                    if (jsxtnm858) // ift
                    {
                      jsxtnm878 = XATSBOOL(true)
                    } else {
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                      // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                      // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[6119],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      let jsxtnm866 = function (arg1) { // timp: forall$test(47)
                        let jsxtnm859 = arg1
                        // I1CMP:start
                        let jsxtnm865 // let
                        { // let
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                          // I1VALDCL
                          let jsxtnm864
                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                          // I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                          // T1IMPallx(foritm$work(51);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(4090(line=244,offs=1)--4135(line=245,offs=37)))
                          // T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pcst(ni)))))))
                          let jsxtnm862 = function (arg1) { // timp: foritm$work(51)
                            let jsxtnm860 = arg1
                            // I1CMP:start
                            let jsxtnm861 = XATSDAPP(jsxtnm840(jsxtnm860))
                            // I1CMP:return:I1Vtnm(I1TNM(861))
                            return jsxtnm861
                          } // endtimp(foritm$work(51))
                          let jsxtnm863 = XATSDAPP(jsxtnm862(jsxtnm859))
                          jsxtnm864 = jsxtnm863
                          XATS000_patck(true)
                          jsxtnm865 = XATSBOOL(true)
                        } // endlet
                        // I1CMP:return:I1Vtnm(I1TNM(865))
                        return jsxtnm865
                      } // endtimp(forall$test(47))
                      let jsxtnm867 = XATSDAPP(jsxtnm866(jsxtnm850))
                      let jsxtnm877 // ift
                      if (jsxtnm867) // ift
                      {
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                        // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                        // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                        // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                        let jsxtnm874 = function (arg1, arg2) { // timp: sint_add$sint(936)
                          let jsxtnm868 = arg1
                          let jsxtnm869 = arg2
                          // I1CMP:start
                          let jsxtnm873 // let
                          { // let
                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                            // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                            // XATS2JS_sint_add$sint_2778
                              // FJARGdarg($list(I1BNDcons(I1TNM(870);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(870))))),I1BNDcons(I1TNM(871);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(871)))))))
                              // I1CMP:start
                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                            let jsxtnm872 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm868, jsxtnm869))
                            jsxtnm873 = jsxtnm872
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(873))
                          return jsxtnm873
                        } // endtimp(sint_add$sint(936))
                        let jsxtnm875 = XATSDAPP(jsxtnm874(jsxtnm850, XATSINT1(1)))
                        let jsxtnm876 = XATSDAPP(loop_2862(jsxtnm849, jsxtnm875))
                        jsxtnm877 = jsxtnm876
                      } else {
                        jsxtnm877 = XATSBOOL(false)
                      } // end(if)
                      jsxtnm878 = jsxtnm877
                    } // end(if)
                    // I1CMP:return:I1Vtnm(I1TNM(878))
                    return jsxtnm878
                  } // endfun(loop_2862)
                  let jsxtnm879 = XATSDAPP(loop_2862(jsxtnm848, XATSINT1(0)))
                  jsxtnm880 = jsxtnm879
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(880))
                return jsxtnm880
              } // endtimp(nint_forall(958))
              jsxtnm882 = jsxtnm881
              let jsxtnm883 = XATSDAPP(jsxtnm882(jsxtnm843))
              jsxtnm884 = jsxtnm883
              XATS000_patck(true)
              jsxtnm885 = XATSVOID
            } // endlet
            jsxtnm886 = jsxtnm885
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(886))
          return jsxtnm886
        } // endtimp(gseq_foritm(402))
        jsxtnm888 = jsxtnm887
        let jsxtnm889 = XATSDAPP(jsxtnm888(jsxtnm839))
        jsxtnm890 = jsxtnm889
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(890))
      return jsxtnm890
    } // endtimp(nint_foritm$f1un(964))
    let jsxtnm895 = function (arg1) { // lam0(T_LAM(0))
      let jsxtnm892 = arg1
      // I1CMP:start
      let jsxtnm893 = XATSDAPP(jsxtnm795(jsxtnm892))
      let jsxtnm894 = XATSDAPP(jsxtnm838(jsxtnm893))
      // I1CMP:return:I1Vtnm(I1TNM(894))
      return jsxtnm894
    } // endfun(lam0)
    let jsxtnm896 = XATSDAPP(jsxtnm891(jsxtnm794, jsxtnm895))
    // I1CMP:return:I1Vtnm(I1TNM(896))
    return jsxtnm896
  } // endfun(lam0)
  let jsxtnm898 = XATSDAPP(jsxtnm837(jsxtnm897))
  // I1CMP:return:I1Vtnm(I1TNM(898))
  return jsxtnm898
} // endtimp(list_make_nfun(1185))
let jsxtnm909 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm900 = arg1
  // I1CMP:start
  // LCSRCsome1(test03_a1sz000.dats)@(759(line=54,offs=22)--760(line=54,offs=23))
  // I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
  // T1IMPallx(sint_mul$sint(938);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
  // T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
  let jsxtnm907 = function (arg1, arg2) { // timp: sint_mul$sint(938)
    let jsxtnm901 = arg1
    let jsxtnm902 = arg2
    // I1CMP:start
    let jsxtnm906 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3111(line=182,offs=1)--3175(line=184,offs=39))
      // I1FUNDCL: XATS2JS_sint_mul$sint(4932)
      // XATS2JS_sint_mul$sint_3114
        // FJARGdarg($list(I1BNDcons(I1TNM(903);I0Pvar(i1(4933));$list(@(i1(4933),I1Vtnm(I1TNM(903))))),I1BNDcons(I1TNM(904);I0Pvar(i2(4934));$list(@(i2(4934),I1Vtnm(I1TNM(904)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_mul$sint);G1Nlist($list()))// I1CMP:return
      let jsxtnm905 = XATSDAPP(XATS2JS_sint_mul$sint(jsxtnm901, jsxtnm902))
      jsxtnm906 = jsxtnm905
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(906))
    return jsxtnm906
  } // endtimp(sint_mul$sint(938))
  let jsxtnm908 = XATSDAPP(jsxtnm907(jsxtnm900, jsxtnm900))
  // I1CMP:return:I1Vtnm(I1TNM(908))
  return jsxtnm908
} // endfun(lam0)
let jsxtnm910 = XATSDAPP(jsxtnm899(XATSINT1(10), jsxtnm909))
jsxtnm911 = jsxtnm910
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(763(line=55,offs=1)--790(line=55,offs=28)))
// I1VALDCL
let jsxtnm948
// LCSRCsome1(test03_a1sz000.dats)@(772(line=55,offs=10)--786(line=55,offs=24))
// I0Etapq(I0Ecst(a1sz_make_list(1119)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(2190(line=92,offs=1)--2204(line=92,offs=15))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(a1sz_make_list(1119);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2822(line=138,offs=1)--2935(line=145,offs=35)))
// T1IMPallx(a1sz_make_list(1119)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[7303],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_make_list(1119);$list(@(a[3026],T2Pvar(a[7303])))))))
let jsxtnm946 = function (arg1) { // timp: a1sz_make_list(1119)
  let jsxtnm912 = arg1
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2867(line=142,offs=1)--2882(line=142,offs=16))
  // I0Etapq(I0Ecst(a1sz_make_fwork(1156)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz001.sats)@(3701(line=176,offs=1)--3716(line=176,offs=16))));$list(T2JAG($list(T2Pvar(a[7303])))))
  // T1IMPallx(a1sz_make_fwork(1156);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(2982(line=167,offs=1)--3177(line=182,offs=2)))
  // T1IMPallx(a1sz_make_fwork(1156)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8889],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_make_fwork(1156);$list(@(x0[3080],T2Pvar(x0[8889])))))))
  let jsxtnm917 = function (arg1) { // timp: a1sz_make_fwork(1156)
    let jsxtnm913 = arg1
    // I1CMP:start
    let jsxtnm916 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(3074(line=175,offs=1)--3175(line=181,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(3082(line=176,offs=1)--3175(line=181,offs=47))
      // I1FUNDCL: XATS2JS_a1sz_make_fwork(5202)
      // XATS2JS_a1sz_make_fwork_3085
        // FJARGdarg($list(I1BNDcons(I1TNM(914);I0Pvar(fwork(5203));$list(@(fwork(5203),I1Vtnm(I1TNM(914)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_make_fwork);G1Nlist($list()))// I1CMP:return
      let jsxtnm915 = XATSDAPP(XATS2JS_a1sz_make_fwork(jsxtnm913))
      jsxtnm916 = jsxtnm915
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(916))
    return jsxtnm916
  } // endtimp(a1sz_make_fwork(1156))
  let jsxtnm944 = function (arg1) { // lam0(T_LAM(0))
    let jsxtnm918 = arg1
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2901(line=145,offs=1)--2912(line=145,offs=12))
    // I0Etapq(I0Ecst(gseq_foritm$f1un(406)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7707(line=443,offs=1)--7723(line=443,offs=17))));$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Pvar(a[7303]),T2Pnone0())))),T2JAG($list(T2Pvar(a[7303])))))
    // T1IMPallx(gseq_foritm$f1un(406);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6627(line=426,offs=1)--6765(line=435,offs=2)))
    // T1IMPallx(gseq_foritm$f1un(406)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6120],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6121],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm$f1un(406);$list(@(xs[1231],T2Pvar(xs[6120])),@(x0[1232],T2Pvar(x0[6121])))))))
    let jsxtnm942 = function (arg1, arg2) { // timp: gseq_foritm$f1un(406)
      let jsxtnm919 = arg1
      let jsxtnm920 = arg2
      // I1CMP:start
      let jsxtnm941 // let
      { // let
        // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6724(line=434,offs=1)--6763(line=434,offs=40)))
        // I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pvar(x0[6121]))))):timp
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6690(line=432,offs=1)--6701(line=432,offs=12))
        // I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Pvar(xs[6120]))),T2JAG($list(T2Pvar(x0[6121])))))
        // T1IMPallx(gseq_foritm(402);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(4997(line=316,offs=1)--5060(line=319,offs=33)))
        // T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7506],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7506],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7506])))),@(x0[1216],T2Pvar(x0[7506])))))))
        let jsxtnm939
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(5045(line=319,offs=18)--5056(line=319,offs=29))
        // I0Etapq(I0Ecst(list_foritm(1234)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(3916(line=174,offs=1)--3927(line=174,offs=12))));$list(T2JAG($list(T2Pvar(x0[7506])))))
        // T1IMPallx(list_foritm(1234);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(4774(line=295,offs=1)--4993(line=314,offs=2)))
        // T1IMPallx(list_foritm(1234)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7505],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_foritm(1234);$list(@(x0[3434],T2Pvar(x0[7505])))))))
        let jsxtnm938 = function (arg1) { // timp: list_foritm(1234)
          let jsxtnm923 = arg1
          // I1CMP:start
          let jsxtnm937 // let
          { // let
            // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(4840(line=302,offs=1)--4991(line=313,offs=37)))
            // I1FUNDCL
            function loop_4843(arg1)
            { // fun
              let jsxtnm924 = arg1
              // I1CMP:start
              let jsxtnm935 // cas
              do {
                // { // cls
                // I1GPTpat(I1BNDcons(I1TNM(925);I0Pfree(I0Pdapp(I0Pcon(list_nil(8));$list()));$list()))
                if (XATS000_ctgeq(jsxtnm924, XATSCTAG("list_nil",0))) { // gpt
                  let jsxtnm925 = jsxtnm924
                  let jsxtnm926 = XATSTUP0([])
                  jsxtnm935 = jsxtnm926
                  break // cls
                } // gpt
                // } // cls
                // { // cls
                // I1GPTpat(I1BNDcons(I1TNM(927);I0Pfree(I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2595)),I0Pvar(xs(2596)))));$list(@(x1(2595),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(927));0)),@(xs(2596),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(927));1)))))
                if (XATS000_ctgeq(jsxtnm924, XATSCTAG("list_cons",1))) { // gpt
                  let jsxtnm927 = jsxtnm924
                  let jsxtnm934 // let
                  { // let
                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(4946(line=312,offs=1)--4974(line=313,offs=20)))
                    // I1VALDCL
                    let jsxtnm932
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(4955(line=313,offs=1)--4966(line=313,offs=12))
                    // I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[7505])))))
                    // T1IMPallx(foritm$work(51);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6724(line=434,offs=1)--6763(line=434,offs=40)))
                    // T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6120],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6121],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    let jsxtnm930 = function (arg1) { // timp: foritm$work(51)
                      let jsxtnm928 = arg1
                      // I1CMP:start
                      let jsxtnm929 = XATSDAPP(jsxtnm920(jsxtnm928))
                      // I1CMP:return:I1Vtnm(I1TNM(929))
                      return jsxtnm929
                    } // endtimp(foritm$work(51))
                    let jsxtnm931 = XATSDAPP(jsxtnm930(XATSP1CN("list_cons", jsxtnm927[0+1])))
                    jsxtnm932 = jsxtnm931
                    XATS000_patck(true)
                    let jsxtnm933 = XATSDAPP(loop_4843(XATSP1CN("list_cons", jsxtnm927[1+1])))
                    jsxtnm934 = jsxtnm933
                  } // endlet
                  jsxtnm935 = jsxtnm934
                  break // cls
                } // gpt
                // } // cls
                XATS000_cfail()
              } while (false) // end-of(do)
              // I1CMP:return:I1Vtnm(I1TNM(935))
              return jsxtnm935
            } // endfun(loop_4843)
            let jsxtnm936 = XATSDAPP(loop_4843(jsxtnm923))
            jsxtnm937 = jsxtnm936
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(937))
          return jsxtnm937
        } // endtimp(list_foritm(1234))
        jsxtnm939 = jsxtnm938
        let jsxtnm940 = XATSDAPP(jsxtnm939(jsxtnm919))
        jsxtnm941 = jsxtnm940
      } // endlet
      // I1CMP:return:I1Vtnm(I1TNM(941))
      return jsxtnm941
    } // endtimp(gseq_foritm$f1un(406))
    let jsxtnm943 = XATSDAPP(jsxtnm942(jsxtnm912, jsxtnm918))
    // I1CMP:return:I1Vtnm(I1TNM(943))
    return jsxtnm943
  } // endfun(lam0)
  let jsxtnm945 = XATSDAPP(jsxtnm917(jsxtnm944))
  // I1CMP:return:I1Vtnm(I1TNM(945))
  return jsxtnm945
} // endtimp(a1sz_make_list(1119))
let jsxtnm947 = XATSDAPP(jsxtnm946(jsxtnm911))
jsxtnm948 = jsxtnm947
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(791(line=56,offs=1)--837(line=57,offs=38)))
// I1VALDCL
let jsxtnm1249
// LCSRCsome1(test03_a1sz000.dats)@(800(line=57,offs=1)--808(line=57,offs=9))
// I0Etapq(I0Ecst(gs_println_a4(822)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13918(line=908,offs=1)--13931(line=908,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))))
// T1IMPallx(gs_println_a4(822);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26458(line=1604,offs=1)--26602(line=1613,offs=59)))
// T1IMPallx(gs_println_a4(822)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7101],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7102],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7103],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7104],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a4(822);$list(@(x0[2570],T2Pvar(x0[7101])),@(x1[2571],T2Pvar(x1[7102])),@(x2[2572],T2Pvar(x2[7103])),@(x3[2573],T2Pvar(x3[7104])))))))
let jsxtnm1242 = function (arg1, arg2, arg3, arg4) { // timp: gs_println_a4(822)
  let jsxtnm949 = arg1
  let jsxtnm950 = arg2
  let jsxtnm951 = arg3
  let jsxtnm952 = arg4
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26546(line=1613,offs=3)--26557(line=1613,offs=14))
  // I0Etapq(I0Ecst(gs_print_a4(809)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11925(line=761,offs=1)--11936(line=761,offs=12))));$list(T2JAG($list(T2Pvar(x0[7101]))),T2JAG($list(T2Pvar(x1[7102]))),T2JAG($list(T2Pvar(x2[7103]))),T2JAG($list(T2Pvar(x3[7104])))))
  // T1IMPallx(gs_print_a4(809);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21590(line=1332,offs=1)--21850(line=1348,offs=4)))
  // T1IMPallx(gs_print_a4(809)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7023],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7024],T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))))),@(x2[7025],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x3[7026],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a4(809);$list(@(x0[2492],T2Pvar(x0[7023])),@(x1[2493],T2Pvar(x1[7024])),@(x2[2494],T2Pvar(x2[7025])),@(x3[2495],T2Pvar(x3[7026])))))))
  let jsxtnm1233 = function (arg1, arg2, arg3, arg4) { // timp: gs_print_a4(809)
    let jsxtnm953 = arg1
    let jsxtnm954 = arg2
    let jsxtnm955 = arg3
    let jsxtnm956 = arg4
    // I1CMP:start
    let jsxtnm1232 // let
    { // let
      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21676(line=1341,offs=1)--21699(line=1342,offs=15)))
      // I1VALDCL
      let jsxtnm960
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21685(line=1342,offs=1)--21697(line=1342,offs=13))
      // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
      // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
      let jsxtnm958 = function () { // timp: gs_print$beg(802)
        // I1CMP:start
        let jsxtnm957 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(957))
        return jsxtnm957
      } // endtimp(gs_print$beg(802))
      let jsxtnm959 = XATSDAPP(jsxtnm958())
      jsxtnm960 = jsxtnm959
      XATS000_patck(true)
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21712(line=1344,offs=3)--21719(line=1344,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7023])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm966
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm965 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm961 = arg1
        // I1CMP:start
        let jsxtnm964 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(962);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(962)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm963 = XATSDAPP(XATS2JS_strn_print(jsxtnm961))
          jsxtnm964 = jsxtnm963
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(964))
        return jsxtnm964
      } // endtimp(strn_print(1040))
      jsxtnm966 = jsxtnm965
      let jsxtnm967 = XATSDAPP(jsxtnm966(jsxtnm953))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21729(line=1344,offs=20)--21741(line=1344,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm969 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm968 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(968))
        return jsxtnm968
      } // endtimp(gs_print$sep(803))
      let jsxtnm970 = XATSDAPP(jsxtnm969())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21746(line=1345,offs=3)--21753(line=1345,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7024])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4710(line=318,offs=1)--4814(line=324,offs=32)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(type_vw_t0);$list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))))>;I1Dtmpsub($list(@(vw[5780],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(type);$list(T2Pvar(vw[5780])))))))))
      let jsxtnm1008 = function (arg1) { // timp: g_print(39)
        let jsxtnm971 = arg1
        // I1CMP:start
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4760(line=323,offs=1)--4767(line=323,offs=8))
        // I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
        // T1IMPallx(g_ptype(202);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1512(line=44,offs=1)--1614(line=51,offs=32)))
        // T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(vt[7293],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(a1sz);$list(T2Pvar(vt[7293])))))))))
        let jsxtnm992 = function () { // timp: g_ptype(202)
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1567(line=50,offs=1)--1572(line=50,offs=6))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm976 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm972 = arg1
            // I1CMP:start
            let jsxtnm975 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(973);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(973)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm974 = XATSDAPP(XATS2JS_strn_print(jsxtnm972))
              jsxtnm975 = jsxtnm974
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(975))
            return jsxtnm975
          } // endtimp(strn_print(1040))
          let jsxtnm977 = XATSDAPP(jsxtnm976(XATSSTRN("a1sz(")))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1583(line=51,offs=1)--1590(line=51,offs=8))
          // I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(vt[7293])))))
          // T1IMPallx(g_ptype(202);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          // T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          let jsxtnm984 = function () { // timp: g_ptype(202)
            // I1CMP:start
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
            // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            let jsxtnm982 = function (arg1) { // timp: strn_print(1040)
              let jsxtnm978 = arg1
              // I1CMP:start
              let jsxtnm981 // let
              { // let
                // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                // I1FUNDCL: XATS2JS_strn_print(5082)
                // XATS2JS_strn_print_2202
                  // FJARGdarg($list(I1BNDcons(I1TNM(979);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(979)))))))
                  // I1CMP:start
                  // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                let jsxtnm980 = XATSDAPP(XATS2JS_strn_print(jsxtnm978))
                jsxtnm981 = jsxtnm980
              } // endlet
              // I1CMP:return:I1Vtnm(I1TNM(981))
              return jsxtnm981
            } // endtimp(strn_print(1040))
            let jsxtnm983 = XATSDAPP(jsxtnm982(XATSSTRN("sint")))
            // I1CMP:return:I1Vtnm(I1TNM(983))
            return jsxtnm983
          } // endtimp(g_ptype(202))
          let jsxtnm985 = XATSDAPP(jsxtnm984())
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1603(line=51,offs=21)--1608(line=51,offs=26))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm990 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm986 = arg1
            // I1CMP:start
            let jsxtnm989 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(987);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(987)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm988 = XATSDAPP(XATS2JS_strn_print(jsxtnm986))
              jsxtnm989 = jsxtnm988
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(989))
            return jsxtnm989
          } // endtimp(strn_print(1040))
          let jsxtnm991 = XATSDAPP(jsxtnm990(XATSSTRN(")")))
          // I1CMP:return:I1Vtnm(I1TNM(991))
          return jsxtnm991
        } // endtimp(g_ptype(202))
        let jsxtnm993 = XATSDAPP(jsxtnm992())
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4783(line=324,offs=1)--4788(line=324,offs=6))
        // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
        // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        let jsxtnm998 = function (arg1) { // timp: strn_print(1040)
          let jsxtnm994 = arg1
          // I1CMP:start
          let jsxtnm997 // let
          { // let
            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
            // I1FUNDCL: XATS2JS_strn_print(5082)
            // XATS2JS_strn_print_2202
              // FJARGdarg($list(I1BNDcons(I1TNM(995);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(995)))))))
              // I1CMP:start
              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
            let jsxtnm996 = XATSDAPP(XATS2JS_strn_print(jsxtnm994))
            jsxtnm997 = jsxtnm996
          } // endlet
          // I1CMP:return:I1Vtnm(I1TNM(997))
          return jsxtnm997
        } // endtimp(strn_print(1040))
        let jsxtnm999 = XATSDAPP(jsxtnm998(XATSSTRN(":")))
        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(4792(line=324,offs=10)--4799(line=324,offs=17))
        // I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(vw[5780])))))
        // T1IMPallx(g_psort(201);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1831(line=74,offs=1)--1885(line=78,offs=22)))
        // T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(tx[5755],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(tx[5755])))))))
        let jsxtnm1006 = function () { // timp: g_psort(201)
          // I1CMP:start
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1866(line=78,offs=3)--1876(line=78,offs=13))
          // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
          // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          let jsxtnm1004 = function (arg1) { // timp: strn_print(1040)
            let jsxtnm1000 = arg1
            // I1CMP:start
            let jsxtnm1003 // let
            { // let
              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
              // I1FUNDCL: XATS2JS_strn_print(5082)
              // XATS2JS_strn_print_2202
                // FJARGdarg($list(I1BNDcons(I1TNM(1001);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1001)))))))
                // I1CMP:start
                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
              let jsxtnm1002 = XATSDAPP(XATS2JS_strn_print(jsxtnm1000))
              jsxtnm1003 = jsxtnm1002
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(1003))
            return jsxtnm1003
          } // endtimp(strn_print(1040))
          let jsxtnm1005 = XATSDAPP(jsxtnm1004(XATSSTRN("tbox")))
          // I1CMP:return:I1Vtnm(I1TNM(1005))
          return jsxtnm1005
        } // endtimp(g_psort(201))
        let jsxtnm1007 = XATSDAPP(jsxtnm1006())
        // I1CMP:return:I1Vtnm(I1TNM(1007))
        return jsxtnm1007
      } // endtimp(g_print(39))
      let jsxtnm1009 = XATSDAPP(jsxtnm1008(jsxtnm954))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21763(line=1345,offs=20)--21775(line=1345,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm1011 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm1010 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(1010))
        return jsxtnm1010
      } // endtimp(gs_print$sep(803))
      let jsxtnm1012 = XATSDAPP(jsxtnm1011())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21780(line=1346,offs=3)--21787(line=1346,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7025])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
      let jsxtnm1018
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
      // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
      // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      let jsxtnm1017 = function (arg1) { // timp: strn_print(1040)
        let jsxtnm1013 = arg1
        // I1CMP:start
        let jsxtnm1016 // let
        { // let
          // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
          // I1FUNDCL: XATS2JS_strn_print(5082)
          // XATS2JS_strn_print_2202
            // FJARGdarg($list(I1BNDcons(I1TNM(1014);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1014)))))))
            // I1CMP:start
            // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
          let jsxtnm1015 = XATSDAPP(XATS2JS_strn_print(jsxtnm1013))
          jsxtnm1016 = jsxtnm1015
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(1016))
        return jsxtnm1016
      } // endtimp(strn_print(1040))
      jsxtnm1018 = jsxtnm1017
      let jsxtnm1019 = XATSDAPP(jsxtnm1018(jsxtnm955))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21797(line=1346,offs=20)--21809(line=1346,offs=32))
      // I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$sep(803);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
      // T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
      let jsxtnm1021 = function () { // timp: gs_print$sep(803)
        // I1CMP:start
        let jsxtnm1020 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(1020))
        return jsxtnm1020
      } // endtimp(gs_print$sep(803))
      let jsxtnm1022 = XATSDAPP(jsxtnm1021())
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21814(line=1347,offs=3)--21821(line=1347,offs=10))
      // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x3[7026])))))
      // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1767(line=65,offs=1)--2003(line=84,offs=4)))
      // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7295])))))))))
      let jsxtnm1227 = function (arg1) { // timp: g_print(39)
        let jsxtnm1023 = arg1
        // I1CMP:start
        let jsxtnm1226 // let
        { // let
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1825(line=72,offs=1)--1847(line=72,offs=23))
          // I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(xs;S2Eapps(S2Ecst(S2Tfun1($list(S2Tbas(T2Bimpr(2;vwtp)));S2Tbas(T2Bimpr(1;tbox)));a1sz);$list(S2Evar(S2Tbas(T2Bimpr(2;vwtp));x0[7295])))))))
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1851(line=74,offs=1)--1884(line=75,offs=25)))
          // I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Pcst(xs)),@(x0[1072],T2Pvar(x0[7295]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1885(line=76,offs=1)--1918(line=77,offs=25)))
          // I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Pcst(xs)),@(x0[1070],T2Pvar(x0[7295]))))):timp
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1919(line=78,offs=1)--1956(line=79,offs=29)))
          // I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Pcst(xs)),@(x0[1068],T2Pvar(x0[7295]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1972(line=83,offs=3)--1983(line=83,offs=14))
          // I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7295]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7295])))))
          // T1IMPallx(gseq_print1(1687);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
          // T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
          let jsxtnm1224 = function (arg1) { // timp: gseq_print1(1687)
            let jsxtnm1024 = arg1
            // I1CMP:start
            let jsxtnm1223 // let
            { // let
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
              // I1VALDCL
              let jsxtnm1033
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm1029 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm1025 = arg1
                // I1CMP:start
                let jsxtnm1028 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(1026);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1026)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm1027 = XATSDAPP(XATS2JS_strn_print(jsxtnm1025))
                  jsxtnm1028 = jsxtnm1027
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(1028))
                return jsxtnm1028
              } // endtimp(strn_print(1040))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
              // I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
              // T1IMPallx(gseq$beg(346);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1919(line=78,offs=1)--1956(line=79,offs=29)))
              // T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1068],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm1030 = function () { // timp: gseq$beg(346)
                // I1CMP:start
                // I1CMP:return:I1Vstr(...)
                return XATSSTRN("a1sz(")
              } // endtimp(gseq$beg(346))
              let jsxtnm1031 = XATSDAPP(jsxtnm1030())
              let jsxtnm1032 = XATSDAPP(jsxtnm1029(jsxtnm1031))
              jsxtnm1033 = jsxtnm1032
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
              // I1VALDCL
              let jsxtnm1213
              let jsxtnm1212 // let
              { // let
                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                // I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
                // I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                // T1IMPallx(gseq_iforitm1(1760);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
                // T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
                let jsxtnm1210 = function (arg1) { // timp: gseq_iforitm1(1760)
                  let jsxtnm1043 = arg1
                  // I1CMP:start
                  let jsxtnm1209 // let
                  { // let
                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                    // I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
                    let jsxtnm1208 // let
                    { // let
                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
                      // I1VALDCL
                      let jsxtnm1207
                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
                      // I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
                      // T1IMPallx(gseq_iforall1(1736);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
                      // T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
                      let jsxtnm1205 = function (arg1) { // timp: gseq_iforall1(1736)
                        let jsxtnm1049 = arg1
                        // I1CMP:start
                        let jsxtnm1204 // let
                        { // let
                          // I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
                          // I1VARDCL
                          // I1CMP:start
                          // I1CMP:return:I1Vint(T_INT01(0))
                          let jsxtnm1050 = XATSVAR1(XATSINT1(0))
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
                          // I1VALDCL
                          let jsxtnm1051
                          jsxtnm1051 = XATSADDR(jsxtnm1050)
                          XATS000_patck(true)
                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
                          // I1VALDCL
                          let jsxtnm1203
                          let jsxtnm1202 // let
                          { // let
                            // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                            // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
                            // I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
                            // T1IMPallx(gseq_forall1(1720);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2365(line=119,offs=1)--2495(line=129,offs=2)))
                            // T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[8814])),@(x0[4325],T2Pvar(x0[8815])))))))
                            let jsxtnm1200 = function (arg1) { // timp: gseq_forall1(1720)
                              let jsxtnm1060 = arg1
                              // I1CMP:start
                              let jsxtnm1199 // let
                              { // let
                                // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8815]))))):timp
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2417(line=124,offs=3)--2428(line=124,offs=14))
                                // I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8814]))),T2JAG($list(T2Pvar(x0[8815])))))
                                // T1IMPallx(gseq_forall(386);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2214(line=93,offs=1)--2345(line=103,offs=2)))
                                // T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7314])))),@(x0[1168],T2Pvar(x0[7314])))))))
                                let jsxtnm1197 = function (arg1) { // timp: gseq_forall(386)
                                  let jsxtnm1061 = arg1
                                  // I1CMP:start
                                  let jsxtnm1196 // let
                                  { // let
                                    // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                    // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[7314]))))):timp
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2272(line=99,offs=1)--2283(line=99,offs=12))
                                    // I0Etapq(I0Ecst(a1sz_forall(1140)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz001.sats)@(1643(line=55,offs=1)--1654(line=55,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                    // T1IMPallx(a1sz_forall(1140);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(1999(line=78,offs=1)--2057(line=81,offs=26)))
                                    // T1IMPallx(a1sz_forall(1140)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7312],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_forall(1140);$list(@(a[3064],T2Pvar(x0[7312])))))))
                                    let jsxtnm1194
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2032(line=81,offs=1)--2043(line=81,offs=12))
                                    // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7312]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7312])))))
                                    // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                                    // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                                    let jsxtnm1193 = function (arg1) { // timp: gasq_forall(609)
                                      let jsxtnm1062 = arg1
                                      // I1CMP:start
                                      let jsxtnm1192 // let
                                      { // let
                                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                                        // I1VALDCL
                                        let jsxtnm1070
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                                        // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                        // T1IMPallx(gasq_length(594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2083(line=89,offs=1)--2146(line=92,offs=33)))
                                        // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7296])))),@(x0[1875],T2Pvar(x0[7296])))))))
                                        let jsxtnm1068
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2131(line=92,offs=18)--2142(line=92,offs=29))
                                        // I0Etapq(I0Ecst(a1sz_length(1125)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3102(line=157,offs=1)--3113(line=157,offs=12))));$list(T2JAG($list(T2Pvar(x0[7296])))))
                                        // T1IMPallx(a1sz_length(1125);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1594(line=50,offs=1)--1768(line=64,offs=2)))
                                        // T1IMPallx(a1sz_length(1125)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8875],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_length(1125);$list(@(a[3038],T2Pvar(a[8875])))))))
                                        let jsxtnm1067 = function (arg1) { // timp: a1sz_length(1125)
                                          let jsxtnm1063 = arg1
                                          // I1CMP:start
                                          let jsxtnm1066 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1684(line=58,offs=1)--1766(line=63,offs=37)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1692(line=59,offs=1)--1766(line=63,offs=37))
                                            // I1FUNDCL: XATS2JS_a1sz_length(5172)
                                            // XATS2JS_a1sz_length_1695
                                              // FJARGdarg($list(I1BNDcons(I1TNM(1064);I0Pvar(A(5173));$list(@(A(5173),I1Vtnm(I1TNM(1064)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_length);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm1065 = XATSDAPP(XATS2JS_a1sz_length(jsxtnm1063))
                                            jsxtnm1066 = jsxtnm1065
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(1066))
                                          return jsxtnm1066
                                        } // endtimp(a1sz_length(1125))
                                        jsxtnm1068 = jsxtnm1067
                                        let jsxtnm1069 = XATSDAPP(jsxtnm1068(jsxtnm1062))
                                        jsxtnm1070 = jsxtnm1069
                                        XATS000_patck(true)
                                        let jsxtnm1191 // let
                                        { // let
                                          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                          // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                                          // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                                          // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                                          // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                                          let jsxtnm1189 = function (arg1) { // timp: nint_forall(958)
                                            let jsxtnm1080 = arg1
                                            // I1CMP:start
                                            let jsxtnm1188 // let
                                            { // let
                                              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                                              // I1FUNDCL
                                              function loop_2862(arg1, arg2)
                                              { // fun
                                                let jsxtnm1081 = arg1
                                                let jsxtnm1082 = arg2
                                                // I1CMP:start
                                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                                let jsxtnm1089 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                                  let jsxtnm1083 = arg1
                                                  let jsxtnm1084 = arg2
                                                  // I1CMP:start
                                                  let jsxtnm1088 // let
                                                  { // let
                                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                                    // XATS2JS_sint_gte$sint_2399
                                                      // FJARGdarg($list(I1BNDcons(I1TNM(1085);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(1085))))),I1BNDcons(I1TNM(1086);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(1086)))))))
                                                      // I1CMP:start
                                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                                    let jsxtnm1087 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm1083, jsxtnm1084))
                                                    jsxtnm1088 = jsxtnm1087
                                                  } // endlet
                                                  // I1CMP:return:I1Vtnm(I1TNM(1088))
                                                  return jsxtnm1088
                                                } // endtimp(sint_gte$sint(931))
                                                let jsxtnm1090 = XATSDAPP(jsxtnm1089(jsxtnm1082, jsxtnm1081))
                                                let jsxtnm1186 // ift
                                                if (jsxtnm1090) // ift
                                                {
                                                  jsxtnm1186 = XATSBOOL(true)
                                                } else {
                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                                  // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                  // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                                  // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                                  let jsxtnm1174 = function (arg1) { // timp: forall$test(47)
                                                    let jsxtnm1091 = arg1
                                                    // I1CMP:start
                                                    let jsxtnm1173 // let
                                                    { // let
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                                      // I1VALDCL
                                                      let jsxtnm1104
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                                      // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2517(line=119,offs=1)--2612(line=123,offs=35)))
                                                      // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7301])))),@(x0[5735],T2Pvar(x0[7301])))))))
                                                      let jsxtnm1102 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                                        let jsxtnm1092 = arg1
                                                        let jsxtnm1093 = arg2
                                                        // I1CMP:start
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2590(line=123,offs=13)--2602(line=123,offs=25))
                                                        // I0Etapq(I0Ecst(a1sz_lget$at(1130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3888(line=213,offs=1)--3900(line=213,offs=13))));$list(T2JAG($list(T2Pvar(x0[7301])))))
                                                        // T1IMPallx(a1sz_lget$at(1130);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1815(line=69,offs=1)--1992(line=84,offs=2)))
                                                        // T1IMPallx(a1sz_lget$at(1130)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8879],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_lget$at(1130);$list(@(a[3048],T2Pvar(a[8879])))))))
                                                        let jsxtnm1100 = function (arg1, arg2) { // timp: a1sz_lget$at(1130)
                                                          let jsxtnm1094 = arg1
                                                          let jsxtnm1095 = arg2
                                                          // I1CMP:start
                                                          let jsxtnm1099 // let
                                                          { // let
                                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1899(line=77,offs=1)--1990(line=83,offs=38)))
                                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1907(line=78,offs=1)--1990(line=83,offs=38))
                                                            // I1FUNDCL: XATS2JS_a1sz_lget$at(5176)
                                                            // XATS2JS_a1sz_lget$at_1910
                                                              // FJARGdarg($list(I1BNDcons(I1TNM(1096);I0Pvar(A(5177));$list(@(A(5177),I1Vtnm(I1TNM(1096))))),I1BNDcons(I1TNM(1097);I0Pvar(i(5178));$list(@(i(5178),I1Vtnm(I1TNM(1097)))))))
                                                              // I1CMP:start
                                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_lget$at);G1Nlist($list()))// I1CMP:return
                                                            let jsxtnm1098 = XATSDAPP(XATS2JS_a1sz_lget$at(jsxtnm1094, jsxtnm1095))
                                                            jsxtnm1099 = jsxtnm1098
                                                          } // endlet
                                                          // I1CMP:return:I1Vtnm(I1TNM(1099))
                                                          return jsxtnm1099
                                                        } // endtimp(a1sz_lget$at(1130))
                                                        let jsxtnm1101 = XATSDAPP(jsxtnm1100(jsxtnm1092, jsxtnm1093))
                                                        // I1CMP:return:I1Vtnm(I1TNM(1101))
                                                        return jsxtnm1101
                                                      } // endtimp(gasq_lget$at$raw(2326))
                                                      let jsxtnm1103 = XATSDAPP(jsxtnm1102(jsxtnm1062, jsxtnm1091))
                                                      jsxtnm1104 = jsxtnm1103
                                                      XATS000_patck(true)
                                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                                      // I1VALDCL
                                                      let jsxtnm1166
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2300(line=101,offs=1)--2343(line=102,offs=35)))
                                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7314],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm1164
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(2328(line=102,offs=20)--2339(line=102,offs=31))
                                                      // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7314])))))
                                                      // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2450(line=127,offs=1)--2493(line=128,offs=35)))
                                                      // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8814],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8815],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm1163
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2477(line=128,offs=19)--2489(line=128,offs=31))
                                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8815])))))
                                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                      let jsxtnm1162 = function (arg1) { // timp: forall$test1(1423)
                                                        let jsxtnm1105 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm1161 // let
                                                        { // let
                                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                                                          // I1VALDCL
                                                          let jsxtnm1110
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                                                          // I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                          // T1IMPallx(p2tr_get(2309);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                                          // T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                                          let jsxtnm1108 = function (arg1) { // timp: p2tr_get(2309)
                                                            let jsxtnm1106 = arg1
                                                            // I1CMP:start
                                                            let jsxtnm1107 = XATS000_dp2tr(jsxtnm1106)
                                                            // I1CMP:return:I1Vtnm(I1TNM(1107))
                                                            return jsxtnm1107
                                                          } // endtimp(p2tr_get(2309))
                                                          let jsxtnm1109 = XATSDAPP(jsxtnm1108(jsxtnm1051))
                                                          jsxtnm1110 = jsxtnm1109
                                                          XATS000_patck(true)
                                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                                                          // I1VALDCL
                                                          let jsxtnm1148
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                                                          // I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                                                          // T1IMPallx(iforall$test1(1433);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                                                          // T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8041],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                          let jsxtnm1146 = function (arg1, arg2) { // timp: iforall$test1(1433)
                                                            let jsxtnm1111 = arg1
                                                            let jsxtnm1112 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm1145 // let
                                                            { // let
                                                              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                                                              // I1VALDCL
                                                              let jsxtnm1144
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                                                              // I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                                                              // T1IMPallx(iforitm$work1(1449);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                                                              // T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7906],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                              let jsxtnm1142 = function (arg1, arg2) { // timp: iforitm$work1(1449)
                                                                let jsxtnm1113 = arg1
                                                                let jsxtnm1114 = arg2
                                                                // I1CMP:start
                                                                let jsxtnm1141 // let
                                                                { // let
                                                                  // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                                                                  // I1VALDCL
                                                                  let jsxtnm1132
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                                                                  // I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                                                                  // T1IMPallx(sint_gt$sint(928);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                                                                  // T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                                                                  let jsxtnm1121 = function (arg1, arg2) { // timp: sint_gt$sint(928)
                                                                    let jsxtnm1115 = arg1
                                                                    let jsxtnm1116 = arg2
                                                                    // I1CMP:start
                                                                    let jsxtnm1120 // let
                                                                    { // let
                                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(1873(line=79,offs=1)--1936(line=81,offs=39))
                                                                      // I1FUNDCL: XATS2JS_sint_gt$sint(4897)
                                                                      // XATS2JS_sint_gt$sint_1876
                                                                        // FJARGdarg($list(I1BNDcons(I1TNM(1117);I0Pvar(i1(4898));$list(@(i1(4898),I1Vtnm(I1TNM(1117))))),I1BNDcons(I1TNM(1118);I0Pvar(i2(4899));$list(@(i2(4899),I1Vtnm(I1TNM(1118)))))))
                                                                        // I1CMP:start
                                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gt$sint);G1Nlist($list()))// I1CMP:return
                                                                      let jsxtnm1119 = XATSDAPP(XATS2JS_sint_gt$sint(jsxtnm1115, jsxtnm1116))
                                                                      jsxtnm1120 = jsxtnm1119
                                                                    } // endlet
                                                                    // I1CMP:return:I1Vtnm(I1TNM(1120))
                                                                    return jsxtnm1120
                                                                  } // endtimp(sint_gt$sint(928))
                                                                  let jsxtnm1122 = XATSDAPP(jsxtnm1121(jsxtnm1113, XATSINT1(0)))
                                                                  let jsxtnm1131 // ift
                                                                  if (jsxtnm1122) // ift
                                                                  {
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                                                                    // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                                                                    // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
                                                                    // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                                                                    let jsxtnm1127 = function (arg1) { // timp: strn_print(1040)
                                                                      let jsxtnm1123 = arg1
                                                                      // I1CMP:start
                                                                      let jsxtnm1126 // let
                                                                      { // let
                                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                                                                        // I1FUNDCL: XATS2JS_strn_print(5082)
                                                                        // XATS2JS_strn_print_2202
                                                                          // FJARGdarg($list(I1BNDcons(I1TNM(1124);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1124)))))))
                                                                          // I1CMP:start
                                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                                                                        let jsxtnm1125 = XATSDAPP(XATS2JS_strn_print(jsxtnm1123))
                                                                        jsxtnm1126 = jsxtnm1125
                                                                      } // endlet
                                                                      // I1CMP:return:I1Vtnm(I1TNM(1126))
                                                                      return jsxtnm1126
                                                                    } // endtimp(strn_print(1040))
                                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                                                                    // I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                                                                    // T1IMPallx(gseq$sep(348);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1851(line=74,offs=1)--1884(line=75,offs=25)))
                                                                    // T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1072],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                                                    let jsxtnm1128 = function () { // timp: gseq$sep(348)
                                                                      // I1CMP:start
                                                                      // I1CMP:return:I1Vstr(...)
                                                                      return XATSSTRN(",")
                                                                    } // endtimp(gseq$sep(348))
                                                                    let jsxtnm1129 = XATSDAPP(jsxtnm1128())
                                                                    let jsxtnm1130 = XATSDAPP(jsxtnm1127(jsxtnm1129))
                                                                    jsxtnm1131 = jsxtnm1130
                                                                  } else {
                                                                  } // end(if)
                                                                  jsxtnm1132 = jsxtnm1131
                                                                  XATS000_patck(true)
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                                                                  // I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                                                                  // T1IMPallx(g_print1(1412);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                                                                  // T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                                                                  let jsxtnm1139
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                                                                  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                                                                  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                                                                  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                                                                  let jsxtnm1138
                                                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                                                                  // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                                                                  // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
                                                                  // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                                                                  let jsxtnm1137 = function (arg1) { // timp: sint_print(922)
                                                                    let jsxtnm1133 = arg1
                                                                    // I1CMP:start
                                                                    let jsxtnm1136 // let
                                                                    { // let
                                                                      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
                                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
                                                                      // I1FUNDCL: XATS2JS_sint_print(4946)
                                                                      // XATS2JS_sint_print_3707
                                                                        // FJARGdarg($list(I1BNDcons(I1TNM(1134);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(1134)))))))
                                                                        // I1CMP:start
                                                                        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
                                                                      let jsxtnm1135 = XATSDAPP(XATS2JS_sint_print(jsxtnm1133))
                                                                      jsxtnm1136 = jsxtnm1135
                                                                    } // endlet
                                                                    // I1CMP:return:I1Vtnm(I1TNM(1136))
                                                                    return jsxtnm1136
                                                                  } // endtimp(sint_print(922))
                                                                  jsxtnm1138 = jsxtnm1137
                                                                  jsxtnm1139 = jsxtnm1138
                                                                  let jsxtnm1140 = XATSDAPP(jsxtnm1139(jsxtnm1114))
                                                                  jsxtnm1141 = jsxtnm1140
                                                                } // endlet
                                                                // I1CMP:return:I1Vtnm(I1TNM(1141))
                                                                return jsxtnm1141
                                                              } // endtimp(iforitm$work1(1449))
                                                              let jsxtnm1143 = XATSDAPP(jsxtnm1142(jsxtnm1111, jsxtnm1112))
                                                              jsxtnm1144 = jsxtnm1143
                                                              XATS000_patck(true)
                                                              jsxtnm1145 = XATSBOOL(true)
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(1145))
                                                            return jsxtnm1145
                                                          } // endtimp(iforall$test1(1433))
                                                          let jsxtnm1147 = XATSDAPP(jsxtnm1146(jsxtnm1110, jsxtnm1105))
                                                          jsxtnm1148 = jsxtnm1147
                                                          XATS000_patck(true)
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                                                          // I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                                          // T1IMPallx(p2tr_set(2310);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                                          // T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                                          let jsxtnm1151 = function (arg1, arg2) { // timp: p2tr_set(2310)
                                                            let jsxtnm1149 = arg1
                                                            let jsxtnm1150 = arg2
                                                            // I1CMP:start
                                                            XATS000_assgn(jsxtnm1149, jsxtnm1150)
                                                            // I1CMP:return:I1V000()
                                                            return XATSVOID
                                                          } // endtimp(p2tr_set(2310))
                                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                                                          // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                          // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                          // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                          let jsxtnm1158 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                            let jsxtnm1152 = arg1
                                                            let jsxtnm1153 = arg2
                                                            // I1CMP:start
                                                            let jsxtnm1157 // let
                                                            { // let
                                                              // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                              // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                              // XATS2JS_sint_add$sint_2778
                                                                // FJARGdarg($list(I1BNDcons(I1TNM(1154);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(1154))))),I1BNDcons(I1TNM(1155);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(1155)))))))
                                                                // I1CMP:start
                                                                // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                              let jsxtnm1156 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm1152, jsxtnm1153))
                                                              jsxtnm1157 = jsxtnm1156
                                                            } // endlet
                                                            // I1CMP:return:I1Vtnm(I1TNM(1157))
                                                            return jsxtnm1157
                                                          } // endtimp(sint_add$sint(936))
                                                          let jsxtnm1159 = XATSDAPP(jsxtnm1158(jsxtnm1110, XATSINT1(1)))
                                                          let jsxtnm1160 = XATSDAPP(jsxtnm1151(jsxtnm1051, jsxtnm1159))
                                                          jsxtnm1161 = jsxtnm1148
                                                        } // endlet
                                                        // I1CMP:return:I1Vtnm(I1TNM(1161))
                                                        return jsxtnm1161
                                                      } // endtimp(forall$test1(1423))
                                                      jsxtnm1163 = jsxtnm1162
                                                      jsxtnm1164 = jsxtnm1163
                                                      let jsxtnm1165 = XATSDAPP(jsxtnm1164(jsxtnm1104))
                                                      jsxtnm1166 = jsxtnm1165
                                                      XATS000_patck(true)
                                                      // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                                      // I1VALDCL
                                                      // I1BNDcons(I1TNM(1168);I0Ptup0($list());$list())
                                                      // I1CMP:start
                                                      // I1LETnew1(I1TNM(1167);...)
                                                        // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(1104))))
                                                      // I1CMP(ival):I1Vtnm(I1TNM(1167))// I1CMP:return
                                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                                      // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                                      // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                                      // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                                      let jsxtnm1171 = function (arg1) { // timp: g_free(23)
                                                        let jsxtnm1169 = arg1
                                                        // I1CMP:start
                                                        let jsxtnm1170 = XATSTUP0([])
                                                        // I1CMP:return:I1Vtnm(I1TNM(1170))
                                                        return jsxtnm1170
                                                      } // endtimp(g_free(23))
                                                      let jsxtnm1172 = XATSDAPP(jsxtnm1171(jsxtnm1104))
                                                      jsxtnm1173 = jsxtnm1166
                                                    } // endlet
                                                    // I1CMP:return:I1Vtnm(I1TNM(1173))
                                                    return jsxtnm1173
                                                  } // endtimp(forall$test(47))
                                                  let jsxtnm1175 = XATSDAPP(jsxtnm1174(jsxtnm1082))
                                                  let jsxtnm1185 // ift
                                                  if (jsxtnm1175) // ift
                                                  {
                                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                                    // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                                    // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                                    // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                                    let jsxtnm1182 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                                      let jsxtnm1176 = arg1
                                                      let jsxtnm1177 = arg2
                                                      // I1CMP:start
                                                      let jsxtnm1181 // let
                                                      { // let
                                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                                        // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                                        // XATS2JS_sint_add$sint_2778
                                                          // FJARGdarg($list(I1BNDcons(I1TNM(1178);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(1178))))),I1BNDcons(I1TNM(1179);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(1179)))))))
                                                          // I1CMP:start
                                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                                        let jsxtnm1180 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm1176, jsxtnm1177))
                                                        jsxtnm1181 = jsxtnm1180
                                                      } // endlet
                                                      // I1CMP:return:I1Vtnm(I1TNM(1181))
                                                      return jsxtnm1181
                                                    } // endtimp(sint_add$sint(936))
                                                    let jsxtnm1183 = XATSDAPP(jsxtnm1182(jsxtnm1082, XATSINT1(1)))
                                                    let jsxtnm1184 = XATSDAPP(loop_2862(jsxtnm1081, jsxtnm1183))
                                                    jsxtnm1185 = jsxtnm1184
                                                  } else {
                                                    jsxtnm1185 = XATSBOOL(false)
                                                  } // end(if)
                                                  jsxtnm1186 = jsxtnm1185
                                                } // end(if)
                                                // I1CMP:return:I1Vtnm(I1TNM(1186))
                                                return jsxtnm1186
                                              } // endfun(loop_2862)
                                              let jsxtnm1187 = XATSDAPP(loop_2862(jsxtnm1080, XATSINT1(0)))
                                              jsxtnm1188 = jsxtnm1187
                                            } // endlet
                                            // I1CMP:return:I1Vtnm(I1TNM(1188))
                                            return jsxtnm1188
                                          } // endtimp(nint_forall(958))
                                          let jsxtnm1190 = XATSDAPP(jsxtnm1189(jsxtnm1070))
                                          jsxtnm1191 = jsxtnm1190
                                        } // endlet
                                        jsxtnm1192 = jsxtnm1191
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(1192))
                                      return jsxtnm1192
                                    } // endtimp(gasq_forall(609))
                                    jsxtnm1194 = jsxtnm1193
                                    let jsxtnm1195 = XATSDAPP(jsxtnm1194(jsxtnm1061))
                                    jsxtnm1196 = jsxtnm1195
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(1196))
                                  return jsxtnm1196
                                } // endtimp(gseq_forall(386))
                                let jsxtnm1198 = XATSDAPP(jsxtnm1197(jsxtnm1060))
                                jsxtnm1199 = jsxtnm1198
                              } // endlet
                              // I1CMP:return:I1Vtnm(I1TNM(1199))
                              return jsxtnm1199
                            } // endtimp(gseq_forall1(1720))
                            let jsxtnm1201 = XATSDAPP(jsxtnm1200(jsxtnm1049))
                            jsxtnm1202 = jsxtnm1201
                          } // endlet
                          jsxtnm1203 = jsxtnm1202
                          XATS000_patck(true)
                          jsxtnm1204 = jsxtnm1203
                        } // endlet
                        // I1CMP:return:I1Vtnm(I1TNM(1204))
                        return jsxtnm1204
                      } // endtimp(gseq_iforall1(1736))
                      let jsxtnm1206 = XATSDAPP(jsxtnm1205(jsxtnm1043))
                      jsxtnm1207 = jsxtnm1206
                      XATS000_patck(true)
                      jsxtnm1208 = XATSVOID
                    } // endlet
                    jsxtnm1209 = jsxtnm1208
                  } // endlet
                  // I1CMP:return:I1Vtnm(I1TNM(1209))
                  return jsxtnm1209
                } // endtimp(gseq_iforitm1(1760))
                let jsxtnm1211 = XATSDAPP(jsxtnm1210(jsxtnm1024))
                jsxtnm1212 = jsxtnm1211
              } // endlet
              jsxtnm1213 = jsxtnm1212
              XATS000_patck(true)
              // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
              // I1VALDCL
              let jsxtnm1222
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
              // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
              // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              let jsxtnm1218 = function (arg1) { // timp: strn_print(1040)
                let jsxtnm1214 = arg1
                // I1CMP:start
                let jsxtnm1217 // let
                { // let
                  // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
                  // I1FUNDCL: XATS2JS_strn_print(5082)
                  // XATS2JS_strn_print_2202
                    // FJARGdarg($list(I1BNDcons(I1TNM(1215);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1215)))))))
                    // I1CMP:start
                    // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
                  let jsxtnm1216 = XATSDAPP(XATS2JS_strn_print(jsxtnm1214))
                  jsxtnm1217 = jsxtnm1216
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(1217))
                return jsxtnm1217
              } // endtimp(strn_print(1040))
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
              // I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
              // T1IMPallx(gseq$end(347);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(1885(line=76,offs=1)--1918(line=77,offs=25)))
              // T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7295],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(a1sz);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(x0[1070],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              let jsxtnm1219 = function () { // timp: gseq$end(347)
                // I1CMP:start
                // I1CMP:return:I1Vstr(...)
                return XATSSTRN(")")
              } // endtimp(gseq$end(347))
              let jsxtnm1220 = XATSDAPP(jsxtnm1219())
              let jsxtnm1221 = XATSDAPP(jsxtnm1218(jsxtnm1220))
              jsxtnm1222 = jsxtnm1221
              XATS000_patck(true)
              jsxtnm1223 = XATSVOID
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(1223))
            return jsxtnm1223
          } // endtimp(gseq_print1(1687))
          let jsxtnm1225 = XATSDAPP(jsxtnm1224(jsxtnm1023))
          jsxtnm1226 = jsxtnm1225
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(1226))
        return jsxtnm1226
      } // endtimp(g_print(39))
      let jsxtnm1228 = XATSDAPP(jsxtnm1227(jsxtnm956))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21831(line=1347,offs=20)--21843(line=1347,offs=32))
      // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
      // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
      // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
      let jsxtnm1230 = function () { // timp: gs_print$end(804)
        // I1CMP:start
        let jsxtnm1229 = XATSTUP0([])
        // I1CMP:return:I1Vtnm(I1TNM(1229))
        return jsxtnm1229
      } // endtimp(gs_print$end(804))
      let jsxtnm1231 = XATSDAPP(jsxtnm1230())
      jsxtnm1232 = jsxtnm1231
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(1232))
    return jsxtnm1232
  } // endtimp(gs_print_a4(809))
  let jsxtnm1234 = XATSDAPP(jsxtnm1233(jsxtnm949, jsxtnm950, jsxtnm951, jsxtnm952))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26588(line=1613,offs=45)--26595(line=1613,offs=52))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm1240
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm1239 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm1235 = arg1
    // I1CMP:start
    let jsxtnm1238 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(1236);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1236)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm1237 = XATSDAPP(XATS2JS_strn_print(jsxtnm1235))
      jsxtnm1238 = jsxtnm1237
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(1238))
    return jsxtnm1238
  } // endtimp(strn_print(1040))
  jsxtnm1240 = jsxtnm1239
  let jsxtnm1241 = XATSDAPP(jsxtnm1240(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(1241))
  return jsxtnm1241
} // endtimp(gs_println_a4(822))
// LCSRCsome1(test03_a1sz000.dats)@(816(line=57,offs=17)--820(line=57,offs=21))
// I0Etapq(I0Ecst(g_type(196)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(1861(line=63,offs=1)--1867(line=63,offs=7))));$list(T2JAG($list())))
// T1IMPallx(g_type(196);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1498(line=45,offs=1)--1558(line=49,offs=22)))
// T1IMPallx(g_type(196)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_type(196);$list()))))
let jsxtnm1246 = function (arg1) { // timp: g_type(196)
  let jsxtnm1243 = arg1
  // I1CMP:start
  let jsxtnm1244 = XATSCAPP("unit", [0])
  let jsxtnm1245 = XATSCAST("castxy_1839", [jsxtnm1244])
  // I1CMP:return:I1Vtnm(I1TNM(1245))
  return jsxtnm1245
} // endtimp(g_type(196))
let jsxtnm1247 = XATSDAPP(jsxtnm1246(jsxtnm948))
let jsxtnm1248 = XATSDAPP(jsxtnm1242(XATSSTRN("ys("), jsxtnm1247, XATSSTRN(") = "), jsxtnm948))
jsxtnm1249 = jsxtnm1248
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(838(line=58,offs=1)--902(line=61,offs=38)))
// I1VALDCL
let jsxtnm1394
// LCSRCsome1(test03_a1sz000.dats)@(857(line=60,offs=9)--889(line=61,offs=25))
// I0Etapq(I0Ecst(GSEQ_foritm$f1un(271)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(6196(line=348,offs=1)--6212(line=348,offs=17))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
// T1IMPallx(GSEQ_foritm$f1un(271);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(4890(line=317,offs=1)--5012(line=324,offs=41)))
// T1IMPallx(GSEQ_foritm$f1un(271)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6701],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6702],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_foritm$f1un(271);$list(@(xs[869],T2Pvar(xs[6701])),@(x0[870],T2Pvar(x0[6702])))))))
let jsxtnm1365 = function (arg1, arg2) { // timp: GSEQ_foritm$f1un(271)
  let jsxtnm1250 = arg1
  let jsxtnm1251 = arg2
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(4955(line=323,offs=1)--4971(line=323,offs=17))
  // I0Etapq(I0Ecst(gseq_foritm$f1un(406)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7707(line=443,offs=1)--7723(line=443,offs=17))));$list(T2JAG($list(T2Pvar(xs[6701]))),T2JAG($list(T2Pvar(x0[6702])))))
  // T1IMPallx(gseq_foritm$f1un(406);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6627(line=426,offs=1)--6765(line=435,offs=2)))
  // T1IMPallx(gseq_foritm$f1un(406)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6120],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6121],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm$f1un(406);$list(@(xs[1231],T2Pvar(xs[6120])),@(x0[1232],T2Pvar(x0[6121])))))))
  let jsxtnm1359 = function (arg1, arg2) { // timp: gseq_foritm$f1un(406)
    let jsxtnm1252 = arg1
    let jsxtnm1253 = arg2
    // I1CMP:start
    let jsxtnm1358 // let
    { // let
      // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6724(line=434,offs=1)--6763(line=434,offs=40)))
      // I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pvar(x0[6121]))))):timp
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6690(line=432,offs=1)--6701(line=432,offs=12))
      // I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Pvar(xs[6120]))),T2JAG($list(T2Pvar(x0[6121])))))
      // T1IMPallx(gseq_foritm(402);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3828(line=215,offs=1)--3959(line=225,offs=2)))
      // T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7326],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7326],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7326])))),@(x0[1216],T2Pvar(x0[7326])))))))
      let jsxtnm1356 = function (arg1) { // timp: gseq_foritm(402)
        let jsxtnm1256 = arg1
        // I1CMP:start
        let jsxtnm1355 // let
        { // let
          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3914(line=223,offs=1)--3957(line=224,offs=35)))
          // I1Dimplmnt0(DIMPLone2(foritm$work1(1443);$list(@(x0[3786],T2Pvar(x0[7326]))))):timp
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3886(line=221,offs=1)--3897(line=221,offs=12))
          // I0Etapq(I0Ecst(a1sz_foritm(1148)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz001.sats)@(2647(line=113,offs=1)--2658(line=113,offs=12))));$list(T2JAG($list(T2Pvar(x0[7326])))))
          // T1IMPallx(a1sz_foritm(1148);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3613(line=200,offs=1)--3671(line=203,offs=26)))
          // T1IMPallx(a1sz_foritm(1148)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7324],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_foritm(1148);$list(@(a[3072],T2Pvar(x0[7324])))))))
          let jsxtnm1353
          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3646(line=203,offs=1)--3657(line=203,offs=12))
          // I0Etapq(I0Ecst(gasq_foritm(621)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(3257(line=174,offs=1)--3268(line=174,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Pvar(x0[7324]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7324])))))
          // T1IMPallx(gasq_foritm(621);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(6012(line=385,offs=1)--6153(line=396,offs=2)))
          // T1IMPallx(gasq_foritm(621)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6540],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6541],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_foritm(621);$list(@(xs[1932],T2Pvar(xs[6540])),@(x0[1933],T2Pvar(x0[6541])))))))
          let jsxtnm1352 = function (arg1) { // timp: gasq_foritm(621)
            let jsxtnm1257 = arg1
            // I1CMP:start
            let jsxtnm1351 // let
            { // let
              // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(6095(line=393,offs=1)--6151(line=395,offs=35)))
              // I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Pvar(xs[6540])),@(x0[4325],T2Pvar(x0[6541]))))):timp
              // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(6061(line=390,offs=1)--6073(line=390,offs=13))
              // I0Etapq(I0Ecst(gseq_foritm1(1752)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(9472(line=507,offs=1)--9484(line=507,offs=13))));$list(T2JAG($list(T2Pvar(xs[6540]))),T2JAG($list(T2Pvar(x0[6541])))))
              // T1IMPallx(gseq_foritm1(1752);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8250(line=546,offs=1)--8441(line=563,offs=2)))
              // T1IMPallx(gseq_foritm1(1752)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8024],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8025],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_foritm1(1752);$list(@(xs[4388],T2Pvar(xs[8024])),@(x0[4389],T2Pvar(x0[8025])))))))
              let jsxtnm1349 = function (arg1) { // timp: gseq_foritm1(1752)
                let jsxtnm1258 = arg1
                // I1CMP:start
                let jsxtnm1348 // let
                { // let
                  // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8362(line=558,offs=1)--8439(line=562,offs=33)))
                  // I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8025]))))):timp
                  let jsxtnm1347 // let
                  { // let
                    // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8309(line=553,offs=1)--8342(line=555,offs=13)))
                    // I1VALDCL
                    let jsxtnm1346
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8317(line=554,offs=1)--8329(line=554,offs=13))
                    // I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8024]))),T2JAG($list(T2Pvar(x0[8025])))))
                    // T1IMPallx(gseq_forall1(1720);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(6095(line=393,offs=1)--6151(line=395,offs=35)))
                    // T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6540],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6541],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[4325],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    let jsxtnm1344
                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(6132(line=395,offs=16)--6143(line=395,offs=27))
                    // I0Etapq(I0Ecst(gasq_forall(609)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq001.sats)@(1921(line=85,offs=1)--1932(line=85,offs=12))));$list(T2JAG($list(T2Pvar(xs[6540]))),T2JAG($list(T2Pvar(x0[6541])))))
                    // T1IMPallx(gasq_forall(609);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2761(line=147,offs=1)--3164(line=186,offs=4)))
                    // T1IMPallx(gasq_forall(609)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_forall(609);$list(@(xs[1908],T2Pvar(xs[6516])),@(x0[1909],T2Pvar(x0[6517])))))))
                    let jsxtnm1343 = function (arg1) { // timp: gasq_forall(609)
                      let jsxtnm1263 = arg1
                      // I1CMP:start
                      let jsxtnm1342 // let
                      { // let
                        // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2812(line=152,offs=1)--2845(line=154,offs=13)))
                        // I1VALDCL
                        let jsxtnm1271
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2821(line=153,offs=1)--2832(line=153,offs=12))
                        // I0Etapq(I0Ecst(gasq_length(594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gasq000.sats)@(1495(line=47,offs=1)--1506(line=47,offs=12))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                        // T1IMPallx(gasq_length(594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2083(line=89,offs=1)--2146(line=92,offs=33)))
                        // T1IMPallx(gasq_length(594)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7296],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_length(594);$list(@(xs[1874],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7296])))),@(x0[1875],T2Pvar(x0[7296])))))))
                        let jsxtnm1269
                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2131(line=92,offs=18)--2142(line=92,offs=29))
                        // I0Etapq(I0Ecst(a1sz_length(1125)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3102(line=157,offs=1)--3113(line=157,offs=12))));$list(T2JAG($list(T2Pvar(x0[7296])))))
                        // T1IMPallx(a1sz_length(1125);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1594(line=50,offs=1)--1768(line=64,offs=2)))
                        // T1IMPallx(a1sz_length(1125)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8875],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_length(1125);$list(@(a[3038],T2Pvar(a[8875])))))))
                        let jsxtnm1268 = function (arg1) { // timp: a1sz_length(1125)
                          let jsxtnm1264 = arg1
                          // I1CMP:start
                          let jsxtnm1267 // let
                          { // let
                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1684(line=58,offs=1)--1766(line=63,offs=37)))
                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1692(line=59,offs=1)--1766(line=63,offs=37))
                            // I1FUNDCL: XATS2JS_a1sz_length(5172)
                            // XATS2JS_a1sz_length_1695
                              // FJARGdarg($list(I1BNDcons(I1TNM(1265);I0Pvar(A(5173));$list(@(A(5173),I1Vtnm(I1TNM(1265)))))))
                              // I1CMP:start
                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_length);G1Nlist($list()))// I1CMP:return
                            let jsxtnm1266 = XATSDAPP(XATS2JS_a1sz_length(jsxtnm1264))
                            jsxtnm1267 = jsxtnm1266
                          } // endlet
                          // I1CMP:return:I1Vtnm(I1TNM(1267))
                          return jsxtnm1267
                        } // endtimp(a1sz_length(1125))
                        jsxtnm1269 = jsxtnm1268
                        let jsxtnm1270 = XATSDAPP(jsxtnm1269(jsxtnm1263))
                        jsxtnm1271 = jsxtnm1270
                        XATS000_patck(true)
                        let jsxtnm1341 // let
                        { // let
                          // I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                          // I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni))))):timp
                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2928(line=162,offs=1)--2939(line=162,offs=12))
                          // I0Etapq(I0Ecst(nint_forall(958)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(1757(line=66,offs=1)--1768(line=66,offs=12))));$list(T2JAG($list())))
                          // T1IMPallx(nint_forall(958);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2796(line=146,offs=1)--2981(line=160,offs=33)))
                          // T1IMPallx(nint_forall(958)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(nint_forall(958);$list()))))
                          let jsxtnm1339 = function (arg1) { // timp: nint_forall(958)
                            let jsxtnm1281 = arg1
                            // I1CMP:start
                            let jsxtnm1338 // let
                            { // let
                              // I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2859(line=151,offs=1)--2980(line=160,offs=32)))
                              // I1FUNDCL
                              function loop_2862(arg1, arg2)
                              { // fun
                                let jsxtnm1282 = arg1
                                let jsxtnm1283 = arg2
                                // I1CMP:start
                                // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2900(line=155,offs=5)--2902(line=155,offs=7))
                                // I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                                // T1IMPallx(sint_gte$sint(931);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                                // T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                                let jsxtnm1290 = function (arg1, arg2) { // timp: sint_gte$sint(931)
                                  let jsxtnm1284 = arg1
                                  let jsxtnm1285 = arg2
                                  // I1CMP:start
                                  let jsxtnm1289 // let
                                  { // let
                                    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2396(line=123,offs=1)--2460(line=125,offs=39))
                                    // I1FUNDCL: XATS2JS_sint_gte$sint(4912)
                                    // XATS2JS_sint_gte$sint_2399
                                      // FJARGdarg($list(I1BNDcons(I1TNM(1286);I0Pvar(i1(4913));$list(@(i1(4913),I1Vtnm(I1TNM(1286))))),I1BNDcons(I1TNM(1287);I0Pvar(i2(4914));$list(@(i2(4914),I1Vtnm(I1TNM(1287)))))))
                                      // I1CMP:start
                                      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_gte$sint);G1Nlist($list()))// I1CMP:return
                                    let jsxtnm1288 = XATSDAPP(XATS2JS_sint_gte$sint(jsxtnm1284, jsxtnm1285))
                                    jsxtnm1289 = jsxtnm1288
                                  } // endlet
                                  // I1CMP:return:I1Vtnm(I1TNM(1289))
                                  return jsxtnm1289
                                } // endtimp(sint_gte$sint(931))
                                let jsxtnm1291 = XATSDAPP(jsxtnm1290(jsxtnm1283, jsxtnm1282))
                                let jsxtnm1336 // ift
                                if (jsxtnm1291) // ift
                                {
                                  jsxtnm1336 = XATSBOOL(true)
                                } else {
                                  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2929(line=159,offs=1)--2940(line=159,offs=12))
                                  // I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                                  // T1IMPallx(forall$test(47);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2955(line=165,offs=1)--3158(line=184,offs=29)))
                                  // T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6516],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6517],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pcst(ni)))))))
                                  let jsxtnm1324 = function (arg1) { // timp: forall$test(47)
                                    let jsxtnm1292 = arg1
                                    // I1CMP:start
                                    let jsxtnm1323 // let
                                    { // let
                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3021(line=172,offs=1)--3077(line=176,offs=21)))
                                      // I1VALDCL
                                      let jsxtnm1305
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3040(line=175,offs=5)--3056(line=175,offs=21))
                                      // I0Etapq(I0Ecst(gasq_lget$at$raw(2326)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(4218(line=252,offs=1)--4234(line=252,offs=17))));$list(T2JAG($list(T2Pvar(xs[6516]))),T2JAG($list(T2Pvar(x0[6517])))))
                                      // T1IMPallx(gasq_lget$at$raw(2326);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2517(line=119,offs=1)--2612(line=123,offs=35)))
                                      // T1IMPallx(gasq_lget$at$raw(2326)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7301],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gasq_lget$at$raw(2326);$list(@(xs[5734],T2Papps(T2Pcst(a1sz);$list(T2Pvar(x0[7301])))),@(x0[5735],T2Pvar(x0[7301])))))))
                                      let jsxtnm1303 = function (arg1, arg2) { // timp: gasq_lget$at$raw(2326)
                                        let jsxtnm1293 = arg1
                                        let jsxtnm1294 = arg2
                                        // I1CMP:start
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz000.dats)@(2590(line=123,offs=13)--2602(line=123,offs=25))
                                        // I0Etapq(I0Ecst(a1sz_lget$at(1130)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/axsz000.sats)@(3888(line=213,offs=1)--3900(line=213,offs=13))));$list(T2JAG($list(T2Pvar(x0[7301])))))
                                        // T1IMPallx(a1sz_lget$at(1130);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1815(line=69,offs=1)--1992(line=84,offs=2)))
                                        // T1IMPallx(a1sz_lget$at(1130)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8879],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(a1sz_lget$at(1130);$list(@(a[3048],T2Pvar(a[8879])))))))
                                        let jsxtnm1301 = function (arg1, arg2) { // timp: a1sz_lget$at(1130)
                                          let jsxtnm1295 = arg1
                                          let jsxtnm1296 = arg2
                                          // I1CMP:start
                                          let jsxtnm1300 // let
                                          { // let
                                            // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1899(line=77,offs=1)--1990(line=83,offs=38)))
                                            // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/axsz000.dats)@(1907(line=78,offs=1)--1990(line=83,offs=38))
                                            // I1FUNDCL: XATS2JS_a1sz_lget$at(5176)
                                            // XATS2JS_a1sz_lget$at_1910
                                              // FJARGdarg($list(I1BNDcons(I1TNM(1297);I0Pvar(A(5177));$list(@(A(5177),I1Vtnm(I1TNM(1297))))),I1BNDcons(I1TNM(1298);I0Pvar(i(5178));$list(@(i(5178),I1Vtnm(I1TNM(1298)))))))
                                              // I1CMP:start
                                              // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_a1sz_lget$at);G1Nlist($list()))// I1CMP:return
                                            let jsxtnm1299 = XATSDAPP(XATS2JS_a1sz_lget$at(jsxtnm1295, jsxtnm1296))
                                            jsxtnm1300 = jsxtnm1299
                                          } // endlet
                                          // I1CMP:return:I1Vtnm(I1TNM(1300))
                                          return jsxtnm1300
                                        } // endtimp(a1sz_lget$at(1130))
                                        let jsxtnm1302 = XATSDAPP(jsxtnm1301(jsxtnm1293, jsxtnm1294))
                                        // I1CMP:return:I1Vtnm(I1TNM(1302))
                                        return jsxtnm1302
                                      } // endtimp(gasq_lget$at$raw(2326))
                                      let jsxtnm1304 = XATSDAPP(jsxtnm1303(jsxtnm1263, jsxtnm1292))
                                      jsxtnm1305 = jsxtnm1304
                                      XATS000_patck(true)
                                      // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3081(line=178,offs=1)--3115(line=180,offs=24)))
                                      // I1VALDCL
                                      let jsxtnm1316
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3094(line=180,offs=3)--3106(line=180,offs=15))
                                      // I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                      // T1IMPallx(forall$test1(1423);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8362(line=558,offs=1)--8439(line=562,offs=33)))
                                      // T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8024],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8025],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                      let jsxtnm1314 = function (arg1) { // timp: forall$test1(1423)
                                        let jsxtnm1306 = arg1
                                        // I1CMP:start
                                        let jsxtnm1313 // let
                                        { // let
                                          // I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8398(line=561,offs=1)--8427(line=562,offs=21)))
                                          // I1VALDCL
                                          let jsxtnm1312
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(8407(line=562,offs=1)--8419(line=562,offs=13))
                                          // I0Etapq(I0Ecst(foritm$work1(1443)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3082(line=186,offs=1)--3094(line=186,offs=13))));$list(T2JAG($list(T2Pvar(x0[8025])))))
                                          // T1IMPallx(foritm$work1(1443);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3914(line=223,offs=1)--3957(line=224,offs=35)))
                                          // T1IMPallx(foritm$work1(1443)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7326],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7326],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work1(1443);$list(@(x0[3786],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                          let jsxtnm1310
                                          // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/axsz001.dats)@(3942(line=224,offs=20)--3953(line=224,offs=31))
                                          // I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[7326])))))
                                          // T1IMPallx(foritm$work(51);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6724(line=434,offs=1)--6763(line=434,offs=40)))
                                          // T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6120],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6121],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                          let jsxtnm1309 = function (arg1) { // timp: foritm$work(51)
                                            let jsxtnm1307 = arg1
                                            // I1CMP:start
                                            let jsxtnm1308 = XATSDAPP(jsxtnm1253(jsxtnm1307))
                                            // I1CMP:return:I1Vtnm(I1TNM(1308))
                                            return jsxtnm1308
                                          } // endtimp(foritm$work(51))
                                          jsxtnm1310 = jsxtnm1309
                                          let jsxtnm1311 = XATSDAPP(jsxtnm1310(jsxtnm1306))
                                          jsxtnm1312 = jsxtnm1311
                                          XATS000_patck(true)
                                          jsxtnm1313 = XATSBOOL(true)
                                        } // endlet
                                        // I1CMP:return:I1Vtnm(I1TNM(1313))
                                        return jsxtnm1313
                                      } // endtimp(forall$test1(1423))
                                      let jsxtnm1315 = XATSDAPP(jsxtnm1314(jsxtnm1305))
                                      jsxtnm1316 = jsxtnm1315
                                      XATS000_patck(true)
                                      // I1Dprvdclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(3119(line=182,offs=1)--3156(line=184,offs=27)))
                                      // I1VALDCL
                                      // I1BNDcons(I1TNM(1318);I0Ptup0($list());$list())
                                      // I1CMP:start
                                      // I1LETnew1(I1TNM(1317);...)
                                        // I1INSdapp(I1Vcst(owed_vt_return0(6));$list(I1Vnone0(),I1Vtnm(I1TNM(1305))))
                                      // I1CMP(ival):I1Vtnm(I1TNM(1317))// I1CMP:return
                                      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gasq001.dats)@(2990(line=168,offs=3)--2996(line=168,offs=9))
                                      // I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6517])))))
                                      // T1IMPallx(g_free(23);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                      // T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                      let jsxtnm1321 = function (arg1) { // timp: g_free(23)
                                        let jsxtnm1319 = arg1
                                        // I1CMP:start
                                        let jsxtnm1320 = XATSTUP0([])
                                        // I1CMP:return:I1Vtnm(I1TNM(1320))
                                        return jsxtnm1320
                                      } // endtimp(g_free(23))
                                      let jsxtnm1322 = XATSDAPP(jsxtnm1321(jsxtnm1305))
                                      jsxtnm1323 = jsxtnm1316
                                    } // endlet
                                    // I1CMP:return:I1Vtnm(I1TNM(1323))
                                    return jsxtnm1323
                                  } // endtimp(forall$test(47))
                                  let jsxtnm1325 = XATSDAPP(jsxtnm1324(jsxtnm1283))
                                  let jsxtnm1335 // ift
                                  if (jsxtnm1325) // ift
                                  {
                                    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(2965(line=160,offs=17)--2966(line=160,offs=18))
                                    // I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                                    // T1IMPallx(sint_add$sint(936);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                                    // T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                                    let jsxtnm1332 = function (arg1, arg2) { // timp: sint_add$sint(936)
                                      let jsxtnm1326 = arg1
                                      let jsxtnm1327 = arg2
                                      // I1CMP:start
                                      let jsxtnm1331 // let
                                      { // let
                                        // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                                        // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(2775(line=154,offs=1)--2839(line=156,offs=39))
                                        // I1FUNDCL: XATS2JS_sint_add$sint(4922)
                                        // XATS2JS_sint_add$sint_2778
                                          // FJARGdarg($list(I1BNDcons(I1TNM(1328);I0Pvar(i1(4923));$list(@(i1(4923),I1Vtnm(I1TNM(1328))))),I1BNDcons(I1TNM(1329);I0Pvar(i2(4924));$list(@(i2(4924),I1Vtnm(I1TNM(1329)))))))
                                          // I1CMP:start
                                          // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_add$sint);G1Nlist($list()))// I1CMP:return
                                        let jsxtnm1330 = XATSDAPP(XATS2JS_sint_add$sint(jsxtnm1326, jsxtnm1327))
                                        jsxtnm1331 = jsxtnm1330
                                      } // endlet
                                      // I1CMP:return:I1Vtnm(I1TNM(1331))
                                      return jsxtnm1331
                                    } // endtimp(sint_add$sint(936))
                                    let jsxtnm1333 = XATSDAPP(jsxtnm1332(jsxtnm1283, XATSINT1(1)))
                                    let jsxtnm1334 = XATSDAPP(loop_2862(jsxtnm1282, jsxtnm1333))
                                    jsxtnm1335 = jsxtnm1334
                                  } else {
                                    jsxtnm1335 = XATSBOOL(false)
                                  } // end(if)
                                  jsxtnm1336 = jsxtnm1335
                                } // end(if)
                                // I1CMP:return:I1Vtnm(I1TNM(1336))
                                return jsxtnm1336
                              } // endfun(loop_2862)
                              let jsxtnm1337 = XATSDAPP(loop_2862(jsxtnm1281, XATSINT1(0)))
                              jsxtnm1338 = jsxtnm1337
                            } // endlet
                            // I1CMP:return:I1Vtnm(I1TNM(1338))
                            return jsxtnm1338
                          } // endtimp(nint_forall(958))
                          let jsxtnm1340 = XATSDAPP(jsxtnm1339(jsxtnm1271))
                          jsxtnm1341 = jsxtnm1340
                        } // endlet
                        jsxtnm1342 = jsxtnm1341
                      } // endlet
                      // I1CMP:return:I1Vtnm(I1TNM(1342))
                      return jsxtnm1342
                    } // endtimp(gasq_forall(609))
                    jsxtnm1344 = jsxtnm1343
                    let jsxtnm1345 = XATSDAPP(jsxtnm1344(jsxtnm1258))
                    jsxtnm1346 = jsxtnm1345
                    XATS000_patck(true)
                    jsxtnm1347 = XATSVOID
                  } // endlet
                  jsxtnm1348 = jsxtnm1347
                } // endlet
                // I1CMP:return:I1Vtnm(I1TNM(1348))
                return jsxtnm1348
              } // endtimp(gseq_foritm1(1752))
              let jsxtnm1350 = XATSDAPP(jsxtnm1349(jsxtnm1257))
              jsxtnm1351 = jsxtnm1350
            } // endlet
            // I1CMP:return:I1Vtnm(I1TNM(1351))
            return jsxtnm1351
          } // endtimp(gasq_foritm(621))
          jsxtnm1353 = jsxtnm1352
          let jsxtnm1354 = XATSDAPP(jsxtnm1353(jsxtnm1256))
          jsxtnm1355 = jsxtnm1354
        } // endlet
        // I1CMP:return:I1Vtnm(I1TNM(1355))
        return jsxtnm1355
      } // endtimp(gseq_foritm(402))
      let jsxtnm1357 = XATSDAPP(jsxtnm1356(jsxtnm1252))
      jsxtnm1358 = jsxtnm1357
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(1358))
    return jsxtnm1358
  } // endtimp(gseq_foritm$f1un(406))
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(4981(line=324,offs=10)--4990(line=324,offs=19))
  // I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6701]))),T2JAG($list(T2Pvar(x0[6702])))))
  // T1IMPallx(GSEQ_unmk(245);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
  // T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(a1sz_vt_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
  let jsxtnm1362 = function (arg1) { // timp: GSEQ_unmk(245)
    let jsxtnm1360 = arg1
    // I1CMP:start
    let jsxtnm1361 = XATSCAST("castxy_1839", [jsxtnm1360])
    // I1CMP:return:I1Vtnm(I1TNM(1361))
    return jsxtnm1361
  } // endtimp(GSEQ_unmk(245))
  let jsxtnm1363 = XATSDAPP(jsxtnm1362(jsxtnm1250))
  let jsxtnm1364 = XATSDAPP(jsxtnm1359(jsxtnm1363, jsxtnm1251))
  // I1CMP:return:I1Vtnm(I1TNM(1364))
  return jsxtnm1364
} // endtimp(GSEQ_foritm$f1un(271))
let jsxtnm1366 = XATSCAST("GSEQ_make_a1sz_4560", [jsxtnm948])
let jsxtnm1375 = function (arg1) { // lam0(T_LAM(0))
  let jsxtnm1367 = arg1
  // I1CMP:start
  // LCSRCsome1(test03_a1sz000.dats)@(878(line=61,offs=14)--883(line=61,offs=19))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
  let jsxtnm1373
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
  // I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(sint_print(922);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3616(line=223,offs=1)--3756(line=234,offs=2)))
  // T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
  let jsxtnm1372 = function (arg1) { // timp: sint_print(922)
    let jsxtnm1368 = arg1
    // I1CMP:start
    let jsxtnm1371 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3696(line=231,offs=1)--3754(line=233,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/gint000.dats)@(3704(line=232,offs=1)--3754(line=233,offs=47))
      // I1FUNDCL: XATS2JS_sint_print(4946)
      // XATS2JS_sint_print_3707
        // FJARGdarg($list(I1BNDcons(I1TNM(1369);I0Pvar(i0(4947));$list(@(i0(4947),I1Vtnm(I1TNM(1369)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_sint_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm1370 = XATSDAPP(XATS2JS_sint_print(jsxtnm1368))
      jsxtnm1371 = jsxtnm1370
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(1371))
    return jsxtnm1371
  } // endtimp(sint_print(922))
  jsxtnm1373 = jsxtnm1372
  let jsxtnm1374 = XATSDAPP(jsxtnm1373(jsxtnm1367))
  // I1CMP:return:I1Vtnm(I1TNM(1374))
  return jsxtnm1374
} // endfun(lam0)
let jsxtnm1376 = XATSDAPP(jsxtnm1365(jsxtnm1366, jsxtnm1375))
// LCSRCsome1(test03_a1sz000.dats)@(891(line=61,offs=27)--899(line=61,offs=35))
// I0Etapq(I0Ecst(gs_println_a0(818)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13710(line=888,offs=1)--13723(line=888,offs=14))));$list(T2JAG($list())))
// T1IMPallx(gs_println_a0(818);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26048(line=1572,offs=1)--26132(line=1577,offs=39)))
// T1IMPallx(gs_println_a0(818)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_println_a0(818);$list()))))
let jsxtnm1392 = function () { // timp: gs_println_a0(818)
  // I1CMP:start
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26096(line=1577,offs=3)--26107(line=1577,offs=14))
  // I0Etapq(I0Ecst(gs_print_a0(805)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11725(line=741,offs=1)--11736(line=741,offs=12))));$list(T2JAG($list())))
  // T1IMPallx(gs_print_a0(805);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20910(line=1285,offs=1)--20986(line=1290,offs=32)))
  // T1IMPallx(gs_print_a0(805)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print_a0(805);$list()))))
  let jsxtnm1383 = function () { // timp: gs_print_a0(805)
    // I1CMP:start
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20955(line=1290,offs=1)--20967(line=1290,offs=13))
    // I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$beg(802);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    // T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    let jsxtnm1378 = function () { // timp: gs_print$beg(802)
      // I1CMP:start
      let jsxtnm1377 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(1377))
      return jsxtnm1377
    } // endtimp(gs_print$beg(802))
    let jsxtnm1379 = XATSDAPP(jsxtnm1378())
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20971(line=1290,offs=17)--20983(line=1290,offs=29))
    // I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    // T1IMPallx(gs_print$end(804);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    // T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    let jsxtnm1381 = function () { // timp: gs_print$end(804)
      // I1CMP:start
      let jsxtnm1380 = XATSTUP0([])
      // I1CMP:return:I1Vtnm(I1TNM(1380))
      return jsxtnm1380
    } // endtimp(gs_print$end(804))
    let jsxtnm1382 = XATSDAPP(jsxtnm1381())
    // I1CMP:return:I1Vtnm(I1TNM(1382))
    return jsxtnm1382
  } // endtimp(gs_print_a0(805))
  let jsxtnm1384 = XATSDAPP(jsxtnm1383())
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26118(line=1577,offs=25)--26125(line=1577,offs=32))
  // I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  // T1IMPallx(g_print(39);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  // T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  let jsxtnm1390
  // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  // I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  // T1IMPallx(strn_print(1040);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2111(line=101,offs=1)--2251(line=112,offs=2)))
  // T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  let jsxtnm1389 = function (arg1) { // timp: strn_print(1040)
    let jsxtnm1385 = arg1
    // I1CMP:start
    let jsxtnm1388 // let
    { // let
      // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2191(line=109,offs=1)--2249(line=111,offs=47)))
      // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/strn000.dats)@(2199(line=110,offs=1)--2249(line=111,offs=47))
      // I1FUNDCL: XATS2JS_strn_print(5082)
      // XATS2JS_strn_print_2202
        // FJARGdarg($list(I1BNDcons(I1TNM(1386);I0Pvar(cs(5083));$list(@(cs(5083),I1Vtnm(I1TNM(1386)))))))
        // I1CMP:start
        // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_strn_print);G1Nlist($list()))// I1CMP:return
      let jsxtnm1387 = XATSDAPP(XATS2JS_strn_print(jsxtnm1385))
      jsxtnm1388 = jsxtnm1387
    } // endlet
    // I1CMP:return:I1Vtnm(I1TNM(1388))
    return jsxtnm1388
  } // endtimp(strn_print(1040))
  jsxtnm1390 = jsxtnm1389
  let jsxtnm1391 = XATSDAPP(jsxtnm1390(XATSSTRN("\n")))
  // I1CMP:return:I1Vtnm(I1TNM(1391))
  return jsxtnm1391
} // endtimp(gs_println_a0(818))
let jsxtnm1393 = XATSDAPP(jsxtnm1392())
jsxtnm1394 = jsxtnm1393
XATS000_patck(true)
// I1Dvaldclist(LCSRCsome1(test03_a1sz000.dats)@(949(line=66,offs=1)--994(line=66,offs=46)))
// I1VALDCL
let jsxtnm1405
// LCSRCsome1(test03_a1sz000.dats)@(958(line=66,offs=10)--969(line=66,offs=21))
// I0Etapq(I0Ecst(console_log(2594)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1544(line=50,offs=1)--1555(line=50,offs=12))));$list(T2JAG($list())))
// T1IMPallx(console_log(2594);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1581(line=53,offs=1)--1730(line=65,offs=2)))
// T1IMPallx(console_log(2594)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(console_log(2594);$list()))))
let jsxtnm1399 = function (arg1) { // timp: console_log(2594)
  let jsxtnm1395 = arg1
  // I1CMP:start
  let jsxtnm1398 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1663(line=61,offs=1)--1728(line=64,offs=34)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1671(line=62,offs=1)--1728(line=64,offs=34))
    // I1FUNDCL: XATS2JS_console_log(4774)
    // XATS2JS_console_log_1674
      // FJARGdarg($list(I1BNDcons(I1TNM(1396);I0Pvar(x0(4775));$list(@(x0(4775),I1Vtnm(I1TNM(1396)))))))
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_console_log);G1Nlist($list()))// I1CMP:return
    let jsxtnm1397 = XATSDAPP(XATS2JS_console_log(jsxtnm1395))
    jsxtnm1398 = jsxtnm1397
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(1398))
  return jsxtnm1398
} // endtimp(console_log(2594))
// LCSRCsome1(test03_a1sz000.dats)@(970(line=66,offs=22)--991(line=66,offs=43))
// I0Etapq(I0Ecst(the_print_store_flush(2597)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1836(line=76,offs=1)--1857(line=76,offs=22))));$list(T2JAG($list())))
// T1IMPallx(the_print_store_flush(2597);LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(1998(line=87,offs=1)--2171(line=98,offs=2)))
// T1IMPallx(the_print_store_flush(2597)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(the_print_store_flush(2597);$list()))))
let jsxtnm1402 = function () { // timp: the_print_store_flush(2597)
  // I1CMP:start
  let jsxtnm1401 // let
  { // let
    // I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2108(line=95,offs=1)--2169(line=97,offs=50)))
    // LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/JS/xtop000.dats)@(2116(line=96,offs=1)--2169(line=97,offs=50))
    // I1FUNDCL: XATS2JS_the_print_store_flush(4778)
    // XATS2JS_the_print_store_flush_2119
      // FJARGdarg($list())
      // I1CMP:start
      // I1CMP(ival):I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2JS_the_print_store_flush);G1Nlist($list()))// I1CMP:return
    let jsxtnm1400 = XATSDAPP(XATS2JS_the_print_store_flush())
    jsxtnm1401 = jsxtnm1400
  } // endlet
  // I1CMP:return:I1Vtnm(I1TNM(1401))
  return jsxtnm1401
} // endtimp(the_print_store_flush(2597))
let jsxtnm1403 = XATSDAPP(jsxtnm1402())
let jsxtnm1404 = XATSDAPP(jsxtnm1399(jsxtnm1403))
jsxtnm1405 = jsxtnm1404
XATS000_patck(true)
// LCSRCsome1(test03_a1sz000.dats)@(1257(line=74,offs=1)--1257(line=74,offs=1))
// I1Dnone1(I0Dnone1(LCSRCsome1(test03_a1sz000.dats)@(1257(line=74,offs=1)--1257(line=74,offs=1));D3Cnone0()))
