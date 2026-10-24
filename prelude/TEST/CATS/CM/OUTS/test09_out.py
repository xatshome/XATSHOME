## Thu Aug  6 10:50:22 PM EDT 2026
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
## /srcgen2/xats2py/srcgen1/xshared/runtime/srcgen2_precats.py]
##
########################################################################
########################################################################
## Sat Jan 17 10:30:51 PM EST 2026
## LCSRCsome1(precats.dats)@(1291(line=30,offs=1)--1332(line=31,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(0;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(UN);G1Estr(T_STRN1_clsd("prelude/SATS/unsfx00.sats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats));...)))
## I1Dextern(LCSRCsome1(precats.dats)@(1978(line=81,offs=1)--2048(line=86,offs=29)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_nilq(2293));$list(I1FUNDCL(XATS2PY_optn_nilq(2);$list(FJARGdarg($list(I1BNDcons(I1TNM(1);I0Pvar(xs(3));$list(@(xs(3),I1Vtnm(I1TNM(1))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_nilq);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_consq(2294));$list(I1FUNDCL(XATS2PY_optn_consq(5);$list(FJARGdarg($list(I1BNDcons(I1TNM(6);I0Pvar(xs(6));$list(@(xs(6),I1Vtnm(I1TNM(6))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_consq);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_head$raw(2295));$list(I1FUNDCL(XATS2PY_optn_head$raw(8);$list(FJARGdarg($list(I1BNDcons(I1TNM(11);I0Pvar(xs(9));$list(@(xs(9),I1Vtnm(I1TNM(11))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_head$raw);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_uncons$raw(2296));$list(I1FUNDCL(XATS2PY_optn_uncons$raw(12);$list(FJARGdarg($list(I1BNDcons(I1TNM(15);I0Pvar(xs(13));$list(@(xs(13),I1Vtnm(I1TNM(15))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_uncons$raw);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_nilq(2297));$list(I1FUNDCL(XATS2PY_list_nilq(16);$list(FJARGdarg($list(I1BNDcons(I1TNM(19);I0Pvar(xs(17));$list(@(xs(17),I1Vtnm(I1TNM(19))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_nilq);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_consq(2298));$list(I1FUNDCL(XATS2PY_list_consq(19);$list(FJARGdarg($list(I1BNDcons(I1TNM(24);I0Pvar(xs(20));$list(@(xs(20),I1Vtnm(I1TNM(24))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_consq);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_head$raw(2299));$list(I1FUNDCL(XATS2PY_list_head$raw(22);$list(FJARGdarg($list(I1BNDcons(I1TNM(29);I0Pvar(xs(23));$list(@(xs(23),I1Vtnm(I1TNM(29))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_head$raw);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_make_f0un(2300));$list(I1FUNDCL(XATS2PY_lazy_make_f0un(27);$list(FJARGdarg($list(I1BNDcons(I1TNM(33);I0Pvar(f0(28));$list(@(f0(28),I1Vtnm(I1TNM(33))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_make_f0un);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_nil(2301));$list(I1FUNDCL(XATS2PY_strmcon_nil(30);$list(FJARGdarg($list()));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_nil);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(3849(line=219,offs=1)--3895(line=220,offs=38)))
def XATS2PY_strmcon_nil(): ## impl
  ## I1CMP:start
  pyxtnm37 = XATSCAPP("strmcon_nil", [0])
  ## I1CMP:return:pyxtnm37
  return pyxtnm37
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(3899(line=222,offs=1)--3989(line=227,offs=38)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_cons(2302));$list(I1FUNDCL(XATS2PY_strmcon_cons(31);$list(FJARGdarg($list(I1BNDcons(I1TNM(38);I0Pvar(x1(32));$list(@(x1(32),I1Vtnm(I1TNM(38))))),I1BNDcons(I1TNM(39);I0Pvar(xs(33));$list(@(xs(33),I1Vtnm(I1TNM(39))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_cons);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_nilq(2303));$list(I1FUNDCL(XATS2PY_strmcon_nilq(36);$list(FJARGdarg($list(I1BNDcons(I1TNM(43);I0Pvar(xs(37));$list(@(xs(37),I1Vtnm(I1TNM(43))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_nilq);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_consq(2304));$list(I1FUNDCL(XATS2PY_strmcon_consq(39);$list(FJARGdarg($list(I1BNDcons(I1TNM(48);I0Pvar(xs(40));$list(@(xs(40),I1Vtnm(I1TNM(48))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_consq);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_head$raw(2305));$list(I1FUNDCL(XATS2PY_strmcon_head$raw(42);$list(FJARGdarg($list(I1BNDcons(I1TNM(53);I0Pvar(xs(43));$list(@(xs(43),I1Vtnm(I1TNM(53))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_head$raw);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_nilq1(2306));$list(I1FUNDCL(XATS2PY_optn_vt_nilq1(47);$list(FJARGdarg($list(I1BNDcons(I1TNM(57);I0Pvar(xs(48));$list(@(xs(48),I1Vtnm(I1TNM(57))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_nilq1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_consq1(2307));$list(I1FUNDCL(XATS2PY_optn_vt_consq1(51);$list(FJARGdarg($list(I1BNDcons(I1TNM(62);I0Pvar(xs(52));$list(@(xs(52),I1Vtnm(I1TNM(62))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_consq1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_head$raw0(2308));$list(I1FUNDCL(XATS2PY_optn_vt_head$raw0(55);$list(FJARGdarg($list(I1BNDcons(I1TNM(67);I0Pvar(xs(56));$list(@(xs(56),I1Vtnm(I1TNM(67))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_head$raw0);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_optn_vt_uncons$raw0(2309));$list(I1FUNDCL(XATS2PY_optn_vt_uncons$raw0(59);$list(FJARGdarg($list(I1BNDcons(I1TNM(71);I0Pvar(xs(60));$list(@(xs(60),I1Vtnm(I1TNM(71))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_optn_vt_uncons$raw0);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_nilq1(2310));$list(I1FUNDCL(XATS2PY_list_vt_nilq1(63);$list(FJARGdarg($list(I1BNDcons(I1TNM(75);I0Pvar(xs(64));$list(@(xs(64),I1Vtnm(I1TNM(75))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_nilq1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_consq1(2311));$list(I1FUNDCL(XATS2PY_list_vt_consq1(66);$list(FJARGdarg($list(I1BNDcons(I1TNM(80);I0Pvar(xs(67));$list(@(xs(67),I1Vtnm(I1TNM(80))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_consq1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_head$raw1(2312));$list(I1FUNDCL(XATS2PY_list_vt_head$raw1(69);$list(FJARGdarg($list(I1BNDcons(I1TNM(85);I0Pvar(xs(70));$list(@(xs(70),I1Vtnm(I1TNM(85))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_head$raw1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_list_vt_tail$raw0(2313));$list(I1FUNDCL(XATS2PY_list_vt_tail$raw0(75);$list(FJARGdarg($list(I1BNDcons(I1TNM(93);I0Pvar(xs(76));$list(@(xs(76),I1Vtnm(I1TNM(93))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_list_vt_tail$raw0);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_vt_eval(2314));$list(I1FUNDCL(XATS2PY_lazy_vt_eval(81);$list(FJARGdarg($list(I1BNDcons(I1TNM(100);I0Pvar(lz(82));$list(@(lz(82),I1Vtnm(I1TNM(100))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_vt_eval);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7173(line=452,offs=1)--7218(line=453,offs=37)))
def XATS2PY_lazy_vt_eval(arg1): ## impl
  pyxtnm101 = arg1
  ## I1CMP:start
  pyxtnm102 = XATS000_dl1az(pyxtnm101)
  ## I1CMP:return:pyxtnm102
  return pyxtnm102
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7222(line=455,offs=1)--7299(line=460,offs=32)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_vt_free(2315));$list(I1FUNDCL(XATS2PY_lazy_vt_free(84);$list(FJARGdarg($list(I1BNDcons(I1TNM(103);I0Pvar(lz(85));$list(@(lz(85),I1Vtnm(I1TNM(103))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_vt_free);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7300(line=461,offs=1)--7345(line=462,offs=37)))
def XATS2PY_lazy_vt_free(arg1): ## impl
  pyxtnm104 = arg1
  ## I1CMP:start
  XATS000_free(pyxtnm104)
  ## I1CMP:return:[]
  return []
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7372(line=466,offs=1)--7456(line=471,offs=35)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_lazy_vt_make_f0un(2316));$list(I1FUNDCL(XATS2PY_lazy_vt_make_f0un(87);$list(FJARGdarg($list(I1BNDcons(I1TNM(105);I0Pvar(f0(88));$list(@(f0(88),I1Vtnm(I1TNM(105))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_lazy_vt_make_f0un);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_nil(2317));$list(I1FUNDCL(XATS2PY_strmcon_vt_nil(90);$list(FJARGdarg($list()));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_nil);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(7634(line=483,offs=1)--7686(line=484,offs=44)))
def XATS2PY_strmcon_vt_nil(): ## impl
  ## I1CMP:start
  pyxtnm109 = XATSCAPP("strmcon_vt_nil", [0])
  ## I1CMP:return:pyxtnm109
  return pyxtnm109
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(7690(line=486,offs=1)--7789(line=491,offs=44)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_cons(2318));$list(I1FUNDCL(XATS2PY_strmcon_vt_cons(91);$list(FJARGdarg($list(I1BNDcons(I1TNM(110);I0Pvar(x1(92));$list(@(x1(92),I1Vtnm(I1TNM(110))))),I1BNDcons(I1TNM(111);I0Pvar(xs(93));$list(@(xs(93),I1Vtnm(I1TNM(111))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_cons);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_nilq1(2319));$list(I1FUNDCL(XATS2PY_strmcon_vt_nilq1(96);$list(FJARGdarg($list(I1BNDcons(I1TNM(115);I0Pvar(xs(97));$list(@(xs(97),I1Vtnm(I1TNM(115))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_nilq1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_consq1(2320));$list(I1FUNDCL(XATS2PY_strmcon_vt_consq1(99);$list(FJARGdarg($list(I1BNDcons(I1TNM(120);I0Pvar(xs(100));$list(@(xs(100),I1Vtnm(I1TNM(120))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_consq1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_head$raw1(2321));$list(I1FUNDCL(XATS2PY_strmcon_vt_head$raw1(102);$list(FJARGdarg($list(I1BNDcons(I1TNM(125);I0Pvar(xs(103));$list(@(xs(103),I1Vtnm(I1TNM(125))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_head$raw1);G1Nlist($list())))))))
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
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strmcon_vt_tail$raw0(2322));$list(I1FUNDCL(XATS2PY_strmcon_vt_tail$raw0(108);$list(FJARGdarg($list(I1BNDcons(I1TNM(133);I0Pvar(xs(109));$list(@(xs(109),I1Vtnm(I1TNM(133))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strmcon_vt_tail$raw0);G1Nlist($list())))))))
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
## I1Dextern(LCSRCsome1(precats.dats)@(8816(line=558,offs=1)--8915(line=563,offs=44)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strxcon_vt_cons(2323));$list(I1FUNDCL(XATS2PY_strxcon_vt_cons(114);$list(FJARGdarg($list(I1BNDcons(I1TNM(140);I0Pvar(x1(115));$list(@(x1(115),I1Vtnm(I1TNM(140))))),I1BNDcons(I1TNM(141);I0Pvar(xs(116));$list(@(xs(116),I1Vtnm(I1TNM(141))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strxcon_vt_cons);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(8916(line=564,offs=1)--8980(line=565,offs=56)))
def XATS2PY_strxcon_vt_cons(arg1, arg2): ## impl
  pyxtnm142 = arg1
  pyxtnm143 = arg2
  ## I1CMP:start
  pyxtnm144 = XATSCAPP("strxcon_vt_cons", [0, pyxtnm142, pyxtnm143])
  ## I1CMP:return:pyxtnm144
  return pyxtnm144
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(9029(line=572,offs=1)--9116(line=577,offs=34)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strxcon_vt_head$raw1(2324));$list(I1FUNDCL(XATS2PY_strxcon_vt_head$raw1(119);$list(FJARGdarg($list(I1BNDcons(I1TNM(145);I0Pvar(xs(120));$list(@(xs(120),I1Vtnm(I1TNM(145))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strxcon_vt_head$raw1);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(9117(line=578,offs=1)--9266(line=587,offs=42)))
def XATS2PY_strxcon_vt_head_raw1(arg1): ## impl
  pyxtnm146 = arg1
  ## I1CMP:start
  pyxtnm152 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(147);I0Pdapp(I0Pcon(strxcon_vt_cons(17));$list(I0Pvar(x1(122)),I0Pvar(xs(123))));$list(@(x1(122),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(147));0)),@(xs(123),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(147));1)))))
    if (XATS000_ctgeq(pyxtnm146, XATSCTAG("strxcon_vt_cons",0))): ## { // gpt
      pyxtnm147 = pyxtnm146
      ## let
      pyxtnm151 = None
      ## I1Dvaldclist(LCSRCsome1(precats.dats)@(9216(line=586,offs=1)--9241(line=587,offs=17)))
      ## I1VALDCL
      pyxtnm149 = None
      pyxtnm148 = XATSCAST("datacopy_1720", [XATSP1CN("strxcon_vt_cons", pyxtnm147[0+1])])
      pyxtnm149 = pyxtnm148
      XATS000_patck(True)
      pyxtnm150 = XATSCAST("enlinear_1756", [pyxtnm149])
      pyxtnm151 = pyxtnm150
      ## end-of(let)
      pyxtnm152 = pyxtnm151
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm152
  return pyxtnm152
## endfun(impl)
## I1Dextern(LCSRCsome1(precats.dats)@(9292(line=592,offs=1)--9386(line=597,offs=41)))
## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strxcon_vt_tail$raw0(2325));$list(I1FUNDCL(XATS2PY_strxcon_vt_tail$raw0(125);$list(FJARGdarg($list(I1BNDcons(I1TNM(153);I0Pvar(xs(126));$list(@(xs(126),I1Vtnm(I1TNM(153))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strxcon_vt_tail$raw0);G1Nlist($list())))))))
## I1Dimplmnt0(LCSRCsome1(precats.dats)@(9387(line=598,offs=1)--9526(line=605,offs=43)))
def XATS2PY_strxcon_vt_tail_raw0(arg1): ## impl
  pyxtnm154 = arg1
  ## I1CMP:start
  pyxtnm159 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(155);I0Pfree(I0Pdapp(I0Pcon(strxcon_vt_cons(17));$list(I0Pvar(x1(128)),I0Pvar(xs(129)))));$list(@(x1(128),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(155));0)),@(xs(129),I1Vp1cn(I0Pcon(strxcon_vt_cons(17));I1Vtnm(I1TNM(155));1)))))
    if (XATS000_ctgeq(pyxtnm154, XATSCTAG("strxcon_vt_cons",0))): ## { // gpt
      pyxtnm155 = pyxtnm154
      ## let
      pyxtnm158 = None
      ## I1Dvaldclist(LCSRCsome1(precats.dats)@(9490(line=605,offs=7)--9515(line=605,offs=32)))
      ## I1VALDCL
      pyxtnm157 = None
      pyxtnm156 = XATSCAST("delinear_1667", [XATSP1CN("strxcon_vt_cons", pyxtnm155[0+1])])
      pyxtnm157 = pyxtnm156
      XATS000_patck(True)
      pyxtnm158 = XATSP1CN("strxcon_vt_cons", pyxtnm155[1+1])
      ## end-of(let)
      pyxtnm159 = pyxtnm158
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:pyxtnm159
  return pyxtnm159
## endfun(impl)
## LCSRCsome1(precats.dats)@(9782(line=613,offs=1)--9782(line=613,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(precats.dats)@(9782(line=613,offs=1)--9782(line=613,offs=1));D3Cnone0()))
########################################################################
########################################################################
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
## LCSRCsome1(test09_llist00.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## I1Dinclude(LCSRCsome1(test09_llist00.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
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
## I1Dinclude(LCSRCsome1(test09_llist00.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
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
## I1Dfundclist(LCSRCsome1(test09_llist00.dats)@(323(line=21,offs=1)--437(line=28,offs=36)))
## I1FUNDCL
def length_326(arg1): ## fun
  pyxtnm1 = arg1
  ## I1CMP:start
  pyxtnm14 = None
  while True: ## do {
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(2);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
    if (XATS000_ctgeq(pyxtnm1, XATSCTAG("list_vt_nil",0))): ## { // gpt
      pyxtnm2 = pyxtnm1
      pyxtnm14 = XATSINT1(0)
      break ## cls
    ## } // gpt
    ## } // cls
    ## { // cls
    ## I1GPTpat(I1BNDcons(I1TNM(3);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pbang(I0Pvar(xs(5132)))));$list(@(xs(5132),I1Vlpcn(LABint(1);I1Vtnm(I1TNM(3)))))))
    if (XATS000_ctgeq(pyxtnm1, XATSCTAG("list_vt_cons",1))): ## { // gpt
      pyxtnm3 = pyxtnm1
      ## LCSRCsome1(test09_llist00.dats)@(426(line=28,offs=25)--427(line=28,offs=26))
      ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
      ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
      def pyxtnm10(arg1, arg2): ## timp: sint_add$sint(936)
        pyxtnm4 = arg1
        pyxtnm5 = arg2
        ## I1CMP:start
        ## let
        pyxtnm9 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(6);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(6))))),I1BNDcons(I1TNM(7);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(7))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
        pyxtnm8 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm4, pyxtnm5))
        pyxtnm9 = pyxtnm8
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(9))
        return pyxtnm9
      ## endtimp(sint_add$sint(936))
      pyxtnm11 = XATSFLAT(XATSLPCN(1, pyxtnm3))
      pyxtnm12 = XATSDAPP(length_326(pyxtnm11))
      pyxtnm13 = XATSDAPP(pyxtnm10(XATSINT1(1), pyxtnm12))
      pyxtnm14 = pyxtnm13
      break ## cls
    ## } // gpt
    ## } // cls
    XATS000_cfail()
  ## } while True // end-of(do-cls)
  ## I1CMP:return:I1Vtnm(I1TNM(14))
  return pyxtnm14
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(484(line=33,offs=1)--523(line=35,offs=18)))
## I1VALDCL
pyxtnm79 = None
## LCSRCsome1(test09_llist00.dats)@(493(line=34,offs=1)--505(line=34,offs=13))
## I0Etapq(I0Ecst(list_vt_make_nfun(2038)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(3083(line=156,offs=1)--3100(line=156,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(list_vt_make_nfun(2038), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2448(line=120,offs=1)--2509(line=123,offs=23)))
## T1IMPallx(list_vt_make_nfun(2038)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8493],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_make_nfun(2038);$list(@(a[5245],T2Pvar(a[8493])))))))
pyxtnm75 = None
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2487(line=123,offs=1)--2506(line=123,offs=20))
## I0Etapq(I0Ecst(nint_map$f1un_llist(969)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3824(line=192,offs=1)--3843(line=192,offs=20))));$list(T2JAG($list(T2Pvar(a[8493])))))
## T1IMPallx(nint_map$f1un_llist(969), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7232(line=482,offs=1)--7375(line=492,offs=2)))
## T1IMPallx(nint_map$f1un_llist(969)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map$f1un_llist(969);$list(@(y0[2872],T2Pvar(y0[7247])))))))
def pyxtnm74(arg1, arg2): ## timp: nint_map$f1un_llist(969)
  pyxtnm15 = arg1
  pyxtnm16 = arg2
  ## I1CMP:start
  ## let
  pyxtnm73 = None
  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
  ## I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Pvar(y0[7247]))))):timp
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7288(line=487,offs=1)--7302(line=487,offs=15))
  ## I0Etapq(I0Ecst(nint_map_llist(968)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3756(line=187,offs=1)--3770(line=187,offs=15))));$list(T2JAG($list(T2Pvar(y0[7247])))))
  ## T1IMPallx(nint_map_llist(968), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6864(line=449,offs=1)--7193(line=480,offs=2)))
  ## T1IMPallx(nint_map_llist(968)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7246],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map_llist(968);$list(@(y0[2870],T2Pvar(y0[7246])))))))
  def pyxtnm71(arg1): ## timp: nint_map_llist(968)
    pyxtnm19 = arg1
    ## I1CMP:start
    ## let
    pyxtnm70 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6958(line=459,offs=1)--6983(line=460,offs=17))
    ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(ys;S2Eapps(S2Ecst(list_vt);$list(S2Evar(y0[7246])))))))
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6987(line=462,offs=1)--7009(line=463,offs=19)))
    ## I1VALDCL
    pyxtnm21 = None
    pyxtnm20 = XATSCAPP("list_vt_nil", [0])
    pyxtnm21 = pyxtnm20
    XATS000_patck(True)
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7013(line=465,offs=1)--7188(line=478,offs=2)))
    ## I1FUNDCL
    def loop_7016(arg1, arg2): ## fun
      pyxtnm22 = arg1
      pyxtnm23 = arg2
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7054(line=470,offs=5)--7056(line=470,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm30(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm24 = arg1
        pyxtnm25 = arg2
        ## I1CMP:start
        ## let
        pyxtnm29 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(26);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(26))))),I1BNDcons(I1TNM(27);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(27))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm28 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm24, pyxtnm25))
        pyxtnm29 = pyxtnm28
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(29))
        return pyxtnm29
      ## endtimp(sint_gte$sint(931))
      pyxtnm31 = XATSDAPP(pyxtnm30(pyxtnm22, pyxtnm19))
      pyxtnm48 = None
      if (pyxtnm31):
        pyxtnm48 = pyxtnm23
      else:
        ## let
        pyxtnm47 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7078(line=473,offs=1)--7107(line=473,offs=30)))
        ## I1VALDCL
        pyxtnm36 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7087(line=473,offs=10)--7095(line=473,offs=18))
        ## I0Etapq(I0Ecst(map$fopr(77)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(4030(line=256,offs=1)--4038(line=256,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Pvar(y0[7246])))))
        ## T1IMPallx(map$fopr(77), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
        ## T1IMPallx(map$fopr(77)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
        def pyxtnm34(arg1): ## timp: map$fopr(77)
          pyxtnm32 = arg1
          ## I1CMP:start
          pyxtnm33 = XATSDAPP(pyxtnm16(pyxtnm32))
          ## I1CMP:return:I1Vtnm(I1TNM(33))
          return pyxtnm33
        ## endtimp(map$fopr(77))
        pyxtnm35 = XATSDAPP(pyxtnm34(pyxtnm22))
        pyxtnm36 = pyxtnm35
        XATS000_patck(True)
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7125(line=476,offs=8)--7126(line=476,offs=9))
        ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
        ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
        ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
        def pyxtnm43(arg1, arg2): ## timp: sint_add$sint(936)
          pyxtnm37 = arg1
          pyxtnm38 = arg2
          ## I1CMP:start
          ## let
          pyxtnm42 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(39);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(39))))),I1BNDcons(I1TNM(40);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(40))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
          pyxtnm41 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm37, pyxtnm38))
          pyxtnm42 = pyxtnm41
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(42))
          return pyxtnm42
        ## endtimp(sint_add$sint(936))
        pyxtnm44 = XATSDAPP(pyxtnm43(pyxtnm22, XATSINT1(1)))
        pyxtnm45 = XATSCAPP("list_vt_cons", [1, pyxtnm36, pyxtnm23])
        pyxtnm46 = XATSDAPP(loop_7016(pyxtnm44, pyxtnm45))
        pyxtnm47 = pyxtnm46
        ## end-of(let)
        pyxtnm48 = pyxtnm47
      ## end-of(if)
      ## I1CMP:return:I1Vtnm(I1TNM(48))
      return pyxtnm48
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6911(line=454,offs=1)--6927(line=454,offs=17))
    ## I0Etapq(I0Ecst(list_vt_reverse0(2046)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4474(line=255,offs=1)--4490(line=255,offs=17))));$list(T2JAG($list(T2Pvar(y0[7246])))))
    ## T1IMPallx(list_vt_reverse0(2046), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7033(line=475,offs=1)--7120(line=478,offs=46)))
    ## T1IMPallx(list_vt_reverse0(2046)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8528],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_reverse0(2046);$list(@(x0[5264],T2Pvar(a[8528])))))))
    def pyxtnm67(arg1): ## timp: list_vt_reverse0(2046)
      pyxtnm49 = arg1
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7075(line=478,offs=1)--7092(line=478,offs=18))
      ## I0Etapq(I0Ecst(list_vt_rappend00(2049)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4855(line=281,offs=1)--4872(line=281,offs=18))));$list(T2JAG($list(T2Pvar(a[8528])))))
      ## T1IMPallx(list_vt_rappend00(2049), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6363(line=426,offs=1)--6772(line=458,offs=2)))
      ## T1IMPallx(list_vt_rappend00(2049)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8524],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_rappend00(2049);$list(@(x0[5271],T2Pvar(a[8524])))))))
      def pyxtnm64(arg1, arg2): ## timp: list_vt_rappend00(2049)
        pyxtnm50 = arg1
        pyxtnm51 = arg2
        ## I1CMP:start
        ## let
        pyxtnm63 = None
        ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6442(line=434,offs=1)--6733(line=456,offs=2)))
        ## I1FUNDCL
        def loop_6445(arg1, arg2): ## fun
          pyxtnm52 = arg1
          pyxtnm53 = arg2
          ## I1CMP:start
          pyxtnm61 = None
          while True: ## do {
            ## { // cls
            ## I1GPTpat(I1BNDcons(I1TNM(54);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
            if (XATS000_ctgeq(pyxtnm52, XATSCTAG("list_vt_nil",0))): ## { // gpt
              pyxtnm54 = pyxtnm52
              pyxtnm61 = pyxtnm53
              break ## cls
            ## } // gpt
            ## } // cls
            ## { // cls
            ## I1GPTpat(I1BNDcons(I1TNM(55);I0Pflat(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pany())));$list()))
            if (XATS000_ctgeq(pyxtnm52, XATSCTAG("list_vt_cons",1))): ## { // gpt
              pyxtnm55 = pyxtnm52
              ## let
              pyxtnm60 = None
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6616(line=450,offs=3)--6631(line=450,offs=18)))
              ## I1VALDCL
              pyxtnm57 = None
              pyxtnm56 = XATSPCON(pyxtnm52,1)
              pyxtnm57 = pyxtnm56
              XATS000_patck(True)
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6634(line=451,offs=3)--6656(line=451,offs=25)))
              ## I1VALDCL
              pyxtnm58 = None
              XATS000_assgn(XATSLPCN(1, pyxtnm52), pyxtnm53)
              pyxtnm58 = XATSVOID
              XATS000_patck(True)
              XATS000_fold(pyxtnm52)
              pyxtnm59 = XATSDAPP(loop_6445(pyxtnm57, pyxtnm52))
              pyxtnm60 = pyxtnm59
              ## end-of(let)
              pyxtnm61 = pyxtnm60
              break ## cls
            ## } // gpt
            ## } // cls
            XATS000_cfail()
          ## } while True // end-of(do-cls)
          ## I1CMP:return:I1Vtnm(I1TNM(61))
          return pyxtnm61
        pyxtnm62 = XATSDAPP(loop_6445(pyxtnm50, pyxtnm51))
        pyxtnm63 = pyxtnm62
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(63))
        return pyxtnm63
      ## endtimp(list_vt_rappend00(2049))
      pyxtnm65 = XATSCAPP("list_vt_nil", [0])
      pyxtnm66 = XATSDAPP(pyxtnm64(pyxtnm49, pyxtnm65))
      ## I1CMP:return:I1Vtnm(I1TNM(66))
      return pyxtnm66
    ## endtimp(list_vt_reverse0(2046))
    pyxtnm68 = XATSDAPP(loop_7016(XATSINT1(0), pyxtnm21))
    pyxtnm69 = XATSDAPP(pyxtnm67(pyxtnm68))
    pyxtnm70 = pyxtnm69
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(70))
    return pyxtnm70
  ## endtimp(nint_map_llist(968))
  pyxtnm72 = XATSDAPP(pyxtnm71(pyxtnm15))
  pyxtnm73 = pyxtnm72
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(73))
  return pyxtnm73
## endtimp(nint_map$f1un_llist(969))
pyxtnm75 = pyxtnm74
def pyxtnm77(arg1): ## { // lam0(T_LAM(0))
  pyxtnm76 = arg1
  ## I1CMP:start
  ## I1CMP:return:I1Vtnm(I1TNM(76))
  return pyxtnm76
## } // end(lam0)
pyxtnm78 = XATSDAPP(pyxtnm75(XATSINT1(10), pyxtnm77))
pyxtnm79 = pyxtnm78
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(527(line=37,offs=1)--546(line=37,offs=20)))
## I1VALDCL
pyxtnm81 = None
pyxtnm80 = XATSDAPP(length_326(pyxtnm79))
pyxtnm81 = pyxtnm80
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(547(line=38,offs=1)--577(line=39,offs=22)))
## I1VALDCL
pyxtnm122 = None
## LCSRCsome1(test09_llist00.dats)@(556(line=39,offs=1)--564(line=39,offs=9))
## I0Etapq(I0Ecst(gs_println_a2(820)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(13791(line=896,offs=1)--13804(line=896,offs=14))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(gs_println_a2(820), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26226(line=1586,offs=1)--26327(line=1592,offs=45)))
## T1IMPallx(gs_println_a2(820)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7096],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7097],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_println_a2(820);$list(@(x0[2565],T2Pvar(x0[7096])),@(x1[2566],T2Pvar(x1[7097])))))))
def pyxtnm120(arg1, arg2): ## timp: gs_println_a2(820)
  pyxtnm82 = arg1
  pyxtnm83 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26285(line=1592,offs=3)--26296(line=1592,offs=14))
  ## I0Etapq(I0Ecst(gs_print_a2(807)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11802(line=749,offs=1)--11813(line=749,offs=12))));$list(T2JAG($list(T2Pvar(x0[7096]))),T2JAG($list(T2Pvar(x1[7097])))))
  ## T1IMPallx(gs_print_a2(807), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21143(line=1303,offs=1)--21306(line=1314,offs=4)))
  ## T1IMPallx(gs_print_a2(807)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7018],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7019],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a2(807);$list(@(x0[2487],T2Pvar(x0[7018])),@(x1[2488],T2Pvar(x1[7019])))))))
  def pyxtnm111(arg1, arg2): ## timp: gs_print_a2(807)
    pyxtnm84 = arg1
    pyxtnm85 = arg2
    ## I1CMP:start
    ## let
    pyxtnm110 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21200(line=1309,offs=1)--21223(line=1310,offs=15)))
    ## I1VALDCL
    pyxtnm89 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21209(line=1310,offs=1)--21221(line=1310,offs=13))
    ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
    ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
    def pyxtnm87(): ## timp: gs_print$beg(802)
      ## I1CMP:start
      pyxtnm86 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(86))
      return pyxtnm86
    ## endtimp(gs_print$beg(802))
    pyxtnm88 = XATSDAPP(pyxtnm87())
    pyxtnm89 = pyxtnm88
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21236(line=1312,offs=3)--21243(line=1312,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7018])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
    pyxtnm95 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm94(arg1): ## timp: strn_print(1040)
      pyxtnm90 = arg1
      ## I1CMP:start
      ## let
      pyxtnm93 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(91);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(91))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm92 = XATSDAPP(XATS2PY_strn_print(pyxtnm90))
      pyxtnm93 = pyxtnm92
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(93))
      return pyxtnm93
    ## endtimp(strn_print(1040))
    pyxtnm95 = pyxtnm94
    pyxtnm96 = XATSDAPP(pyxtnm95(pyxtnm84))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21253(line=1312,offs=20)--21265(line=1312,offs=32))
    ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
    ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
    def pyxtnm98(): ## timp: gs_print$sep(803)
      ## I1CMP:start
      pyxtnm97 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(97))
      return pyxtnm97
    ## endtimp(gs_print$sep(803))
    pyxtnm99 = XATSDAPP(pyxtnm98())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21270(line=1313,offs=3)--21277(line=1313,offs=10))
    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7019])))))
    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
    pyxtnm105 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
    ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
    ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
    def pyxtnm104(arg1): ## timp: sint_print(922)
      pyxtnm100 = arg1
      ## I1CMP:start
      ## let
      pyxtnm103 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(101);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(101))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
      pyxtnm102 = XATSDAPP(XATS2PY_sint_print(pyxtnm100))
      pyxtnm103 = pyxtnm102
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(103))
      return pyxtnm103
    ## endtimp(sint_print(922))
    pyxtnm105 = pyxtnm104
    pyxtnm106 = XATSDAPP(pyxtnm105(pyxtnm85))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21287(line=1313,offs=20)--21299(line=1313,offs=32))
    ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
    ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
    ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
    def pyxtnm108(): ## timp: gs_print$end(804)
      ## I1CMP:start
      pyxtnm107 = XATSTUP0([])
      ## I1CMP:return:I1Vtnm(I1TNM(107))
      return pyxtnm107
    ## endtimp(gs_print$end(804))
    pyxtnm109 = XATSDAPP(pyxtnm108())
    pyxtnm110 = pyxtnm109
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(110))
    return pyxtnm110
  ## endtimp(gs_print_a2(807))
  pyxtnm112 = XATSDAPP(pyxtnm111(pyxtnm82, pyxtnm83))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(26313(line=1592,offs=31)--26320(line=1592,offs=38))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm118 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm117(arg1): ## timp: strn_print(1040)
    pyxtnm113 = arg1
    ## I1CMP:start
    ## let
    pyxtnm116 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(114);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(114))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm115 = XATSDAPP(XATS2PY_strn_print(pyxtnm113))
    pyxtnm116 = pyxtnm115
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(116))
    return pyxtnm116
  ## endtimp(strn_print(1040))
  pyxtnm118 = pyxtnm117
  pyxtnm119 = XATSDAPP(pyxtnm118(XATSSTRN("\n")))
  ## I1CMP:return:I1Vtnm(I1TNM(119))
  return pyxtnm119
## endtimp(gs_println_a2(820))
pyxtnm121 = XATSDAPP(pyxtnm120(XATSSTRN("ln = "), pyxtnm81))
pyxtnm122 = pyxtnm121
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(581(line=41,offs=1)--620(line=42,offs=31)))
## I1VALDCL
pyxtnm166 = None
## LCSRCsome1(test09_llist00.dats)@(590(line=42,offs=1)--598(line=42,offs=9))
## I0Etapq(I0Ecst(list_vt_map0$f1un(2105)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(5135(line=313,offs=1)--5152(line=313,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(list_vt_map0$f1un(2105), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5246(line=321,offs=1)--5385(line=330,offs=2)))
## T1IMPallx(list_vt_map0$f1un(2105)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8570],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8571],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_map0$f1un(2105);$list(@(x0[5350],T2Pvar(x0[8570])),@(y0[5351],T2Pvar(y0[8571])))))))
def pyxtnm154(arg1, arg2): ## timp: list_vt_map0$f1un(2105)
  pyxtnm123 = arg1
  pyxtnm124 = arg2
  ## I1CMP:start
  ## let
  pyxtnm153 = None
  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5344(line=329,offs=1)--5383(line=329,offs=40)))
  ## I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Pvar(x0[8570])),@(y0[3858],T2Pvar(y0[8571]))))):timp
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5310(line=327,offs=3)--5322(line=327,offs=15))
  ## I0Etapq(I0Ecst(list_vt_map0(2103)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(4887(line=297,offs=1)--4899(line=297,offs=13))));$list(T2JAG($list(T2Pvar(x0[8570]))),T2JAG($list(T2Pvar(y0[8571])))))
  ## T1IMPallx(list_vt_map0(2103), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(4753(line=281,offs=1)--5205(line=319,offs=4)))
  ## T1IMPallx(list_vt_map0(2103)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8567],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8568],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_map0(2103);$list(@(x0[5344],T2Pvar(x0[8567])),@(y0[5345],T2Pvar(y0[8568])))))))
  def pyxtnm151(arg1): ## timp: list_vt_map0(2103)
    pyxtnm127 = arg1
    ## I1CMP:start
    ## let
    pyxtnm150 = None
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(4813(line=287,offs=1)--5104(line=311,offs=2)))
    ## I1FUNDCL
    def loop_4816(arg1, arg2): ## fun
      pyxtnm128 = arg1
      pyxtnm129 = arg2
      ## I1CMP:start
      pyxtnm144 = None
      while True: ## do {
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(130);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
        if (XATS000_ctgeq(pyxtnm128, XATSCTAG("list_vt_nil",0))): ## { // gpt
          pyxtnm130 = pyxtnm128
          pyxtnm131 = XATSCAPP("list_vt_nil", [0])
          XATS000_assgn(XATSADDR(pyxtnm129), pyxtnm131)
          pyxtnm144 = XATSVOID
          break ## cls
        ## } // gpt
        ## } // cls
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(132);I0Pfree(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x0(4373)),I0Pvar(xs(4374)))));$list(@(x0(4373),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(132));0)),@(xs(4374),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(132));1)))))
        if (XATS000_ctgeq(pyxtnm128, XATSCTAG("list_vt_cons",1))): ## { // gpt
          pyxtnm132 = pyxtnm128
          ## let
          pyxtnm143 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(4997(line=303,offs=1)--5027(line=304,offs=22)))
          ## I1VALDCL
          pyxtnm137 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5006(line=304,offs=1)--5015(line=304,offs=10))
          ## I0Etapq(I0Ecst(map$fopr0(1484)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(5345(line=363,offs=1)--5354(line=363,offs=10))));$list(T2JAG($list(T2Pvar(x0[8567]))),T2JAG($list(T2Pvar(y0[8568])))))
          ## T1IMPallx(map$fopr0(1484), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5344(line=329,offs=1)--5383(line=329,offs=40)))
          ## T1IMPallx(map$fopr0(1484)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8570],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8571],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[3858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
          def pyxtnm135(arg1): ## timp: map$fopr0(1484)
            pyxtnm133 = arg1
            ## I1CMP:start
            pyxtnm134 = XATSDAPP(pyxtnm124(pyxtnm133))
            ## I1CMP:return:I1Vtnm(I1TNM(134))
            return pyxtnm134
          ## endtimp(map$fopr0(1484))
          pyxtnm136 = XATSDAPP(pyxtnm135(XATSP1CN("list_vt_cons", pyxtnm132[0+1])))
          pyxtnm137 = pyxtnm136
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5028(line=305,offs=1)--5064(line=306,offs=28)))
          ## I1VALDCL
          pyxtnm139 = None
          pyxtnm138 = XATSCAPP("list_vt_cons", [1, pyxtnm137, XATSTOP0])
          XATS000_assgn(XATSADDR(pyxtnm129), pyxtnm138)
          pyxtnm139 = XATSVOID
          XATS000_patck(True)
          pyxtnm140 = XATSFLAT(pyxtnm129)
          pyxtnm141 = XATSDAPP(loop_4816(XATSP1CN("list_vt_cons", pyxtnm132[1+1]), XATSLPCN(1, pyxtnm140)))
          pyxtnm142 = XATSFLAT(pyxtnm129)
          XATS000_fold(pyxtnm142)
          pyxtnm143 = XATSVOID
          ## end-of(let)
          pyxtnm144 = pyxtnm143
          break ## cls
        ## } // gpt
        ## } // cls
        XATS000_cfail()
      ## } while True // end-of(do-cls)
      ## I1CMP:return:I1Vtnm(I1TNM(144))
      return pyxtnm144
    ## let
    pyxtnm149 = None
    ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5140(line=316,offs=3)--5159(line=316,offs=22)))
    ## I1VARDCL
    pyxtnm145 = XATSVAR0()
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5162(line=317,offs=3)--5183(line=317,offs=24)))
    ## I1VALDCL
    pyxtnm147 = None
    pyxtnm146 = XATSDAPP(loop_4816(pyxtnm127, XATSADDR(pyxtnm145)))
    pyxtnm147 = pyxtnm146
    XATS000_patck(True)
    pyxtnm148 = XATSFLAT(pyxtnm145)
    pyxtnm149 = pyxtnm148
    ## end-of(let)
    pyxtnm150 = pyxtnm149
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(150))
    return pyxtnm150
  ## endtimp(list_vt_map0(2103))
  pyxtnm152 = XATSDAPP(pyxtnm151(pyxtnm123))
  pyxtnm153 = pyxtnm152
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(153))
  return pyxtnm153
## endtimp(list_vt_map0$f1un(2105))
def pyxtnm164(arg1): ## { // lam0(T_LAM(0))
  pyxtnm155 = arg1
  ## I1CMP:start
  ## LCSRCsome1(test09_llist00.dats)@(617(line=42,offs=28)--618(line=42,offs=29))
  ## I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(sint_mul$sint(938), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
  ## T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
  def pyxtnm162(arg1, arg2): ## timp: sint_mul$sint(938)
    pyxtnm156 = arg1
    pyxtnm157 = arg2
    ## I1CMP:start
    ## let
    pyxtnm161 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mul$sint(2621));$list(I1FUNDCL(XATS2PY_sint_mul$sint(4901);$list(FJARGdarg($list(I1BNDcons(I1TNM(158);I0Pvar(i1(4902));$list(@(i1(4902),I1Vtnm(I1TNM(158))))),I1BNDcons(I1TNM(159);I0Pvar(i2(4903));$list(@(i2(4903),I1Vtnm(I1TNM(159))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mul$sint);G1Nlist($list())))))))
    pyxtnm160 = XATSDAPP(XATS2PY_sint_mul_sint(pyxtnm156, pyxtnm157))
    pyxtnm161 = pyxtnm160
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(161))
    return pyxtnm161
  ## endtimp(sint_mul$sint(938))
  pyxtnm163 = XATSDAPP(pyxtnm162(pyxtnm155, pyxtnm155))
  ## I1CMP:return:I1Vtnm(I1TNM(163))
  return pyxtnm163
## } // end(lam0)
pyxtnm165 = XATSDAPP(pyxtnm154(pyxtnm79, pyxtnm164))
pyxtnm166 = pyxtnm165
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(621(line=43,offs=1)--656(line=43,offs=36)))
## I1VALDCL
pyxtnm472 = None
## LCSRCsome1(test09_llist00.dats)@(630(line=43,offs=10)--637(line=43,offs=17))
## I0Etapq(I0Ecst(gs_print0_a3(1976)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1751(line=73,offs=1)--1763(line=73,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print0_a3(1976), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1853(line=75,offs=1)--2020(line=84,offs=21)))
## T1IMPallx(gs_print0_a3(1976)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8303],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8304],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[8305],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print0_a3(1976);$list(@(x0[5041],T2Pvar(x0[8303])),@(x1[5042],T2Pvar(x1[8304])),@(x2[5043],T2Pvar(x2[8305])))))))
def pyxtnm470(arg1, arg2, arg3): ## timp: gs_print0_a3(1976)
  pyxtnm167 = arg1
  pyxtnm168 = arg2
  pyxtnm169 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1924(line=81,offs=3)--1937(line=81,offs=16))
  ## I0Etapq(I0Ecst(gs_print0$beg(1970)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1430(line=43,offs=1)--1443(line=43,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print0$beg(1970), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1436(line=42,offs=1)--1475(line=44,offs=21)))
  ## T1IMPallx(gs_print0$beg(1970)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$beg(1970);$list()))))
  def pyxtnm171(): ## timp: gs_print0$beg(1970)
    ## I1CMP:start
    pyxtnm170 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(170))
    return pyxtnm170
  ## endtimp(gs_print0$beg(1970))
  pyxtnm172 = XATSDAPP(pyxtnm171())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1945(line=82,offs=3)--1953(line=82,offs=11))
  ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[8303])))))
  ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  pyxtnm179 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm178 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm177(arg1): ## timp: strn_print(1040)
    pyxtnm173 = arg1
    ## I1CMP:start
    ## let
    pyxtnm176 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(174);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(174))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm175 = XATSDAPP(XATS2PY_strn_print(pyxtnm173))
    pyxtnm176 = pyxtnm175
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(176))
    return pyxtnm176
  ## endtimp(strn_print(1040))
  pyxtnm178 = pyxtnm177
  pyxtnm179 = pyxtnm178
  pyxtnm180 = XATSDAPP(pyxtnm179(pyxtnm167))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1964(line=83,offs=3)--1972(line=83,offs=11))
  ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x1[8304])))))
  ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2815(line=148,offs=1)--2899(line=154,offs=2)))
  ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8497])))))))))
  def pyxtnm457(arg1): ## timp: g_print0(1411)
    pyxtnm181 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2865(line=153,offs=1)--2876(line=153,offs=12))
    ## I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[8497]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[8497])))))
    ## T1IMPallx(gseq_print0(1686), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    ## T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    def pyxtnm455(arg1): ## timp: gseq_print0(1686)
      pyxtnm182 = arg1
      ## I1CMP:start
      ## let
      pyxtnm454 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
      ## I1VALDCL
      pyxtnm191 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm187(arg1): ## timp: strn_print(1040)
        pyxtnm183 = arg1
        ## I1CMP:start
        ## let
        pyxtnm186 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(184);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(184))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm185 = XATSDAPP(XATS2PY_strn_print(pyxtnm183))
        pyxtnm186 = pyxtnm185
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(186))
        return pyxtnm186
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8496])))),@(x0[1068],T2Pvar(x0[8496])))))))
      def pyxtnm188(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("list_vt(")
      ## endtimp(gseq$beg(346))
      pyxtnm189 = XATSDAPP(pyxtnm188())
      pyxtnm190 = XATSDAPP(pyxtnm187(pyxtnm189))
      pyxtnm191 = pyxtnm190
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
      ## I1VALDCL
      pyxtnm444 = None
      ## let
      pyxtnm443 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
      ## I1VALDCL
      pyxtnm200 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
      ## I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$prlen(350), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
      ## T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
      def pyxtnm198(): ## timp: gseq$prlen(350)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
        ## I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
        ## T1IMPallx(sint_neg(923), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
        ## T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
        def pyxtnm196(arg1): ## timp: sint_neg(923)
          pyxtnm192 = arg1
          ## I1CMP:start
          ## let
          pyxtnm195 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_neg(2612));$list(I1FUNDCL(XATS2PY_sint_neg(4857);$list(FJARGdarg($list(I1BNDcons(I1TNM(193);I0Pvar(i1(4858));$list(@(i1(4858),I1Vtnm(I1TNM(193))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_neg);G1Nlist($list())))))))
          pyxtnm194 = XATSDAPP(XATS2PY_sint_neg(pyxtnm192))
          pyxtnm195 = pyxtnm194
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(195))
          return pyxtnm195
        ## endtimp(sint_neg(923))
        pyxtnm197 = XATSDAPP(pyxtnm196(XATSINT1(1)))
        ## I1CMP:return:I1Vtnm(I1TNM(197))
        return pyxtnm197
      ## endtimp(gseq$prlen(350))
      pyxtnm199 = XATSDAPP(pyxtnm198())
      pyxtnm200 = pyxtnm199
      XATS000_patck(True)
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm233(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm227 = arg1
        pyxtnm228 = arg2
        ## I1CMP:start
        ## let
        pyxtnm232 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(229);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(229))))),I1BNDcons(I1TNM(230);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(230))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm231 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm227, pyxtnm228))
        pyxtnm232 = pyxtnm231
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(232))
        return pyxtnm232
      ## endtimp(sint_gte$sint(931))
      pyxtnm234 = XATSDAPP(pyxtnm233(pyxtnm200, XATSINT1(0)))
      pyxtnm442 = None
      if (pyxtnm234):
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
        ## I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
        ## T1IMPallx(g_void(22), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
        ## T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
        def pyxtnm237(arg1): ## timp: g_void(22)
          pyxtnm235 = arg1
          ## I1CMP:start
          pyxtnm236 = XATSTUP0([])
          ## I1CMP:return:I1Vtnm(I1TNM(236))
          return pyxtnm236
        ## endtimp(g_void(22))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
        ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
        def pyxtnm341(arg1): ## timp: gseq_iforall0(1735)
          pyxtnm238 = arg1
          ## I1CMP:start
          ## let
          pyxtnm340 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm239 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
          ## I1VALDCL
          pyxtnm240 = None
          pyxtnm240 = XATSADDR(pyxtnm239)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
          ## I1VALDCL
          pyxtnm339 = None
          ## let
          pyxtnm338 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
          ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
          ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
          pyxtnm336 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
          ## T1IMPallx(list_vt_forall0(2062), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
          ## T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8837],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8837])))))))
          def pyxtnm335(arg1): ## timp: list_vt_forall0(2062)
            pyxtnm249 = arg1
            ## I1CMP:start
            ## let
            pyxtnm334 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
            ## I1FUNDCL
            def test_2076(arg1): ## fun
              pyxtnm250 = arg1
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
              ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8837])))))
              ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
              ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              def pyxtnm326(arg1): ## timp: forall$test0(1422)
                pyxtnm251 = arg1
                ## I1CMP:start
                ## let
                pyxtnm325 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                ## I1VALDCL
                pyxtnm256 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                def pyxtnm254(arg1): ## timp: p2tr_get(2309)
                  pyxtnm252 = arg1
                  ## I1CMP:start
                  pyxtnm253 = XATS000_dp2tr(pyxtnm252)
                  ## I1CMP:return:I1Vtnm(I1TNM(253))
                  return pyxtnm253
                ## endtimp(p2tr_get(2309))
                pyxtnm255 = XATSDAPP(pyxtnm254(pyxtnm240))
                pyxtnm256 = pyxtnm255
                XATS000_patck(True)
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                ## I1VALDCL
                pyxtnm312 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                def pyxtnm310(arg1, arg2): ## timp: iforall$test0(1432)
                  pyxtnm257 = arg1
                  pyxtnm258 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm309 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                  ## I1VALDCL
                  pyxtnm276 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                  ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                  ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                  def pyxtnm265(arg1, arg2): ## timp: sint_gt$sint(928)
                    pyxtnm259 = arg1
                    pyxtnm260 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm264 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(261);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(261))))),I1BNDcons(I1TNM(262);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(262))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                    pyxtnm263 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm259, pyxtnm260))
                    pyxtnm264 = pyxtnm263
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(264))
                    return pyxtnm264
                  ## endtimp(sint_gt$sint(928))
                  pyxtnm266 = XATSDAPP(pyxtnm265(pyxtnm257, XATSINT1(0)))
                  pyxtnm275 = None
                  if (pyxtnm266):
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                    def pyxtnm271(arg1): ## timp: strn_print(1040)
                      pyxtnm267 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm270 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(268);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(268))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                      pyxtnm269 = XATSDAPP(XATS2PY_strn_print(pyxtnm267))
                      pyxtnm270 = pyxtnm269
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(270))
                      return pyxtnm270
                    ## endtimp(strn_print(1040))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                    ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                    ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                    def pyxtnm272(): ## timp: gseq$sep(348)
                      ## I1CMP:start
                      ## I1CMP:return:I1Vstr(...)
                      return XATSSTRN(",")
                    ## endtimp(gseq$sep(348))
                    pyxtnm273 = XATSDAPP(pyxtnm272())
                    pyxtnm274 = XATSDAPP(pyxtnm271(pyxtnm273))
                    pyxtnm275 = pyxtnm274
                  ## else: None
                  ## end-of(if)
                  pyxtnm276 = pyxtnm275
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                  ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                  ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                  def pyxtnm283(arg1, arg2): ## timp: sint_gte$sint(931)
                    pyxtnm277 = arg1
                    pyxtnm278 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm282 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(279);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(279))))),I1BNDcons(I1TNM(280);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(280))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                    pyxtnm281 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm277, pyxtnm278))
                    pyxtnm282 = pyxtnm281
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(282))
                    return pyxtnm282
                  ## endtimp(sint_gte$sint(931))
                  pyxtnm284 = XATSDAPP(pyxtnm283(pyxtnm257, pyxtnm200))
                  pyxtnm308 = None
                  if (pyxtnm284):
                    ## let
                    pyxtnm299 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                    ## I1VALDCL
                    pyxtnm289 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                    ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                    ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                    def pyxtnm287(arg1): ## timp: g_free(23)
                      pyxtnm285 = arg1
                      ## I1CMP:start
                      pyxtnm286 = XATSTUP0([])
                      ## I1CMP:return:I1Vtnm(I1TNM(286))
                      return pyxtnm286
                    ## endtimp(g_free(23))
                    pyxtnm288 = XATSDAPP(pyxtnm287(pyxtnm258))
                    pyxtnm289 = pyxtnm288
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                    ## I1VALDCL
                    pyxtnm298 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                    def pyxtnm294(arg1): ## timp: strn_print(1040)
                      pyxtnm290 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm293 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(291);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(291))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                      pyxtnm292 = XATSDAPP(XATS2PY_strn_print(pyxtnm290))
                      pyxtnm293 = pyxtnm292
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(293))
                      return pyxtnm293
                    ## endtimp(strn_print(1040))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                    ## I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(gseq$rst(349), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                    ## T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                    def pyxtnm295(): ## timp: gseq$rst(349)
                      ## I1CMP:start
                      ## I1CMP:return:I1Vstr(...)
                      return XATSSTRN("...")
                    ## endtimp(gseq$rst(349))
                    pyxtnm296 = XATSDAPP(pyxtnm295())
                    pyxtnm297 = XATSDAPP(pyxtnm294(pyxtnm296))
                    pyxtnm298 = pyxtnm297
                    XATS000_patck(True)
                    pyxtnm299 = XATSBOOL(False)
                    ## end-of(let)
                    pyxtnm308 = pyxtnm299
                  else:
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                    ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                    ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                    pyxtnm306 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                    pyxtnm305 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                    ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                    ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                    def pyxtnm304(arg1): ## timp: sint_print(922)
                      pyxtnm300 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm303 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(301);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(301))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                      pyxtnm302 = XATSDAPP(XATS2PY_sint_print(pyxtnm300))
                      pyxtnm303 = pyxtnm302
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(303))
                      return pyxtnm303
                    ## endtimp(sint_print(922))
                    pyxtnm305 = pyxtnm304
                    pyxtnm306 = pyxtnm305
                    pyxtnm307 = XATSDAPP(pyxtnm306(pyxtnm258))
                    pyxtnm308 = XATSBOOL(True)
                  ## end-of(if)
                  pyxtnm309 = pyxtnm308
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(309))
                  return pyxtnm309
                ## endtimp(iforall$test0(1432))
                pyxtnm311 = XATSDAPP(pyxtnm310(pyxtnm256, pyxtnm251))
                pyxtnm312 = pyxtnm311
                XATS000_patck(True)
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                def pyxtnm315(arg1, arg2): ## timp: p2tr_set(2310)
                  pyxtnm313 = arg1
                  pyxtnm314 = arg2
                  ## I1CMP:start
                  XATS000_assgn(pyxtnm313, pyxtnm314)
                  ## I1CMP:return:I1V000()
                  return XATSVOID
                ## endtimp(p2tr_set(2310))
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                def pyxtnm322(arg1, arg2): ## timp: sint_add$sint(936)
                  pyxtnm316 = arg1
                  pyxtnm317 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm321 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(318);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(318))))),I1BNDcons(I1TNM(319);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(319))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                  pyxtnm320 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm316, pyxtnm317))
                  pyxtnm321 = pyxtnm320
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(321))
                  return pyxtnm321
                ## endtimp(sint_add$sint(936))
                pyxtnm323 = XATSDAPP(pyxtnm322(pyxtnm256, XATSINT1(1)))
                pyxtnm324 = XATSDAPP(pyxtnm315(pyxtnm240, pyxtnm323))
                pyxtnm325 = pyxtnm312
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(325))
                return pyxtnm325
              ## endtimp(forall$test0(1422))
              pyxtnm327 = XATSDAPP(pyxtnm326(pyxtnm250))
              ## I1CMP:return:I1Vtnm(I1TNM(327))
              return pyxtnm327
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
            ## I1FUNDCL
            def free_2128(arg1): ## fun
              pyxtnm328 = arg1
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
              ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8837])))))
              ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
              ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
              def pyxtnm331(arg1): ## timp: g_free(23)
                pyxtnm329 = arg1
                ## I1CMP:start
                pyxtnm330 = XATSTUP0([])
                ## I1CMP:return:I1Vtnm(I1TNM(330))
                return pyxtnm330
              ## endtimp(g_free(23))
              pyxtnm332 = XATSDAPP(pyxtnm331(pyxtnm328))
              ## I1CMP:return:I1Vtnm(I1TNM(332))
              return pyxtnm332
            pyxtnm333 = XATSDAPP(XATS2PY_list_vt_forall0_f1un(pyxtnm249, test_2076, free_2128))
            pyxtnm334 = pyxtnm333
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(334))
            return pyxtnm334
          ## endtimp(list_vt_forall0(2062))
          pyxtnm336 = pyxtnm335
          pyxtnm337 = XATSDAPP(pyxtnm336(pyxtnm238))
          pyxtnm338 = pyxtnm337
          ## end-of(let)
          pyxtnm339 = pyxtnm338
          XATS000_patck(True)
          pyxtnm340 = pyxtnm339
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(340))
          return pyxtnm340
        ## endtimp(gseq_iforall0(1735))
        pyxtnm342 = XATSDAPP(pyxtnm341(pyxtnm182))
        pyxtnm343 = XATSDAPP(pyxtnm237(pyxtnm342))
        pyxtnm442 = pyxtnm343
      else:
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforitm0(1759), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
        ## T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
        def pyxtnm440(arg1): ## timp: gseq_iforitm0(1759)
          pyxtnm344 = arg1
          ## I1CMP:start
          ## let
          pyxtnm439 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
          ## let
          pyxtnm438 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
          ## I1VALDCL
          pyxtnm437 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
          ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
          ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
          def pyxtnm435(arg1): ## timp: gseq_iforall0(1735)
            pyxtnm350 = arg1
            ## I1CMP:start
            ## let
            pyxtnm434 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm351 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
            ## I1VALDCL
            pyxtnm352 = None
            pyxtnm352 = XATSADDR(pyxtnm351)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
            ## I1VALDCL
            pyxtnm433 = None
            ## let
            pyxtnm432 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
            ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
            ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
            pyxtnm430 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
            ## I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
            ## T1IMPallx(list_vt_forall0(2062), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
            ## T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8837],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8837])))))))
            def pyxtnm429(arg1): ## timp: list_vt_forall0(2062)
              pyxtnm361 = arg1
              ## I1CMP:start
              ## let
              pyxtnm428 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
              ## I1FUNDCL
              def test_2076(arg1): ## fun
                pyxtnm362 = arg1
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8837])))))
                ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                def pyxtnm420(arg1): ## timp: forall$test0(1422)
                  pyxtnm363 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm419 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                  ## I1VALDCL
                  pyxtnm368 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                  ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                  ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                  ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                  def pyxtnm366(arg1): ## timp: p2tr_get(2309)
                    pyxtnm364 = arg1
                    ## I1CMP:start
                    pyxtnm365 = XATS000_dp2tr(pyxtnm364)
                    ## I1CMP:return:I1Vtnm(I1TNM(365))
                    return pyxtnm365
                  ## endtimp(p2tr_get(2309))
                  pyxtnm367 = XATSDAPP(pyxtnm366(pyxtnm352))
                  pyxtnm368 = pyxtnm367
                  XATS000_patck(True)
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                  ## I1VALDCL
                  pyxtnm406 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                  ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                  ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                  ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm404(arg1, arg2): ## timp: iforall$test0(1432)
                    pyxtnm369 = arg1
                    pyxtnm370 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm403 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                    ## I1VALDCL
                    pyxtnm402 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                    ## I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                    ## T1IMPallx(iforitm$work0(1448), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                    ## T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm400(arg1, arg2): ## timp: iforitm$work0(1448)
                      pyxtnm371 = arg1
                      pyxtnm372 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm399 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                      ## I1VALDCL
                      pyxtnm390 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                      ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                      ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                      def pyxtnm379(arg1, arg2): ## timp: sint_gt$sint(928)
                        pyxtnm373 = arg1
                        pyxtnm374 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm378 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(375);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(375))))),I1BNDcons(I1TNM(376);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(376))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                        pyxtnm377 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm373, pyxtnm374))
                        pyxtnm378 = pyxtnm377
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(378))
                        return pyxtnm378
                      ## endtimp(sint_gt$sint(928))
                      pyxtnm380 = XATSDAPP(pyxtnm379(pyxtnm371, XATSINT1(0)))
                      pyxtnm389 = None
                      if (pyxtnm380):
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                        def pyxtnm385(arg1): ## timp: strn_print(1040)
                          pyxtnm381 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm384 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(382);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(382))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                          pyxtnm383 = XATSDAPP(XATS2PY_strn_print(pyxtnm381))
                          pyxtnm384 = pyxtnm383
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(384))
                          return pyxtnm384
                        ## endtimp(strn_print(1040))
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                        ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                        ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                        ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                        def pyxtnm386(): ## timp: gseq$sep(348)
                          ## I1CMP:start
                          ## I1CMP:return:I1Vstr(...)
                          return XATSSTRN(",")
                        ## endtimp(gseq$sep(348))
                        pyxtnm387 = XATSDAPP(pyxtnm386())
                        pyxtnm388 = XATSDAPP(pyxtnm385(pyxtnm387))
                        pyxtnm389 = pyxtnm388
                      ## else: None
                      ## end-of(if)
                      pyxtnm390 = pyxtnm389
                      XATS000_patck(True)
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                      ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                      ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                      ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                      pyxtnm397 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                      pyxtnm396 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                      ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                      ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                      def pyxtnm395(arg1): ## timp: sint_print(922)
                        pyxtnm391 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm394 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(392);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(392))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                        pyxtnm393 = XATSDAPP(XATS2PY_sint_print(pyxtnm391))
                        pyxtnm394 = pyxtnm393
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(394))
                        return pyxtnm394
                      ## endtimp(sint_print(922))
                      pyxtnm396 = pyxtnm395
                      pyxtnm397 = pyxtnm396
                      pyxtnm398 = XATSDAPP(pyxtnm397(pyxtnm372))
                      pyxtnm399 = pyxtnm398
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(399))
                      return pyxtnm399
                    ## endtimp(iforitm$work0(1448))
                    pyxtnm401 = XATSDAPP(pyxtnm400(pyxtnm369, pyxtnm370))
                    pyxtnm402 = pyxtnm401
                    XATS000_patck(True)
                    pyxtnm403 = XATSBOOL(True)
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(403))
                    return pyxtnm403
                  ## endtimp(iforall$test0(1432))
                  pyxtnm405 = XATSDAPP(pyxtnm404(pyxtnm368, pyxtnm363))
                  pyxtnm406 = pyxtnm405
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                  ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                  ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                  ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                  def pyxtnm409(arg1, arg2): ## timp: p2tr_set(2310)
                    pyxtnm407 = arg1
                    pyxtnm408 = arg2
                    ## I1CMP:start
                    XATS000_assgn(pyxtnm407, pyxtnm408)
                    ## I1CMP:return:I1V000()
                    return XATSVOID
                  ## endtimp(p2tr_set(2310))
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                  ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                  ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                  def pyxtnm416(arg1, arg2): ## timp: sint_add$sint(936)
                    pyxtnm410 = arg1
                    pyxtnm411 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm415 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(412);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(412))))),I1BNDcons(I1TNM(413);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(413))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                    pyxtnm414 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm410, pyxtnm411))
                    pyxtnm415 = pyxtnm414
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(415))
                    return pyxtnm415
                  ## endtimp(sint_add$sint(936))
                  pyxtnm417 = XATSDAPP(pyxtnm416(pyxtnm368, XATSINT1(1)))
                  pyxtnm418 = XATSDAPP(pyxtnm409(pyxtnm352, pyxtnm417))
                  pyxtnm419 = pyxtnm406
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(419))
                  return pyxtnm419
                ## endtimp(forall$test0(1422))
                pyxtnm421 = XATSDAPP(pyxtnm420(pyxtnm362))
                ## I1CMP:return:I1Vtnm(I1TNM(421))
                return pyxtnm421
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
              ## I1FUNDCL
              def free_2128(arg1): ## fun
                pyxtnm422 = arg1
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8837])))))
                ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                def pyxtnm425(arg1): ## timp: g_free(23)
                  pyxtnm423 = arg1
                  ## I1CMP:start
                  pyxtnm424 = XATSTUP0([])
                  ## I1CMP:return:I1Vtnm(I1TNM(424))
                  return pyxtnm424
                ## endtimp(g_free(23))
                pyxtnm426 = XATSDAPP(pyxtnm425(pyxtnm422))
                ## I1CMP:return:I1Vtnm(I1TNM(426))
                return pyxtnm426
              pyxtnm427 = XATSDAPP(XATS2PY_list_vt_forall0_f1un(pyxtnm361, test_2076, free_2128))
              pyxtnm428 = pyxtnm427
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(428))
              return pyxtnm428
            ## endtimp(list_vt_forall0(2062))
            pyxtnm430 = pyxtnm429
            pyxtnm431 = XATSDAPP(pyxtnm430(pyxtnm350))
            pyxtnm432 = pyxtnm431
            ## end-of(let)
            pyxtnm433 = pyxtnm432
            XATS000_patck(True)
            pyxtnm434 = pyxtnm433
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(434))
            return pyxtnm434
          ## endtimp(gseq_iforall0(1735))
          pyxtnm436 = XATSDAPP(pyxtnm435(pyxtnm344))
          pyxtnm437 = pyxtnm436
          XATS000_patck(True)
          pyxtnm438 = XATSVOID
          ## end-of(let)
          pyxtnm439 = pyxtnm438
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(439))
          return pyxtnm439
        ## endtimp(gseq_iforitm0(1759))
        pyxtnm441 = XATSDAPP(pyxtnm440(pyxtnm182))
        pyxtnm442 = pyxtnm441
      ## end-of(if)
      pyxtnm443 = pyxtnm442
      ## end-of(let)
      pyxtnm444 = pyxtnm443
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
      ## I1VALDCL
      pyxtnm453 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm449(arg1): ## timp: strn_print(1040)
        pyxtnm445 = arg1
        ## I1CMP:start
        ## let
        pyxtnm448 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(446);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(446))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm447 = XATSDAPP(XATS2PY_strn_print(pyxtnm445))
        pyxtnm448 = pyxtnm447
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(448))
        return pyxtnm448
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8495])))),@(x0[1070],T2Pvar(x0[8495])))))))
      def pyxtnm450(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm451 = XATSDAPP(pyxtnm450())
      pyxtnm452 = XATSDAPP(pyxtnm449(pyxtnm451))
      pyxtnm453 = pyxtnm452
      XATS000_patck(True)
      pyxtnm454 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(454))
      return pyxtnm454
    ## endtimp(gseq_print0(1686))
    pyxtnm456 = XATSDAPP(pyxtnm455(pyxtnm181))
    ## I1CMP:return:I1Vtnm(I1TNM(456))
    return pyxtnm456
  ## endtimp(g_print0(1411))
  pyxtnm458 = XATSDAPP(pyxtnm457(pyxtnm168))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1982(line=83,offs=21)--1990(line=83,offs=29))
  ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x2[8305])))))
  ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  pyxtnm465 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm464 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm463(arg1): ## timp: strn_print(1040)
    pyxtnm459 = arg1
    ## I1CMP:start
    ## let
    pyxtnm462 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(460);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(460))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm461 = XATSDAPP(XATS2PY_strn_print(pyxtnm459))
    pyxtnm462 = pyxtnm461
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(462))
    return pyxtnm462
  ## endtimp(strn_print(1040))
  pyxtnm464 = pyxtnm463
  pyxtnm465 = pyxtnm464
  pyxtnm466 = XATSDAPP(pyxtnm465(pyxtnm169))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(2002(line=84,offs=3)--2015(line=84,offs=16))
  ## I0Etapq(I0Ecst(gs_print0$end(1971)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1466(line=46,offs=1)--1479(line=46,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print0$end(1971), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1479(line=46,offs=1)--1518(line=48,offs=21)))
  ## T1IMPallx(gs_print0$end(1971)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$end(1971);$list()))))
  def pyxtnm468(): ## timp: gs_print0$end(1971)
    ## I1CMP:start
    pyxtnm467 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(467))
    return pyxtnm467
  ## endtimp(gs_print0$end(1971))
  pyxtnm469 = XATSDAPP(pyxtnm468())
  ## I1CMP:return:I1Vtnm(I1TNM(469))
  return pyxtnm469
## endtimp(gs_print0_a3(1976))
pyxtnm471 = XATSDAPP(pyxtnm470(XATSSTRN("ns = "), pyxtnm166, XATSSTRN("\n")))
pyxtnm472 = pyxtnm471
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(703(line=48,offs=1)--742(line=50,offs=18)))
## I1VALDCL
pyxtnm537 = None
## LCSRCsome1(test09_llist00.dats)@(712(line=49,offs=1)--724(line=49,offs=13))
## I0Etapq(I0Ecst(list_vt_make_nfun(2038)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(3083(line=156,offs=1)--3100(line=156,offs=18))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(list_vt_make_nfun(2038), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2448(line=120,offs=1)--2509(line=123,offs=23)))
## T1IMPallx(list_vt_make_nfun(2038)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8493],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_make_nfun(2038);$list(@(a[5245],T2Pvar(a[8493])))))))
pyxtnm533 = None
## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2487(line=123,offs=1)--2506(line=123,offs=20))
## I0Etapq(I0Ecst(nint_map$f1un_llist(969)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3824(line=192,offs=1)--3843(line=192,offs=20))));$list(T2JAG($list(T2Pvar(a[8493])))))
## T1IMPallx(nint_map$f1un_llist(969), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7232(line=482,offs=1)--7375(line=492,offs=2)))
## T1IMPallx(nint_map$f1un_llist(969)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map$f1un_llist(969);$list(@(y0[2872],T2Pvar(y0[7247])))))))
def pyxtnm532(arg1, arg2): ## timp: nint_map$f1un_llist(969)
  pyxtnm473 = arg1
  pyxtnm474 = arg2
  ## I1CMP:start
  ## let
  pyxtnm531 = None
  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
  ## I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Pvar(y0[7247]))))):timp
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7288(line=487,offs=1)--7302(line=487,offs=15))
  ## I0Etapq(I0Ecst(nint_map_llist(968)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint001.sats)@(3756(line=187,offs=1)--3770(line=187,offs=15))));$list(T2JAG($list(T2Pvar(y0[7247])))))
  ## T1IMPallx(nint_map_llist(968), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6864(line=449,offs=1)--7193(line=480,offs=2)))
  ## T1IMPallx(nint_map_llist(968)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7246],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(nint_map_llist(968);$list(@(y0[2870],T2Pvar(y0[7246])))))))
  def pyxtnm529(arg1): ## timp: nint_map_llist(968)
    pyxtnm477 = arg1
    ## I1CMP:start
    ## let
    pyxtnm528 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6958(line=459,offs=1)--6983(line=460,offs=17))
    ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(ys;S2Eapps(S2Ecst(list_vt);$list(S2Evar(y0[7246])))))))
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6987(line=462,offs=1)--7009(line=463,offs=19)))
    ## I1VALDCL
    pyxtnm479 = None
    pyxtnm478 = XATSCAPP("list_vt_nil", [0])
    pyxtnm479 = pyxtnm478
    XATS000_patck(True)
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7013(line=465,offs=1)--7188(line=478,offs=2)))
    ## I1FUNDCL
    def loop_7016(arg1, arg2): ## fun
      pyxtnm480 = arg1
      pyxtnm481 = arg2
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7054(line=470,offs=5)--7056(line=470,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm488(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm482 = arg1
        pyxtnm483 = arg2
        ## I1CMP:start
        ## let
        pyxtnm487 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(484);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(484))))),I1BNDcons(I1TNM(485);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(485))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm486 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm482, pyxtnm483))
        pyxtnm487 = pyxtnm486
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(487))
        return pyxtnm487
      ## endtimp(sint_gte$sint(931))
      pyxtnm489 = XATSDAPP(pyxtnm488(pyxtnm480, pyxtnm477))
      pyxtnm506 = None
      if (pyxtnm489):
        pyxtnm506 = pyxtnm481
      else:
        ## let
        pyxtnm505 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7078(line=473,offs=1)--7107(line=473,offs=30)))
        ## I1VALDCL
        pyxtnm494 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7087(line=473,offs=10)--7095(line=473,offs=18))
        ## I0Etapq(I0Ecst(map$fopr(77)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(4030(line=256,offs=1)--4038(line=256,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Pvar(y0[7246])))))
        ## T1IMPallx(map$fopr(77), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7329(line=490,offs=1)--7373(line=491,offs=36)))
        ## T1IMPallx(map$fopr(77)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(y0[7247],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr(77);$list(@(x0[498],T2Pcst(ni)),@(y0[499],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
        def pyxtnm492(arg1): ## timp: map$fopr(77)
          pyxtnm490 = arg1
          ## I1CMP:start
          pyxtnm491 = XATSDAPP(pyxtnm474(pyxtnm490))
          ## I1CMP:return:I1Vtnm(I1TNM(491))
          return pyxtnm491
        ## endtimp(map$fopr(77))
        pyxtnm493 = XATSDAPP(pyxtnm492(pyxtnm480))
        pyxtnm494 = pyxtnm493
        XATS000_patck(True)
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(7125(line=476,offs=8)--7126(line=476,offs=9))
        ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
        ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
        ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
        def pyxtnm501(arg1, arg2): ## timp: sint_add$sint(936)
          pyxtnm495 = arg1
          pyxtnm496 = arg2
          ## I1CMP:start
          ## let
          pyxtnm500 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(497);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(497))))),I1BNDcons(I1TNM(498);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(498))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
          pyxtnm499 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm495, pyxtnm496))
          pyxtnm500 = pyxtnm499
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(500))
          return pyxtnm500
        ## endtimp(sint_add$sint(936))
        pyxtnm502 = XATSDAPP(pyxtnm501(pyxtnm480, XATSINT1(1)))
        pyxtnm503 = XATSCAPP("list_vt_cons", [1, pyxtnm494, pyxtnm481])
        pyxtnm504 = XATSDAPP(loop_7016(pyxtnm502, pyxtnm503))
        pyxtnm505 = pyxtnm504
        ## end-of(let)
        pyxtnm506 = pyxtnm505
      ## end-of(if)
      ## I1CMP:return:I1Vtnm(I1TNM(506))
      return pyxtnm506
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint001.dats)@(6911(line=454,offs=1)--6927(line=454,offs=17))
    ## I0Etapq(I0Ecst(list_vt_reverse0(2046)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4474(line=255,offs=1)--4490(line=255,offs=17))));$list(T2JAG($list(T2Pvar(y0[7246])))))
    ## T1IMPallx(list_vt_reverse0(2046), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7033(line=475,offs=1)--7120(line=478,offs=46)))
    ## T1IMPallx(list_vt_reverse0(2046)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8528],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_reverse0(2046);$list(@(x0[5264],T2Pvar(a[8528])))))))
    def pyxtnm525(arg1): ## timp: list_vt_reverse0(2046)
      pyxtnm507 = arg1
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(7075(line=478,offs=1)--7092(line=478,offs=18))
      ## I0Etapq(I0Ecst(list_vt_rappend00(2049)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list000_vt.sats)@(4855(line=281,offs=1)--4872(line=281,offs=18))));$list(T2JAG($list(T2Pvar(a[8528])))))
      ## T1IMPallx(list_vt_rappend00(2049), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6363(line=426,offs=1)--6772(line=458,offs=2)))
      ## T1IMPallx(list_vt_rappend00(2049)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8524],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_rappend00(2049);$list(@(x0[5271],T2Pvar(a[8524])))))))
      def pyxtnm522(arg1, arg2): ## timp: list_vt_rappend00(2049)
        pyxtnm508 = arg1
        pyxtnm509 = arg2
        ## I1CMP:start
        ## let
        pyxtnm521 = None
        ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6442(line=434,offs=1)--6733(line=456,offs=2)))
        ## I1FUNDCL
        def loop_6445(arg1, arg2): ## fun
          pyxtnm510 = arg1
          pyxtnm511 = arg2
          ## I1CMP:start
          pyxtnm519 = None
          while True: ## do {
            ## { // cls
            ## I1GPTpat(I1BNDcons(I1TNM(512);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
            if (XATS000_ctgeq(pyxtnm510, XATSCTAG("list_vt_nil",0))): ## { // gpt
              pyxtnm512 = pyxtnm510
              pyxtnm519 = pyxtnm511
              break ## cls
            ## } // gpt
            ## } // cls
            ## { // cls
            ## I1GPTpat(I1BNDcons(I1TNM(513);I0Pflat(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pany(),I0Pany())));$list()))
            if (XATS000_ctgeq(pyxtnm510, XATSCTAG("list_vt_cons",1))): ## { // gpt
              pyxtnm513 = pyxtnm510
              ## let
              pyxtnm518 = None
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6616(line=450,offs=3)--6631(line=450,offs=18)))
              ## I1VALDCL
              pyxtnm515 = None
              pyxtnm514 = XATSPCON(pyxtnm510,1)
              pyxtnm515 = pyxtnm514
              XATS000_patck(True)
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(6634(line=451,offs=3)--6656(line=451,offs=25)))
              ## I1VALDCL
              pyxtnm516 = None
              XATS000_assgn(XATSLPCN(1, pyxtnm510), pyxtnm511)
              pyxtnm516 = XATSVOID
              XATS000_patck(True)
              XATS000_fold(pyxtnm510)
              pyxtnm517 = XATSDAPP(loop_6445(pyxtnm515, pyxtnm510))
              pyxtnm518 = pyxtnm517
              ## end-of(let)
              pyxtnm519 = pyxtnm518
              break ## cls
            ## } // gpt
            ## } // cls
            XATS000_cfail()
          ## } while True // end-of(do-cls)
          ## I1CMP:return:I1Vtnm(I1TNM(519))
          return pyxtnm519
        pyxtnm520 = XATSDAPP(loop_6445(pyxtnm508, pyxtnm509))
        pyxtnm521 = pyxtnm520
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(521))
        return pyxtnm521
      ## endtimp(list_vt_rappend00(2049))
      pyxtnm523 = XATSCAPP("list_vt_nil", [0])
      pyxtnm524 = XATSDAPP(pyxtnm522(pyxtnm507, pyxtnm523))
      ## I1CMP:return:I1Vtnm(I1TNM(524))
      return pyxtnm524
    ## endtimp(list_vt_reverse0(2046))
    pyxtnm526 = XATSDAPP(loop_7016(XATSINT1(0), pyxtnm479))
    pyxtnm527 = XATSDAPP(pyxtnm525(pyxtnm526))
    pyxtnm528 = pyxtnm527
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(528))
    return pyxtnm528
  ## endtimp(nint_map_llist(968))
  pyxtnm530 = XATSDAPP(pyxtnm529(pyxtnm473))
  pyxtnm531 = pyxtnm530
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(531))
  return pyxtnm531
## endtimp(nint_map$f1un_llist(969))
pyxtnm533 = pyxtnm532
def pyxtnm535(arg1): ## { // lam0(T_LAM(0))
  pyxtnm534 = arg1
  ## I1CMP:start
  ## I1CMP:return:I1Vtnm(I1TNM(534))
  return pyxtnm534
## } // end(lam0)
pyxtnm536 = XATSDAPP(pyxtnm533(XATSINT1(10), pyxtnm535))
pyxtnm537 = pyxtnm536
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(743(line=51,offs=1)--785(line=52,offs=34)))
## I1VALDCL
pyxtnm576 = None
## LCSRCsome1(test09_llist00.dats)@(752(line=52,offs=1)--763(line=52,offs=12))
## I0Etapq(I0Ecst(list_vt_maprev0$f1un(2109)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(5822(line=357,offs=1)--5842(line=357,offs=21))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(list_vt_maprev0$f1un(2109), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5904(line=371,offs=1)--6049(line=380,offs=2)))
## T1IMPallx(list_vt_maprev0$f1un(2109)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8576],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8577],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_maprev0$f1un(2109);$list(@(x0[5362],T2Pvar(x0[8576])),@(y0[5363],T2Pvar(y0[8577])))))))
def pyxtnm564(arg1, arg2): ## timp: list_vt_maprev0$f1un(2109)
  pyxtnm538 = arg1
  pyxtnm539 = arg2
  ## I1CMP:start
  ## let
  pyxtnm563 = None
  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(6008(line=379,offs=1)--6047(line=379,offs=40)))
  ## I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Pvar(x0[8576])),@(y0[3858],T2Pvar(y0[8577]))))):timp
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5971(line=377,offs=3)--5986(line=377,offs=18))
  ## I0Etapq(I0Ecst(list_vt_maprev0(2107)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(5556(line=341,offs=1)--5571(line=341,offs=16))));$list(T2JAG($list(T2Pvar(x0[8576]))),T2JAG($list(T2Pvar(y0[8577])))))
  ## T1IMPallx(list_vt_maprev0(2107), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5474(line=335,offs=1)--5860(line=369,offs=2)))
  ## T1IMPallx(list_vt_maprev0(2107)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8572],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8573],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_maprev0(2107);$list(@(x0[5356],T2Pvar(x0[8572])),@(y0[5357],T2Pvar(y0[8573])))))))
  def pyxtnm561(arg1): ## timp: list_vt_maprev0(2107)
    pyxtnm542 = arg1
    ## I1CMP:start
    ## let
    pyxtnm560 = None
    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5586(line=347,offs=1)--5855(line=367,offs=2)))
    ## I1FUNDCL
    def loop_5589(arg1, arg2): ## fun
      pyxtnm543 = arg1
      pyxtnm544 = arg2
      ## I1CMP:start
      pyxtnm555 = None
      while True: ## do {
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(545);I0Pfree(I0Pdapp(I0Pcon(list_vt_nil(10));$list()));$list()))
        if (XATS000_ctgeq(pyxtnm543, XATSCTAG("list_vt_nil",0))): ## { // gpt
          pyxtnm545 = pyxtnm543
          pyxtnm555 = pyxtnm544
          break ## cls
        ## } // gpt
        ## } // cls
        ## { // cls
        ## I1GPTpat(I1BNDcons(I1TNM(546);I0Pfree(I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x0(4384)),I0Pvar(xs(4385)))));$list(@(x0(4384),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(546));0)),@(xs(4385),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(546));1)))))
        if (XATS000_ctgeq(pyxtnm543, XATSCTAG("list_vt_cons",1))): ## { // gpt
          pyxtnm546 = pyxtnm543
          ## let
          pyxtnm554 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5748(line=362,offs=3)--5780(line=363,offs=24)))
          ## I1VALDCL
          pyxtnm551 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5759(line=363,offs=3)--5768(line=363,offs=12))
          ## I0Etapq(I0Ecst(map$fopr0(1484)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(5345(line=363,offs=1)--5354(line=363,offs=10))));$list(T2JAG($list(T2Pvar(x0[8572]))),T2JAG($list(T2Pvar(y0[8573])))))
          ## T1IMPallx(map$fopr0(1484), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(6008(line=379,offs=1)--6047(line=379,offs=40)))
          ## T1IMPallx(map$fopr0(1484)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8576],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8577],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(map$fopr0(1484);$list(@(x0[3857],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[3858],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
          def pyxtnm549(arg1): ## timp: map$fopr0(1484)
            pyxtnm547 = arg1
            ## I1CMP:start
            pyxtnm548 = XATSDAPP(pyxtnm539(pyxtnm547))
            ## I1CMP:return:I1Vtnm(I1TNM(548))
            return pyxtnm548
          ## endtimp(map$fopr0(1484))
          pyxtnm550 = XATSDAPP(pyxtnm549(XATSP1CN("list_vt_cons", pyxtnm546[0+1])))
          pyxtnm551 = pyxtnm550
          XATS000_patck(True)
          pyxtnm552 = XATSCAPP("list_vt_cons", [1, pyxtnm551, pyxtnm544])
          pyxtnm553 = XATSDAPP(loop_5589(XATSP1CN("list_vt_cons", pyxtnm546[1+1]), pyxtnm552))
          pyxtnm554 = pyxtnm553
          ## end-of(let)
          pyxtnm555 = pyxtnm554
          break ## cls
        ## } // gpt
        ## } // cls
        XATS000_cfail()
      ## } while True // end-of(do-cls)
      ## I1CMP:return:I1Vtnm(I1TNM(555))
      return pyxtnm555
    ## let
    pyxtnm559 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(5525(line=341,offs=1)--5547(line=342,offs=14)))
    ## I1VALDCL
    pyxtnm557 = None
    pyxtnm556 = XATSCAPP("list_vt_nil", [0])
    pyxtnm557 = pyxtnm556
    XATS000_patck(True)
    pyxtnm558 = XATSDAPP(loop_5589(pyxtnm542, pyxtnm557))
    pyxtnm559 = pyxtnm558
    ## end-of(let)
    pyxtnm560 = pyxtnm559
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(560))
    return pyxtnm560
  ## endtimp(list_vt_maprev0(2107))
  pyxtnm562 = XATSDAPP(pyxtnm561(pyxtnm538))
  pyxtnm563 = pyxtnm562
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(563))
  return pyxtnm563
## endtimp(list_vt_maprev0$f1un(2109))
def pyxtnm574(arg1): ## { // lam0(T_LAM(0))
  pyxtnm565 = arg1
  ## I1CMP:start
  ## LCSRCsome1(test09_llist00.dats)@(782(line=52,offs=31)--783(line=52,offs=32))
  ## I0Etapq(I0Ecst(sint_mul$sint(938)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3211(line=150,offs=1)--3224(line=150,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(sint_mul$sint(938), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3013(line=173,offs=1)--3177(line=185,offs=2)))
  ## T1IMPallx(sint_mul$sint(938)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_mul$sint(938);$list()))))
  def pyxtnm572(arg1, arg2): ## timp: sint_mul$sint(938)
    pyxtnm566 = arg1
    pyxtnm567 = arg2
    ## I1CMP:start
    ## let
    pyxtnm571 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3103(line=181,offs=1)--3175(line=184,offs=39)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_mul$sint(2621));$list(I1FUNDCL(XATS2PY_sint_mul$sint(4901);$list(FJARGdarg($list(I1BNDcons(I1TNM(568);I0Pvar(i1(4902));$list(@(i1(4902),I1Vtnm(I1TNM(568))))),I1BNDcons(I1TNM(569);I0Pvar(i2(4903));$list(@(i2(4903),I1Vtnm(I1TNM(569))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_mul$sint);G1Nlist($list())))))))
    pyxtnm570 = XATSDAPP(XATS2PY_sint_mul_sint(pyxtnm566, pyxtnm567))
    pyxtnm571 = pyxtnm570
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(571))
    return pyxtnm571
  ## endtimp(sint_mul$sint(938))
  pyxtnm573 = XATSDAPP(pyxtnm572(pyxtnm565, pyxtnm565))
  ## I1CMP:return:I1Vtnm(I1TNM(573))
  return pyxtnm573
## } // end(lam0)
pyxtnm575 = XATSDAPP(pyxtnm564(pyxtnm537, pyxtnm574))
pyxtnm576 = pyxtnm575
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test09_llist00.dats)@(786(line=53,offs=1)--821(line=53,offs=36)))
## I1VALDCL
pyxtnm882 = None
## LCSRCsome1(test09_llist00.dats)@(795(line=53,offs=10)--802(line=53,offs=17))
## I0Etapq(I0Ecst(gs_print0_a3(1976)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1751(line=73,offs=1)--1763(line=73,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print0_a3(1976), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1853(line=75,offs=1)--2020(line=84,offs=21)))
## T1IMPallx(gs_print0_a3(1976)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8303],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8304],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[8305],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print0_a3(1976);$list(@(x0[5041],T2Pvar(x0[8303])),@(x1[5042],T2Pvar(x1[8304])),@(x2[5043],T2Pvar(x2[8305])))))))
def pyxtnm880(arg1, arg2, arg3): ## timp: gs_print0_a3(1976)
  pyxtnm577 = arg1
  pyxtnm578 = arg2
  pyxtnm579 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1924(line=81,offs=3)--1937(line=81,offs=16))
  ## I0Etapq(I0Ecst(gs_print0$beg(1970)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1430(line=43,offs=1)--1443(line=43,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print0$beg(1970), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1436(line=42,offs=1)--1475(line=44,offs=21)))
  ## T1IMPallx(gs_print0$beg(1970)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$beg(1970);$list()))))
  def pyxtnm581(): ## timp: gs_print0$beg(1970)
    ## I1CMP:start
    pyxtnm580 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(580))
    return pyxtnm580
  ## endtimp(gs_print0$beg(1970))
  pyxtnm582 = XATSDAPP(pyxtnm581())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1945(line=82,offs=3)--1953(line=82,offs=11))
  ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[8303])))))
  ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  pyxtnm589 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
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
  pyxtnm589 = pyxtnm588
  pyxtnm590 = XATSDAPP(pyxtnm589(pyxtnm577))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1964(line=83,offs=3)--1972(line=83,offs=11))
  ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x1[8304])))))
  ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2815(line=148,offs=1)--2899(line=154,offs=2)))
  ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8497])))))))))
  def pyxtnm867(arg1): ## timp: g_print0(1411)
    pyxtnm591 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2865(line=153,offs=1)--2876(line=153,offs=12))
    ## I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[8497]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[8497])))))
    ## T1IMPallx(gseq_print0(1686), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    ## T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    def pyxtnm865(arg1): ## timp: gseq_print0(1686)
      pyxtnm592 = arg1
      ## I1CMP:start
      ## let
      pyxtnm864 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
      ## I1VALDCL
      pyxtnm601 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm597(arg1): ## timp: strn_print(1040)
        pyxtnm593 = arg1
        ## I1CMP:start
        ## let
        pyxtnm596 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(594);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(594))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm595 = XATSDAPP(XATS2PY_strn_print(pyxtnm593))
        pyxtnm596 = pyxtnm595
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(596))
        return pyxtnm596
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8496],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8496])))),@(x0[1068],T2Pvar(x0[8496])))))))
      def pyxtnm598(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("list_vt(")
      ## endtimp(gseq$beg(346))
      pyxtnm599 = XATSDAPP(pyxtnm598())
      pyxtnm600 = XATSDAPP(pyxtnm597(pyxtnm599))
      pyxtnm601 = pyxtnm600
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
      ## I1VALDCL
      pyxtnm854 = None
      ## let
      pyxtnm853 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
      ## I1VALDCL
      pyxtnm610 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
      ## I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$prlen(350), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
      ## T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
      def pyxtnm608(): ## timp: gseq$prlen(350)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
        ## I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
        ## T1IMPallx(sint_neg(923), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
        ## T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
        def pyxtnm606(arg1): ## timp: sint_neg(923)
          pyxtnm602 = arg1
          ## I1CMP:start
          ## let
          pyxtnm605 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_neg(2612));$list(I1FUNDCL(XATS2PY_sint_neg(4857);$list(FJARGdarg($list(I1BNDcons(I1TNM(603);I0Pvar(i1(4858));$list(@(i1(4858),I1Vtnm(I1TNM(603))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_neg);G1Nlist($list())))))))
          pyxtnm604 = XATSDAPP(XATS2PY_sint_neg(pyxtnm602))
          pyxtnm605 = pyxtnm604
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(605))
          return pyxtnm605
        ## endtimp(sint_neg(923))
        pyxtnm607 = XATSDAPP(pyxtnm606(XATSINT1(1)))
        ## I1CMP:return:I1Vtnm(I1TNM(607))
        return pyxtnm607
      ## endtimp(gseq$prlen(350))
      pyxtnm609 = XATSDAPP(pyxtnm608())
      pyxtnm610 = pyxtnm609
      XATS000_patck(True)
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm643(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm637 = arg1
        pyxtnm638 = arg2
        ## I1CMP:start
        ## let
        pyxtnm642 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(639);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(639))))),I1BNDcons(I1TNM(640);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(640))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm641 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm637, pyxtnm638))
        pyxtnm642 = pyxtnm641
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(642))
        return pyxtnm642
      ## endtimp(sint_gte$sint(931))
      pyxtnm644 = XATSDAPP(pyxtnm643(pyxtnm610, XATSINT1(0)))
      pyxtnm852 = None
      if (pyxtnm644):
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
        ## I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
        ## T1IMPallx(g_void(22), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
        ## T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
        def pyxtnm647(arg1): ## timp: g_void(22)
          pyxtnm645 = arg1
          ## I1CMP:start
          pyxtnm646 = XATSTUP0([])
          ## I1CMP:return:I1Vtnm(I1TNM(646))
          return pyxtnm646
        ## endtimp(g_void(22))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
        ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
        def pyxtnm751(arg1): ## timp: gseq_iforall0(1735)
          pyxtnm648 = arg1
          ## I1CMP:start
          ## let
          pyxtnm750 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm649 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
          ## I1VALDCL
          pyxtnm650 = None
          pyxtnm650 = XATSADDR(pyxtnm649)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
          ## I1VALDCL
          pyxtnm749 = None
          ## let
          pyxtnm748 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
          ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
          ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
          pyxtnm746 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
          ## T1IMPallx(list_vt_forall0(2062), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
          ## T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8837],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8837])))))))
          def pyxtnm745(arg1): ## timp: list_vt_forall0(2062)
            pyxtnm659 = arg1
            ## I1CMP:start
            ## let
            pyxtnm744 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
            ## I1FUNDCL
            def test_2076(arg1): ## fun
              pyxtnm660 = arg1
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
              ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8837])))))
              ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
              ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
              def pyxtnm736(arg1): ## timp: forall$test0(1422)
                pyxtnm661 = arg1
                ## I1CMP:start
                ## let
                pyxtnm735 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                ## I1VALDCL
                pyxtnm666 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                def pyxtnm664(arg1): ## timp: p2tr_get(2309)
                  pyxtnm662 = arg1
                  ## I1CMP:start
                  pyxtnm663 = XATS000_dp2tr(pyxtnm662)
                  ## I1CMP:return:I1Vtnm(I1TNM(663))
                  return pyxtnm663
                ## endtimp(p2tr_get(2309))
                pyxtnm665 = XATSDAPP(pyxtnm664(pyxtnm650))
                pyxtnm666 = pyxtnm665
                XATS000_patck(True)
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                ## I1VALDCL
                pyxtnm722 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                def pyxtnm720(arg1, arg2): ## timp: iforall$test0(1432)
                  pyxtnm667 = arg1
                  pyxtnm668 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm719 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                  ## I1VALDCL
                  pyxtnm686 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                  ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                  ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                  def pyxtnm675(arg1, arg2): ## timp: sint_gt$sint(928)
                    pyxtnm669 = arg1
                    pyxtnm670 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm674 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(671);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(671))))),I1BNDcons(I1TNM(672);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(672))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                    pyxtnm673 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm669, pyxtnm670))
                    pyxtnm674 = pyxtnm673
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(674))
                    return pyxtnm674
                  ## endtimp(sint_gt$sint(928))
                  pyxtnm676 = XATSDAPP(pyxtnm675(pyxtnm667, XATSINT1(0)))
                  pyxtnm685 = None
                  if (pyxtnm676):
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                    def pyxtnm681(arg1): ## timp: strn_print(1040)
                      pyxtnm677 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm680 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(678);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(678))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                      pyxtnm679 = XATSDAPP(XATS2PY_strn_print(pyxtnm677))
                      pyxtnm680 = pyxtnm679
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(680))
                      return pyxtnm680
                    ## endtimp(strn_print(1040))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                    ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                    ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                    def pyxtnm682(): ## timp: gseq$sep(348)
                      ## I1CMP:start
                      ## I1CMP:return:I1Vstr(...)
                      return XATSSTRN(",")
                    ## endtimp(gseq$sep(348))
                    pyxtnm683 = XATSDAPP(pyxtnm682())
                    pyxtnm684 = XATSDAPP(pyxtnm681(pyxtnm683))
                    pyxtnm685 = pyxtnm684
                  ## else: None
                  ## end-of(if)
                  pyxtnm686 = pyxtnm685
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                  ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                  ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                  def pyxtnm693(arg1, arg2): ## timp: sint_gte$sint(931)
                    pyxtnm687 = arg1
                    pyxtnm688 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm692 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(689);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(689))))),I1BNDcons(I1TNM(690);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(690))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                    pyxtnm691 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm687, pyxtnm688))
                    pyxtnm692 = pyxtnm691
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(692))
                    return pyxtnm692
                  ## endtimp(sint_gte$sint(931))
                  pyxtnm694 = XATSDAPP(pyxtnm693(pyxtnm667, pyxtnm610))
                  pyxtnm718 = None
                  if (pyxtnm694):
                    ## let
                    pyxtnm709 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                    ## I1VALDCL
                    pyxtnm699 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                    ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                    ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                    def pyxtnm697(arg1): ## timp: g_free(23)
                      pyxtnm695 = arg1
                      ## I1CMP:start
                      pyxtnm696 = XATSTUP0([])
                      ## I1CMP:return:I1Vtnm(I1TNM(696))
                      return pyxtnm696
                    ## endtimp(g_free(23))
                    pyxtnm698 = XATSDAPP(pyxtnm697(pyxtnm668))
                    pyxtnm699 = pyxtnm698
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                    ## I1VALDCL
                    pyxtnm708 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                    def pyxtnm704(arg1): ## timp: strn_print(1040)
                      pyxtnm700 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm703 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(701);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(701))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                      pyxtnm702 = XATSDAPP(XATS2PY_strn_print(pyxtnm700))
                      pyxtnm703 = pyxtnm702
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(703))
                      return pyxtnm703
                    ## endtimp(strn_print(1040))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                    ## I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(gseq$rst(349), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                    ## T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                    def pyxtnm705(): ## timp: gseq$rst(349)
                      ## I1CMP:start
                      ## I1CMP:return:I1Vstr(...)
                      return XATSSTRN("...")
                    ## endtimp(gseq$rst(349))
                    pyxtnm706 = XATSDAPP(pyxtnm705())
                    pyxtnm707 = XATSDAPP(pyxtnm704(pyxtnm706))
                    pyxtnm708 = pyxtnm707
                    XATS000_patck(True)
                    pyxtnm709 = XATSBOOL(False)
                    ## end-of(let)
                    pyxtnm718 = pyxtnm709
                  else:
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                    ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                    ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                    ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                    pyxtnm716 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                    ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                    ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                    ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                    pyxtnm715 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                    ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                    ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                    def pyxtnm714(arg1): ## timp: sint_print(922)
                      pyxtnm710 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm713 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(711);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(711))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                      pyxtnm712 = XATSDAPP(XATS2PY_sint_print(pyxtnm710))
                      pyxtnm713 = pyxtnm712
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(713))
                      return pyxtnm713
                    ## endtimp(sint_print(922))
                    pyxtnm715 = pyxtnm714
                    pyxtnm716 = pyxtnm715
                    pyxtnm717 = XATSDAPP(pyxtnm716(pyxtnm668))
                    pyxtnm718 = XATSBOOL(True)
                  ## end-of(if)
                  pyxtnm719 = pyxtnm718
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(719))
                  return pyxtnm719
                ## endtimp(iforall$test0(1432))
                pyxtnm721 = XATSDAPP(pyxtnm720(pyxtnm666, pyxtnm661))
                pyxtnm722 = pyxtnm721
                XATS000_patck(True)
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                def pyxtnm725(arg1, arg2): ## timp: p2tr_set(2310)
                  pyxtnm723 = arg1
                  pyxtnm724 = arg2
                  ## I1CMP:start
                  XATS000_assgn(pyxtnm723, pyxtnm724)
                  ## I1CMP:return:I1V000()
                  return XATSVOID
                ## endtimp(p2tr_set(2310))
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                def pyxtnm732(arg1, arg2): ## timp: sint_add$sint(936)
                  pyxtnm726 = arg1
                  pyxtnm727 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm731 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(728);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(728))))),I1BNDcons(I1TNM(729);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(729))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                  pyxtnm730 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm726, pyxtnm727))
                  pyxtnm731 = pyxtnm730
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(731))
                  return pyxtnm731
                ## endtimp(sint_add$sint(936))
                pyxtnm733 = XATSDAPP(pyxtnm732(pyxtnm666, XATSINT1(1)))
                pyxtnm734 = XATSDAPP(pyxtnm725(pyxtnm650, pyxtnm733))
                pyxtnm735 = pyxtnm722
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(735))
                return pyxtnm735
              ## endtimp(forall$test0(1422))
              pyxtnm737 = XATSDAPP(pyxtnm736(pyxtnm660))
              ## I1CMP:return:I1Vtnm(I1TNM(737))
              return pyxtnm737
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
            ## I1FUNDCL
            def free_2128(arg1): ## fun
              pyxtnm738 = arg1
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
              ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8837])))))
              ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
              ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
              def pyxtnm741(arg1): ## timp: g_free(23)
                pyxtnm739 = arg1
                ## I1CMP:start
                pyxtnm740 = XATSTUP0([])
                ## I1CMP:return:I1Vtnm(I1TNM(740))
                return pyxtnm740
              ## endtimp(g_free(23))
              pyxtnm742 = XATSDAPP(pyxtnm741(pyxtnm738))
              ## I1CMP:return:I1Vtnm(I1TNM(742))
              return pyxtnm742
            pyxtnm743 = XATSDAPP(XATS2PY_list_vt_forall0_f1un(pyxtnm659, test_2076, free_2128))
            pyxtnm744 = pyxtnm743
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(744))
            return pyxtnm744
          ## endtimp(list_vt_forall0(2062))
          pyxtnm746 = pyxtnm745
          pyxtnm747 = XATSDAPP(pyxtnm746(pyxtnm648))
          pyxtnm748 = pyxtnm747
          ## end-of(let)
          pyxtnm749 = pyxtnm748
          XATS000_patck(True)
          pyxtnm750 = pyxtnm749
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(750))
          return pyxtnm750
        ## endtimp(gseq_iforall0(1735))
        pyxtnm752 = XATSDAPP(pyxtnm751(pyxtnm592))
        pyxtnm753 = XATSDAPP(pyxtnm647(pyxtnm752))
        pyxtnm852 = pyxtnm753
      else:
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforitm0(1759), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
        ## T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
        def pyxtnm850(arg1): ## timp: gseq_iforitm0(1759)
          pyxtnm754 = arg1
          ## I1CMP:start
          ## let
          pyxtnm849 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
          ## let
          pyxtnm848 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
          ## I1VALDCL
          pyxtnm847 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
          ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
          ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
          def pyxtnm845(arg1): ## timp: gseq_iforall0(1735)
            pyxtnm760 = arg1
            ## I1CMP:start
            ## let
            pyxtnm844 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm761 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
            ## I1VALDCL
            pyxtnm762 = None
            pyxtnm762 = XATSADDR(pyxtnm761)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
            ## I1VALDCL
            pyxtnm843 = None
            ## let
            pyxtnm842 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
            ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1968(line=90,offs=1)--2039(line=93,offs=40)))
            ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8545],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8545])))),@(x0[4323],T2Pvar(x0[8545])))))))
            pyxtnm840 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2020(line=93,offs=21)--2035(line=93,offs=36))
            ## I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[8545])))))
            ## T1IMPallx(list_vt_forall0(2062), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
            ## T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8837],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8837])))))))
            def pyxtnm839(arg1): ## timp: list_vt_forall0(2062)
              pyxtnm771 = arg1
              ## I1CMP:start
              ## let
              pyxtnm838 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
              ## I1FUNDCL
              def test_2076(arg1): ## fun
                pyxtnm772 = arg1
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8837])))))
                ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                def pyxtnm830(arg1): ## timp: forall$test0(1422)
                  pyxtnm773 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm829 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                  ## I1VALDCL
                  pyxtnm778 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                  ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                  ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                  ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                  def pyxtnm776(arg1): ## timp: p2tr_get(2309)
                    pyxtnm774 = arg1
                    ## I1CMP:start
                    pyxtnm775 = XATS000_dp2tr(pyxtnm774)
                    ## I1CMP:return:I1Vtnm(I1TNM(775))
                    return pyxtnm775
                  ## endtimp(p2tr_get(2309))
                  pyxtnm777 = XATSDAPP(pyxtnm776(pyxtnm762))
                  pyxtnm778 = pyxtnm777
                  XATS000_patck(True)
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                  ## I1VALDCL
                  pyxtnm816 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                  ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                  ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                  ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm814(arg1, arg2): ## timp: iforall$test0(1432)
                    pyxtnm779 = arg1
                    pyxtnm780 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm813 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                    ## I1VALDCL
                    pyxtnm812 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                    ## I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                    ## T1IMPallx(iforitm$work0(1448), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                    ## T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm810(arg1, arg2): ## timp: iforitm$work0(1448)
                      pyxtnm781 = arg1
                      pyxtnm782 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm809 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                      ## I1VALDCL
                      pyxtnm800 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                      ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                      ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                      def pyxtnm789(arg1, arg2): ## timp: sint_gt$sint(928)
                        pyxtnm783 = arg1
                        pyxtnm784 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm788 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(785);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(785))))),I1BNDcons(I1TNM(786);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(786))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                        pyxtnm787 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm783, pyxtnm784))
                        pyxtnm788 = pyxtnm787
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(788))
                        return pyxtnm788
                      ## endtimp(sint_gt$sint(928))
                      pyxtnm790 = XATSDAPP(pyxtnm789(pyxtnm781, XATSINT1(0)))
                      pyxtnm799 = None
                      if (pyxtnm790):
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                        def pyxtnm795(arg1): ## timp: strn_print(1040)
                          pyxtnm791 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm794 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(792);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(792))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                          pyxtnm793 = XATSDAPP(XATS2PY_strn_print(pyxtnm791))
                          pyxtnm794 = pyxtnm793
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(794))
                          return pyxtnm794
                        ## endtimp(strn_print(1040))
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                        ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                        ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                        ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8494],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                        def pyxtnm796(): ## timp: gseq$sep(348)
                          ## I1CMP:start
                          ## I1CMP:return:I1Vstr(...)
                          return XATSSTRN(",")
                        ## endtimp(gseq$sep(348))
                        pyxtnm797 = XATSDAPP(pyxtnm796())
                        pyxtnm798 = XATSDAPP(pyxtnm795(pyxtnm797))
                        pyxtnm799 = pyxtnm798
                      ## else: None
                      ## end-of(if)
                      pyxtnm800 = pyxtnm799
                      XATS000_patck(True)
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                      ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                      ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                      ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                      pyxtnm807 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                      ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                      ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                      ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                      pyxtnm806 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                      ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                      ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                      def pyxtnm805(arg1): ## timp: sint_print(922)
                        pyxtnm801 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm804 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(802);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(802))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                        pyxtnm803 = XATSDAPP(XATS2PY_sint_print(pyxtnm801))
                        pyxtnm804 = pyxtnm803
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(804))
                        return pyxtnm804
                      ## endtimp(sint_print(922))
                      pyxtnm806 = pyxtnm805
                      pyxtnm807 = pyxtnm806
                      pyxtnm808 = XATSDAPP(pyxtnm807(pyxtnm782))
                      pyxtnm809 = pyxtnm808
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(809))
                      return pyxtnm809
                    ## endtimp(iforitm$work0(1448))
                    pyxtnm811 = XATSDAPP(pyxtnm810(pyxtnm779, pyxtnm780))
                    pyxtnm812 = pyxtnm811
                    XATS000_patck(True)
                    pyxtnm813 = XATSBOOL(True)
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(813))
                    return pyxtnm813
                  ## endtimp(iforall$test0(1432))
                  pyxtnm815 = XATSDAPP(pyxtnm814(pyxtnm778, pyxtnm773))
                  pyxtnm816 = pyxtnm815
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                  ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                  ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                  ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                  def pyxtnm819(arg1, arg2): ## timp: p2tr_set(2310)
                    pyxtnm817 = arg1
                    pyxtnm818 = arg2
                    ## I1CMP:start
                    XATS000_assgn(pyxtnm817, pyxtnm818)
                    ## I1CMP:return:I1V000()
                    return XATSVOID
                  ## endtimp(p2tr_set(2310))
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                  ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                  ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                  ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                  def pyxtnm826(arg1, arg2): ## timp: sint_add$sint(936)
                    pyxtnm820 = arg1
                    pyxtnm821 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm825 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(822);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(822))))),I1BNDcons(I1TNM(823);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(823))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                    pyxtnm824 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm820, pyxtnm821))
                    pyxtnm825 = pyxtnm824
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(825))
                    return pyxtnm825
                  ## endtimp(sint_add$sint(936))
                  pyxtnm827 = XATSDAPP(pyxtnm826(pyxtnm778, XATSINT1(1)))
                  pyxtnm828 = XATSDAPP(pyxtnm819(pyxtnm762, pyxtnm827))
                  pyxtnm829 = pyxtnm816
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(829))
                  return pyxtnm829
                ## endtimp(forall$test0(1422))
                pyxtnm831 = XATSDAPP(pyxtnm830(pyxtnm772))
                ## I1CMP:return:I1Vtnm(I1TNM(831))
                return pyxtnm831
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
              ## I1FUNDCL
              def free_2128(arg1): ## fun
                pyxtnm832 = arg1
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8837])))))
                ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                def pyxtnm835(arg1): ## timp: g_free(23)
                  pyxtnm833 = arg1
                  ## I1CMP:start
                  pyxtnm834 = XATSTUP0([])
                  ## I1CMP:return:I1Vtnm(I1TNM(834))
                  return pyxtnm834
                ## endtimp(g_free(23))
                pyxtnm836 = XATSDAPP(pyxtnm835(pyxtnm832))
                ## I1CMP:return:I1Vtnm(I1TNM(836))
                return pyxtnm836
              pyxtnm837 = XATSDAPP(XATS2PY_list_vt_forall0_f1un(pyxtnm771, test_2076, free_2128))
              pyxtnm838 = pyxtnm837
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(838))
              return pyxtnm838
            ## endtimp(list_vt_forall0(2062))
            pyxtnm840 = pyxtnm839
            pyxtnm841 = XATSDAPP(pyxtnm840(pyxtnm760))
            pyxtnm842 = pyxtnm841
            ## end-of(let)
            pyxtnm843 = pyxtnm842
            XATS000_patck(True)
            pyxtnm844 = pyxtnm843
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(844))
            return pyxtnm844
          ## endtimp(gseq_iforall0(1735))
          pyxtnm846 = XATSDAPP(pyxtnm845(pyxtnm754))
          pyxtnm847 = pyxtnm846
          XATS000_patck(True)
          pyxtnm848 = XATSVOID
          ## end-of(let)
          pyxtnm849 = pyxtnm848
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(849))
          return pyxtnm849
        ## endtimp(gseq_iforitm0(1759))
        pyxtnm851 = XATSDAPP(pyxtnm850(pyxtnm592))
        pyxtnm852 = pyxtnm851
      ## end-of(if)
      pyxtnm853 = pyxtnm852
      ## end-of(let)
      pyxtnm854 = pyxtnm853
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
      ## I1VALDCL
      pyxtnm863 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm859(arg1): ## timp: strn_print(1040)
        pyxtnm855 = arg1
        ## I1CMP:start
        ## let
        pyxtnm858 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(856);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(856))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm857 = XATSDAPP(XATS2PY_strn_print(pyxtnm855))
        pyxtnm858 = pyxtnm857
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(858))
        return pyxtnm858
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[8495],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8495])))),@(x0[1070],T2Pvar(x0[8495])))))))
      def pyxtnm860(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm861 = XATSDAPP(pyxtnm860())
      pyxtnm862 = XATSDAPP(pyxtnm859(pyxtnm861))
      pyxtnm863 = pyxtnm862
      XATS000_patck(True)
      pyxtnm864 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(864))
      return pyxtnm864
    ## endtimp(gseq_print0(1686))
    pyxtnm866 = XATSDAPP(pyxtnm865(pyxtnm591))
    ## I1CMP:return:I1Vtnm(I1TNM(866))
    return pyxtnm866
  ## endtimp(g_print0(1411))
  pyxtnm868 = XATSDAPP(pyxtnm867(pyxtnm578))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1982(line=83,offs=21)--1990(line=83,offs=29))
  ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x2[8305])))))
  ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
  ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
  pyxtnm875 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm874 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm873(arg1): ## timp: strn_print(1040)
    pyxtnm869 = arg1
    ## I1CMP:start
    ## let
    pyxtnm872 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(870);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(870))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm871 = XATSDAPP(XATS2PY_strn_print(pyxtnm869))
    pyxtnm872 = pyxtnm871
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(872))
    return pyxtnm872
  ## endtimp(strn_print(1040))
  pyxtnm874 = pyxtnm873
  pyxtnm875 = pyxtnm874
  pyxtnm876 = XATSDAPP(pyxtnm875(pyxtnm579))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(2002(line=84,offs=3)--2015(line=84,offs=16))
  ## I0Etapq(I0Ecst(gs_print0$end(1971)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1466(line=46,offs=1)--1479(line=46,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print0$end(1971), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(1479(line=46,offs=1)--1518(line=48,offs=21)))
  ## T1IMPallx(gs_print0$end(1971)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print0$end(1971);$list()))))
  def pyxtnm878(): ## timp: gs_print0$end(1971)
    ## I1CMP:start
    pyxtnm877 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(877))
    return pyxtnm877
  ## endtimp(gs_print0$end(1971))
  pyxtnm879 = XATSDAPP(pyxtnm878())
  ## I1CMP:return:I1Vtnm(I1TNM(879))
  return pyxtnm879
## endtimp(gs_print0_a3(1976))
pyxtnm881 = XATSDAPP(pyxtnm880(XATSSTRN("ns = "), pyxtnm576, XATSSTRN("\n")))
pyxtnm882 = pyxtnm881
XATS000_patck(True)
## LCSRCsome1(test09_llist00.dats)@(1084(line=61,offs=1)--1084(line=61,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test09_llist00.dats)@(1084(line=61,offs=1)--1084(line=61,offs=1));D3Cnone0()))
