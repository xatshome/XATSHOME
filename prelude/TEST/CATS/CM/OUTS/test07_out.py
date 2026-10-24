## Thu Aug  6 10:50:01 PM EDT 2026
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
## LCSRCsome1(test07_gseq000.dats)@(106(line=8,offs=1)--146(line=9,offs=28))
## I1Di0dcl(I0Dd3ecl(D3Cstaload(1;T_SRP_STALOAD();G1Ea2pp(G1Eid0(=);G1Eid0(_);G1Estr(T_STRN1_clsd("prelude/DATS/gdbg000.dats";27)));$optn(FPATH(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats));...)))
## I1Dinclude(LCSRCsome1(test07_gseq000.dats)@(190(line=13,offs=1)--231(line=14,offs=33)))
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
## I1Dinclude(LCSRCsome1(test07_gseq000.dats)@(232(line=15,offs=1)--276(line=16,offs=36)))
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
## LCSRCsome1(test07_gseq000.dats)@(379(line=26,offs=1)--427(line=27,offs=32))
## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Cd1ecl(D1Cdefine(T_SRP_DEFINE();T_IDALP(GZ2SEQ);$list(G1MAGdarg($list(G1ARGnode(T_IDALP(xs)),G1ARGnode(T_IDALP(ys)))));$optn(G1Ea1pp(G1Eid0(GSEQ_z2make);G1Elist($list(G1Ea1pp(G1Eid0(GSEQ);G1Elist($list(G1Eid0(xs)))),G1Ea1pp(G1Eid0(GSEQ);G1Elist($list(G1Eid0(ys)))))))))))))
## LCSRCsome1(test07_gseq000.dats)@(436(line=29,offs=1)--484(line=30,offs=32))
## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Cd1ecl(D1Cdefine(T_SRP_DEFINE();T_IDALP(GX2SEQ);$list(G1MAGdarg($list(G1ARGnode(T_IDALP(xs)),G1ARGnode(T_IDALP(ys)))));$optn(G1Ea1pp(G1Eid0(GSEQ_x2make);G1Elist($list(G1Ea1pp(G1Eid0(GSEQ);G1Elist($list(G1Eid0(xs)))),G1Ea1pp(G1Eid0(GSEQ);G1Elist($list(G1Eid0(ys)))))))))))))
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(531(line=35,offs=1)--554(line=35,offs=24)))
## I1VALDCL
pyxtnm16 = None
## LCSRCsome1(test07_gseq000.dats)@(540(line=35,offs=10)--544(line=35,offs=14))
## I0Etapq(I0Ecst(list_make_t0up3(1208)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list000.sats)@(6340(line=402,offs=1)--6355(line=402,offs=16))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(list_make_t0up3(1208), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(9938(line=695,offs=1)--10048(line=702,offs=4)))
## T1IMPallx(list_make_t0up3(1208)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7467],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_make_t0up3(1208);$list(@(x0[3403],T2Pvar(x0[7467])))))))
def pyxtnm13(arg1): ## timp: list_make_t0up3(1208)
  pyxtnm1 = arg1
  ## I1CMP:start
  ## let
  pyxtnm12 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(9983(line=699,offs=1)--10005(line=699,offs=23)))
  ## I1VALDCL
  pyxtnm2 = None
  pyxtnm2 = pyxtnm1
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(10013(line=701,offs=3)--10027(line=701,offs=17))
  ## I0Etapq(I0Ecst(list_make_3val(1183)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list000.sats)@(2572(line=134,offs=1)--2586(line=134,offs=15))));$list(T2JAG($list(T2Pvar(x0[7467])))))
  ## T1IMPallx(list_make_3val(1183), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(8500(line=590,offs=1)--8607(line=596,offs=31)))
  ## T1IMPallx(list_make_3val(1183)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7457],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_make_3val(1183);$list(@(a[3345],T2Pvar(x0[7457])))))))
  def pyxtnm10(arg1, arg2, arg3): ## timp: list_make_3val(1183)
    pyxtnm3 = arg1
    pyxtnm4 = arg2
    pyxtnm5 = arg3
    ## I1CMP:start
    pyxtnm6 = XATSCAPP("list_nil", [0])
    pyxtnm7 = XATSCAPP("list_cons", [1, pyxtnm5, pyxtnm6])
    pyxtnm8 = XATSCAPP("list_cons", [1, pyxtnm4, pyxtnm7])
    pyxtnm9 = XATSCAPP("list_cons", [1, pyxtnm3, pyxtnm8])
    ## I1CMP:return:I1Vtnm(I1TNM(9))
    return pyxtnm9
  ## endtimp(list_make_3val(1183))
  pyxtnm11 = XATSDAPP(pyxtnm10(XATSP1RJ(XATSTRCD(0), pyxtnm2[0]), XATSP1RJ(XATSTRCD(0), pyxtnm2[1]), XATSP1RJ(XATSTRCD(0), pyxtnm2[2])))
  pyxtnm12 = pyxtnm11
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(12))
  return pyxtnm12
## endtimp(list_make_t0up3(1208))
pyxtnm14 = XATSTUP1(XATSTRCD(0), [XATSINT1(1), XATSINT1(2), XATSINT1(3)])
pyxtnm15 = XATSDAPP(pyxtnm13(pyxtnm14))
pyxtnm16 = pyxtnm15
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(555(line=36,offs=1)--582(line=36,offs=28)))
## I1VALDCL
pyxtnm33 = None
## LCSRCsome1(test07_gseq000.dats)@(564(line=36,offs=10)--568(line=36,offs=14))
## I0Etapq(I0Ecst(list_make_t0up4(1209)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list000.sats)@(6405(line=407,offs=1)--6420(line=407,offs=16))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(list_make_t0up4(1209), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(10187(line=712,offs=1)--10316(line=721,offs=4)))
## T1IMPallx(list_make_t0up4(1209)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7468],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_make_t0up4(1209);$list(@(x0[3404],T2Pvar(x0[7468])))))))
def pyxtnm30(arg1): ## timp: list_make_t0up4(1209)
  pyxtnm17 = arg1
  ## I1CMP:start
  ## let
  pyxtnm29 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(10232(line=716,offs=1)--10258(line=717,offs=23)))
  ## I1VALDCL
  pyxtnm18 = None
  pyxtnm18 = pyxtnm17
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(10280(line=720,offs=3)--10294(line=720,offs=17))
  ## I0Etapq(I0Ecst(list_make_3val(1183)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list000.sats)@(2572(line=134,offs=1)--2586(line=134,offs=15))));$list(T2JAG($list(T2Pvar(x0[7468])))))
  ## T1IMPallx(list_make_3val(1183), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(8500(line=590,offs=1)--8607(line=596,offs=31)))
  ## T1IMPallx(list_make_3val(1183)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7457],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_make_3val(1183);$list(@(a[3345],T2Pvar(x0[7457])))))))
  def pyxtnm26(arg1, arg2, arg3): ## timp: list_make_3val(1183)
    pyxtnm19 = arg1
    pyxtnm20 = arg2
    pyxtnm21 = arg3
    ## I1CMP:start
    pyxtnm22 = XATSCAPP("list_nil", [0])
    pyxtnm23 = XATSCAPP("list_cons", [1, pyxtnm21, pyxtnm22])
    pyxtnm24 = XATSCAPP("list_cons", [1, pyxtnm20, pyxtnm23])
    pyxtnm25 = XATSCAPP("list_cons", [1, pyxtnm19, pyxtnm24])
    ## I1CMP:return:I1Vtnm(I1TNM(25))
    return pyxtnm25
  ## endtimp(list_make_3val(1183))
  pyxtnm27 = XATSDAPP(pyxtnm26(XATSP1RJ(XATSTRCD(0), pyxtnm18[1]), XATSP1RJ(XATSTRCD(0), pyxtnm18[2]), XATSP1RJ(XATSTRCD(0), pyxtnm18[3])))
  pyxtnm28 = XATSCAPP("list_cons", [1, XATSP1RJ(XATSTRCD(0), pyxtnm18[0]), pyxtnm27])
  pyxtnm29 = pyxtnm28
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(29))
  return pyxtnm29
## endtimp(list_make_t0up4(1209))
pyxtnm31 = XATSTUP1(XATSTRCD(0), [XATSINT1(10), XATSINT1(20), XATSINT1(30), XATSINT1(40)])
pyxtnm32 = XATSDAPP(pyxtnm30(pyxtnm31))
pyxtnm33 = pyxtnm32
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(583(line=37,offs=1)--617(line=37,offs=35)))
## I1VALDCL
pyxtnm360 = None
## LCSRCsome1(test07_gseq000.dats)@(592(line=37,offs=10)--598(line=37,offs=16))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm358(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm34 = arg1
  pyxtnm35 = arg2
  pyxtnm36 = arg3
  ## I1CMP:start
  ## let
  pyxtnm357 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm40 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm38(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm37 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(37))
    return pyxtnm37
  ## endtimp(gs_print$beg(802))
  pyxtnm39 = XATSDAPP(pyxtnm38())
  pyxtnm40 = pyxtnm39
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm46 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm45(arg1): ## timp: strn_print(1040)
    pyxtnm41 = arg1
    ## I1CMP:start
    ## let
    pyxtnm44 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(42);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(42))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm43 = XATSDAPP(XATS2PY_strn_print(pyxtnm41))
    pyxtnm44 = pyxtnm43
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(44))
    return pyxtnm44
  ## endtimp(strn_print(1040))
  pyxtnm46 = pyxtnm45
  pyxtnm47 = XATSDAPP(pyxtnm46(pyxtnm34))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm49(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm48 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(48))
    return pyxtnm48
  ## endtimp(gs_print$sep(803))
  pyxtnm50 = XATSDAPP(pyxtnm49())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3531(line=203,offs=1)--3606(line=208,offs=30)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7418],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7418])))))))))
  def pyxtnm342(arg1): ## timp: g_print(39)
    pyxtnm51 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3577(line=208,offs=1)--3587(line=208,offs=11))
    ## I0Etapq(I0Ecst(gseq_print(353)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2942(line=185,offs=1)--2952(line=185,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Pvar(x0[7418]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7418])))))
    ## T1IMPallx(gseq_print(353), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2867(line=161,offs=1)--2928(line=164,offs=33)))
    ## T1IMPallx(gseq_print(353)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6056],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6057],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print(353);$list(@(xs[1081],T2Pvar(xs[6056])),@(x0[1082],T2Pvar(x0[6057])))))))
    pyxtnm340 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2909(line=164,offs=14)--2920(line=164,offs=25))
    ## I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Pvar(xs[6056]))),T2JAG($list(T2Pvar(x0[6057])))))
    ## T1IMPallx(gseq_print0(1686), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    ## T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    def pyxtnm339(arg1): ## timp: gseq_print0(1686)
      pyxtnm52 = arg1
      ## I1CMP:start
      ## let
      pyxtnm338 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
      ## I1VALDCL
      pyxtnm61 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm57(arg1): ## timp: strn_print(1040)
        pyxtnm53 = arg1
        ## I1CMP:start
        ## let
        pyxtnm56 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(54);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(54))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm55 = XATSDAPP(XATS2PY_strn_print(pyxtnm53))
        pyxtnm56 = pyxtnm55
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(56))
        return pyxtnm56
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3473(line=198,offs=1)--3527(line=201,offs=27)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7417],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7417],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7417])))),@(x0[1068],T2Pvar(x0[7417])))))))
      def pyxtnm58(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("list(")
      ## endtimp(gseq$beg(346))
      pyxtnm59 = XATSDAPP(pyxtnm58())
      pyxtnm60 = XATSDAPP(pyxtnm57(pyxtnm59))
      pyxtnm61 = pyxtnm60
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
      ## I1VALDCL
      pyxtnm328 = None
      ## let
      pyxtnm327 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
      ## I1VALDCL
      pyxtnm70 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
      ## I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$prlen(350), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
      ## T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
      def pyxtnm68(): ## timp: gseq$prlen(350)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
        ## I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
        ## T1IMPallx(sint_neg(923), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
        ## T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
        def pyxtnm66(arg1): ## timp: sint_neg(923)
          pyxtnm62 = arg1
          ## I1CMP:start
          ## let
          pyxtnm65 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_neg(2612));$list(I1FUNDCL(XATS2PY_sint_neg(4857);$list(FJARGdarg($list(I1BNDcons(I1TNM(63);I0Pvar(i1(4858));$list(@(i1(4858),I1Vtnm(I1TNM(63))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_neg);G1Nlist($list())))))))
          pyxtnm64 = XATSDAPP(XATS2PY_sint_neg(pyxtnm62))
          pyxtnm65 = pyxtnm64
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(65))
          return pyxtnm65
        ## endtimp(sint_neg(923))
        pyxtnm67 = XATSDAPP(pyxtnm66(XATSINT1(1)))
        ## I1CMP:return:I1Vtnm(I1TNM(67))
        return pyxtnm67
      ## endtimp(gseq$prlen(350))
      pyxtnm69 = XATSDAPP(pyxtnm68())
      pyxtnm70 = pyxtnm69
      XATS000_patck(True)
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm103(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm97 = arg1
        pyxtnm98 = arg2
        ## I1CMP:start
        ## let
        pyxtnm102 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(99);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(99))))),I1BNDcons(I1TNM(100);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(100))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm101 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm97, pyxtnm98))
        pyxtnm102 = pyxtnm101
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(102))
        return pyxtnm102
      ## endtimp(sint_gte$sint(931))
      pyxtnm104 = XATSDAPP(pyxtnm103(pyxtnm70, XATSINT1(0)))
      pyxtnm326 = None
      if (pyxtnm104):
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
        ## I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
        ## T1IMPallx(g_void(22), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
        ## T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
        def pyxtnm107(arg1): ## timp: g_void(22)
          pyxtnm105 = arg1
          ## I1CMP:start
          pyxtnm106 = XATSTUP0([])
          ## I1CMP:return:I1Vtnm(I1TNM(106))
          return pyxtnm106
        ## endtimp(g_void(22))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
        ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
        def pyxtnm218(arg1): ## timp: gseq_iforall0(1735)
          pyxtnm108 = arg1
          ## I1CMP:start
          ## let
          pyxtnm217 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm109 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
          ## I1VALDCL
          pyxtnm110 = None
          pyxtnm110 = XATSADDR(pyxtnm109)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
          ## I1VALDCL
          pyxtnm216 = None
          ## let
          pyxtnm215 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
          ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
          ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
          def pyxtnm213(arg1): ## timp: gseq_forall0(1719)
            pyxtnm119 = arg1
            ## I1CMP:start
            ## let
            pyxtnm212 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
            ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
            ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1841(line=78,offs=1)--1904(line=81,offs=33)))
            ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7480])))),@(x0[1168],T2Pvar(x0[7480])))))))
            pyxtnm210 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1889(line=81,offs=18)--1900(line=81,offs=29))
            ## I0Etapq(I0Ecst(list_forall(1222)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(2160(line=92,offs=1)--2171(line=92,offs=12))));$list(T2JAG($list(T2Pvar(x0[7480])))))
            ## T1IMPallx(list_forall(1222), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1591(line=53,offs=1)--1837(line=76,offs=2)))
            ## T1IMPallx(list_forall(1222)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7479],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_forall(1222);$list(@(x0[3422],T2Pvar(x0[7479])))))))
            def pyxtnm209(arg1): ## timp: list_forall(1222)
              pyxtnm120 = arg1
              ## I1CMP:start
              ## let
              pyxtnm208 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1657(line=60,offs=1)--1835(line=75,offs=31)))
              ## I1FUNDCL
              def loop_1660(arg1): ## fun
                pyxtnm121 = arg1
                ## I1CMP:start
                pyxtnm206 = None
                while True: ## do {
                  ## { // cls
                  ## I1GPTpat(I1BNDcons(I1TNM(122);I0Pfree(I0Pdapp(I0Pcon(list_nil(8));$list()));$list()))
                  if (XATS000_ctgeq(pyxtnm121, XATSCTAG("list_nil",0))): ## { // gpt
                    pyxtnm122 = pyxtnm121
                    pyxtnm206 = XATSBOOL(True)
                    break ## cls
                  ## } // gpt
                  ## } // cls
                  ## { // cls
                  ## I1GPTpat(I1BNDcons(I1TNM(123);I0Pfree(I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2573)),I0Pvar(xs(2574)))));$list(@(x1(2573),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(123));0)),@(xs(2574),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(123));1)))))
                  if (XATS000_ctgeq(pyxtnm121, XATSCTAG("list_cons",1))): ## { // gpt
                    pyxtnm123 = pyxtnm121
                    ## let
                    pyxtnm205 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1761(line=71,offs=1)--1791(line=72,offs=20)))
                    ## I1VALDCL
                    pyxtnm202 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1772(line=72,offs=1)--1783(line=72,offs=12))
                    ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7479])))))
                    ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                    ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    pyxtnm200 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                    ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                    ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                    ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm199(arg1): ## timp: forall$test0(1422)
                      pyxtnm124 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm198 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                      ## I1VALDCL
                      pyxtnm129 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                      ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                      ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                      def pyxtnm127(arg1): ## timp: p2tr_get(2309)
                        pyxtnm125 = arg1
                        ## I1CMP:start
                        pyxtnm126 = XATS000_dp2tr(pyxtnm125)
                        ## I1CMP:return:I1Vtnm(I1TNM(126))
                        return pyxtnm126
                      ## endtimp(p2tr_get(2309))
                      pyxtnm128 = XATSDAPP(pyxtnm127(pyxtnm110))
                      pyxtnm129 = pyxtnm128
                      XATS000_patck(True)
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                      ## I1VALDCL
                      pyxtnm185 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                      ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                      ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                      ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm183(arg1, arg2): ## timp: iforall$test0(1432)
                        pyxtnm130 = arg1
                        pyxtnm131 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm182 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                        ## I1VALDCL
                        pyxtnm149 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                        def pyxtnm138(arg1, arg2): ## timp: sint_gt$sint(928)
                          pyxtnm132 = arg1
                          pyxtnm133 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm137 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(134);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(134))))),I1BNDcons(I1TNM(135);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(135))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm136 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm132, pyxtnm133))
                          pyxtnm137 = pyxtnm136
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(137))
                          return pyxtnm137
                        ## endtimp(sint_gt$sint(928))
                        pyxtnm139 = XATSDAPP(pyxtnm138(pyxtnm130, XATSINT1(0)))
                        pyxtnm148 = None
                        if (pyxtnm139):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm144(arg1): ## timp: strn_print(1040)
                            pyxtnm140 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm143 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(141);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(141))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm142 = XATSDAPP(XATS2PY_strn_print(pyxtnm140))
                            pyxtnm143 = pyxtnm142
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(143))
                            return pyxtnm143
                          ## endtimp(strn_print(1040))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                          ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3371(line=190,offs=1)--3421(line=193,offs=23)))
                          ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7415])))),@(x0[1072],T2Pvar(x0[7415])))))))
                          def pyxtnm145(): ## timp: gseq$sep(348)
                            ## I1CMP:start
                            ## I1CMP:return:I1Vstr(...)
                            return XATSSTRN(",")
                          ## endtimp(gseq$sep(348))
                          pyxtnm146 = XATSDAPP(pyxtnm145())
                          pyxtnm147 = XATSDAPP(pyxtnm144(pyxtnm146))
                          pyxtnm148 = pyxtnm147
                        ## else: None
                        ## end-of(if)
                        pyxtnm149 = pyxtnm148
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                        ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                        ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                        def pyxtnm156(arg1, arg2): ## timp: sint_gte$sint(931)
                          pyxtnm150 = arg1
                          pyxtnm151 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm155 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(152);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(152))))),I1BNDcons(I1TNM(153);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(153))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                          pyxtnm154 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm150, pyxtnm151))
                          pyxtnm155 = pyxtnm154
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(155))
                          return pyxtnm155
                        ## endtimp(sint_gte$sint(931))
                        pyxtnm157 = XATSDAPP(pyxtnm156(pyxtnm130, pyxtnm70))
                        pyxtnm181 = None
                        if (pyxtnm157):
                          ## let
                          pyxtnm172 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                          ## I1VALDCL
                          pyxtnm162 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                          ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                          ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                          def pyxtnm160(arg1): ## timp: g_free(23)
                            pyxtnm158 = arg1
                            ## I1CMP:start
                            pyxtnm159 = XATSTUP0([])
                            ## I1CMP:return:I1Vtnm(I1TNM(159))
                            return pyxtnm159
                          ## endtimp(g_free(23))
                          pyxtnm161 = XATSDAPP(pyxtnm160(pyxtnm131))
                          pyxtnm162 = pyxtnm161
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                          ## I1VALDCL
                          pyxtnm171 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm167(arg1): ## timp: strn_print(1040)
                            pyxtnm163 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm166 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(164);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(164))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm165 = XATSDAPP(XATS2PY_strn_print(pyxtnm163))
                            pyxtnm166 = pyxtnm165
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(166))
                            return pyxtnm166
                          ## endtimp(strn_print(1040))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                          ## I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(gseq$rst(349), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                          ## T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                          def pyxtnm168(): ## timp: gseq$rst(349)
                            ## I1CMP:start
                            ## I1CMP:return:I1Vstr(...)
                            return XATSSTRN("...")
                          ## endtimp(gseq$rst(349))
                          pyxtnm169 = XATSDAPP(pyxtnm168())
                          pyxtnm170 = XATSDAPP(pyxtnm167(pyxtnm169))
                          pyxtnm171 = pyxtnm170
                          XATS000_patck(True)
                          pyxtnm172 = XATSBOOL(False)
                          ## end-of(let)
                          pyxtnm181 = pyxtnm172
                        else:
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                          ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                          ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                          pyxtnm179 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                          pyxtnm178 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                          ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                          ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                          def pyxtnm177(arg1): ## timp: sint_print(922)
                            pyxtnm173 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm176 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(174);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(174))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                            pyxtnm175 = XATSDAPP(XATS2PY_sint_print(pyxtnm173))
                            pyxtnm176 = pyxtnm175
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(176))
                            return pyxtnm176
                          ## endtimp(sint_print(922))
                          pyxtnm178 = pyxtnm177
                          pyxtnm179 = pyxtnm178
                          pyxtnm180 = XATSDAPP(pyxtnm179(pyxtnm131))
                          pyxtnm181 = XATSBOOL(True)
                        ## end-of(if)
                        pyxtnm182 = pyxtnm181
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(182))
                        return pyxtnm182
                      ## endtimp(iforall$test0(1432))
                      pyxtnm184 = XATSDAPP(pyxtnm183(pyxtnm129, pyxtnm124))
                      pyxtnm185 = pyxtnm184
                      XATS000_patck(True)
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                      ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                      ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                      def pyxtnm188(arg1, arg2): ## timp: p2tr_set(2310)
                        pyxtnm186 = arg1
                        pyxtnm187 = arg2
                        ## I1CMP:start
                        XATS000_assgn(pyxtnm186, pyxtnm187)
                        ## I1CMP:return:I1V000()
                        return XATSVOID
                      ## endtimp(p2tr_set(2310))
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                      ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                      ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                      def pyxtnm195(arg1, arg2): ## timp: sint_add$sint(936)
                        pyxtnm189 = arg1
                        pyxtnm190 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm194 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(191);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(191))))),I1BNDcons(I1TNM(192);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(192))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                        pyxtnm193 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm189, pyxtnm190))
                        pyxtnm194 = pyxtnm193
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(194))
                        return pyxtnm194
                      ## endtimp(sint_add$sint(936))
                      pyxtnm196 = XATSDAPP(pyxtnm195(pyxtnm129, XATSINT1(1)))
                      pyxtnm197 = XATSDAPP(pyxtnm188(pyxtnm110, pyxtnm196))
                      pyxtnm198 = pyxtnm185
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(198))
                      return pyxtnm198
                    ## endtimp(forall$test0(1422))
                    pyxtnm200 = pyxtnm199
                    pyxtnm201 = XATSDAPP(pyxtnm200(XATSP1CN("list_cons", pyxtnm123[0+1])))
                    pyxtnm202 = pyxtnm201
                    XATS000_patck(True)
                    pyxtnm204 = None
                    if (pyxtnm202):
                      pyxtnm203 = XATSDAPP(loop_1660(XATSP1CN("list_cons", pyxtnm123[1+1])))
                      pyxtnm204 = pyxtnm203
                    else:
                      pyxtnm204 = XATSBOOL(False)
                    ## end-of(if)
                    pyxtnm205 = pyxtnm204
                    ## end-of(let)
                    pyxtnm206 = pyxtnm205
                    break ## cls
                  ## } // gpt
                  ## } // cls
                  XATS000_cfail()
                ## } while True // end-of(do-cls)
                ## I1CMP:return:I1Vtnm(I1TNM(206))
                return pyxtnm206
              pyxtnm207 = XATSDAPP(loop_1660(pyxtnm120))
              pyxtnm208 = pyxtnm207
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(208))
              return pyxtnm208
            ## endtimp(list_forall(1222))
            pyxtnm210 = pyxtnm209
            pyxtnm211 = XATSDAPP(pyxtnm210(pyxtnm119))
            pyxtnm212 = pyxtnm211
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(212))
            return pyxtnm212
          ## endtimp(gseq_forall0(1719))
          pyxtnm214 = XATSDAPP(pyxtnm213(pyxtnm108))
          pyxtnm215 = pyxtnm214
          ## end-of(let)
          pyxtnm216 = pyxtnm215
          XATS000_patck(True)
          pyxtnm217 = pyxtnm216
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(217))
          return pyxtnm217
        ## endtimp(gseq_iforall0(1735))
        pyxtnm219 = XATSDAPP(pyxtnm218(pyxtnm52))
        pyxtnm220 = XATSDAPP(pyxtnm107(pyxtnm219))
        pyxtnm326 = pyxtnm220
      else:
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforitm0(1759), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
        ## T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
        def pyxtnm324(arg1): ## timp: gseq_iforitm0(1759)
          pyxtnm221 = arg1
          ## I1CMP:start
          ## let
          pyxtnm323 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
          ## let
          pyxtnm322 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
          ## I1VALDCL
          pyxtnm321 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
          ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
          ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
          def pyxtnm319(arg1): ## timp: gseq_iforall0(1735)
            pyxtnm227 = arg1
            ## I1CMP:start
            ## let
            pyxtnm318 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm228 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
            ## I1VALDCL
            pyxtnm229 = None
            pyxtnm229 = XATSADDR(pyxtnm228)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
            ## I1VALDCL
            pyxtnm317 = None
            ## let
            pyxtnm316 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
            ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
            ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
            def pyxtnm314(arg1): ## timp: gseq_forall0(1719)
              pyxtnm238 = arg1
              ## I1CMP:start
              ## let
              pyxtnm313 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
              ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
              ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
              ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1841(line=78,offs=1)--1904(line=81,offs=33)))
              ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7480])))),@(x0[1168],T2Pvar(x0[7480])))))))
              pyxtnm311 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1889(line=81,offs=18)--1900(line=81,offs=29))
              ## I0Etapq(I0Ecst(list_forall(1222)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(2160(line=92,offs=1)--2171(line=92,offs=12))));$list(T2JAG($list(T2Pvar(x0[7480])))))
              ## T1IMPallx(list_forall(1222), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1591(line=53,offs=1)--1837(line=76,offs=2)))
              ## T1IMPallx(list_forall(1222)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7479],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_forall(1222);$list(@(x0[3422],T2Pvar(x0[7479])))))))
              def pyxtnm310(arg1): ## timp: list_forall(1222)
                pyxtnm239 = arg1
                ## I1CMP:start
                ## let
                pyxtnm309 = None
                ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1657(line=60,offs=1)--1835(line=75,offs=31)))
                ## I1FUNDCL
                def loop_1660(arg1): ## fun
                  pyxtnm240 = arg1
                  ## I1CMP:start
                  pyxtnm307 = None
                  while True: ## do {
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(241);I0Pfree(I0Pdapp(I0Pcon(list_nil(8));$list()));$list()))
                    if (XATS000_ctgeq(pyxtnm240, XATSCTAG("list_nil",0))): ## { // gpt
                      pyxtnm241 = pyxtnm240
                      pyxtnm307 = XATSBOOL(True)
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(242);I0Pfree(I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2573)),I0Pvar(xs(2574)))));$list(@(x1(2573),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(242));0)),@(xs(2574),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(242));1)))))
                    if (XATS000_ctgeq(pyxtnm240, XATSCTAG("list_cons",1))): ## { // gpt
                      pyxtnm242 = pyxtnm240
                      ## let
                      pyxtnm306 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1761(line=71,offs=1)--1791(line=72,offs=20)))
                      ## I1VALDCL
                      pyxtnm303 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1772(line=72,offs=1)--1783(line=72,offs=12))
                      ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7479])))))
                      ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                      ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      pyxtnm301 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                      ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                      ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                      ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm300(arg1): ## timp: forall$test0(1422)
                        pyxtnm243 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm299 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                        ## I1VALDCL
                        pyxtnm248 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                        ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                        ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                        ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                        def pyxtnm246(arg1): ## timp: p2tr_get(2309)
                          pyxtnm244 = arg1
                          ## I1CMP:start
                          pyxtnm245 = XATS000_dp2tr(pyxtnm244)
                          ## I1CMP:return:I1Vtnm(I1TNM(245))
                          return pyxtnm245
                        ## endtimp(p2tr_get(2309))
                        pyxtnm247 = XATSDAPP(pyxtnm246(pyxtnm229))
                        pyxtnm248 = pyxtnm247
                        XATS000_patck(True)
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                        ## I1VALDCL
                        pyxtnm286 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                        ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                        ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                        ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        def pyxtnm284(arg1, arg2): ## timp: iforall$test0(1432)
                          pyxtnm249 = arg1
                          pyxtnm250 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm283 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                          ## I1VALDCL
                          pyxtnm282 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                          ## I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                          ## T1IMPallx(iforitm$work0(1448), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                          ## T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          def pyxtnm280(arg1, arg2): ## timp: iforitm$work0(1448)
                            pyxtnm251 = arg1
                            pyxtnm252 = arg2
                            ## I1CMP:start
                            ## let
                            pyxtnm279 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                            ## I1VALDCL
                            pyxtnm270 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                            ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                            ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                            def pyxtnm259(arg1, arg2): ## timp: sint_gt$sint(928)
                              pyxtnm253 = arg1
                              pyxtnm254 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm258 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(255);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(255))))),I1BNDcons(I1TNM(256);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(256))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                              pyxtnm257 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm253, pyxtnm254))
                              pyxtnm258 = pyxtnm257
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(258))
                              return pyxtnm258
                            ## endtimp(sint_gt$sint(928))
                            pyxtnm260 = XATSDAPP(pyxtnm259(pyxtnm251, XATSINT1(0)))
                            pyxtnm269 = None
                            if (pyxtnm260):
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
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
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                              ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                              ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3371(line=190,offs=1)--3421(line=193,offs=23)))
                              ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7415])))),@(x0[1072],T2Pvar(x0[7415])))))))
                              def pyxtnm266(): ## timp: gseq$sep(348)
                                ## I1CMP:start
                                ## I1CMP:return:I1Vstr(...)
                                return XATSSTRN(",")
                              ## endtimp(gseq$sep(348))
                              pyxtnm267 = XATSDAPP(pyxtnm266())
                              pyxtnm268 = XATSDAPP(pyxtnm265(pyxtnm267))
                              pyxtnm269 = pyxtnm268
                            ## else: None
                            ## end-of(if)
                            pyxtnm270 = pyxtnm269
                            XATS000_patck(True)
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                            ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                            ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                            ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                            pyxtnm277 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                            ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                            ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                            ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                            pyxtnm276 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                            ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                            ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                            def pyxtnm275(arg1): ## timp: sint_print(922)
                              pyxtnm271 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm274 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(272);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(272))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                              pyxtnm273 = XATSDAPP(XATS2PY_sint_print(pyxtnm271))
                              pyxtnm274 = pyxtnm273
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(274))
                              return pyxtnm274
                            ## endtimp(sint_print(922))
                            pyxtnm276 = pyxtnm275
                            pyxtnm277 = pyxtnm276
                            pyxtnm278 = XATSDAPP(pyxtnm277(pyxtnm252))
                            pyxtnm279 = pyxtnm278
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(279))
                            return pyxtnm279
                          ## endtimp(iforitm$work0(1448))
                          pyxtnm281 = XATSDAPP(pyxtnm280(pyxtnm249, pyxtnm250))
                          pyxtnm282 = pyxtnm281
                          XATS000_patck(True)
                          pyxtnm283 = XATSBOOL(True)
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(283))
                          return pyxtnm283
                        ## endtimp(iforall$test0(1432))
                        pyxtnm285 = XATSDAPP(pyxtnm284(pyxtnm248, pyxtnm243))
                        pyxtnm286 = pyxtnm285
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                        ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                        ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                        ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                        def pyxtnm289(arg1, arg2): ## timp: p2tr_set(2310)
                          pyxtnm287 = arg1
                          pyxtnm288 = arg2
                          ## I1CMP:start
                          XATS000_assgn(pyxtnm287, pyxtnm288)
                          ## I1CMP:return:I1V000()
                          return XATSVOID
                        ## endtimp(p2tr_set(2310))
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                        ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                        ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                        def pyxtnm296(arg1, arg2): ## timp: sint_add$sint(936)
                          pyxtnm290 = arg1
                          pyxtnm291 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm295 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(292);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(292))))),I1BNDcons(I1TNM(293);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(293))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                          pyxtnm294 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm290, pyxtnm291))
                          pyxtnm295 = pyxtnm294
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(295))
                          return pyxtnm295
                        ## endtimp(sint_add$sint(936))
                        pyxtnm297 = XATSDAPP(pyxtnm296(pyxtnm248, XATSINT1(1)))
                        pyxtnm298 = XATSDAPP(pyxtnm289(pyxtnm229, pyxtnm297))
                        pyxtnm299 = pyxtnm286
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(299))
                        return pyxtnm299
                      ## endtimp(forall$test0(1422))
                      pyxtnm301 = pyxtnm300
                      pyxtnm302 = XATSDAPP(pyxtnm301(XATSP1CN("list_cons", pyxtnm242[0+1])))
                      pyxtnm303 = pyxtnm302
                      XATS000_patck(True)
                      pyxtnm305 = None
                      if (pyxtnm303):
                        pyxtnm304 = XATSDAPP(loop_1660(XATSP1CN("list_cons", pyxtnm242[1+1])))
                        pyxtnm305 = pyxtnm304
                      else:
                        pyxtnm305 = XATSBOOL(False)
                      ## end-of(if)
                      pyxtnm306 = pyxtnm305
                      ## end-of(let)
                      pyxtnm307 = pyxtnm306
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    XATS000_cfail()
                  ## } while True // end-of(do-cls)
                  ## I1CMP:return:I1Vtnm(I1TNM(307))
                  return pyxtnm307
                pyxtnm308 = XATSDAPP(loop_1660(pyxtnm239))
                pyxtnm309 = pyxtnm308
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(309))
                return pyxtnm309
              ## endtimp(list_forall(1222))
              pyxtnm311 = pyxtnm310
              pyxtnm312 = XATSDAPP(pyxtnm311(pyxtnm238))
              pyxtnm313 = pyxtnm312
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(313))
              return pyxtnm313
            ## endtimp(gseq_forall0(1719))
            pyxtnm315 = XATSDAPP(pyxtnm314(pyxtnm227))
            pyxtnm316 = pyxtnm315
            ## end-of(let)
            pyxtnm317 = pyxtnm316
            XATS000_patck(True)
            pyxtnm318 = pyxtnm317
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(318))
            return pyxtnm318
          ## endtimp(gseq_iforall0(1735))
          pyxtnm320 = XATSDAPP(pyxtnm319(pyxtnm221))
          pyxtnm321 = pyxtnm320
          XATS000_patck(True)
          pyxtnm322 = XATSVOID
          ## end-of(let)
          pyxtnm323 = pyxtnm322
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(323))
          return pyxtnm323
        ## endtimp(gseq_iforitm0(1759))
        pyxtnm325 = XATSDAPP(pyxtnm324(pyxtnm52))
        pyxtnm326 = pyxtnm325
      ## end-of(if)
      pyxtnm327 = pyxtnm326
      ## end-of(let)
      pyxtnm328 = pyxtnm327
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
      ## I1VALDCL
      pyxtnm337 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm333(arg1): ## timp: strn_print(1040)
        pyxtnm329 = arg1
        ## I1CMP:start
        ## let
        pyxtnm332 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(330);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(330))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm331 = XATSDAPP(XATS2PY_strn_print(pyxtnm329))
        pyxtnm332 = pyxtnm331
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(332))
        return pyxtnm332
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3422(line=194,offs=1)--3472(line=197,offs=23)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7416],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7416],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7416])))),@(x0[1070],T2Pvar(x0[7416])))))))
      def pyxtnm334(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm335 = XATSDAPP(pyxtnm334())
      pyxtnm336 = XATSDAPP(pyxtnm333(pyxtnm335))
      pyxtnm337 = pyxtnm336
      XATS000_patck(True)
      pyxtnm338 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(338))
      return pyxtnm338
    ## endtimp(gseq_print0(1686))
    pyxtnm340 = pyxtnm339
    pyxtnm341 = XATSDAPP(pyxtnm340(pyxtnm51))
    ## I1CMP:return:I1Vtnm(I1TNM(341))
    return pyxtnm341
  ## endtimp(g_print(39))
  pyxtnm343 = XATSDAPP(pyxtnm342(pyxtnm35))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm345(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm344 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(344))
    return pyxtnm344
  ## endtimp(gs_print$sep(803))
  pyxtnm346 = XATSDAPP(pyxtnm345())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm352 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm351(arg1): ## timp: strn_print(1040)
    pyxtnm347 = arg1
    ## I1CMP:start
    ## let
    pyxtnm350 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(348);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(348))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm349 = XATSDAPP(XATS2PY_strn_print(pyxtnm347))
    pyxtnm350 = pyxtnm349
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(350))
    return pyxtnm350
  ## endtimp(strn_print(1040))
  pyxtnm352 = pyxtnm351
  pyxtnm353 = XATSDAPP(pyxtnm352(pyxtnm36))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm355(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm354 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(354))
    return pyxtnm354
  ## endtimp(gs_print$end(804))
  pyxtnm356 = XATSDAPP(pyxtnm355())
  pyxtnm357 = pyxtnm356
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(357))
  return pyxtnm357
## endtimp(gs_print_a3(808))
pyxtnm359 = XATSDAPP(pyxtnm358(XATSSTRN("xs = "), pyxtnm16, XATSSTRN("\n")))
pyxtnm360 = pyxtnm359
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(618(line=38,offs=1)--652(line=38,offs=35)))
## I1VALDCL
pyxtnm687 = None
## LCSRCsome1(test07_gseq000.dats)@(627(line=38,offs=10)--633(line=38,offs=16))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm685(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm361 = arg1
  pyxtnm362 = arg2
  pyxtnm363 = arg3
  ## I1CMP:start
  ## let
  pyxtnm684 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm367 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm365(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm364 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(364))
    return pyxtnm364
  ## endtimp(gs_print$beg(802))
  pyxtnm366 = XATSDAPP(pyxtnm365())
  pyxtnm367 = pyxtnm366
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm373 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm372(arg1): ## timp: strn_print(1040)
    pyxtnm368 = arg1
    ## I1CMP:start
    ## let
    pyxtnm371 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(369);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(369))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm370 = XATSDAPP(XATS2PY_strn_print(pyxtnm368))
    pyxtnm371 = pyxtnm370
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(371))
    return pyxtnm371
  ## endtimp(strn_print(1040))
  pyxtnm373 = pyxtnm372
  pyxtnm374 = XATSDAPP(pyxtnm373(pyxtnm361))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm376(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm375 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(375))
    return pyxtnm375
  ## endtimp(gs_print$sep(803))
  pyxtnm377 = XATSDAPP(pyxtnm376())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3531(line=203,offs=1)--3606(line=208,offs=30)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7418],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7418])))))))))
  def pyxtnm669(arg1): ## timp: g_print(39)
    pyxtnm378 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3577(line=208,offs=1)--3587(line=208,offs=11))
    ## I0Etapq(I0Ecst(gseq_print(353)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2942(line=185,offs=1)--2952(line=185,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Pvar(x0[7418]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[7418])))))
    ## T1IMPallx(gseq_print(353), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2867(line=161,offs=1)--2928(line=164,offs=33)))
    ## T1IMPallx(gseq_print(353)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6056],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6057],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print(353);$list(@(xs[1081],T2Pvar(xs[6056])),@(x0[1082],T2Pvar(x0[6057])))))))
    pyxtnm667 = None
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(2909(line=164,offs=14)--2920(line=164,offs=25))
    ## I0Etapq(I0Ecst(gseq_print0(1686)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3950(line=241,offs=1)--3961(line=241,offs=12))));$list(T2JAG($list(T2Pvar(xs[6056]))),T2JAG($list(T2Pvar(x0[6057])))))
    ## T1IMPallx(gseq_print0(1686), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3743(line=212,offs=1)--4428(line=280,offs=7)))
    ## T1IMPallx(gseq_print0(1686)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_print0(1686);$list(@(xs[4219],T2Pvar(xs[7903])),@(x0[4220],T2Pvar(x0[7904])))))))
    def pyxtnm666(arg1): ## timp: gseq_print0(1686)
      pyxtnm379 = arg1
      ## I1CMP:start
      ## let
      pyxtnm665 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3797(line=218,offs=1)--3839(line=220,offs=21)))
      ## I1VALDCL
      pyxtnm388 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3806(line=219,offs=1)--3816(line=219,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm384(arg1): ## timp: strn_print(1040)
        pyxtnm380 = arg1
        ## I1CMP:start
        ## let
        pyxtnm383 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(381);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(381))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm382 = XATSDAPP(XATS2PY_strn_print(pyxtnm380))
        pyxtnm383 = pyxtnm382
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(383))
        return pyxtnm383
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3820(line=220,offs=2)--3828(line=220,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3473(line=198,offs=1)--3527(line=201,offs=27)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7417],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7417],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7417])))),@(x0[1068],T2Pvar(x0[7417])))))))
      def pyxtnm385(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("list(")
      ## endtimp(gseq$beg(346))
      pyxtnm386 = XATSDAPP(pyxtnm385())
      pyxtnm387 = XATSDAPP(pyxtnm384(pyxtnm386))
      pyxtnm388 = pyxtnm387
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3843(line=222,offs=1)--4373(line=275,offs=2)))
      ## I1VALDCL
      pyxtnm655 = None
      ## let
      pyxtnm654 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3955(line=236,offs=1)--3992(line=238,offs=27)))
      ## I1VALDCL
      pyxtnm397 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3966(line=238,offs=1)--3976(line=238,offs=11))
      ## I0Etapq(I0Ecst(gseq$prlen(350)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2613(line=154,offs=1)--2623(line=154,offs=11))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$prlen(350), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1773(line=71,offs=1)--1828(line=74,offs=27)))
      ## T1IMPallx(gseq$prlen(350)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6034],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6035],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$prlen(350);$list(@(xs[1075],T2Pvar(xs[6034])),@(x0[1076],T2Pvar(x0[6035])))))))
      def pyxtnm395(): ## timp: gseq$prlen(350)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1824(line=74,offs=23)--1825(line=74,offs=24))
        ## I0Etapq(I0Ecst(sint_neg(923)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1585(line=55,offs=1)--1593(line=55,offs=9))));$list(T2JAG($list())))
        ## T1IMPallx(sint_neg(923), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1430(line=40,offs=1)--1565(line=51,offs=31)))
        ## T1IMPallx(sint_neg(923)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_neg(923);$list()))))
        def pyxtnm393(arg1): ## timp: sint_neg(923)
          pyxtnm389 = arg1
          ## I1CMP:start
          ## let
          pyxtnm392 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1506(line=48,offs=1)--1563(line=51,offs=29)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_neg(2612));$list(I1FUNDCL(XATS2PY_sint_neg(4857);$list(FJARGdarg($list(I1BNDcons(I1TNM(390);I0Pvar(i1(4858));$list(@(i1(4858),I1Vtnm(I1TNM(390))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_neg);G1Nlist($list())))))))
          pyxtnm391 = XATSDAPP(XATS2PY_sint_neg(pyxtnm389))
          pyxtnm392 = pyxtnm391
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(392))
          return pyxtnm392
        ## endtimp(sint_neg(923))
        pyxtnm394 = XATSDAPP(pyxtnm393(XATSINT1(1)))
        ## I1CMP:return:I1Vtnm(I1TNM(394))
        return pyxtnm394
      ## endtimp(gseq$prlen(350))
      pyxtnm396 = XATSDAPP(pyxtnm395())
      pyxtnm397 = pyxtnm396
      XATS000_patck(True)
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Pvar(x0[7904]))))):timp
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
      ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[7904]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3861(line=225,offs=5)--3863(line=225,offs=7))
      ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
      ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
      ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
      def pyxtnm430(arg1, arg2): ## timp: sint_gte$sint(931)
        pyxtnm424 = arg1
        pyxtnm425 = arg2
        ## I1CMP:start
        ## let
        pyxtnm429 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(426);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(426))))),I1BNDcons(I1TNM(427);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(427))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
        pyxtnm428 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm424, pyxtnm425))
        pyxtnm429 = pyxtnm428
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(429))
        return pyxtnm429
      ## endtimp(sint_gte$sint(931))
      pyxtnm431 = XATSDAPP(pyxtnm430(pyxtnm397, XATSINT1(0)))
      pyxtnm653 = None
      if (pyxtnm431):
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3872(line=227,offs=1)--3878(line=227,offs=7))
        ## I0Etapq(I0Ecst(g_void(22)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1519(line=50,offs=1)--1525(line=50,offs=7))));$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))))))
        ## T1IMPallx(g_void(22), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1457(line=44,offs=1)--1497(line=46,offs=22)))
        ## T1IMPallx(g_void(22)<$list(T2JAG($list(T2Papps(T2Pcst(bool_type);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5784],T2Papps(T2Pcst(bool_type);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_void(22);$list(@(a[430],T2Pvar(x0[5784])))))))
        def pyxtnm434(arg1): ## timp: g_void(22)
          pyxtnm432 = arg1
          ## I1CMP:start
          pyxtnm433 = XATSTUP0([])
          ## I1CMP:return:I1Vtnm(I1TNM(433))
          return pyxtnm433
        ## endtimp(g_void(22))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3881(line=229,offs=1)--3894(line=229,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
        ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
        def pyxtnm545(arg1): ## timp: gseq_iforall0(1735)
          pyxtnm435 = arg1
          ## I1CMP:start
          ## let
          pyxtnm544 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm436 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
          ## I1VALDCL
          pyxtnm437 = None
          pyxtnm437 = XATSADDR(pyxtnm436)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
          ## I1VALDCL
          pyxtnm543 = None
          ## let
          pyxtnm542 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
          ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
          ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
          def pyxtnm540(arg1): ## timp: gseq_forall0(1719)
            pyxtnm446 = arg1
            ## I1CMP:start
            ## let
            pyxtnm539 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
            ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
            ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1841(line=78,offs=1)--1904(line=81,offs=33)))
            ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7480])))),@(x0[1168],T2Pvar(x0[7480])))))))
            pyxtnm537 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1889(line=81,offs=18)--1900(line=81,offs=29))
            ## I0Etapq(I0Ecst(list_forall(1222)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(2160(line=92,offs=1)--2171(line=92,offs=12))));$list(T2JAG($list(T2Pvar(x0[7480])))))
            ## T1IMPallx(list_forall(1222), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1591(line=53,offs=1)--1837(line=76,offs=2)))
            ## T1IMPallx(list_forall(1222)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7479],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_forall(1222);$list(@(x0[3422],T2Pvar(x0[7479])))))))
            def pyxtnm536(arg1): ## timp: list_forall(1222)
              pyxtnm447 = arg1
              ## I1CMP:start
              ## let
              pyxtnm535 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1657(line=60,offs=1)--1835(line=75,offs=31)))
              ## I1FUNDCL
              def loop_1660(arg1): ## fun
                pyxtnm448 = arg1
                ## I1CMP:start
                pyxtnm533 = None
                while True: ## do {
                  ## { // cls
                  ## I1GPTpat(I1BNDcons(I1TNM(449);I0Pfree(I0Pdapp(I0Pcon(list_nil(8));$list()));$list()))
                  if (XATS000_ctgeq(pyxtnm448, XATSCTAG("list_nil",0))): ## { // gpt
                    pyxtnm449 = pyxtnm448
                    pyxtnm533 = XATSBOOL(True)
                    break ## cls
                  ## } // gpt
                  ## } // cls
                  ## { // cls
                  ## I1GPTpat(I1BNDcons(I1TNM(450);I0Pfree(I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2573)),I0Pvar(xs(2574)))));$list(@(x1(2573),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(450));0)),@(xs(2574),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(450));1)))))
                  if (XATS000_ctgeq(pyxtnm448, XATSCTAG("list_cons",1))): ## { // gpt
                    pyxtnm450 = pyxtnm448
                    ## let
                    pyxtnm532 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1761(line=71,offs=1)--1791(line=72,offs=20)))
                    ## I1VALDCL
                    pyxtnm529 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1772(line=72,offs=1)--1783(line=72,offs=12))
                    ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7479])))))
                    ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                    ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    pyxtnm527 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                    ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                    ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                    ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                    def pyxtnm526(arg1): ## timp: forall$test0(1422)
                      pyxtnm451 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm525 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                      ## I1VALDCL
                      pyxtnm456 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                      ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                      ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                      def pyxtnm454(arg1): ## timp: p2tr_get(2309)
                        pyxtnm452 = arg1
                        ## I1CMP:start
                        pyxtnm453 = XATS000_dp2tr(pyxtnm452)
                        ## I1CMP:return:I1Vtnm(I1TNM(453))
                        return pyxtnm453
                      ## endtimp(p2tr_get(2309))
                      pyxtnm455 = XATSDAPP(pyxtnm454(pyxtnm437))
                      pyxtnm456 = pyxtnm455
                      XATS000_patck(True)
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                      ## I1VALDCL
                      pyxtnm512 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                      ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                      ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4125(line=250,offs=1)--4368(line=273,offs=32)))
                      ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm510(arg1, arg2): ## timp: iforall$test0(1432)
                        pyxtnm457 = arg1
                        pyxtnm458 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm509 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4313(line=271,offs=1)--4367(line=273,offs=31)))
                        ## I1VALDCL
                        pyxtnm476 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4328(line=272,offs=7)--4329(line=272,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                        def pyxtnm465(arg1, arg2): ## timp: sint_gt$sint(928)
                          pyxtnm459 = arg1
                          pyxtnm460 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm464 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(461);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(461))))),I1BNDcons(I1TNM(462);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(462))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm463 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm459, pyxtnm460))
                          pyxtnm464 = pyxtnm463
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(464))
                          return pyxtnm464
                        ## endtimp(sint_gt$sint(928))
                        pyxtnm466 = XATSDAPP(pyxtnm465(pyxtnm457, XATSINT1(0)))
                        pyxtnm475 = None
                        if (pyxtnm466):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4337(line=273,offs=1)--4347(line=273,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm471(arg1): ## timp: strn_print(1040)
                            pyxtnm467 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm470 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(468);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(468))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm469 = XATSDAPP(XATS2PY_strn_print(pyxtnm467))
                            pyxtnm470 = pyxtnm469
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(470))
                            return pyxtnm470
                          ## endtimp(strn_print(1040))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4348(line=273,offs=12)--4356(line=273,offs=20))
                          ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3371(line=190,offs=1)--3421(line=193,offs=23)))
                          ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7415])))),@(x0[1072],T2Pvar(x0[7415])))))))
                          def pyxtnm472(): ## timp: gseq$sep(348)
                            ## I1CMP:start
                            ## I1CMP:return:I1Vstr(...)
                            return XATSSTRN(",")
                          ## endtimp(gseq$sep(348))
                          pyxtnm473 = XATSDAPP(pyxtnm472())
                          pyxtnm474 = XATSDAPP(pyxtnm471(pyxtnm473))
                          pyxtnm475 = pyxtnm474
                        ## else: None
                        ## end-of(if)
                        pyxtnm476 = pyxtnm475
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4173(line=255,offs=4)--4175(line=255,offs=6))
                        ## I0Etapq(I0Ecst(sint_gte$sint(931)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2408(line=104,offs=1)--2421(line=104,offs=14))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gte$sint(931), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2298(line=114,offs=1)--2462(line=126,offs=2)))
                        ## T1IMPallx(sint_gte$sint(931)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gte$sint(931);$list()))))
                        def pyxtnm483(arg1, arg2): ## timp: sint_gte$sint(931)
                          pyxtnm477 = arg1
                          pyxtnm478 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm482 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2388(line=122,offs=1)--2460(line=125,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gte$sint(2617));$list(I1FUNDCL(XATS2PY_sint_gte$sint(4881);$list(FJARGdarg($list(I1BNDcons(I1TNM(479);I0Pvar(i1(4882));$list(@(i1(4882),I1Vtnm(I1TNM(479))))),I1BNDcons(I1TNM(480);I0Pvar(i2(4883));$list(@(i2(4883),I1Vtnm(I1TNM(480))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gte$sint);G1Nlist($list())))))))
                          pyxtnm481 = XATSDAPP(XATS2PY_sint_gte_sint(pyxtnm477, pyxtnm478))
                          pyxtnm482 = pyxtnm481
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(482))
                          return pyxtnm482
                        ## endtimp(sint_gte$sint(931))
                        pyxtnm484 = XATSDAPP(pyxtnm483(pyxtnm457, pyxtnm397))
                        pyxtnm508 = None
                        if (pyxtnm484):
                          ## let
                          pyxtnm499 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4207(line=261,offs=1)--4226(line=261,offs=20)))
                          ## I1VALDCL
                          pyxtnm489 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4216(line=261,offs=10)--4222(line=261,offs=16))
                          ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                          ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                          def pyxtnm487(arg1): ## timp: g_free(23)
                            pyxtnm485 = arg1
                            ## I1CMP:start
                            pyxtnm486 = XATSTUP0([])
                            ## I1CMP:return:I1Vtnm(I1TNM(486))
                            return pyxtnm486
                          ## endtimp(g_free(23))
                          pyxtnm488 = XATSDAPP(pyxtnm487(pyxtnm458))
                          pyxtnm489 = pyxtnm488
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4227(line=262,offs=1)--4267(line=264,offs=21)))
                          ## I1VALDCL
                          pyxtnm498 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4236(line=263,offs=1)--4246(line=263,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm494(arg1): ## timp: strn_print(1040)
                            pyxtnm490 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm493 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(491);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(491))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm492 = XATSDAPP(XATS2PY_strn_print(pyxtnm490))
                            pyxtnm493 = pyxtnm492
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(493))
                            return pyxtnm493
                          ## endtimp(strn_print(1040))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4248(line=264,offs=2)--4256(line=264,offs=10))
                          ## I0Etapq(I0Ecst(gseq$rst(349)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2516(line=142,offs=1)--2524(line=142,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(gseq$rst(349), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq000.dats)@(1627(line=57,offs=1)--1681(line=60,offs=26)))
                          ## T1IMPallx(gseq$rst(349)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6032],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6033],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$rst(349);$list(@(xs[1073],T2Pvar(xs[6032])),@(x0[1074],T2Pvar(x0[6033])))))))
                          def pyxtnm495(): ## timp: gseq$rst(349)
                            ## I1CMP:start
                            ## I1CMP:return:I1Vstr(...)
                            return XATSSTRN("...")
                          ## endtimp(gseq$rst(349))
                          pyxtnm496 = XATSDAPP(pyxtnm495())
                          pyxtnm497 = XATSDAPP(pyxtnm494(pyxtnm496))
                          pyxtnm498 = pyxtnm497
                          XATS000_patck(True)
                          pyxtnm499 = XATSBOOL(False)
                          ## end-of(let)
                          pyxtnm508 = pyxtnm499
                        else:
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4280(line=268,offs=1)--4288(line=268,offs=9))
                          ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                          ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                          ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                          pyxtnm506 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                          pyxtnm505 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                          ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                          ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                          def pyxtnm504(arg1): ## timp: sint_print(922)
                            pyxtnm500 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm503 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(501);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(501))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                            pyxtnm502 = XATSDAPP(XATS2PY_sint_print(pyxtnm500))
                            pyxtnm503 = pyxtnm502
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(503))
                            return pyxtnm503
                          ## endtimp(sint_print(922))
                          pyxtnm505 = pyxtnm504
                          pyxtnm506 = pyxtnm505
                          pyxtnm507 = XATSDAPP(pyxtnm506(pyxtnm458))
                          pyxtnm508 = XATSBOOL(True)
                        ## end-of(if)
                        pyxtnm509 = pyxtnm508
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(509))
                        return pyxtnm509
                      ## endtimp(iforall$test0(1432))
                      pyxtnm511 = XATSDAPP(pyxtnm510(pyxtnm456, pyxtnm451))
                      pyxtnm512 = pyxtnm511
                      XATS000_patck(True)
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                      ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                      ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                      ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                      def pyxtnm515(arg1, arg2): ## timp: p2tr_set(2310)
                        pyxtnm513 = arg1
                        pyxtnm514 = arg2
                        ## I1CMP:start
                        XATS000_assgn(pyxtnm513, pyxtnm514)
                        ## I1CMP:return:I1V000()
                        return XATSVOID
                      ## endtimp(p2tr_set(2310))
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                      ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                      ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                      ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                      def pyxtnm522(arg1, arg2): ## timp: sint_add$sint(936)
                        pyxtnm516 = arg1
                        pyxtnm517 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm521 = None
                        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(518);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(518))))),I1BNDcons(I1TNM(519);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(519))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                        pyxtnm520 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm516, pyxtnm517))
                        pyxtnm521 = pyxtnm520
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(521))
                        return pyxtnm521
                      ## endtimp(sint_add$sint(936))
                      pyxtnm523 = XATSDAPP(pyxtnm522(pyxtnm456, XATSINT1(1)))
                      pyxtnm524 = XATSDAPP(pyxtnm515(pyxtnm437, pyxtnm523))
                      pyxtnm525 = pyxtnm512
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(525))
                      return pyxtnm525
                    ## endtimp(forall$test0(1422))
                    pyxtnm527 = pyxtnm526
                    pyxtnm528 = XATSDAPP(pyxtnm527(XATSP1CN("list_cons", pyxtnm450[0+1])))
                    pyxtnm529 = pyxtnm528
                    XATS000_patck(True)
                    pyxtnm531 = None
                    if (pyxtnm529):
                      pyxtnm530 = XATSDAPP(loop_1660(XATSP1CN("list_cons", pyxtnm450[1+1])))
                      pyxtnm531 = pyxtnm530
                    else:
                      pyxtnm531 = XATSBOOL(False)
                    ## end-of(if)
                    pyxtnm532 = pyxtnm531
                    ## end-of(let)
                    pyxtnm533 = pyxtnm532
                    break ## cls
                  ## } // gpt
                  ## } // cls
                  XATS000_cfail()
                ## } while True // end-of(do-cls)
                ## I1CMP:return:I1Vtnm(I1TNM(533))
                return pyxtnm533
              pyxtnm534 = XATSDAPP(loop_1660(pyxtnm447))
              pyxtnm535 = pyxtnm534
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(535))
              return pyxtnm535
            ## endtimp(list_forall(1222))
            pyxtnm537 = pyxtnm536
            pyxtnm538 = XATSDAPP(pyxtnm537(pyxtnm446))
            pyxtnm539 = pyxtnm538
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(539))
            return pyxtnm539
          ## endtimp(gseq_forall0(1719))
          pyxtnm541 = XATSDAPP(pyxtnm540(pyxtnm435))
          pyxtnm542 = pyxtnm541
          ## end-of(let)
          pyxtnm543 = pyxtnm542
          XATS000_patck(True)
          pyxtnm544 = pyxtnm543
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(544))
          return pyxtnm544
        ## endtimp(gseq_iforall0(1735))
        pyxtnm546 = XATSDAPP(pyxtnm545(pyxtnm379))
        pyxtnm547 = XATSDAPP(pyxtnm434(pyxtnm546))
        pyxtnm653 = pyxtnm547
      else:
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3915(line=232,offs=1)--3928(line=232,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforitm0(1759)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10850(line=584,offs=1)--10863(line=584,offs=14))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
        ## T1IMPallx(gseq_iforitm0(1759), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9751(line=659,offs=1)--9956(line=676,offs=2)))
        ## T1IMPallx(gseq_iforitm0(1759)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforitm0(1759);$list(@(xs[4402],T2Pvar(xs[8038])),@(x0[4403],T2Pvar(x0[8039])))))))
        def pyxtnm651(arg1): ## timp: gseq_iforitm0(1759)
          pyxtnm548 = arg1
          ## I1CMP:start
          ## let
          pyxtnm650 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
          ## I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Pvar(x0[8039]))))):timp
          ## let
          pyxtnm649 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9811(line=666,offs=1)--9847(line=668,offs=15)))
          ## I1VALDCL
          pyxtnm648 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9819(line=667,offs=1)--9832(line=667,offs=14))
          ## I0Etapq(I0Ecst(gseq_iforall0(1735)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6480(line=342,offs=1)--6493(line=342,offs=14))));$list(T2JAG($list(T2Pvar(xs[8038]))),T2JAG($list(T2Pvar(x0[8039])))))
          ## T1IMPallx(gseq_iforall0(1735), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5675(line=349,offs=1)--5978(line=375,offs=2)))
          ## T1IMPallx(gseq_iforall0(1735)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_iforall0(1735);$list(@(xs[4354],T2Pvar(xs[8006])),@(x0[4355],T2Pvar(x0[8007])))))))
          def pyxtnm646(arg1): ## timp: gseq_iforall0(1735)
            pyxtnm554 = arg1
            ## I1CMP:start
            ## let
            pyxtnm645 = None
            ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5743(line=356,offs=1)--5759(line=356,offs=17)))
            ## I1VARDCL
            ## I1CMP:start
            ## I1CMP:return:I1Vint(T_INT01(0))
            pyxtnm555 = XATSVAR1(XATSINT1(0))
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5763(line=358,offs=1)--5781(line=358,offs=19)))
            ## I1VALDCL
            pyxtnm556 = None
            pyxtnm556 = XATSADDR(pyxtnm555)
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5785(line=360,offs=1)--5973(line=373,offs=2)))
            ## I1VALDCL
            pyxtnm644 = None
            ## let
            pyxtnm643 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
            ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[8007]))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5796(line=362,offs=1)--5808(line=362,offs=13))
            ## I0Etapq(I0Ecst(gseq_forall0(1719)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3648(line=181,offs=1)--3660(line=181,offs=13))));$list(T2JAG($list(T2Pvar(xs[8006]))),T2JAG($list(T2Pvar(x0[8007])))))
            ## T1IMPallx(gseq_forall0(1719), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2231(line=107,offs=1)--2361(line=117,offs=2)))
            ## T1IMPallx(gseq_forall0(1719)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall0(1719);$list(@(xs[4322],T2Pvar(xs[8812])),@(x0[4323],T2Pvar(x0[8813])))))))
            def pyxtnm641(arg1): ## timp: gseq_forall0(1719)
              pyxtnm565 = arg1
              ## I1CMP:start
              ## let
              pyxtnm640 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
              ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[8813]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2283(line=112,offs=3)--2294(line=112,offs=14))
              ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[8812]))),T2JAG($list(T2Pvar(x0[8813])))))
              ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1841(line=78,offs=1)--1904(line=81,offs=33)))
              ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7480])))),@(x0[1168],T2Pvar(x0[7480])))))))
              pyxtnm638 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1889(line=81,offs=18)--1900(line=81,offs=29))
              ## I0Etapq(I0Ecst(list_forall(1222)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(2160(line=92,offs=1)--2171(line=92,offs=12))));$list(T2JAG($list(T2Pvar(x0[7480])))))
              ## T1IMPallx(list_forall(1222), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1591(line=53,offs=1)--1837(line=76,offs=2)))
              ## T1IMPallx(list_forall(1222)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7479],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_forall(1222);$list(@(x0[3422],T2Pvar(x0[7479])))))))
              def pyxtnm637(arg1): ## timp: list_forall(1222)
                pyxtnm566 = arg1
                ## I1CMP:start
                ## let
                pyxtnm636 = None
                ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1657(line=60,offs=1)--1835(line=75,offs=31)))
                ## I1FUNDCL
                def loop_1660(arg1): ## fun
                  pyxtnm567 = arg1
                  ## I1CMP:start
                  pyxtnm634 = None
                  while True: ## do {
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(568);I0Pfree(I0Pdapp(I0Pcon(list_nil(8));$list()));$list()))
                    if (XATS000_ctgeq(pyxtnm567, XATSCTAG("list_nil",0))): ## { // gpt
                      pyxtnm568 = pyxtnm567
                      pyxtnm634 = XATSBOOL(True)
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(569);I0Pfree(I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2573)),I0Pvar(xs(2574)))));$list(@(x1(2573),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(569));0)),@(xs(2574),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(569));1)))))
                    if (XATS000_ctgeq(pyxtnm567, XATSCTAG("list_cons",1))): ## { // gpt
                      pyxtnm569 = pyxtnm567
                      ## let
                      pyxtnm633 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1761(line=71,offs=1)--1791(line=72,offs=20)))
                      ## I1VALDCL
                      pyxtnm630 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1772(line=72,offs=1)--1783(line=72,offs=12))
                      ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7479])))))
                      ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2316(line=115,offs=1)--2359(line=116,offs=35)))
                      ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8812],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8813],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      pyxtnm628 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(2343(line=116,offs=19)--2355(line=116,offs=31))
                      ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8813])))))
                      ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5831(line=365,offs=1)--5971(line=372,offs=37)))
                      ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8006],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8007],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                      def pyxtnm627(arg1): ## timp: forall$test0(1422)
                        pyxtnm570 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm626 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5905(line=371,offs=1)--5934(line=371,offs=30)))
                        ## I1VALDCL
                        pyxtnm575 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5918(line=371,offs=14)--5926(line=371,offs=22))
                        ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                        ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                        ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                        def pyxtnm573(arg1): ## timp: p2tr_get(2309)
                          pyxtnm571 = arg1
                          ## I1CMP:start
                          pyxtnm572 = XATS000_dp2tr(pyxtnm571)
                          ## I1CMP:return:I1Vtnm(I1TNM(572))
                          return pyxtnm572
                        ## endtimp(p2tr_get(2309))
                        pyxtnm574 = XATSDAPP(pyxtnm573(pyxtnm556))
                        pyxtnm575 = pyxtnm574
                        XATS000_patck(True)
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5935(line=372,offs=1)--5969(line=372,offs=35)))
                        ## I1VALDCL
                        pyxtnm613 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5944(line=372,offs=10)--5957(line=372,offs=23))
                        ## I0Etapq(I0Ecst(iforall$test0(1432)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2570(line=145,offs=1)--2583(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[8007])))))
                        ## T1IMPallx(iforall$test0(1432), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9867(line=671,offs=1)--9954(line=675,offs=38)))
                        ## T1IMPallx(iforall$test0(1432)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[8038],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[8039],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforall$test0(1432);$list(@(x0[3775],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                        def pyxtnm611(arg1, arg2): ## timp: iforall$test0(1432)
                          pyxtnm576 = arg1
                          pyxtnm577 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm610 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9908(line=674,offs=1)--9942(line=675,offs=26)))
                          ## I1VALDCL
                          pyxtnm609 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9917(line=675,offs=1)--9930(line=675,offs=14))
                          ## I0Etapq(I0Ecst(iforitm$work0(1448)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3293(line=203,offs=1)--3306(line=203,offs=14))));$list(T2JAG($list(T2Pvar(x0[8039])))))
                          ## T1IMPallx(iforitm$work0(1448), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(3996(line=240,offs=1)--4121(line=248,offs=32)))
                          ## T1IMPallx(iforitm$work0(1448)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[7903],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[7904],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(iforitm$work0(1448);$list(@(x0[3791],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                          def pyxtnm607(arg1, arg2): ## timp: iforitm$work0(1448)
                            pyxtnm578 = arg1
                            pyxtnm579 = arg2
                            ## I1CMP:start
                            ## let
                            pyxtnm606 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4066(line=246,offs=1)--4120(line=248,offs=31)))
                            ## I1VALDCL
                            pyxtnm597 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4081(line=247,offs=7)--4082(line=247,offs=8))
                            ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                            ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                            def pyxtnm586(arg1, arg2): ## timp: sint_gt$sint(928)
                              pyxtnm580 = arg1
                              pyxtnm581 = arg2
                              ## I1CMP:start
                              ## let
                              pyxtnm585 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(582);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(582))))),I1BNDcons(I1TNM(583);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(583))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                              pyxtnm584 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm580, pyxtnm581))
                              pyxtnm585 = pyxtnm584
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(585))
                              return pyxtnm585
                            ## endtimp(sint_gt$sint(928))
                            pyxtnm587 = XATSDAPP(pyxtnm586(pyxtnm578, XATSINT1(0)))
                            pyxtnm596 = None
                            if (pyxtnm587):
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4090(line=248,offs=1)--4100(line=248,offs=11))
                              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                              def pyxtnm592(arg1): ## timp: strn_print(1040)
                                pyxtnm588 = arg1
                                ## I1CMP:start
                                ## let
                                pyxtnm591 = None
                                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(589);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(589))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                                pyxtnm590 = XATSDAPP(XATS2PY_strn_print(pyxtnm588))
                                pyxtnm591 = pyxtnm590
                                ## end-of(let)
                                ## I1CMP:return:I1Vtnm(I1TNM(591))
                                return pyxtnm591
                              ## endtimp(strn_print(1040))
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4101(line=248,offs=12)--4109(line=248,offs=20))
                              ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
                              ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3371(line=190,offs=1)--3421(line=193,offs=23)))
                              ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7415],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7415])))),@(x0[1072],T2Pvar(x0[7415])))))))
                              def pyxtnm593(): ## timp: gseq$sep(348)
                                ## I1CMP:start
                                ## I1CMP:return:I1Vstr(...)
                                return XATSSTRN(",")
                              ## endtimp(gseq$sep(348))
                              pyxtnm594 = XATSDAPP(pyxtnm593())
                              pyxtnm595 = XATSDAPP(pyxtnm592(pyxtnm594))
                              pyxtnm596 = pyxtnm595
                            ## else: None
                            ## end-of(if)
                            pyxtnm597 = pyxtnm596
                            XATS000_patck(True)
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4040(line=244,offs=3)--4048(line=244,offs=11))
                            ## I0Etapq(I0Ecst(g_print0(1411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2080(line=106,offs=1)--2088(line=106,offs=9))));$list(T2JAG($list(T2Pvar(x0[7904])))))
                            ## T1IMPallx(g_print0(1411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1589(line=56,offs=1)--1634(line=58,offs=27)))
                            ## T1IMPallx(g_print0(1411)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8802],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print0(1411);$list(@(x0[3749],T2Pvar(x0[8802])))))))
                            pyxtnm604 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1623(line=58,offs=16)--1630(line=58,offs=23))
                            ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8802])))))
                            ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                            ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                            pyxtnm603 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                            ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                            ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                            def pyxtnm602(arg1): ## timp: sint_print(922)
                              pyxtnm598 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm601 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(599);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(599))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                              pyxtnm600 = XATSDAPP(XATS2PY_sint_print(pyxtnm598))
                              pyxtnm601 = pyxtnm600
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(601))
                              return pyxtnm601
                            ## endtimp(sint_print(922))
                            pyxtnm603 = pyxtnm602
                            pyxtnm604 = pyxtnm603
                            pyxtnm605 = XATSDAPP(pyxtnm604(pyxtnm579))
                            pyxtnm606 = pyxtnm605
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(606))
                            return pyxtnm606
                          ## endtimp(iforitm$work0(1448))
                          pyxtnm608 = XATSDAPP(pyxtnm607(pyxtnm576, pyxtnm577))
                          pyxtnm609 = pyxtnm608
                          XATS000_patck(True)
                          pyxtnm610 = XATSBOOL(True)
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(610))
                          return pyxtnm610
                        ## endtimp(iforall$test0(1432))
                        pyxtnm612 = XATSDAPP(pyxtnm611(pyxtnm575, pyxtnm570))
                        pyxtnm613 = pyxtnm612
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5869(line=368,offs=5)--5877(line=368,offs=13))
                        ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                        ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                        ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                        def pyxtnm616(arg1, arg2): ## timp: p2tr_set(2310)
                          pyxtnm614 = arg1
                          pyxtnm615 = arg2
                          ## I1CMP:start
                          XATS000_assgn(pyxtnm614, pyxtnm615)
                          ## I1CMP:return:I1V000()
                          return XATSVOID
                        ## endtimp(p2tr_set(2310))
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(5888(line=368,offs=24)--5889(line=368,offs=25))
                        ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                        ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                        def pyxtnm623(arg1, arg2): ## timp: sint_add$sint(936)
                          pyxtnm617 = arg1
                          pyxtnm618 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm622 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(619);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(619))))),I1BNDcons(I1TNM(620);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(620))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                          pyxtnm621 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm617, pyxtnm618))
                          pyxtnm622 = pyxtnm621
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(622))
                          return pyxtnm622
                        ## endtimp(sint_add$sint(936))
                        pyxtnm624 = XATSDAPP(pyxtnm623(pyxtnm575, XATSINT1(1)))
                        pyxtnm625 = XATSDAPP(pyxtnm616(pyxtnm556, pyxtnm624))
                        pyxtnm626 = pyxtnm613
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(626))
                        return pyxtnm626
                      ## endtimp(forall$test0(1422))
                      pyxtnm628 = pyxtnm627
                      pyxtnm629 = XATSDAPP(pyxtnm628(XATSP1CN("list_cons", pyxtnm569[0+1])))
                      pyxtnm630 = pyxtnm629
                      XATS000_patck(True)
                      pyxtnm632 = None
                      if (pyxtnm630):
                        pyxtnm631 = XATSDAPP(loop_1660(XATSP1CN("list_cons", pyxtnm569[1+1])))
                        pyxtnm632 = pyxtnm631
                      else:
                        pyxtnm632 = XATSBOOL(False)
                      ## end-of(if)
                      pyxtnm633 = pyxtnm632
                      ## end-of(let)
                      pyxtnm634 = pyxtnm633
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    XATS000_cfail()
                  ## } while True // end-of(do-cls)
                  ## I1CMP:return:I1Vtnm(I1TNM(634))
                  return pyxtnm634
                pyxtnm635 = XATSDAPP(loop_1660(pyxtnm566))
                pyxtnm636 = pyxtnm635
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(636))
                return pyxtnm636
              ## endtimp(list_forall(1222))
              pyxtnm638 = pyxtnm637
              pyxtnm639 = XATSDAPP(pyxtnm638(pyxtnm565))
              pyxtnm640 = pyxtnm639
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(640))
              return pyxtnm640
            ## endtimp(gseq_forall0(1719))
            pyxtnm642 = XATSDAPP(pyxtnm641(pyxtnm554))
            pyxtnm643 = pyxtnm642
            ## end-of(let)
            pyxtnm644 = pyxtnm643
            XATS000_patck(True)
            pyxtnm645 = pyxtnm644
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(645))
            return pyxtnm645
          ## endtimp(gseq_iforall0(1735))
          pyxtnm647 = XATSDAPP(pyxtnm646(pyxtnm548))
          pyxtnm648 = pyxtnm647
          XATS000_patck(True)
          pyxtnm649 = XATSVOID
          ## end-of(let)
          pyxtnm650 = pyxtnm649
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(650))
          return pyxtnm650
        ## endtimp(gseq_iforitm0(1759))
        pyxtnm652 = XATSDAPP(pyxtnm651(pyxtnm379))
        pyxtnm653 = pyxtnm652
      ## end-of(if)
      pyxtnm654 = pyxtnm653
      ## end-of(let)
      pyxtnm655 = pyxtnm654
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4377(line=277,offs=1)--4418(line=278,offs=33)))
      ## I1VALDCL
      pyxtnm664 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4386(line=278,offs=1)--4396(line=278,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm660(arg1): ## timp: strn_print(1040)
        pyxtnm656 = arg1
        ## I1CMP:start
        ## let
        pyxtnm659 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(657);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(657))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm658 = XATSDAPP(XATS2PY_strn_print(pyxtnm656))
        pyxtnm659 = pyxtnm658
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(659))
        return pyxtnm659
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4399(line=278,offs=14)--4407(line=278,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7903]))),T2JAG($list(T2Pvar(x0[7904])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(3422(line=194,offs=1)--3472(line=197,offs=23)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7416],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7416],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7416])))),@(x0[1070],T2Pvar(x0[7416])))))))
      def pyxtnm661(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm662 = XATSDAPP(pyxtnm661())
      pyxtnm663 = XATSDAPP(pyxtnm660(pyxtnm662))
      pyxtnm664 = pyxtnm663
      XATS000_patck(True)
      pyxtnm665 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(665))
      return pyxtnm665
    ## endtimp(gseq_print0(1686))
    pyxtnm667 = pyxtnm666
    pyxtnm668 = XATSDAPP(pyxtnm667(pyxtnm378))
    ## I1CMP:return:I1Vtnm(I1TNM(668))
    return pyxtnm668
  ## endtimp(g_print(39))
  pyxtnm670 = XATSDAPP(pyxtnm669(pyxtnm362))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm672(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm671 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(671))
    return pyxtnm671
  ## endtimp(gs_print$sep(803))
  pyxtnm673 = XATSDAPP(pyxtnm672())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm679 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm678(arg1): ## timp: strn_print(1040)
    pyxtnm674 = arg1
    ## I1CMP:start
    ## let
    pyxtnm677 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(675);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(675))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm676 = XATSDAPP(XATS2PY_strn_print(pyxtnm674))
    pyxtnm677 = pyxtnm676
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(677))
    return pyxtnm677
  ## endtimp(strn_print(1040))
  pyxtnm679 = pyxtnm678
  pyxtnm680 = XATSDAPP(pyxtnm679(pyxtnm363))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm682(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm681 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(681))
    return pyxtnm681
  ## endtimp(gs_print$end(804))
  pyxtnm683 = XATSDAPP(pyxtnm682())
  pyxtnm684 = pyxtnm683
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(684))
  return pyxtnm684
## endtimp(gs_print_a3(808))
pyxtnm686 = XATSDAPP(pyxtnm685(XATSSTRN("ys = "), pyxtnm33, XATSSTRN("\n")))
pyxtnm687 = pyxtnm686
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(680(line=42,offs=1)--705(line=43,offs=15)))
## I1VALDCL
pyxtnm701 = None
## LCSRCsome1(test07_gseq000.dats)@(691(line=43,offs=1)--705(line=43,offs=15))
## I0Etapq(I0Ecst(GSEQ_z2make(592)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq002.sats)@(9456(line=625,offs=1)--9467(line=625,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
## T1IMPallx(GSEQ_z2make(592), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2000(line=75,offs=1)--2110(line=82,offs=35)))
## T1IMPallx(GSEQ_z2make(592)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6428],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6429],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6430],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6431],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_z2make(592);$list(@(xs[1866],T2Pvar(xs[6428])),@(x0[1867],T2Pvar(x0[6429])),@(ys[1868],T2Pvar(ys[6430])),@(y0[1869],T2Pvar(y0[6431])))))))
def pyxtnm697(arg1, arg2): ## timp: GSEQ_z2make(592)
  pyxtnm688 = arg1
  pyxtnm689 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2087(line=82,offs=12)--2097(line=82,offs=22))
  ## I0Etapq(I0Ecst(z2tup_make(134)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(2180(line=102,offs=1)--2190(line=102,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(xs[6428]),T2Pvar(x0[6429]))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(ys[6430]),T2Pvar(y0[6431])))))))
  ## T1IMPallx(z2tup_make(134), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1518(line=46,offs=1)--1595(line=52,offs=23)))
  ## T1IMPallx(z2tup_make(134)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(a0[5800],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5801],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(z2tup_make(134);$list(@(xs[598],T2Pvar(a0[5800])),@(ys[599],T2Pvar(a1[5801])))))))
  def pyxtnm694(arg1, arg2): ## timp: z2tup_make(134)
    pyxtnm690 = arg1
    pyxtnm691 = arg2
    ## I1CMP:start
    pyxtnm692 = XATSTUP1(XATSTRCD(0), [pyxtnm690, pyxtnm691])
    pyxtnm693 = XATSCAST("castxy_1839", [pyxtnm692])
    ## I1CMP:return:I1Vtnm(I1TNM(693))
    return pyxtnm693
  ## endtimp(z2tup_make(134))
  pyxtnm695 = XATSDAPP(pyxtnm694(pyxtnm688, pyxtnm689))
  pyxtnm696 = XATSCAST("castxy_1839", [pyxtnm695])
  ## I1CMP:return:I1Vtnm(I1TNM(696))
  return pyxtnm696
## endtimp(GSEQ_z2make(592))
pyxtnm698 = XATSCAST("GSEQ_make_list_5900", [pyxtnm16])
pyxtnm699 = XATSCAST("GSEQ_make_list_5900", [pyxtnm33])
pyxtnm700 = XATSDAPP(pyxtnm697(pyxtnm698, pyxtnm699))
pyxtnm701 = pyxtnm700
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(706(line=44,offs=1)--746(line=45,offs=30)))
## I1VALDCL
pyxtnm940 = None
## LCSRCsome1(test07_gseq000.dats)@(717(line=45,offs=1)--723(line=45,offs=7))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm938(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm702 = arg1
  pyxtnm703 = arg2
  pyxtnm704 = arg3
  ## I1CMP:start
  ## let
  pyxtnm937 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm708 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm706(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm705 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(705))
    return pyxtnm705
  ## endtimp(gs_print$beg(802))
  pyxtnm707 = XATSDAPP(pyxtnm706())
  pyxtnm708 = pyxtnm707
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm714 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm713(arg1): ## timp: strn_print(1040)
    pyxtnm709 = arg1
    ## I1CMP:start
    ## let
    pyxtnm712 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(710);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(710))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm711 = XATSDAPP(XATS2PY_strn_print(pyxtnm709))
    pyxtnm712 = pyxtnm711
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(712))
    return pyxtnm712
  ## endtimp(strn_print(1040))
  pyxtnm714 = pyxtnm713
  pyxtnm715 = XATSDAPP(pyxtnm714(pyxtnm702))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm717(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm716 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(716))
    return pyxtnm716
  ## endtimp(gs_print$sep(803))
  pyxtnm718 = XATSDAPP(pyxtnm717())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2332(line=119,offs=1)--2432(line=124,offs=27)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))>;I1Dtmpsub($list(@(t0[5762],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pvar(t0[5762])))))))
  def pyxtnm922(arg1): ## timp: g_print(39)
    pyxtnm719 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2367(line=122,offs=3)--2372(line=122,offs=8))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm724(arg1): ## timp: strn_print(1040)
      pyxtnm720 = arg1
      ## I1CMP:start
      ## let
      pyxtnm723 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(721);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(721))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm722 = XATSDAPP(XATS2PY_strn_print(pyxtnm720))
      pyxtnm723 = pyxtnm722
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(723))
      return pyxtnm723
    ## endtimp(strn_print(1040))
    pyxtnm725 = XATSDAPP(pyxtnm724(XATSSTRN("$val(")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2382(line=123,offs=3)--2389(line=123,offs=10))
    ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[5762])))))
    ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
    ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6652],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
    def pyxtnm900(): ## timp: g_ptype(202)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm730(arg1): ## timp: strn_print(1040)
        pyxtnm726 = arg1
        ## I1CMP:start
        ## let
        pyxtnm729 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(727);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(727))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm728 = XATSDAPP(XATS2PY_strn_print(pyxtnm726))
        pyxtnm729 = pyxtnm728
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(729))
        return pyxtnm729
      ## endtimp(strn_print(1040))
      pyxtnm731 = XATSDAPP(pyxtnm730(XATSSTRN("GSEQ(")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1668(line=59,offs=1)--1807(line=67,offs=29)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))>;I1Dtmpsub($list(@(a0[5804],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5805],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(z2tup);$list(T2Pvar(a0[5804]),T2Pvar(a1[5805])))))))))
      def pyxtnm850(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1737(line=65,offs=3)--1742(line=65,offs=8))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm736(arg1): ## timp: strn_print(1040)
          pyxtnm732 = arg1
          ## I1CMP:start
          ## let
          pyxtnm735 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(733);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(733))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm734 = XATSDAPP(XATS2PY_strn_print(pyxtnm732))
          pyxtnm735 = pyxtnm734
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(735))
          return pyxtnm735
        ## endtimp(strn_print(1040))
        pyxtnm737 = XATSDAPP(pyxtnm736(XATSSTRN("z2tup(")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1753(line=66,offs=3)--1760(line=66,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[5804])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6652],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
        def pyxtnm786(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm742(arg1): ## timp: strn_print(1040)
            pyxtnm738 = arg1
            ## I1CMP:start
            ## let
            pyxtnm741 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(739);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(739))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm740 = XATSDAPP(XATS2PY_strn_print(pyxtnm738))
            pyxtnm741 = pyxtnm740
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(741))
            return pyxtnm741
          ## endtimp(strn_print(1040))
          pyxtnm743 = XATSDAPP(pyxtnm742(XATSSTRN("GSEQ(")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1626(line=57,offs=1)--1728(line=64,offs=32)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(t0[7401],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(list);$list(T2Pvar(t0[7401])))))))))
          def pyxtnm764(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1681(line=63,offs=1)--1686(line=63,offs=6))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm748(arg1): ## timp: strn_print(1040)
              pyxtnm744 = arg1
              ## I1CMP:start
              ## let
              pyxtnm747 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(745);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(745))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm746 = XATSDAPP(XATS2PY_strn_print(pyxtnm744))
              pyxtnm747 = pyxtnm746
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(747))
              return pyxtnm747
            ## endtimp(strn_print(1040))
            pyxtnm749 = XATSDAPP(pyxtnm748(XATSSTRN("list(")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1697(line=64,offs=1)--1704(line=64,offs=8))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[7401])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
            def pyxtnm756(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm754(arg1): ## timp: strn_print(1040)
                pyxtnm750 = arg1
                ## I1CMP:start
                ## let
                pyxtnm753 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(751);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(751))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm752 = XATSDAPP(XATS2PY_strn_print(pyxtnm750))
                pyxtnm753 = pyxtnm752
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(753))
                return pyxtnm753
              ## endtimp(strn_print(1040))
              pyxtnm755 = XATSDAPP(pyxtnm754(XATSSTRN("sint")))
              ## I1CMP:return:I1Vtnm(I1TNM(755))
              return pyxtnm755
            ## endtimp(g_ptype(202))
            pyxtnm757 = XATSDAPP(pyxtnm756())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1717(line=64,offs=21)--1722(line=64,offs=26))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm762(arg1): ## timp: strn_print(1040)
              pyxtnm758 = arg1
              ## I1CMP:start
              ## let
              pyxtnm761 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(759);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(759))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm760 = XATSDAPP(XATS2PY_strn_print(pyxtnm758))
              pyxtnm761 = pyxtnm760
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(761))
              return pyxtnm761
            ## endtimp(strn_print(1040))
            pyxtnm763 = XATSDAPP(pyxtnm762(XATSSTRN(")")))
            ## I1CMP:return:I1Vtnm(I1TNM(763))
            return pyxtnm763
          ## endtimp(g_ptype(202))
          pyxtnm765 = XATSDAPP(pyxtnm764())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm770(arg1): ## timp: strn_print(1040)
            pyxtnm766 = arg1
            ## I1CMP:start
            ## let
            pyxtnm769 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(767);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(767))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm768 = XATSDAPP(XATS2PY_strn_print(pyxtnm766))
            pyxtnm769 = pyxtnm768
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(769))
            return pyxtnm769
          ## endtimp(strn_print(1040))
          pyxtnm771 = XATSDAPP(pyxtnm770(XATSSTRN(",")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          def pyxtnm778(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm776(arg1): ## timp: strn_print(1040)
              pyxtnm772 = arg1
              ## I1CMP:start
              ## let
              pyxtnm775 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(773);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(773))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm774 = XATSDAPP(XATS2PY_strn_print(pyxtnm772))
              pyxtnm775 = pyxtnm774
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(775))
              return pyxtnm775
            ## endtimp(strn_print(1040))
            pyxtnm777 = XATSDAPP(pyxtnm776(XATSSTRN("sint")))
            ## I1CMP:return:I1Vtnm(I1TNM(777))
            return pyxtnm777
          ## endtimp(g_ptype(202))
          pyxtnm779 = XATSDAPP(pyxtnm778())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm784(arg1): ## timp: strn_print(1040)
            pyxtnm780 = arg1
            ## I1CMP:start
            ## let
            pyxtnm783 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(781);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(781))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm782 = XATSDAPP(XATS2PY_strn_print(pyxtnm780))
            pyxtnm783 = pyxtnm782
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(783))
            return pyxtnm783
          ## endtimp(strn_print(1040))
          pyxtnm785 = XATSDAPP(pyxtnm784(XATSSTRN(")")))
          ## I1CMP:return:I1Vtnm(I1TNM(785))
          return pyxtnm785
        ## endtimp(g_ptype(202))
        pyxtnm787 = XATSDAPP(pyxtnm786())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1768(line=66,offs=18)--1773(line=66,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm792(arg1): ## timp: strn_print(1040)
          pyxtnm788 = arg1
          ## I1CMP:start
          ## let
          pyxtnm791 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(789);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(789))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm790 = XATSDAPP(XATS2PY_strn_print(pyxtnm788))
          pyxtnm791 = pyxtnm790
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(791))
          return pyxtnm791
        ## endtimp(strn_print(1040))
        pyxtnm793 = XATSDAPP(pyxtnm792(XATSSTRN(",")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1781(line=67,offs=3)--1788(line=67,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[5805])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6652],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
        def pyxtnm842(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm798(arg1): ## timp: strn_print(1040)
            pyxtnm794 = arg1
            ## I1CMP:start
            ## let
            pyxtnm797 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(795);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(795))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm796 = XATSDAPP(XATS2PY_strn_print(pyxtnm794))
            pyxtnm797 = pyxtnm796
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(797))
            return pyxtnm797
          ## endtimp(strn_print(1040))
          pyxtnm799 = XATSDAPP(pyxtnm798(XATSSTRN("GSEQ(")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1626(line=57,offs=1)--1728(line=64,offs=32)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(t0[7401],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(list);$list(T2Pvar(t0[7401])))))))))
          def pyxtnm820(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1681(line=63,offs=1)--1686(line=63,offs=6))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm804(arg1): ## timp: strn_print(1040)
              pyxtnm800 = arg1
              ## I1CMP:start
              ## let
              pyxtnm803 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(801);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(801))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm802 = XATSDAPP(XATS2PY_strn_print(pyxtnm800))
              pyxtnm803 = pyxtnm802
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(803))
              return pyxtnm803
            ## endtimp(strn_print(1040))
            pyxtnm805 = XATSDAPP(pyxtnm804(XATSSTRN("list(")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1697(line=64,offs=1)--1704(line=64,offs=8))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[7401])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
            def pyxtnm812(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm810(arg1): ## timp: strn_print(1040)
                pyxtnm806 = arg1
                ## I1CMP:start
                ## let
                pyxtnm809 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(807);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(807))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm808 = XATSDAPP(XATS2PY_strn_print(pyxtnm806))
                pyxtnm809 = pyxtnm808
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(809))
                return pyxtnm809
              ## endtimp(strn_print(1040))
              pyxtnm811 = XATSDAPP(pyxtnm810(XATSSTRN("sint")))
              ## I1CMP:return:I1Vtnm(I1TNM(811))
              return pyxtnm811
            ## endtimp(g_ptype(202))
            pyxtnm813 = XATSDAPP(pyxtnm812())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1717(line=64,offs=21)--1722(line=64,offs=26))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm818(arg1): ## timp: strn_print(1040)
              pyxtnm814 = arg1
              ## I1CMP:start
              ## let
              pyxtnm817 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(815);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(815))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm816 = XATSDAPP(XATS2PY_strn_print(pyxtnm814))
              pyxtnm817 = pyxtnm816
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(817))
              return pyxtnm817
            ## endtimp(strn_print(1040))
            pyxtnm819 = XATSDAPP(pyxtnm818(XATSSTRN(")")))
            ## I1CMP:return:I1Vtnm(I1TNM(819))
            return pyxtnm819
          ## endtimp(g_ptype(202))
          pyxtnm821 = XATSDAPP(pyxtnm820())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm826(arg1): ## timp: strn_print(1040)
            pyxtnm822 = arg1
            ## I1CMP:start
            ## let
            pyxtnm825 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(823);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(823))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm824 = XATSDAPP(XATS2PY_strn_print(pyxtnm822))
            pyxtnm825 = pyxtnm824
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(825))
            return pyxtnm825
          ## endtimp(strn_print(1040))
          pyxtnm827 = XATSDAPP(pyxtnm826(XATSSTRN(",")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          def pyxtnm834(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm832(arg1): ## timp: strn_print(1040)
              pyxtnm828 = arg1
              ## I1CMP:start
              ## let
              pyxtnm831 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(829);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(829))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm830 = XATSDAPP(XATS2PY_strn_print(pyxtnm828))
              pyxtnm831 = pyxtnm830
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(831))
              return pyxtnm831
            ## endtimp(strn_print(1040))
            pyxtnm833 = XATSDAPP(pyxtnm832(XATSSTRN("sint")))
            ## I1CMP:return:I1Vtnm(I1TNM(833))
            return pyxtnm833
          ## endtimp(g_ptype(202))
          pyxtnm835 = XATSDAPP(pyxtnm834())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm840(arg1): ## timp: strn_print(1040)
            pyxtnm836 = arg1
            ## I1CMP:start
            ## let
            pyxtnm839 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(837);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(837))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm838 = XATSDAPP(XATS2PY_strn_print(pyxtnm836))
            pyxtnm839 = pyxtnm838
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(839))
            return pyxtnm839
          ## endtimp(strn_print(1040))
          pyxtnm841 = XATSDAPP(pyxtnm840(XATSSTRN(")")))
          ## I1CMP:return:I1Vtnm(I1TNM(841))
          return pyxtnm841
        ## endtimp(g_ptype(202))
        pyxtnm843 = XATSDAPP(pyxtnm842())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1796(line=67,offs=18)--1801(line=67,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm848(arg1): ## timp: strn_print(1040)
          pyxtnm844 = arg1
          ## I1CMP:start
          ## let
          pyxtnm847 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(845);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(845))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm846 = XATSDAPP(XATS2PY_strn_print(pyxtnm844))
          pyxtnm847 = pyxtnm846
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(847))
          return pyxtnm847
        ## endtimp(strn_print(1040))
        pyxtnm849 = XATSDAPP(pyxtnm848(XATSSTRN(")")))
        ## I1CMP:return:I1Vtnm(I1TNM(849))
        return pyxtnm849
      ## endtimp(g_ptype(202))
      pyxtnm851 = XATSDAPP(pyxtnm850())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm856(arg1): ## timp: strn_print(1040)
        pyxtnm852 = arg1
        ## I1CMP:start
        ## let
        pyxtnm855 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(853);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(853))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm854 = XATSDAPP(XATS2PY_strn_print(pyxtnm852))
        pyxtnm855 = pyxtnm854
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(855))
        return pyxtnm855
      ## endtimp(strn_print(1040))
      pyxtnm857 = XATSDAPP(pyxtnm856(XATSSTRN(",")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1835(line=66,offs=1)--1973(line=74,offs=29)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(a0[7352],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7353],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7352]),T2Pvar(a1[7353])))))))))
      def pyxtnm892(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1903(line=72,offs=3)--1908(line=72,offs=8))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm862(arg1): ## timp: strn_print(1040)
          pyxtnm858 = arg1
          ## I1CMP:start
          ## let
          pyxtnm861 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(859);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(859))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm860 = XATSDAPP(XATS2PY_strn_print(pyxtnm858))
          pyxtnm861 = pyxtnm860
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(861))
          return pyxtnm861
        ## endtimp(strn_print(1040))
        pyxtnm863 = XATSDAPP(pyxtnm862(XATSSTRN("t0up2(")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1919(line=73,offs=3)--1926(line=73,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[7352])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
        def pyxtnm870(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm868(arg1): ## timp: strn_print(1040)
            pyxtnm864 = arg1
            ## I1CMP:start
            ## let
            pyxtnm867 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(865);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(865))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm866 = XATSDAPP(XATS2PY_strn_print(pyxtnm864))
            pyxtnm867 = pyxtnm866
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(867))
            return pyxtnm867
          ## endtimp(strn_print(1040))
          pyxtnm869 = XATSDAPP(pyxtnm868(XATSSTRN("sint")))
          ## I1CMP:return:I1Vtnm(I1TNM(869))
          return pyxtnm869
        ## endtimp(g_ptype(202))
        pyxtnm871 = XATSDAPP(pyxtnm870())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1934(line=73,offs=18)--1939(line=73,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm876(arg1): ## timp: strn_print(1040)
          pyxtnm872 = arg1
          ## I1CMP:start
          ## let
          pyxtnm875 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(873);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(873))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm874 = XATSDAPP(XATS2PY_strn_print(pyxtnm872))
          pyxtnm875 = pyxtnm874
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(875))
          return pyxtnm875
        ## endtimp(strn_print(1040))
        pyxtnm877 = XATSDAPP(pyxtnm876(XATSSTRN(",")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1947(line=74,offs=3)--1954(line=74,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[7353])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
        def pyxtnm884(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm882(arg1): ## timp: strn_print(1040)
            pyxtnm878 = arg1
            ## I1CMP:start
            ## let
            pyxtnm881 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(879);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(879))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm880 = XATSDAPP(XATS2PY_strn_print(pyxtnm878))
            pyxtnm881 = pyxtnm880
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(881))
            return pyxtnm881
          ## endtimp(strn_print(1040))
          pyxtnm883 = XATSDAPP(pyxtnm882(XATSSTRN("sint")))
          ## I1CMP:return:I1Vtnm(I1TNM(883))
          return pyxtnm883
        ## endtimp(g_ptype(202))
        pyxtnm885 = XATSDAPP(pyxtnm884())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1962(line=74,offs=18)--1967(line=74,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm890(arg1): ## timp: strn_print(1040)
          pyxtnm886 = arg1
          ## I1CMP:start
          ## let
          pyxtnm889 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(887);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(887))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm888 = XATSDAPP(XATS2PY_strn_print(pyxtnm886))
          pyxtnm889 = pyxtnm888
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(889))
          return pyxtnm889
        ## endtimp(strn_print(1040))
        pyxtnm891 = XATSDAPP(pyxtnm890(XATSSTRN(")")))
        ## I1CMP:return:I1Vtnm(I1TNM(891))
        return pyxtnm891
      ## endtimp(g_ptype(202))
      pyxtnm893 = XATSDAPP(pyxtnm892())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm898(arg1): ## timp: strn_print(1040)
        pyxtnm894 = arg1
        ## I1CMP:start
        ## let
        pyxtnm897 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(895);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(895))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm896 = XATSDAPP(XATS2PY_strn_print(pyxtnm894))
        pyxtnm897 = pyxtnm896
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(897))
        return pyxtnm897
      ## endtimp(strn_print(1040))
      pyxtnm899 = XATSDAPP(pyxtnm898(XATSSTRN(")")))
      ## I1CMP:return:I1Vtnm(I1TNM(899))
      return pyxtnm899
    ## endtimp(g_ptype(202))
    pyxtnm901 = XATSDAPP(pyxtnm900())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2397(line=123,offs=18)--2402(line=123,offs=23))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm906(arg1): ## timp: strn_print(1040)
      pyxtnm902 = arg1
      ## I1CMP:start
      ## let
      pyxtnm905 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(903);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(903))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm904 = XATSDAPP(XATS2PY_strn_print(pyxtnm902))
      pyxtnm905 = pyxtnm904
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(905))
      return pyxtnm905
    ## endtimp(strn_print(1040))
    pyxtnm907 = XATSDAPP(pyxtnm906(XATSSTRN(":")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2408(line=124,offs=3)--2415(line=124,offs=10))
    ## I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(t0[5762])))))
    ## T1IMPallx(g_psort(201), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1776(line=69,offs=1)--1830(line=73,offs=22)))
    ## T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))>;I1Dtmpsub($list(@(t0[5754],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(t0[5754])))))))
    def pyxtnm914(): ## timp: g_psort(201)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1811(line=73,offs=3)--1821(line=73,offs=13))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm912(arg1): ## timp: strn_print(1040)
        pyxtnm908 = arg1
        ## I1CMP:start
        ## let
        pyxtnm911 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(909);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(909))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm910 = XATSDAPP(XATS2PY_strn_print(pyxtnm908))
        pyxtnm911 = pyxtnm910
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(911))
        return pyxtnm911
      ## endtimp(strn_print(1040))
      pyxtnm913 = XATSDAPP(pyxtnm912(XATSSTRN("type")))
      ## I1CMP:return:I1Vtnm(I1TNM(913))
      return pyxtnm913
    ## endtimp(g_psort(201))
    pyxtnm915 = XATSDAPP(pyxtnm914())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2423(line=124,offs=18)--2428(line=124,offs=23))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm920(arg1): ## timp: strn_print(1040)
      pyxtnm916 = arg1
      ## I1CMP:start
      ## let
      pyxtnm919 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(917);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(917))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm918 = XATSDAPP(XATS2PY_strn_print(pyxtnm916))
      pyxtnm919 = pyxtnm918
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(919))
      return pyxtnm919
    ## endtimp(strn_print(1040))
    pyxtnm921 = XATSDAPP(pyxtnm920(XATSSTRN(")")))
    ## I1CMP:return:I1Vtnm(I1TNM(921))
    return pyxtnm921
  ## endtimp(g_print(39))
  pyxtnm923 = XATSDAPP(pyxtnm922(pyxtnm703))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm925(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm924 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(924))
    return pyxtnm924
  ## endtimp(gs_print$sep(803))
  pyxtnm926 = XATSDAPP(pyxtnm925())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm932 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm931(arg1): ## timp: strn_print(1040)
    pyxtnm927 = arg1
    ## I1CMP:start
    ## let
    pyxtnm930 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(928);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(928))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm929 = XATSDAPP(XATS2PY_strn_print(pyxtnm927))
    pyxtnm930 = pyxtnm929
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(930))
    return pyxtnm930
  ## endtimp(strn_print(1040))
  pyxtnm932 = pyxtnm931
  pyxtnm933 = XATSDAPP(pyxtnm932(pyxtnm704))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm935(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm934 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(934))
    return pyxtnm934
  ## endtimp(gs_print$end(804))
  pyxtnm936 = XATSDAPP(pyxtnm935())
  pyxtnm937 = pyxtnm936
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(937))
  return pyxtnm937
## endtimp(gs_print_a3(808))
pyxtnm939 = XATSDAPP(pyxtnm938(XATSSTRN("ztup = "), pyxtnm701, XATSSTRN("\n")))
pyxtnm940 = pyxtnm939
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(750(line=47,offs=1)--774(line=47,offs=25)))
## I1VALDCL
pyxtnm1167 = None
## LCSRCsome1(test07_gseq000.dats)@(761(line=47,offs=12)--768(line=47,offs=19))
## I0Etapq(I0Ecst(GSEQ_listize(251)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(3280(line=173,offs=1)--3292(line=173,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))
## T1IMPallx(GSEQ_listize(251), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2477(line=125,offs=1)--2579(line=132,offs=35)))
## T1IMPallx(GSEQ_listize(251)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6663],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6664],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(GSEQ_listize(251);$list(@(xs[829],T2Pvar(xs[6663])),@(x0[830],T2Pvar(x0[6664])))))))
def pyxtnm1165(arg1): ## timp: GSEQ_listize(251)
  pyxtnm941 = arg1
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2532(line=131,offs=1)--2544(line=131,offs=13))
  ## I0Etapq(I0Ecst(gseq_listize(377)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(2446(line=117,offs=1)--2458(line=117,offs=13))));$list(T2JAG($list(T2Pvar(xs[6663]))),T2JAG($list(T2Pvar(x0[6664])))))
  ## T1IMPallx(gseq_listize(377), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1870(line=72,offs=1)--2083(line=88,offs=2)))
  ## T1IMPallx(gseq_listize(377)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6082],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6083],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_listize(377);$list(@(xs[1131],T2Pvar(xs[6082])),@(x0[1132],T2Pvar(x0[6083])))))))
  def pyxtnm1159(arg1): ## timp: gseq_listize(377)
    pyxtnm942 = arg1
    ## I1CMP:start
    ## let
    pyxtnm1158 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1969(line=82,offs=1)--1991(line=82,offs=23)))
    ## I1VALDCL
    pyxtnm944 = None
    pyxtnm943 = XATSCAPP("list_vt_nil", [0])
    pyxtnm944 = pyxtnm943
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1992(line=83,offs=1)--2017(line=83,offs=26))
    ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(r0;S2Eapps(S2Ecst(list_vt);$list(S2Evar(x0[6083])))))))
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2018(line=84,offs=1)--2081(line=87,offs=32)))
    ## I1Dimplmnt0(DIMPLone2(rfolditm$fopr(56);$list(@(x0[470],T2Pvar(x0[6083])),@(r0[471],T2Pcst(r0))))):timp
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1925(line=78,offs=1)--1938(line=78,offs=14))
    ## I0Etapq(I0Ecst(gseq_rfolditm(411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(8790(line=502,offs=1)--8803(line=502,offs=14))));$list(T2JAG($list(T2Pvar(xs[6082]))),T2JAG($list(T2Pvar(x0[6083]))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[6083]),T2Pnone0()))))))
    ## T1IMPallx(gseq_rfolditm(411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8831(line=582,offs=1)--9143(line=608,offs=2)))
    ## T1IMPallx(gseq_rfolditm(411)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6140],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6141],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(r0[6142],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_rfolditm(411);$list(@(xs[1242],T2Pvar(xs[6140])),@(x0[1243],T2Pvar(x0[6141])),@(r0[1244],T2Pvar(r0[6142])))))))
    def pyxtnm1156(arg1, arg2): ## timp: gseq_rfolditm(411)
      pyxtnm948 = arg1
      pyxtnm949 = arg2
      ## I1CMP:start
      ## let
      pyxtnm1155 = None
      ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8911(line=590,offs=1)--8926(line=590,offs=16)))
      ## I1VARDCL
      ## I1CMP:start
      ## I1CMP:return:I1Vtnm(I1TNM(949))
      pyxtnm950 = XATSVAR1(pyxtnm949)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8930(line=592,offs=1)--8948(line=592,offs=19)))
      ## I1VALDCL
      pyxtnm951 = None
      pyxtnm951 = XATSADDR(pyxtnm950)
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8952(line=594,offs=1)--9138(line=606,offs=41)))
      ## I1VALDCL
      pyxtnm1153 = None
      ## let
      pyxtnm1152 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8998(line=599,offs=1)--9137(line=606,offs=40)))
      ## I1Dimplmnt0(DIMPLone2(rforitm$work(52);$list(@(x0[465],T2Pvar(x0[6141]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8963(line=596,offs=1)--8975(line=596,offs=13))
      ## I0Etapq(I0Ecst(gseq_rforitm(403)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7124(line=406,offs=1)--7136(line=406,offs=13))));$list(T2JAG($list(T2Pvar(xs[6140]))),T2JAG($list(T2Pvar(x0[6141])))))
      ## T1IMPallx(gseq_rforitm(403), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6837(line=439,offs=1)--7028(line=456,offs=2)))
      ## T1IMPallx(gseq_rforitm(403)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6122],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6123],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_rforitm(403);$list(@(xs[1217],T2Pvar(xs[6122])),@(x0[1218],T2Pvar(x0[6123])))))))
      def pyxtnm1150(arg1): ## timp: gseq_rforitm(403)
        pyxtnm959 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1149 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6949(line=451,offs=1)--7026(line=455,offs=33)))
        ## I1Dimplmnt0(DIMPLone2(rforall$test(48);$list(@(x0[461],T2Pvar(x0[6123]))))):timp
        ## let
        pyxtnm1148 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6896(line=446,offs=1)--6929(line=448,offs=13)))
        ## I1VALDCL
        pyxtnm1147 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6904(line=447,offs=1)--6916(line=447,offs=13))
        ## I0Etapq(I0Ecst(gseq_rforall(388)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3813(line=218,offs=1)--3825(line=218,offs=13))));$list(T2JAG($list(T2Pvar(xs[6122]))),T2JAG($list(T2Pvar(x0[6123])))))
        ## T1IMPallx(gseq_rforall(388), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2525(line=116,offs=1)--2848(line=142,offs=2)))
        ## T1IMPallx(gseq_rforall(388)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6436],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6437],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6438],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6439],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_rforall(388);$list(@(xs[1171],T2Papps(T2Pcst(gz2seq);$list(T2Pvar(xs[6436]),T2Pvar(x0[6437]),T2Pvar(ys[6438]),T2Pvar(y0[6439])))),@(x0[1172],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6437])),S2LAB(LABint(1);T2Pvar(y0[6439]))))))))))
        def pyxtnm1145(arg1): ## timp: gseq_rforall(388)
          pyxtnm964 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1144 = None
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2679(line=132,offs=1)--2713(line=134,offs=26)))
          ## I1VALDCL
          pyxtnm969 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2697(line=134,offs=10)--2707(line=134,offs=20))
          ## I0Etapq(I0Ecst(z2tup_unmk(135)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(2241(line=107,offs=1)--2251(line=107,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(xs[6436]),T2Pvar(x0[6437]))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(ys[6438]),T2Pvar(y0[6439])))))))
          ## T1IMPallx(z2tup_unmk(135), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1596(line=53,offs=1)--1664(line=57,offs=29)))
          ## T1IMPallx(z2tup_unmk(135)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(a0[5802],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5803],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(z2tup_unmk(135);$list(@(xs[600],T2Pvar(a0[5802])),@(ys[601],T2Pvar(a1[5803])))))))
          def pyxtnm967(arg1): ## timp: z2tup_unmk(135)
            pyxtnm965 = arg1
            ## I1CMP:start
            pyxtnm966 = XATSCAST("castxy_1839", [pyxtnm965])
            ## I1CMP:return:I1Vtnm(I1TNM(966))
            return pyxtnm966
          ## endtimp(z2tup_unmk(135))
          pyxtnm968 = XATSDAPP(pyxtnm967(pyxtnm964))
          pyxtnm969 = pyxtnm968
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2714(line=135,offs=1)--2775(line=136,offs=31)))
          ## I1VALDCL
          pyxtnm974 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2723(line=135,offs=10)--2732(line=135,offs=19))
          ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6436]))),T2JAG($list(T2Pvar(x0[6437])))))
          ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
          ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
          def pyxtnm972(arg1): ## timp: GSEQ_unmk(245)
            pyxtnm970 = arg1
            ## I1CMP:start
            pyxtnm971 = XATSCAST("castxy_1839", [pyxtnm970])
            ## I1CMP:return:I1Vtnm(I1TNM(971))
            return pyxtnm971
          ## endtimp(GSEQ_unmk(245))
          pyxtnm973 = XATSDAPP(pyxtnm972(XATSP0RJ(pyxtnm969[0])))
          pyxtnm974 = pyxtnm973
          XATS000_patck(True)
          ## I1VALDCL
          pyxtnm979 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2754(line=136,offs=10)--2763(line=136,offs=19))
          ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(ys[6438]))),T2JAG($list(T2Pvar(y0[6439])))))
          ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
          ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
          def pyxtnm977(arg1): ## timp: GSEQ_unmk(245)
            pyxtnm975 = arg1
            ## I1CMP:start
            pyxtnm976 = XATSCAST("castxy_1839", [pyxtnm975])
            ## I1CMP:return:I1Vtnm(I1TNM(976))
            return pyxtnm976
          ## endtimp(GSEQ_unmk(245))
          pyxtnm978 = XATSDAPP(pyxtnm977(XATSP0RJ(pyxtnm969[1])))
          pyxtnm979 = pyxtnm978
          XATS000_patck(True)
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2779(line=138,offs=1)--2843(line=140,offs=41)))
          ## I1Dimplmnt0(DIMPLone2(z2rforall$test(137);$list(@(x1[604],T2Pvar(x0[6437])),@(x2[605],T2Pvar(y0[6439]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2627(line=127,offs=1)--2641(line=127,offs=15))
          ## I0Etapq(I0Ecst(gseq_z2rforall(546)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq002.sats)@(3031(line=164,offs=1)--3045(line=164,offs=15))));$list(T2JAG($list(T2Pvar(xs[6436]))),T2JAG($list(T2Pvar(x0[6437]))),T2JAG($list(T2Pvar(ys[6438]))),T2JAG($list(T2Pvar(y0[6439])))))
          ## T1IMPallx(gseq_z2rforall(546), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(5828(line=362,offs=1)--6142(line=386,offs=4)))
          ## T1IMPallx(gseq_z2rforall(546)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6460],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6461],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6462],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6463],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_z2rforall(546);$list(@(xs[1652],T2Pvar(xs[6460])),@(x0[1653],T2Pvar(x0[6461])),@(ys[1654],T2Pvar(ys[6462])),@(y0[1655],T2Pvar(y0[6463])))))))
          def pyxtnm1142(arg1, arg2): ## timp: gseq_z2rforall(546)
            pyxtnm984 = arg1
            pyxtnm985 = arg2
            ## I1CMP:start
            ## let
            pyxtnm1141 = None
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(5909(line=370,offs=1)--5942(line=371,offs=25)))
            ## I1VALDCL
            pyxtnm1000 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(5918(line=371,offs=1)--5930(line=371,offs=13))
            ## I0Etapq(I0Ecst(gseq_strmize(378)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(2503(line=122,offs=1)--2515(line=122,offs=13))));$list(T2JAG($list(T2Pvar(xs[6460]))),T2JAG($list(T2Pvar(x0[6461])))))
            ## T1IMPallx(gseq_strmize(378), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6711(line=443,offs=1)--6775(line=445,offs=46)))
            ## T1IMPallx(gseq_strmize(378)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7520],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7520],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_strmize(378);$list(@(xs[1133],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7520])))),@(x0[1134],T2Pvar(x0[7520])))))))
            pyxtnm998 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6759(line=445,offs=30)--6771(line=445,offs=42))
            ## I0Etapq(I0Ecst(list_strmize(1218)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(1677(line=61,offs=1)--1689(line=61,offs=13))));$list(T2JAG($list(T2Pvar(x0[7520])))))
            ## T1IMPallx(list_strmize(1218), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6452(line=418,offs=1)--6671(line=441,offs=2)))
            ## T1IMPallx(list_strmize(1218)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7519],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_strmize(1218);$list(@(a[3416],T2Pvar(x0[7519])))))))
            def pyxtnm997(arg1): ## timp: list_strmize(1218)
              pyxtnm986 = arg1
              ## I1CMP:start
              ## let
              pyxtnm996 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6526(line=427,offs=1)--6666(line=439,offs=2)))
              ## I1FUNDCL
              def auxmain_6529(arg1): ## fun
                pyxtnm987 = arg1
                ## I1CMP:start
                def pyxtnm994(tlaz): ## { // l1azy
                  ## I1CMP:start
                  pyxtnm993 = None
                  while True: ## do {
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(988);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
                    if (XATS000_ctgeq(pyxtnm987, XATSCTAG("list_nil",0))): ## { // gpt
                      pyxtnm988 = pyxtnm987
                      pyxtnm989 = XATSCAPP("strmcon_vt_nil", [0])
                      pyxtnm993 = pyxtnm989
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(990);I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x0(2605)),I0Pvar(xs(2606))));$list(@(x0(2605),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(990));0)),@(xs(2606),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(990));1)))))
                    if (XATS000_ctgeq(pyxtnm987, XATSCTAG("list_cons",1))): ## { // gpt
                      pyxtnm990 = pyxtnm987
                      pyxtnm991 = XATSDAPP(auxmain_6529(XATSP1CN("list_cons", pyxtnm990[1+1])))
                      pyxtnm992 = XATSCAPP("strmcon_vt_cons", [1, XATSP1CN("list_cons", pyxtnm990[0+1]), pyxtnm991])
                      pyxtnm993 = pyxtnm992
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    XATS000_cfail()
                  ## } while True // end-of(do-cls)
                  ## I1CMP:return:I1Vtnm(I1TNM(993))
                  return pyxtnm993
                ## } // end(l1azy)
                ## I1CMP:return:I1Vtnm(I1TNM(994))
                return pyxtnm994
              pyxtnm995 = XATSDAPP(auxmain_6529(pyxtnm986))
              pyxtnm996 = pyxtnm995
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(996))
              return pyxtnm996
            ## endtimp(list_strmize(1218))
            pyxtnm998 = pyxtnm997
            pyxtnm999 = XATSDAPP(pyxtnm998(pyxtnm984))
            pyxtnm1000 = pyxtnm999
            XATS000_patck(True)
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(5943(line=372,offs=1)--5976(line=373,offs=25)))
            ## I1VALDCL
            pyxtnm1015 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(5952(line=373,offs=1)--5964(line=373,offs=13))
            ## I0Etapq(I0Ecst(gseq_strmize(378)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(2503(line=122,offs=1)--2515(line=122,offs=13))));$list(T2JAG($list(T2Pvar(ys[6462]))),T2JAG($list(T2Pvar(y0[6463])))))
            ## T1IMPallx(gseq_strmize(378), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6711(line=443,offs=1)--6775(line=445,offs=46)))
            ## T1IMPallx(gseq_strmize(378)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7520],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7520],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_strmize(378);$list(@(xs[1133],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7520])))),@(x0[1134],T2Pvar(x0[7520])))))))
            pyxtnm1013 = None
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6759(line=445,offs=30)--6771(line=445,offs=42))
            ## I0Etapq(I0Ecst(list_strmize(1218)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(1677(line=61,offs=1)--1689(line=61,offs=13))));$list(T2JAG($list(T2Pvar(x0[7520])))))
            ## T1IMPallx(list_strmize(1218), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6452(line=418,offs=1)--6671(line=441,offs=2)))
            ## T1IMPallx(list_strmize(1218)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7519],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_strmize(1218);$list(@(a[3416],T2Pvar(x0[7519])))))))
            def pyxtnm1012(arg1): ## timp: list_strmize(1218)
              pyxtnm1001 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1011 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(6526(line=427,offs=1)--6666(line=439,offs=2)))
              ## I1FUNDCL
              def auxmain_6529(arg1): ## fun
                pyxtnm1002 = arg1
                ## I1CMP:start
                def pyxtnm1009(tlaz): ## { // l1azy
                  ## I1CMP:start
                  pyxtnm1008 = None
                  while True: ## do {
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(1003);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
                    if (XATS000_ctgeq(pyxtnm1002, XATSCTAG("list_nil",0))): ## { // gpt
                      pyxtnm1003 = pyxtnm1002
                      pyxtnm1004 = XATSCAPP("strmcon_vt_nil", [0])
                      pyxtnm1008 = pyxtnm1004
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(1005);I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x0(2605)),I0Pvar(xs(2606))));$list(@(x0(2605),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1005));0)),@(xs(2606),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1005));1)))))
                    if (XATS000_ctgeq(pyxtnm1002, XATSCTAG("list_cons",1))): ## { // gpt
                      pyxtnm1005 = pyxtnm1002
                      pyxtnm1006 = XATSDAPP(auxmain_6529(XATSP1CN("list_cons", pyxtnm1005[1+1])))
                      pyxtnm1007 = XATSCAPP("strmcon_vt_cons", [1, XATSP1CN("list_cons", pyxtnm1005[0+1]), pyxtnm1006])
                      pyxtnm1008 = pyxtnm1007
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    XATS000_cfail()
                  ## } while True // end-of(do-cls)
                  ## I1CMP:return:I1Vtnm(I1TNM(1008))
                  return pyxtnm1008
                ## } // end(l1azy)
                ## I1CMP:return:I1Vtnm(I1TNM(1009))
                return pyxtnm1009
              pyxtnm1010 = XATSDAPP(auxmain_6529(pyxtnm1001))
              pyxtnm1011 = pyxtnm1010
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1011))
              return pyxtnm1011
            ## endtimp(list_strmize(1218))
            pyxtnm1013 = pyxtnm1012
            pyxtnm1014 = XATSDAPP(pyxtnm1013(pyxtnm985))
            pyxtnm1015 = pyxtnm1014
            XATS000_patck(True)
            ## let
            pyxtnm1140 = None
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(6061(line=381,offs=1)--6136(line=384,offs=38)))
            ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6461])),S2LAB(LABint(1);T2Pvar(y0[6463])))))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(5988(line=376,offs=1)--6003(line=376,offs=16))
            ## I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6461])),S2LAB(LABint(1);T2Pvar(y0[6463]))))))))
            ## T1IMPallx(list_vt_forall0(2062), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
            ## T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8837],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8837])))))))
            def pyxtnm1064(arg1): ## timp: list_vt_forall0(2062)
              pyxtnm1020 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1063 = None
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
              ## I1FUNDCL
              def test_2076(arg1): ## fun
                pyxtnm1021 = arg1
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
                ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8837])))))
                ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas001_vt.dats)@(1771(line=71,offs=1)--1820(line=73,offs=31)))
                ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[5824],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[5824])))))))
                pyxtnm1055 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gbas001_vt.dats)@(1805(line=73,offs=16)--1816(line=73,offs=27))
                ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[5824])))))
                ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(6061(line=381,offs=1)--6136(line=384,offs=38)))
                ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6460],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6461],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6462],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6463],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                def pyxtnm1054(arg1): ## timp: forall$test(47)
                  pyxtnm1022 = arg1
                  ## I1CMP:start
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(6101(line=384,offs=3)--6115(line=384,offs=17))
                  ## I0Etapq(I0Ecst(z2rforall$test(137)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(2412(line=122,offs=1)--2426(line=122,offs=15))));$list(T2JAG($list(T2Pvar(x0[6461]))),T2JAG($list(T2Pvar(y0[6463])))))
                  ## T1IMPallx(z2rforall$test(137), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2779(line=138,offs=1)--2843(line=140,offs=41)))
                  ## T1IMPallx(z2rforall$test(137)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6436],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6437],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6438],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6439],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(z2rforall$test(137);$list(@(x1[604],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[605],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                  def pyxtnm1050(arg1, arg2): ## timp: z2rforall$test(137)
                    pyxtnm1023 = arg1
                    pyxtnm1024 = arg2
                    ## I1CMP:start
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2822(line=140,offs=20)--2834(line=140,offs=32))
                    ## I0Etapq(I0Ecst(rforall$test(48)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2041(line=99,offs=1)--2053(line=99,offs=13))));$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6437])),S2LAB(LABint(1);T2Pvar(y0[6439]))))))))
                    ## T1IMPallx(rforall$test(48), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6949(line=451,offs=1)--7026(line=455,offs=33)))
                    ## T1IMPallx(rforall$test(48)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6122],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6123],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(rforall$test(48);$list(@(x0[461],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                    def pyxtnm1047(arg1): ## timp: rforall$test(48)
                      pyxtnm1025 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm1046 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6985(line=454,offs=1)--7014(line=455,offs=21)))
                      ## I1VALDCL
                      pyxtnm1045 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6994(line=455,offs=1)--7006(line=455,offs=13))
                      ## I0Etapq(I0Ecst(rforitm$work(52)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2379(line=127,offs=1)--2391(line=127,offs=13))));$list(T2JAG($list(T2Pvar(x0[6123])))))
                      ## T1IMPallx(rforitm$work(52), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8998(line=599,offs=1)--9137(line=606,offs=40)))
                      ## T1IMPallx(rforitm$work(52)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6140],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6141],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(r0[6142],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(rforitm$work(52);$list(@(x0[465],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                      def pyxtnm1043(arg1): ## timp: rforitm$work(52)
                        pyxtnm1026 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm1042 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9068(line=605,offs=1)--9097(line=605,offs=30)))
                        ## I1VALDCL
                        pyxtnm1031 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9081(line=605,offs=14)--9089(line=605,offs=22))
                        ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Pvar(r0[6142])))))
                        ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                        ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                        def pyxtnm1029(arg1): ## timp: p2tr_get(2309)
                          pyxtnm1027 = arg1
                          ## I1CMP:start
                          pyxtnm1028 = XATS000_dp2tr(pyxtnm1027)
                          ## I1CMP:return:I1Vtnm(I1TNM(1028))
                          return pyxtnm1028
                        ## endtimp(p2tr_get(2309))
                        pyxtnm1030 = XATSDAPP(pyxtnm1029(pyxtnm951))
                        pyxtnm1031 = pyxtnm1030
                        XATS000_patck(True)
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9098(line=606,offs=1)--9136(line=606,offs=39)))
                        ## I1VALDCL
                        pyxtnm1037 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9107(line=606,offs=10)--9120(line=606,offs=23))
                        ## I0Etapq(I0Ecst(rfolditm$fopr(56)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2598(line=145,offs=1)--2611(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[6141]))),T2JAG($list(T2Pvar(r0[6142])))))
                        ## T1IMPallx(rfolditm$fopr(56), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2018(line=84,offs=1)--2081(line=87,offs=32)))
                        ## T1IMPallx(rfolditm$fopr(56)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6082],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6083],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(rfolditm$fopr(56);$list(@(x0[470],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(r0[471],T2Papps(T2Pcst(list_vt);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))))
                        def pyxtnm1035(arg1, arg2): ## timp: rfolditm$fopr(56)
                          pyxtnm1032 = arg1
                          pyxtnm1033 = arg2
                          ## I1CMP:start
                          pyxtnm1034 = XATSCAPP("list_vt_cons", [1, pyxtnm1032, pyxtnm1033])
                          ## I1CMP:return:I1Vtnm(I1TNM(1034))
                          return pyxtnm1034
                        ## endtimp(rfolditm$fopr(56))
                        pyxtnm1036 = XATSDAPP(pyxtnm1035(pyxtnm1026, pyxtnm1031))
                        pyxtnm1037 = pyxtnm1036
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9038(line=602,offs=7)--9046(line=602,offs=15))
                        ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Pvar(r0[6142])))))
                        ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                        ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                        def pyxtnm1040(arg1, arg2): ## timp: p2tr_set(2310)
                          pyxtnm1038 = arg1
                          pyxtnm1039 = arg2
                          ## I1CMP:start
                          XATS000_assgn(pyxtnm1038, pyxtnm1039)
                          ## I1CMP:return:I1V000()
                          return XATSVOID
                        ## endtimp(p2tr_set(2310))
                        pyxtnm1041 = XATSDAPP(pyxtnm1040(pyxtnm951, pyxtnm1037))
                        pyxtnm1042 = pyxtnm1041
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(1042))
                        return pyxtnm1042
                      ## endtimp(rforitm$work(52))
                      pyxtnm1044 = XATSDAPP(pyxtnm1043(pyxtnm1025))
                      pyxtnm1045 = pyxtnm1044
                      XATS000_patck(True)
                      pyxtnm1046 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(1046))
                      return pyxtnm1046
                    ## endtimp(rforall$test(48))
                    pyxtnm1048 = XATSTUP1(XATSTRCD(0), [pyxtnm1023, pyxtnm1024])
                    pyxtnm1049 = XATSDAPP(pyxtnm1047(pyxtnm1048))
                    ## I1CMP:return:I1Vtnm(I1TNM(1049))
                    return pyxtnm1049
                  ## endtimp(z2rforall$test(137))
                  pyxtnm1051 = XATSPFLT(pyxtnm1022[0])
                  pyxtnm1052 = XATSPFLT(pyxtnm1022[1])
                  pyxtnm1053 = XATSDAPP(pyxtnm1050(pyxtnm1051, pyxtnm1052))
                  ## I1CMP:return:I1Vtnm(I1TNM(1053))
                  return pyxtnm1053
                ## endtimp(forall$test(47))
                pyxtnm1055 = pyxtnm1054
                pyxtnm1056 = XATSDAPP(pyxtnm1055(pyxtnm1021))
                ## I1CMP:return:I1Vtnm(I1TNM(1056))
                return pyxtnm1056
              ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
              ## I1FUNDCL
              def free_2128(arg1): ## fun
                pyxtnm1057 = arg1
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
                ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8837])))))
                ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/tupl000_vt.dats)@(2935(line=152,offs=1)--2999(line=155,offs=38)))
                ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(a0[8480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[8481],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Papps(T2Pcst(t0up_vt);$list(T2Pvar(a0[8480]),T2Pvar(a1[8481])))))))))
                def pyxtnm1060(arg1): ## timp: g_free(23)
                  pyxtnm1058 = arg1
                  ## I1CMP:start
                  pyxtnm1059 = XATSTUP0([])
                  ## I1CMP:return:I1Vtnm(I1TNM(1059))
                  return pyxtnm1059
                ## endtimp(g_free(23))
                pyxtnm1061 = XATSDAPP(pyxtnm1060(pyxtnm1057))
                ## I1CMP:return:I1Vtnm(I1TNM(1061))
                return pyxtnm1061
              pyxtnm1062 = XATSDAPP(XATS2PY_list_vt_forall0_f1un(pyxtnm1020, test_2076, free_2128))
              pyxtnm1063 = pyxtnm1062
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1063))
              return pyxtnm1063
            ## endtimp(list_vt_forall0(2062))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(6015(line=378,offs=1)--6034(line=378,offs=20))
            ## I0Etapq(I0Ecst(strm_vt_z2rlistize0(2260)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm002_vt.sats)@(4136(line=217,offs=1)--4155(line=217,offs=20))));$list(T2JAG($list(T2Pvar(x0[6461]))),T2JAG($list(T2Pvar(y0[6463])))))
            ## T1IMPallx(strm_vt_z2rlistize0(2260), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(5870(line=380,offs=1)--5997(line=387,offs=37)))
            ## T1IMPallx(strm_vt_z2rlistize0(2260)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8753],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8754],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_z2rlistize0(2260);$list(@(x0[5641],T2Pvar(x0[8753])),@(y0[5642],T2Pvar(y0[8754])))))))
            def pyxtnm1137(arg1, arg2): ## timp: strm_vt_z2rlistize0(2260)
              pyxtnm1065 = arg1
              pyxtnm1066 = arg2
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(5932(line=385,offs=1)--5949(line=385,offs=18))
              ## I0Etapq(I0Ecst(strm_vt_rlistize0(2229)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm001_vt.sats)@(9196(line=478,offs=1)--9213(line=478,offs=18))));$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[8753])),S2LAB(LABint(1);T2Pvar(y0[8754]))))))))
              ## T1IMPallx(strm_vt_rlistize0(2229), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(8143(line=518,offs=1)--8436(line=541,offs=2)))
              ## T1IMPallx(strm_vt_rlistize0(2229)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8704],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(strm_vt_rlistize0(2229);$list(@(x0[5573],T2Pvar(x0[8704])))))))
              def pyxtnm1080(arg1): ## timp: strm_vt_rlistize0(2229)
                pyxtnm1067 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1079 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(8220(line=526,offs=1)--8242(line=526,offs=23)))
                ## I1VALDCL
                pyxtnm1069 = None
                pyxtnm1068 = XATSCAPP("list_vt_nil", [0])
                pyxtnm1069 = pyxtnm1068
                XATS000_patck(True)
                ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm001_vt.dats)@(8246(line=528,offs=1)--8434(line=540,offs=35)))
                ## I1FUNDCL
                def loop_8249(arg1, arg2): ## fun
                  pyxtnm1070 = arg1
                  pyxtnm1071 = arg2
                  ## I1CMP:start
                  pyxtnm1072 = XATS000_dl1az(pyxtnm1070)
                  pyxtnm1077 = None
                  while True: ## do {
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(1073);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
                    if (XATS000_ctgeq(pyxtnm1072, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
                      pyxtnm1073 = pyxtnm1072
                      pyxtnm1077 = pyxtnm1071
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    ## { // cls
                    ## I1GPTpat(I1BNDcons(I1TNM(1074);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(4569)),I0Pvar(xs(4570)))));$list(@(x1(4569),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(1074));0)),@(xs(4570),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(1074));1)))))
                    if (XATS000_ctgeq(pyxtnm1072, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
                      pyxtnm1074 = pyxtnm1072
                      pyxtnm1075 = XATSCAPP("list_vt_cons", [1, XATSP1CN("strmcon_vt_cons", pyxtnm1074[0+1]), pyxtnm1071])
                      pyxtnm1076 = XATSDAPP(loop_8249(XATSP1CN("strmcon_vt_cons", pyxtnm1074[1+1]), pyxtnm1075))
                      pyxtnm1077 = pyxtnm1076
                      break ## cls
                    ## } // gpt
                    ## } // cls
                    XATS000_cfail()
                  ## } while True // end-of(do-cls)
                  ## I1CMP:return:I1Vtnm(I1TNM(1077))
                  return pyxtnm1077
                pyxtnm1078 = XATSDAPP(loop_8249(pyxtnm1067, pyxtnm1069))
                pyxtnm1079 = pyxtnm1078
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1079))
                return pyxtnm1079
              ## endtimp(strm_vt_rlistize0(2229))
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(5962(line=387,offs=2)--5980(line=387,offs=20))
              ## I0Etapq(I0Ecst(strm_vt_z2strmize0(2258)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm002_vt.sats)@(3947(line=205,offs=1)--3965(line=205,offs=19))));$list(T2JAG($list(T2Pvar(x0[8753]))),T2JAG($list(T2Pvar(y0[8754])))))
              ## T1IMPallx(strm_vt_z2strmize0(2258), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(6001(line=389,offs=1)--6192(line=403,offs=2)))
              ## T1IMPallx(strm_vt_z2strmize0(2258)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8755],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8756],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_z2strmize0(2258);$list(@(x0[5637],T2Pvar(x0[8755])),@(y0[5638],T2Pvar(y0[8756])))))))
              def pyxtnm1134(arg1, arg2): ## timp: strm_vt_z2strmize0(2258)
                pyxtnm1081 = arg1
                pyxtnm1082 = arg2
                ## I1CMP:start
                ## let
                pyxtnm1133 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(6112(line=399,offs=1)--6134(line=399,offs=23))
                ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(z0;S2Etrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);S2Evar(x0[8755])),S2LAB(LABint(1);S2Evar(y0[8756]))))))))
                ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(6138(line=401,offs=1)--6190(line=402,offs=44)))
                ## I1Dimplmnt0(DIMPLone2(z2map$fopr0(1564);$list(@(x0[4009],T2Pvar(x0[8755])),@(y0[4010],T2Pvar(y0[8756])),@(z0[4011],T2Pcst(z0))))):timp
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(6065(line=395,offs=2)--6079(line=395,offs=16))
                ## I0Etapq(I0Ecst(strm_vt_z2map0(2254)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm002_vt.sats)@(3127(line=152,offs=1)--3141(line=152,offs=15))));$list(T2JAG($list(T2Pvar(x0[8755]))),T2JAG($list(T2Pvar(y0[8756]))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[8755])),S2LAB(LABint(1);T2Pvar(y0[8756]))))))))
                ## T1IMPallx(strm_vt_z2map0(2254), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4041(line=237,offs=1)--4548(line=281,offs=2)))
                ## T1IMPallx(strm_vt_z2map0(2254)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8739],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8740],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(z0[8741],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(strm_vt_z2map0(2254);$list(@(x0[5625],T2Pvar(x0[8739])),@(y0[5626],T2Pvar(y0[8740])),@(z0[5627],T2Pvar(z0[8741])))))))
                def pyxtnm1131(arg1, arg2): ## timp: strm_vt_z2map0(2254)
                  pyxtnm1086 = arg1
                  pyxtnm1087 = arg2
                  ## I1CMP:start
                  ## let
                  pyxtnm1130 = None
                  ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4137(line=246,offs=1)--4537(line=280,offs=2)))
                  ## I1FUNDCL
                  def auxmain_4140(arg1, arg2): ## fun
                    pyxtnm1088 = arg1
                    pyxtnm1089 = arg2
                    ## I1CMP:start
                    def pyxtnm1128(tlaz): ## { // l1azy
                      ## I1CMP:start
                      pyxtnm1090 = XATS000_dl1az(pyxtnm1088)
                      pyxtnm1121 = None
                      while True: ## do {
                        ## { // cls
                        ## I1GPTpat(I1BNDcons(I1TNM(1091);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
                        if (XATS000_ctgeq(pyxtnm1090, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
                          pyxtnm1091 = pyxtnm1090
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4276(line=261,offs=1)--4280(line=261,offs=5))
                          ## I0Etapq(I0Ecst(strm_vt_free(2160)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm000_vt.sats)@(1995(line=91,offs=1)--2007(line=91,offs=13))));$list(T2JAG($list(T2Pvar(y0[8740])))))
                          ## T1IMPallx(strm_vt_free(2160), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm000_vt.dats)@(2418(line=125,offs=1)--2465(line=127,offs=29)))
                          ## T1IMPallx(strm_vt_free(2160)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8640],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_free(2160);$list(@(a[5466],T2Pvar(a[8640])))))))
                          def pyxtnm1093(arg1): ## timp: strm_vt_free(2160)
                            pyxtnm1092 = arg1
                            ## I1CMP:start
                            XATS000_free(pyxtnm1092)
                            ## I1CMP:return:I1V000()
                            return XATSVOID
                          ## endtimp(strm_vt_free(2160))
                          pyxtnm1094 = XATSDAPP(pyxtnm1093(pyxtnm1089))
                          pyxtnm1095 = XATSCAPP("strmcon_vt_nil", [0])
                          pyxtnm1121 = pyxtnm1095
                          break ## cls
                        ## } // gpt
                        ## } // cls
                        ## { // cls
                        ## I1GPTpat(I1BNDcons(I1TNM(1096);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(x1(4644)),I0Pvar(xs(4645)))));$list(@(x1(4644),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(1096));0)),@(xs(4645),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(1096));1)))))
                        if (XATS000_ctgeq(pyxtnm1090, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
                          pyxtnm1096 = pyxtnm1090
                          pyxtnm1097 = XATS000_dl1az(pyxtnm1089)
                          pyxtnm1120 = None
                          while True: ## do {
                            ## { // cls
                            ## I1GPTpat(I1BNDcons(I1TNM(1098);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_nil(15));$list()));$list()))
                            if (XATS000_ctgeq(pyxtnm1097, XATSCTAG("strmcon_vt_nil",0))): ## { // gpt
                              pyxtnm1098 = pyxtnm1097
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4376(line=270,offs=1)--4380(line=270,offs=5))
                              ## I0Etapq(I0Ecst(gs_free_a1(761)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(6126(line=309,offs=1)--6136(line=309,offs=11))));$list(T2JAG($list(T2Pvar(x0[8739])))))
                              ## T1IMPallx(gs_free_a1(761), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(10294(line=604,offs=1)--10355(line=609,offs=18)))
                              ## T1IMPallx(gs_free_a1(761)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[6825],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_free_a1(761);$list(@(x0[2252],T2Pvar(x0[6825])))))))
                              def pyxtnm1104(arg1): ## timp: gs_free_a1(761)
                                pyxtnm1099 = arg1
                                ## I1CMP:start
                                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(10340(line=609,offs=3)--10346(line=609,offs=9))
                                ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[6825])))))
                                ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas000.dats)@(1607(line=56,offs=1)--1647(line=58,offs=22)))
                                ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[5785],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Pvar(x0[5785])))))))
                                def pyxtnm1102(arg1): ## timp: g_free(23)
                                  pyxtnm1100 = arg1
                                  ## I1CMP:start
                                  pyxtnm1101 = XATSTUP0([])
                                  ## I1CMP:return:I1Vtnm(I1TNM(1101))
                                  return pyxtnm1101
                                ## endtimp(g_free(23))
                                pyxtnm1103 = XATSDAPP(pyxtnm1102(pyxtnm1099))
                                ## I1CMP:return:I1Vtnm(I1TNM(1103))
                                return pyxtnm1103
                              ## endtimp(gs_free_a1(761))
                              pyxtnm1105 = XATSDAPP(pyxtnm1104(XATSP1CN("strmcon_vt_cons", pyxtnm1096[0+1])))
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4386(line=271,offs=1)--4390(line=271,offs=5))
                              ## I0Etapq(I0Ecst(strm_vt_free(2160)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/strm000_vt.sats)@(1995(line=91,offs=1)--2007(line=91,offs=13))));$list(T2JAG($list(T2Pvar(x0[8739])))))
                              ## T1IMPallx(strm_vt_free(2160), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm000_vt.dats)@(2418(line=125,offs=1)--2465(line=127,offs=29)))
                              ## T1IMPallx(strm_vt_free(2160)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[8640],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(strm_vt_free(2160);$list(@(a[5466],T2Pvar(a[8640])))))))
                              def pyxtnm1107(arg1): ## timp: strm_vt_free(2160)
                                pyxtnm1106 = arg1
                                ## I1CMP:start
                                XATS000_free(pyxtnm1106)
                                ## I1CMP:return:I1V000()
                                return XATSVOID
                              ## endtimp(strm_vt_free(2160))
                              pyxtnm1108 = XATSDAPP(pyxtnm1107(XATSP1CN("strmcon_vt_cons", pyxtnm1096[1+1])))
                              pyxtnm1109 = XATSCAPP("strmcon_vt_nil", [0])
                              pyxtnm1120 = pyxtnm1109
                              break ## cls
                            ## } // gpt
                            ## } // cls
                            ## { // cls
                            ## I1GPTpat(I1BNDcons(I1TNM(1110);I0Pfree(I0Pdapp(I0Pcon(strmcon_vt_cons(16));$list(I0Pvar(y1(4646)),I0Pvar(ys(4647)))));$list(@(y1(4646),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(1110));0)),@(ys(4647),I1Vp1cn(I0Pcon(strmcon_vt_cons(16));I1Vtnm(I1TNM(1110));1)))))
                            if (XATS000_ctgeq(pyxtnm1097, XATSCTAG("strmcon_vt_cons",1))): ## { // gpt
                              pyxtnm1110 = pyxtnm1097
                              ## let
                              pyxtnm1119 = None
                              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4449(line=276,offs=1)--4489(line=277,offs=32)))
                              ## I1VALDCL
                              pyxtnm1116 = None
                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(4458(line=277,offs=1)--4469(line=277,offs=12))
                              ## I0Etapq(I0Ecst(z2map$fopr0(1564)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas002_vt.sats)@(3251(line=191,offs=1)--3262(line=191,offs=12))));$list(T2JAG($list(T2Pvar(x0[8739]))),T2JAG($list(T2Pvar(y0[8740]))),T2JAG($list(T2Pvar(z0[8741])))))
                              ## T1IMPallx(z2map$fopr0(1564), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/strm002_vt.dats)@(6138(line=401,offs=1)--6190(line=402,offs=44)))
                              ## T1IMPallx(z2map$fopr0(1564)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8755],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[8756],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(z2map$fopr0(1564);$list(@(x0[4009],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[4010],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(z0[4011],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                              def pyxtnm1114(arg1, arg2): ## timp: z2map$fopr0(1564)
                                pyxtnm1111 = arg1
                                pyxtnm1112 = arg2
                                ## I1CMP:start
                                pyxtnm1113 = XATSTUP1(XATSTRCD(0), [pyxtnm1111, pyxtnm1112])
                                ## I1CMP:return:I1Vtnm(I1TNM(1113))
                                return pyxtnm1113
                              ## endtimp(z2map$fopr0(1564))
                              pyxtnm1115 = XATSDAPP(pyxtnm1114(XATSP1CN("strmcon_vt_cons", pyxtnm1096[0+1]), XATSP1CN("strmcon_vt_cons", pyxtnm1110[0+1])))
                              pyxtnm1116 = pyxtnm1115
                              XATS000_patck(True)
                              pyxtnm1117 = XATSDAPP(auxmain_4140(XATSP1CN("strmcon_vt_cons", pyxtnm1096[1+1]), XATSP1CN("strmcon_vt_cons", pyxtnm1110[1+1])))
                              pyxtnm1118 = XATSCAPP("strmcon_vt_cons", [1, pyxtnm1116, pyxtnm1117])
                              pyxtnm1119 = pyxtnm1118
                              ## end-of(let)
                              pyxtnm1120 = pyxtnm1119
                              break ## cls
                            ## } // gpt
                            ## } // cls
                            XATS000_cfail()
                          ## } while True // end-of(do-cls)
                          pyxtnm1121 = pyxtnm1120
                          break ## cls
                        ## } // gpt
                        ## } // cls
                        XATS000_cfail()
                      ## } while True // end-of(do-cls)
                      ## I1CMP:return:I1Vtnm(I1TNM(1121))
                      return pyxtnm1121
                    ## } // end(l1azy)
                    ## I1CMP:return:I1Vtnm(I1TNM(1128))
                    return pyxtnm1128
                  pyxtnm1129 = XATSDAPP(auxmain_4140(pyxtnm1086, pyxtnm1087))
                  pyxtnm1130 = pyxtnm1129
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1130))
                  return pyxtnm1130
                ## endtimp(strm_vt_z2map0(2254))
                pyxtnm1132 = XATSDAPP(pyxtnm1131(pyxtnm1081, pyxtnm1082))
                pyxtnm1133 = pyxtnm1132
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1133))
                return pyxtnm1133
              ## endtimp(strm_vt_z2strmize0(2258))
              pyxtnm1135 = XATSDAPP(pyxtnm1134(pyxtnm1065, pyxtnm1066))
              pyxtnm1136 = XATSDAPP(pyxtnm1080(pyxtnm1135))
              ## I1CMP:return:I1Vtnm(I1TNM(1136))
              return pyxtnm1136
            ## endtimp(strm_vt_z2rlistize0(2260))
            pyxtnm1138 = XATSDAPP(pyxtnm1137(pyxtnm1000, pyxtnm1015))
            pyxtnm1139 = XATSDAPP(pyxtnm1064(pyxtnm1138))
            pyxtnm1140 = pyxtnm1139
            ## end-of(let)
            pyxtnm1141 = pyxtnm1140
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1141))
            return pyxtnm1141
          ## endtimp(gseq_z2rforall(546))
          pyxtnm1143 = XATSDAPP(pyxtnm1142(pyxtnm974, pyxtnm979))
          pyxtnm1144 = pyxtnm1143
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1144))
          return pyxtnm1144
        ## endtimp(gseq_rforall(388))
        pyxtnm1146 = XATSDAPP(pyxtnm1145(pyxtnm959))
        pyxtnm1147 = pyxtnm1146
        XATS000_patck(True)
        pyxtnm1148 = XATSVOID
        ## end-of(let)
        pyxtnm1149 = pyxtnm1148
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1149))
        return pyxtnm1149
      ## endtimp(gseq_rforitm(403))
      pyxtnm1151 = XATSDAPP(pyxtnm1150(pyxtnm948))
      pyxtnm1152 = pyxtnm1151
      ## end-of(let)
      pyxtnm1153 = pyxtnm1152
      XATS000_patck(True)
      pyxtnm1154 = XATSFLAT(pyxtnm950)
      pyxtnm1155 = pyxtnm1154
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(1155))
      return pyxtnm1155
    ## endtimp(gseq_rfolditm(411))
    pyxtnm1157 = XATSDAPP(pyxtnm1156(pyxtnm942, pyxtnm944))
    pyxtnm1158 = pyxtnm1157
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(1158))
    return pyxtnm1158
  ## endtimp(gseq_listize(377))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2554(line=132,offs=10)--2563(line=132,offs=19))
  ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6663]))),T2JAG($list(T2Pvar(x0[6664])))))
  ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
  ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6650],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
  def pyxtnm1162(arg1): ## timp: GSEQ_unmk(245)
    pyxtnm1160 = arg1
    ## I1CMP:start
    pyxtnm1161 = XATSCAST("castxy_1839", [pyxtnm1160])
    ## I1CMP:return:I1Vtnm(I1TNM(1161))
    return pyxtnm1161
  ## endtimp(GSEQ_unmk(245))
  pyxtnm1163 = XATSDAPP(pyxtnm1162(pyxtnm941))
  pyxtnm1164 = XATSDAPP(pyxtnm1159(pyxtnm1163))
  ## I1CMP:return:I1Vtnm(I1TNM(1164))
  return pyxtnm1164
## endtimp(GSEQ_listize(251))
pyxtnm1166 = XATSDAPP(pyxtnm1165(pyxtnm701))
pyxtnm1167 = pyxtnm1166
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(775(line=48,offs=1)--825(line=49,offs=40)))
## I1VALDCL
pyxtnm1367 = None
## LCSRCsome1(test07_gseq000.dats)@(786(line=49,offs=1)--793(line=49,offs=8))
## I0Etapq(I0Ecst(gs_print1_a3(1988)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3614(line=218,offs=1)--3626(line=218,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print1_a3(1988), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5507(line=274,offs=1)--5674(line=283,offs=21)))
## T1IMPallx(gs_print1_a3(1988)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8381],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8382],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x2[8383],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a3(1988);$list(@(x0[5119],T2Pvar(x0[8381])),@(x1[5120],T2Pvar(x1[8382])),@(x2[5121],T2Pvar(x2[8383])))))))
def pyxtnm1365(arg1, arg2, arg3): ## timp: gs_print1_a3(1988)
  pyxtnm1168 = arg1
  pyxtnm1169 = arg2
  pyxtnm1170 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5578(line=280,offs=3)--5591(line=280,offs=16))
  ## I0Etapq(I0Ecst(gs_print1$beg(1972)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print1$beg(1972), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
  ## T1IMPallx(gs_print1$beg(1972)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$beg(1972);$list()))))
  def pyxtnm1172(): ## timp: gs_print1$beg(1972)
    ## I1CMP:start
    pyxtnm1171 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(1171))
    return pyxtnm1171
  ## endtimp(gs_print1$beg(1972))
  pyxtnm1173 = XATSDAPP(pyxtnm1172())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5599(line=281,offs=3)--5607(line=281,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[8381])))))
  ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
  pyxtnm1180 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm1179 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm1178(arg1): ## timp: strn_print(1040)
    pyxtnm1174 = arg1
    ## I1CMP:start
    ## let
    pyxtnm1177 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1175);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1175))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm1176 = XATSDAPP(XATS2PY_strn_print(pyxtnm1174))
    pyxtnm1177 = pyxtnm1176
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(1177))
    return pyxtnm1177
  ## endtimp(strn_print(1040))
  pyxtnm1179 = pyxtnm1178
  pyxtnm1180 = pyxtnm1179
  pyxtnm1181 = XATSDAPP(pyxtnm1180(pyxtnm1168))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5618(line=282,offs=3)--5626(line=282,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[8382])))))
  ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2935(line=156,offs=1)--3019(line=162,offs=2)))
  ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8498],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8498])))))))))
  def pyxtnm1352(arg1): ## timp: g_print1(1412)
    pyxtnm1182 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2985(line=161,offs=1)--2996(line=161,offs=12))
    ## I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[8498]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[8498])))))
    ## T1IMPallx(gseq_print1(1687), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
    ## T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x0[7906],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
    def pyxtnm1350(arg1): ## timp: gseq_print1(1687)
      pyxtnm1183 = arg1
      ## I1CMP:start
      ## let
      pyxtnm1349 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
      ## I1VALDCL
      pyxtnm1192 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm1188(arg1): ## timp: strn_print(1040)
        pyxtnm1184 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1187 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1185);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1185))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm1186 = XATSDAPP(XATS2PY_strn_print(pyxtnm1184))
        pyxtnm1187 = pyxtnm1186
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1187))
        return pyxtnm1187
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8496],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(x0[8496],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8496])))),@(x0[1068],T2Pvar(x0[8496])))))))
      def pyxtnm1189(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("list_vt(")
      ## endtimp(gseq$beg(346))
      pyxtnm1190 = XATSDAPP(pyxtnm1189())
      pyxtnm1191 = XATSDAPP(pyxtnm1188(pyxtnm1190))
      pyxtnm1192 = pyxtnm1191
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
      ## I1VALDCL
      pyxtnm1339 = None
      ## let
      pyxtnm1338 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq_iforitm1(1760), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x0[8041],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
      def pyxtnm1336(arg1): ## timp: gseq_iforitm1(1760)
        pyxtnm1202 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1335 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
        ## let
        pyxtnm1334 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
        ## I1VALDCL
        pyxtnm1333 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
        ## T1IMPallx(gseq_iforall1(1736), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
        ## T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x0[8009],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
        def pyxtnm1331(arg1): ## timp: gseq_iforall1(1736)
          pyxtnm1208 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1330 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm1209 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
          ## I1VALDCL
          pyxtnm1210 = None
          pyxtnm1210 = XATSADDR(pyxtnm1209)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
          ## I1VALDCL
          pyxtnm1329 = None
          ## let
          pyxtnm1328 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
          ## T1IMPallx(gseq_forall1(1720), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2048(line=94,offs=1)--2119(line=97,offs=40)))
          ## T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8546],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(x0[8546],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8546])))),@(x0[4325],T2Pvar(x0[8546])))))))
          pyxtnm1326 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2100(line=97,offs=21)--2115(line=97,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall1(2063)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1481(line=47,offs=1)--1496(line=47,offs=16))));$list(T2JAG($list(T2Pvar(x0[8546])))))
          ## T1IMPallx(list_vt_forall1(2063), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1707(line=67,offs=1)--1964(line=88,offs=2)))
          ## T1IMPallx(list_vt_forall1(2063)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8544],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(list_vt_forall1(2063);$list(@(x0[5291],T2Pvar(x0[8544])))))))
          def pyxtnm1325(arg1): ## timp: list_vt_forall1(2063)
            pyxtnm1219 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1324 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1777(line=74,offs=1)--1962(line=87,offs=38)))
            ## I1FUNDCL
            def loop_1780(arg1): ## fun
              pyxtnm1220 = arg1
              ## I1CMP:start
              pyxtnm1322 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(1221);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
                if (XATS000_ctgeq(pyxtnm1220, XATSCTAG("list_vt_nil",0))): ## { // gpt
                  pyxtnm1221 = pyxtnm1220
                  pyxtnm1322 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(1222);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(4347)),I0Pvar(xs(4348))));$list(@(x1(4347),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(1222));0)),@(xs(4348),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(1222));1)))))
                if (XATS000_ctgeq(pyxtnm1220, XATSCTAG("list_vt_cons",1))): ## { // gpt
                  pyxtnm1222 = pyxtnm1220
                  ## let
                  pyxtnm1321 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1890(line=85,offs=1)--1921(line=86,offs=21)))
                  ## I1VALDCL
                  pyxtnm1318 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1901(line=86,offs=1)--1913(line=86,offs=13))
                  ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8544])))))
                  ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                  ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x0[8009],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                  def pyxtnm1316(arg1): ## timp: forall$test1(1423)
                    pyxtnm1223 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm1315 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                    ## I1VALDCL
                    pyxtnm1228 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                    def pyxtnm1226(arg1): ## timp: p2tr_get(2309)
                      pyxtnm1224 = arg1
                      ## I1CMP:start
                      pyxtnm1225 = XATS000_dp2tr(pyxtnm1224)
                      ## I1CMP:return:I1Vtnm(I1TNM(1225))
                      return pyxtnm1225
                    ## endtimp(p2tr_get(2309))
                    pyxtnm1227 = XATSDAPP(pyxtnm1226(pyxtnm1210))
                    pyxtnm1228 = pyxtnm1227
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                    ## I1VALDCL
                    pyxtnm1302 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                    ## T1IMPallx(iforall$test1(1433), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                    ## T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x0[8041],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                    def pyxtnm1300(arg1, arg2): ## timp: iforall$test1(1433)
                      pyxtnm1229 = arg1
                      pyxtnm1230 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm1299 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                      ## I1VALDCL
                      pyxtnm1298 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                      ## I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                      ## T1IMPallx(iforitm$work1(1449), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                      ## T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0()))),@(x0[7906],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                      def pyxtnm1296(arg1, arg2): ## timp: iforitm$work1(1449)
                        pyxtnm1231 = arg1
                        pyxtnm1232 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm1295 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                        ## I1VALDCL
                        pyxtnm1250 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                        def pyxtnm1239(arg1, arg2): ## timp: sint_gt$sint(928)
                          pyxtnm1233 = arg1
                          pyxtnm1234 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm1238 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(1235);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(1235))))),I1BNDcons(I1TNM(1236);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(1236))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm1237 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm1233, pyxtnm1234))
                          pyxtnm1238 = pyxtnm1237
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(1238))
                          return pyxtnm1238
                        ## endtimp(sint_gt$sint(928))
                        pyxtnm1240 = XATSDAPP(pyxtnm1239(pyxtnm1231, XATSINT1(0)))
                        pyxtnm1249 = None
                        if (pyxtnm1240):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm1245(arg1): ## timp: strn_print(1040)
                            pyxtnm1241 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm1244 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1242);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1242))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm1243 = XATSDAPP(XATS2PY_strn_print(pyxtnm1241))
                            pyxtnm1244 = pyxtnm1243
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(1244))
                            return pyxtnm1244
                          ## endtimp(strn_print(1040))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                          ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                          ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                          ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8494],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(x0[8494],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                          def pyxtnm1246(): ## timp: gseq$sep(348)
                            ## I1CMP:start
                            ## I1CMP:return:I1Vstr(...)
                            return XATSSTRN(",")
                          ## endtimp(gseq$sep(348))
                          pyxtnm1247 = XATSDAPP(pyxtnm1246())
                          pyxtnm1248 = XATSDAPP(pyxtnm1245(pyxtnm1247))
                          pyxtnm1249 = pyxtnm1248
                        ## else: None
                        ## end-of(if)
                        pyxtnm1250 = pyxtnm1249
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                        ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                        ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                        ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8803],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                        pyxtnm1293 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                        ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                        ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2567(line=116,offs=1)--2780(line=135,offs=4)))
                        ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(a0[7362],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7363],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7362]),T2Pvar(a1[7363])))))))))
                        def pyxtnm1292(arg1): ## timp: g_print(39)
                          pyxtnm1251 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm1291 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2635(line=124,offs=1)--2662(line=125,offs=19)))
                          ## I1VALDCL
                          pyxtnm1258 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2646(line=125,offs=3)--2656(line=125,offs=13))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm1256(arg1): ## timp: strn_print(1040)
                            pyxtnm1252 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm1255 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1253);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1253))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm1254 = XATSDAPP(XATS2PY_strn_print(pyxtnm1252))
                            pyxtnm1255 = pyxtnm1254
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(1255))
                            return pyxtnm1255
                          ## endtimp(strn_print(1040))
                          pyxtnm1257 = XATSDAPP(pyxtnm1256(XATSSTRN("@(")))
                          pyxtnm1258 = pyxtnm1257
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2663(line=126,offs=1)--2692(line=127,offs=21)))
                          ## I1VALDCL
                          pyxtnm1267 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2674(line=127,offs=3)--2681(line=127,offs=10))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(a0[7362])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                          pyxtnm1264 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                          ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                          ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                          def pyxtnm1263(arg1): ## timp: sint_print(922)
                            pyxtnm1259 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm1262 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(1260);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(1260))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                            pyxtnm1261 = XATSDAPP(XATS2PY_sint_print(pyxtnm1259))
                            pyxtnm1262 = pyxtnm1261
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(1262))
                            return pyxtnm1262
                          ## endtimp(sint_print(922))
                          pyxtnm1264 = pyxtnm1263
                          pyxtnm1265 = XATSPFLT(pyxtnm1251[0])
                          pyxtnm1266 = XATSDAPP(pyxtnm1264(pyxtnm1265))
                          pyxtnm1267 = pyxtnm1266
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2696(line=129,offs=1)--2715(line=129,offs=20)))
                          ## I1VALDCL
                          pyxtnm1274 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2705(line=129,offs=10)--2710(line=129,offs=15))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm1272(arg1): ## timp: strn_print(1040)
                            pyxtnm1268 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm1271 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1269);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1269))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm1270 = XATSDAPP(XATS2PY_strn_print(pyxtnm1268))
                            pyxtnm1271 = pyxtnm1270
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(1271))
                            return pyxtnm1271
                          ## endtimp(strn_print(1040))
                          pyxtnm1273 = XATSDAPP(pyxtnm1272(XATSSTRN(",")))
                          pyxtnm1274 = pyxtnm1273
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2716(line=130,offs=1)--2745(line=131,offs=21)))
                          ## I1VALDCL
                          pyxtnm1283 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2727(line=131,offs=3)--2734(line=131,offs=10))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(a1[7363])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                          pyxtnm1280 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                          ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                          ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                          def pyxtnm1279(arg1): ## timp: sint_print(922)
                            pyxtnm1275 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm1278 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(1276);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(1276))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                            pyxtnm1277 = XATSDAPP(XATS2PY_sint_print(pyxtnm1275))
                            pyxtnm1278 = pyxtnm1277
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(1278))
                            return pyxtnm1278
                          ## endtimp(sint_print(922))
                          pyxtnm1280 = pyxtnm1279
                          pyxtnm1281 = XATSPFLT(pyxtnm1251[1])
                          pyxtnm1282 = XATSDAPP(pyxtnm1280(pyxtnm1281))
                          pyxtnm1283 = pyxtnm1282
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2749(line=133,offs=1)--2773(line=133,offs=25)))
                          ## I1VALDCL
                          pyxtnm1290 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2758(line=133,offs=10)--2768(line=133,offs=20))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm1288(arg1): ## timp: strn_print(1040)
                            pyxtnm1284 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm1287 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1285);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1285))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm1286 = XATSDAPP(XATS2PY_strn_print(pyxtnm1284))
                            pyxtnm1287 = pyxtnm1286
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(1287))
                            return pyxtnm1287
                          ## endtimp(strn_print(1040))
                          pyxtnm1289 = XATSDAPP(pyxtnm1288(XATSSTRN(")")))
                          pyxtnm1290 = pyxtnm1289
                          XATS000_patck(True)
                          pyxtnm1291 = XATSVOID
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(1291))
                          return pyxtnm1291
                        ## endtimp(g_print(39))
                        pyxtnm1293 = pyxtnm1292
                        pyxtnm1294 = XATSDAPP(pyxtnm1293(pyxtnm1232))
                        pyxtnm1295 = pyxtnm1294
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(1295))
                        return pyxtnm1295
                      ## endtimp(iforitm$work1(1449))
                      pyxtnm1297 = XATSDAPP(pyxtnm1296(pyxtnm1229, pyxtnm1230))
                      pyxtnm1298 = pyxtnm1297
                      XATS000_patck(True)
                      pyxtnm1299 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(1299))
                      return pyxtnm1299
                    ## endtimp(iforall$test1(1433))
                    pyxtnm1301 = XATSDAPP(pyxtnm1300(pyxtnm1228, pyxtnm1223))
                    pyxtnm1302 = pyxtnm1301
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                    def pyxtnm1305(arg1, arg2): ## timp: p2tr_set(2310)
                      pyxtnm1303 = arg1
                      pyxtnm1304 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm1303, pyxtnm1304)
                      ## I1CMP:return:I1V000()
                      return XATSVOID
                    ## endtimp(p2tr_set(2310))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                    def pyxtnm1312(arg1, arg2): ## timp: sint_add$sint(936)
                      pyxtnm1306 = arg1
                      pyxtnm1307 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm1311 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(1308);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(1308))))),I1BNDcons(I1TNM(1309);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(1309))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm1310 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm1306, pyxtnm1307))
                      pyxtnm1311 = pyxtnm1310
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(1311))
                      return pyxtnm1311
                    ## endtimp(sint_add$sint(936))
                    pyxtnm1313 = XATSDAPP(pyxtnm1312(pyxtnm1228, XATSINT1(1)))
                    pyxtnm1314 = XATSDAPP(pyxtnm1305(pyxtnm1210, pyxtnm1313))
                    pyxtnm1315 = pyxtnm1302
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(1315))
                    return pyxtnm1315
                  ## endtimp(forall$test1(1423))
                  pyxtnm1317 = XATSDAPP(pyxtnm1316(XATSP1CN("list_vt_cons", pyxtnm1222[0+1])))
                  pyxtnm1318 = pyxtnm1317
                  XATS000_patck(True)
                  pyxtnm1320 = None
                  if (pyxtnm1318):
                    pyxtnm1319 = XATSDAPP(loop_1780(XATSP1CN("list_vt_cons", pyxtnm1222[1+1])))
                    pyxtnm1320 = pyxtnm1319
                  else:
                    pyxtnm1320 = XATSBOOL(False)
                  ## end-of(if)
                  pyxtnm1321 = pyxtnm1320
                  ## end-of(let)
                  pyxtnm1322 = pyxtnm1321
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:I1Vtnm(I1TNM(1322))
              return pyxtnm1322
            pyxtnm1323 = XATSDAPP(loop_1780(pyxtnm1219))
            pyxtnm1324 = pyxtnm1323
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1324))
            return pyxtnm1324
          ## endtimp(list_vt_forall1(2063))
          pyxtnm1326 = pyxtnm1325
          pyxtnm1327 = XATSDAPP(pyxtnm1326(pyxtnm1208))
          pyxtnm1328 = pyxtnm1327
          ## end-of(let)
          pyxtnm1329 = pyxtnm1328
          XATS000_patck(True)
          pyxtnm1330 = pyxtnm1329
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1330))
          return pyxtnm1330
        ## endtimp(gseq_iforall1(1736))
        pyxtnm1332 = XATSDAPP(pyxtnm1331(pyxtnm1202))
        pyxtnm1333 = pyxtnm1332
        XATS000_patck(True)
        pyxtnm1334 = XATSVOID
        ## end-of(let)
        pyxtnm1335 = pyxtnm1334
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1335))
        return pyxtnm1335
      ## endtimp(gseq_iforitm1(1760))
      pyxtnm1337 = XATSDAPP(pyxtnm1336(pyxtnm1183))
      pyxtnm1338 = pyxtnm1337
      ## end-of(let)
      pyxtnm1339 = pyxtnm1338
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
      ## I1VALDCL
      pyxtnm1348 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm1344(arg1): ## timp: strn_print(1040)
        pyxtnm1340 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1343 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1341);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1341))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm1342 = XATSDAPP(XATS2PY_strn_print(pyxtnm1340))
        pyxtnm1343 = pyxtnm1342
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1343))
        return pyxtnm1343
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(x0[8495],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),@(x0[8495],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8495])))),@(x0[1070],T2Pvar(x0[8495])))))))
      def pyxtnm1345(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm1346 = XATSDAPP(pyxtnm1345())
      pyxtnm1347 = XATSDAPP(pyxtnm1344(pyxtnm1346))
      pyxtnm1348 = pyxtnm1347
      XATS000_patck(True)
      pyxtnm1349 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(1349))
      return pyxtnm1349
    ## endtimp(gseq_print1(1687))
    pyxtnm1351 = XATSDAPP(pyxtnm1350(pyxtnm1182))
    ## I1CMP:return:I1Vtnm(I1TNM(1351))
    return pyxtnm1351
  ## endtimp(g_print1(1412))
  pyxtnm1353 = XATSDAPP(pyxtnm1352(pyxtnm1169))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5636(line=282,offs=21)--5644(line=282,offs=29))
  ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[8383])))))
  ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
  pyxtnm1360 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm1359 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm1358(arg1): ## timp: strn_print(1040)
    pyxtnm1354 = arg1
    ## I1CMP:start
    ## let
    pyxtnm1357 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1355);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1355))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm1356 = XATSDAPP(XATS2PY_strn_print(pyxtnm1354))
    pyxtnm1357 = pyxtnm1356
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(1357))
    return pyxtnm1357
  ## endtimp(strn_print(1040))
  pyxtnm1359 = pyxtnm1358
  pyxtnm1360 = pyxtnm1359
  pyxtnm1361 = XATSDAPP(pyxtnm1360(pyxtnm1170))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5656(line=283,offs=3)--5669(line=283,offs=16))
  ## I0Etapq(I0Ecst(gs_print1$end(1973)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print1$end(1973), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
  ## T1IMPallx(gs_print1$end(1973)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$end(1973);$list()))))
  def pyxtnm1363(): ## timp: gs_print1$end(1973)
    ## I1CMP:start
    pyxtnm1362 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(1362))
    return pyxtnm1362
  ## endtimp(gs_print1$end(1973))
  pyxtnm1364 = XATSDAPP(pyxtnm1363())
  ## I1CMP:return:I1Vtnm(I1TNM(1364))
  return pyxtnm1364
## endtimp(gs_print1_a3(1988))
pyxtnm1366 = XATSDAPP(pyxtnm1365(XATSSTRN("listize(ztup) = "), pyxtnm1167, XATSSTRN("\n")))
pyxtnm1367 = pyxtnm1366
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(852(line=53,offs=1)--892(line=55,offs=17)))
## I1VALDCL
pyxtnm1380 = None
## LCSRCsome1(test07_gseq000.dats)@(864(line=54,offs=1)--875(line=54,offs=12))
## I0Etapq(I0Ecst(GSEQ_x2make(593)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq002.sats)@(9581(line=634,offs=1)--9592(line=634,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))
## T1IMPallx(GSEQ_x2make(593), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3586(line=198,offs=1)--3697(line=205,offs=35)))
## T1IMPallx(GSEQ_x2make(593)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6444],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6445],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6446],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(y0[6447],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(GSEQ_x2make(593);$list(@(xs[1870],T2Pvar(xs[6444])),@(x0[1871],T2Pvar(x0[6445])),@(ys[1872],T2Pvar(ys[6446])),@(y0[1873],T2Pvar(y0[6447])))))))
def pyxtnm1377(arg1, arg2): ## timp: GSEQ_x2make(593)
  pyxtnm1368 = arg1
  pyxtnm1369 = arg2
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3674(line=205,offs=12)--3684(line=205,offs=22))
  ## I0Etapq(I0Ecst(x2tup_make(176)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(5696(line=382,offs=1)--5706(line=382,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(xs[6444]),T2Pvar(x0[6445]))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(ys[6446]),T2Pvar(y0[6447])))))))
  ## T1IMPallx(x2tup_make(176), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1854(line=72,offs=1)--1931(line=78,offs=23)))
  ## T1IMPallx(x2tup_make(176)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))>;I1Dtmpsub($list(@(a0[5806],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5807],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))));I1Dimplmnt0(DIMPLone2(x2tup_make(176);$list(@(xs[712],T2Pvar(a0[5806])),@(ys[713],T2Pvar(a1[5807])))))))
  def pyxtnm1374(arg1, arg2): ## timp: x2tup_make(176)
    pyxtnm1370 = arg1
    pyxtnm1371 = arg2
    ## I1CMP:start
    pyxtnm1372 = XATSTUP1(XATSTRCD(0), [pyxtnm1370, pyxtnm1371])
    pyxtnm1373 = XATSCAST("castxy_1839", [pyxtnm1372])
    ## I1CMP:return:I1Vtnm(I1TNM(1373))
    return pyxtnm1373
  ## endtimp(x2tup_make(176))
  pyxtnm1375 = XATSDAPP(pyxtnm1374(pyxtnm1368, pyxtnm1369))
  pyxtnm1376 = XATSCAST("castxy_1839", [pyxtnm1375])
  ## I1CMP:return:I1Vtnm(I1TNM(1376))
  return pyxtnm1376
## endtimp(GSEQ_x2make(593))
pyxtnm1378 = XATSCAST("GSEQ_make_list_5900", [pyxtnm16])
pyxtnm1379 = XATSDAPP(pyxtnm1377(pyxtnm1378, pyxtnm701))
pyxtnm1380 = pyxtnm1379
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(893(line=56,offs=1)--936(line=57,offs=32)))
## I1VALDCL
pyxtnm1773 = None
## LCSRCsome1(test07_gseq000.dats)@(905(line=57,offs=1)--911(line=57,offs=7))
## I0Etapq(I0Ecst(gs_print_a3(808)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11856(line=754,offs=1)--11867(line=754,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print_a3(808), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21342(line=1316,offs=1)--21554(line=1330,offs=4)))
## T1IMPallx(gs_print_a3(808)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7020],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[7021],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),@(x2[7022],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print_a3(808);$list(@(x0[2489],T2Pvar(x0[7020])),@(x1[2490],T2Pvar(x1[7021])),@(x2[2491],T2Pvar(x2[7022])))))))
def pyxtnm1771(arg1, arg2, arg3): ## timp: gs_print_a3(808)
  pyxtnm1381 = arg1
  pyxtnm1382 = arg2
  pyxtnm1383 = arg3
  ## I1CMP:start
  ## let
  pyxtnm1770 = None
  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21414(line=1324,offs=1)--21437(line=1325,offs=15)))
  ## I1VALDCL
  pyxtnm1387 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21423(line=1325,offs=1)--21435(line=1325,offs=13))
  ## I0Etapq(I0Ecst(gs_print$beg(802)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11602(line=730,offs=1)--11614(line=730,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$beg(802), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20714(line=1268,offs=1)--20752(line=1270,offs=20)))
  ## T1IMPallx(gs_print$beg(802)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$beg(802);$list()))))
  def pyxtnm1385(): ## timp: gs_print$beg(802)
    ## I1CMP:start
    pyxtnm1384 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(1384))
    return pyxtnm1384
  ## endtimp(gs_print$beg(802))
  pyxtnm1386 = XATSDAPP(pyxtnm1385())
  pyxtnm1387 = pyxtnm1386
  XATS000_patck(True)
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21450(line=1327,offs=3)--21457(line=1327,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[7020])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm1393 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm1392(arg1): ## timp: strn_print(1040)
    pyxtnm1388 = arg1
    ## I1CMP:start
    ## let
    pyxtnm1391 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1389);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1389))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm1390 = XATSDAPP(XATS2PY_strn_print(pyxtnm1388))
    pyxtnm1391 = pyxtnm1390
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(1391))
    return pyxtnm1391
  ## endtimp(strn_print(1040))
  pyxtnm1393 = pyxtnm1392
  pyxtnm1394 = XATSDAPP(pyxtnm1393(pyxtnm1381))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21467(line=1327,offs=20)--21479(line=1327,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm1396(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm1395 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(1395))
    return pyxtnm1395
  ## endtimp(gs_print$sep(803))
  pyxtnm1397 = XATSDAPP(pyxtnm1396())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21484(line=1328,offs=3)--21491(line=1328,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x1[7021])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2332(line=119,offs=1)--2432(line=124,offs=27)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))))>;I1Dtmpsub($list(@(t0[5762],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pvar(t0[5762])))))))
  def pyxtnm1755(arg1): ## timp: g_print(39)
    pyxtnm1398 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2367(line=122,offs=3)--2372(line=122,offs=8))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm1403(arg1): ## timp: strn_print(1040)
      pyxtnm1399 = arg1
      ## I1CMP:start
      ## let
      pyxtnm1402 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1400);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1400))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm1401 = XATSDAPP(XATS2PY_strn_print(pyxtnm1399))
      pyxtnm1402 = pyxtnm1401
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(1402))
      return pyxtnm1402
    ## endtimp(strn_print(1040))
    pyxtnm1404 = XATSDAPP(pyxtnm1403(XATSSTRN("$val(")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2382(line=123,offs=3)--2389(line=123,offs=10))
    ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[5762])))))
    ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
    ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6652],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
    def pyxtnm1733(): ## timp: g_ptype(202)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm1409(arg1): ## timp: strn_print(1040)
        pyxtnm1405 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1408 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1406);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1406))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm1407 = XATSDAPP(XATS2PY_strn_print(pyxtnm1405))
        pyxtnm1408 = pyxtnm1407
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1408))
        return pyxtnm1408
      ## endtimp(strn_print(1040))
      pyxtnm1410 = XATSDAPP(pyxtnm1409(XATSSTRN("GSEQ(")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(2004(line=85,offs=1)--2143(line=93,offs=29)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))>;I1Dtmpsub($list(@(a0[5810],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5811],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(x2tup);$list(T2Pvar(a0[5810]),T2Pvar(a1[5811])))))))))
      def pyxtnm1655(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(2073(line=91,offs=3)--2078(line=91,offs=8))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm1415(arg1): ## timp: strn_print(1040)
          pyxtnm1411 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1414 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1412);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1412))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm1413 = XATSDAPP(XATS2PY_strn_print(pyxtnm1411))
          pyxtnm1414 = pyxtnm1413
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1414))
          return pyxtnm1414
        ## endtimp(strn_print(1040))
        pyxtnm1416 = XATSDAPP(pyxtnm1415(XATSSTRN("x2tup(")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(2089(line=92,offs=3)--2096(line=92,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[5810])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6652],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
        def pyxtnm1465(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1421(arg1): ## timp: strn_print(1040)
            pyxtnm1417 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1420 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1418);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1418))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1419 = XATSDAPP(XATS2PY_strn_print(pyxtnm1417))
            pyxtnm1420 = pyxtnm1419
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1420))
            return pyxtnm1420
          ## endtimp(strn_print(1040))
          pyxtnm1422 = XATSDAPP(pyxtnm1421(XATSSTRN("GSEQ(")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1626(line=57,offs=1)--1728(line=64,offs=32)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(t0[7401],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(list);$list(T2Pvar(t0[7401])))))))))
          def pyxtnm1443(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1681(line=63,offs=1)--1686(line=63,offs=6))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1427(arg1): ## timp: strn_print(1040)
              pyxtnm1423 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1426 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1424);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1424))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1425 = XATSDAPP(XATS2PY_strn_print(pyxtnm1423))
              pyxtnm1426 = pyxtnm1425
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1426))
              return pyxtnm1426
            ## endtimp(strn_print(1040))
            pyxtnm1428 = XATSDAPP(pyxtnm1427(XATSSTRN("list(")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1697(line=64,offs=1)--1704(line=64,offs=8))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[7401])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
            def pyxtnm1435(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1433(arg1): ## timp: strn_print(1040)
                pyxtnm1429 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1432 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1430);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1430))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1431 = XATSDAPP(XATS2PY_strn_print(pyxtnm1429))
                pyxtnm1432 = pyxtnm1431
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1432))
                return pyxtnm1432
              ## endtimp(strn_print(1040))
              pyxtnm1434 = XATSDAPP(pyxtnm1433(XATSSTRN("sint")))
              ## I1CMP:return:I1Vtnm(I1TNM(1434))
              return pyxtnm1434
            ## endtimp(g_ptype(202))
            pyxtnm1436 = XATSDAPP(pyxtnm1435())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1717(line=64,offs=21)--1722(line=64,offs=26))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1441(arg1): ## timp: strn_print(1040)
              pyxtnm1437 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1440 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1438);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1438))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1439 = XATSDAPP(XATS2PY_strn_print(pyxtnm1437))
              pyxtnm1440 = pyxtnm1439
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1440))
              return pyxtnm1440
            ## endtimp(strn_print(1040))
            pyxtnm1442 = XATSDAPP(pyxtnm1441(XATSSTRN(")")))
            ## I1CMP:return:I1Vtnm(I1TNM(1442))
            return pyxtnm1442
          ## endtimp(g_ptype(202))
          pyxtnm1444 = XATSDAPP(pyxtnm1443())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1449(arg1): ## timp: strn_print(1040)
            pyxtnm1445 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1448 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1446);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1446))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1447 = XATSDAPP(XATS2PY_strn_print(pyxtnm1445))
            pyxtnm1448 = pyxtnm1447
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1448))
            return pyxtnm1448
          ## endtimp(strn_print(1040))
          pyxtnm1450 = XATSDAPP(pyxtnm1449(XATSSTRN(",")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          def pyxtnm1457(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1455(arg1): ## timp: strn_print(1040)
              pyxtnm1451 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1454 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1452);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1452))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1453 = XATSDAPP(XATS2PY_strn_print(pyxtnm1451))
              pyxtnm1454 = pyxtnm1453
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1454))
              return pyxtnm1454
            ## endtimp(strn_print(1040))
            pyxtnm1456 = XATSDAPP(pyxtnm1455(XATSSTRN("sint")))
            ## I1CMP:return:I1Vtnm(I1TNM(1456))
            return pyxtnm1456
          ## endtimp(g_ptype(202))
          pyxtnm1458 = XATSDAPP(pyxtnm1457())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1463(arg1): ## timp: strn_print(1040)
            pyxtnm1459 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1462 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1460);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1460))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1461 = XATSDAPP(XATS2PY_strn_print(pyxtnm1459))
            pyxtnm1462 = pyxtnm1461
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1462))
            return pyxtnm1462
          ## endtimp(strn_print(1040))
          pyxtnm1464 = XATSDAPP(pyxtnm1463(XATSSTRN(")")))
          ## I1CMP:return:I1Vtnm(I1TNM(1464))
          return pyxtnm1464
        ## endtimp(g_ptype(202))
        pyxtnm1466 = XATSDAPP(pyxtnm1465())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(2104(line=92,offs=18)--2109(line=92,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm1471(arg1): ## timp: strn_print(1040)
          pyxtnm1467 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1470 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1468);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1468))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm1469 = XATSDAPP(XATS2PY_strn_print(pyxtnm1467))
          pyxtnm1470 = pyxtnm1469
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1470))
          return pyxtnm1470
        ## endtimp(strn_print(1040))
        pyxtnm1472 = XATSDAPP(pyxtnm1471(XATSSTRN(",")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(2117(line=93,offs=3)--2124(line=93,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[5811])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6652],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
        def pyxtnm1647(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1477(arg1): ## timp: strn_print(1040)
            pyxtnm1473 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1476 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1474);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1474))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1475 = XATSDAPP(XATS2PY_strn_print(pyxtnm1473))
            pyxtnm1476 = pyxtnm1475
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1476))
            return pyxtnm1476
          ## endtimp(strn_print(1040))
          pyxtnm1478 = XATSDAPP(pyxtnm1477(XATSSTRN("GSEQ(")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1668(line=59,offs=1)--1807(line=67,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))>;I1Dtmpsub($list(@(a0[5804],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5805],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(z2tup);$list(T2Pvar(a0[5804]),T2Pvar(a1[5805])))))))))
          def pyxtnm1597(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1737(line=65,offs=3)--1742(line=65,offs=8))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1483(arg1): ## timp: strn_print(1040)
              pyxtnm1479 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1482 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1480);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1480))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1481 = XATSDAPP(XATS2PY_strn_print(pyxtnm1479))
              pyxtnm1482 = pyxtnm1481
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1482))
              return pyxtnm1482
            ## endtimp(strn_print(1040))
            pyxtnm1484 = XATSDAPP(pyxtnm1483(XATSSTRN("z2tup(")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1753(line=66,offs=3)--1760(line=66,offs=10))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[5804])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6652],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
            def pyxtnm1533(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1489(arg1): ## timp: strn_print(1040)
                pyxtnm1485 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1488 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1486);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1486))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1487 = XATSDAPP(XATS2PY_strn_print(pyxtnm1485))
                pyxtnm1488 = pyxtnm1487
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1488))
                return pyxtnm1488
              ## endtimp(strn_print(1040))
              pyxtnm1490 = XATSDAPP(pyxtnm1489(XATSSTRN("GSEQ(")))
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
              ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
              ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1626(line=57,offs=1)--1728(line=64,offs=32)))
              ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(t0[7401],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(list);$list(T2Pvar(t0[7401])))))))))
              def pyxtnm1511(): ## timp: g_ptype(202)
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1681(line=63,offs=1)--1686(line=63,offs=6))
                ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                def pyxtnm1495(arg1): ## timp: strn_print(1040)
                  pyxtnm1491 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1494 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1492);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1492))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                  pyxtnm1493 = XATSDAPP(XATS2PY_strn_print(pyxtnm1491))
                  pyxtnm1494 = pyxtnm1493
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1494))
                  return pyxtnm1494
                ## endtimp(strn_print(1040))
                pyxtnm1496 = XATSDAPP(pyxtnm1495(XATSSTRN("list(")))
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1697(line=64,offs=1)--1704(line=64,offs=8))
                ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[7401])))))
                ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
                ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
                def pyxtnm1503(): ## timp: g_ptype(202)
                  ## I1CMP:start
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
                  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                  def pyxtnm1501(arg1): ## timp: strn_print(1040)
                    pyxtnm1497 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm1500 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1498);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1498))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                    pyxtnm1499 = XATSDAPP(XATS2PY_strn_print(pyxtnm1497))
                    pyxtnm1500 = pyxtnm1499
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(1500))
                    return pyxtnm1500
                  ## endtimp(strn_print(1040))
                  pyxtnm1502 = XATSDAPP(pyxtnm1501(XATSSTRN("sint")))
                  ## I1CMP:return:I1Vtnm(I1TNM(1502))
                  return pyxtnm1502
                ## endtimp(g_ptype(202))
                pyxtnm1504 = XATSDAPP(pyxtnm1503())
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1717(line=64,offs=21)--1722(line=64,offs=26))
                ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                def pyxtnm1509(arg1): ## timp: strn_print(1040)
                  pyxtnm1505 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1508 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1506);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1506))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                  pyxtnm1507 = XATSDAPP(XATS2PY_strn_print(pyxtnm1505))
                  pyxtnm1508 = pyxtnm1507
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1508))
                  return pyxtnm1508
                ## endtimp(strn_print(1040))
                pyxtnm1510 = XATSDAPP(pyxtnm1509(XATSSTRN(")")))
                ## I1CMP:return:I1Vtnm(I1TNM(1510))
                return pyxtnm1510
              ## endtimp(g_ptype(202))
              pyxtnm1512 = XATSDAPP(pyxtnm1511())
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1517(arg1): ## timp: strn_print(1040)
                pyxtnm1513 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1516 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1514);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1514))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1515 = XATSDAPP(XATS2PY_strn_print(pyxtnm1513))
                pyxtnm1516 = pyxtnm1515
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1516))
                return pyxtnm1516
              ## endtimp(strn_print(1040))
              pyxtnm1518 = XATSDAPP(pyxtnm1517(XATSSTRN(",")))
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
              ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
              ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
              ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
              def pyxtnm1525(): ## timp: g_ptype(202)
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
                ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                def pyxtnm1523(arg1): ## timp: strn_print(1040)
                  pyxtnm1519 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1522 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1520);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1520))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                  pyxtnm1521 = XATSDAPP(XATS2PY_strn_print(pyxtnm1519))
                  pyxtnm1522 = pyxtnm1521
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1522))
                  return pyxtnm1522
                ## endtimp(strn_print(1040))
                pyxtnm1524 = XATSDAPP(pyxtnm1523(XATSSTRN("sint")))
                ## I1CMP:return:I1Vtnm(I1TNM(1524))
                return pyxtnm1524
              ## endtimp(g_ptype(202))
              pyxtnm1526 = XATSDAPP(pyxtnm1525())
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1531(arg1): ## timp: strn_print(1040)
                pyxtnm1527 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1530 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1528);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1528))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1529 = XATSDAPP(XATS2PY_strn_print(pyxtnm1527))
                pyxtnm1530 = pyxtnm1529
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1530))
                return pyxtnm1530
              ## endtimp(strn_print(1040))
              pyxtnm1532 = XATSDAPP(pyxtnm1531(XATSSTRN(")")))
              ## I1CMP:return:I1Vtnm(I1TNM(1532))
              return pyxtnm1532
            ## endtimp(g_ptype(202))
            pyxtnm1534 = XATSDAPP(pyxtnm1533())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1768(line=66,offs=18)--1773(line=66,offs=23))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1539(arg1): ## timp: strn_print(1040)
              pyxtnm1535 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1538 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1536);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1536))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1537 = XATSDAPP(XATS2PY_strn_print(pyxtnm1535))
              pyxtnm1538 = pyxtnm1537
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1538))
              return pyxtnm1538
            ## endtimp(strn_print(1040))
            pyxtnm1540 = XATSDAPP(pyxtnm1539(XATSSTRN(",")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1781(line=67,offs=3)--1788(line=67,offs=10))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[5805])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1576(line=53,offs=1)--1715(line=61,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(xs[6651],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6652],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(GSEQ);$list(T2Pvar(xs[6651]),T2Pvar(x0[6652])))))))))
            def pyxtnm1589(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1646(line=59,offs=3)--1651(line=59,offs=8))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1545(arg1): ## timp: strn_print(1040)
                pyxtnm1541 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1544 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1542);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1542))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1543 = XATSDAPP(XATS2PY_strn_print(pyxtnm1541))
                pyxtnm1544 = pyxtnm1543
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1544))
                return pyxtnm1544
              ## endtimp(strn_print(1040))
              pyxtnm1546 = XATSDAPP(pyxtnm1545(XATSSTRN("GSEQ(")))
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1661(line=60,offs=3)--1668(line=60,offs=10))
              ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(xs[6651])))))
              ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1626(line=57,offs=1)--1728(line=64,offs=32)))
              ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))))>;I1Dtmpsub($list(@(t0[7401],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(list);$list(T2Pvar(t0[7401])))))))))
              def pyxtnm1567(): ## timp: g_ptype(202)
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1681(line=63,offs=1)--1686(line=63,offs=6))
                ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                def pyxtnm1551(arg1): ## timp: strn_print(1040)
                  pyxtnm1547 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1550 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1548);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1548))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                  pyxtnm1549 = XATSDAPP(XATS2PY_strn_print(pyxtnm1547))
                  pyxtnm1550 = pyxtnm1549
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1550))
                  return pyxtnm1550
                ## endtimp(strn_print(1040))
                pyxtnm1552 = XATSDAPP(pyxtnm1551(XATSSTRN("list(")))
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1697(line=64,offs=1)--1704(line=64,offs=8))
                ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(t0[7401])))))
                ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
                ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
                def pyxtnm1559(): ## timp: g_ptype(202)
                  ## I1CMP:start
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
                  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                  def pyxtnm1557(arg1): ## timp: strn_print(1040)
                    pyxtnm1553 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm1556 = None
                    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1554);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1554))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                    pyxtnm1555 = XATSDAPP(XATS2PY_strn_print(pyxtnm1553))
                    pyxtnm1556 = pyxtnm1555
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(1556))
                    return pyxtnm1556
                  ## endtimp(strn_print(1040))
                  pyxtnm1558 = XATSDAPP(pyxtnm1557(XATSSTRN("sint")))
                  ## I1CMP:return:I1Vtnm(I1TNM(1558))
                  return pyxtnm1558
                ## endtimp(g_ptype(202))
                pyxtnm1560 = XATSDAPP(pyxtnm1559())
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list000.dats)@(1717(line=64,offs=21)--1722(line=64,offs=26))
                ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                def pyxtnm1565(arg1): ## timp: strn_print(1040)
                  pyxtnm1561 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1564 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1562);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1562))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                  pyxtnm1563 = XATSDAPP(XATS2PY_strn_print(pyxtnm1561))
                  pyxtnm1564 = pyxtnm1563
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1564))
                  return pyxtnm1564
                ## endtimp(strn_print(1040))
                pyxtnm1566 = XATSDAPP(pyxtnm1565(XATSSTRN(")")))
                ## I1CMP:return:I1Vtnm(I1TNM(1566))
                return pyxtnm1566
              ## endtimp(g_ptype(202))
              pyxtnm1568 = XATSDAPP(pyxtnm1567())
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1573(arg1): ## timp: strn_print(1040)
                pyxtnm1569 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1572 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1570);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1570))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1571 = XATSDAPP(XATS2PY_strn_print(pyxtnm1569))
                pyxtnm1572 = pyxtnm1571
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1572))
                return pyxtnm1572
              ## endtimp(strn_print(1040))
              pyxtnm1574 = XATSDAPP(pyxtnm1573(XATSSTRN(",")))
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
              ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
              ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
              ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
              def pyxtnm1581(): ## timp: g_ptype(202)
                ## I1CMP:start
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
                ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                def pyxtnm1579(arg1): ## timp: strn_print(1040)
                  pyxtnm1575 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1578 = None
                  ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                  ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1576);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1576))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                  pyxtnm1577 = XATSDAPP(XATS2PY_strn_print(pyxtnm1575))
                  pyxtnm1578 = pyxtnm1577
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1578))
                  return pyxtnm1578
                ## endtimp(strn_print(1040))
                pyxtnm1580 = XATSDAPP(pyxtnm1579(XATSSTRN("sint")))
                ## I1CMP:return:I1Vtnm(I1TNM(1580))
                return pyxtnm1580
              ## endtimp(g_ptype(202))
              pyxtnm1582 = XATSDAPP(pyxtnm1581())
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1587(arg1): ## timp: strn_print(1040)
                pyxtnm1583 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1586 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1584);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1584))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1585 = XATSDAPP(XATS2PY_strn_print(pyxtnm1583))
                pyxtnm1586 = pyxtnm1585
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1586))
                return pyxtnm1586
              ## endtimp(strn_print(1040))
              pyxtnm1588 = XATSDAPP(pyxtnm1587(XATSSTRN(")")))
              ## I1CMP:return:I1Vtnm(I1TNM(1588))
              return pyxtnm1588
            ## endtimp(g_ptype(202))
            pyxtnm1590 = XATSDAPP(pyxtnm1589())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1796(line=67,offs=18)--1801(line=67,offs=23))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1595(arg1): ## timp: strn_print(1040)
              pyxtnm1591 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1594 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1592);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1592))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1593 = XATSDAPP(XATS2PY_strn_print(pyxtnm1591))
              pyxtnm1594 = pyxtnm1593
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1594))
              return pyxtnm1594
            ## endtimp(strn_print(1040))
            pyxtnm1596 = XATSDAPP(pyxtnm1595(XATSSTRN(")")))
            ## I1CMP:return:I1Vtnm(I1TNM(1596))
            return pyxtnm1596
          ## endtimp(g_ptype(202))
          pyxtnm1598 = XATSDAPP(pyxtnm1597())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1603(arg1): ## timp: strn_print(1040)
            pyxtnm1599 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1602 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1600);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1600))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1601 = XATSDAPP(XATS2PY_strn_print(pyxtnm1599))
            pyxtnm1602 = pyxtnm1601
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1602))
            return pyxtnm1602
          ## endtimp(strn_print(1040))
          pyxtnm1604 = XATSDAPP(pyxtnm1603(XATSSTRN(",")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1835(line=66,offs=1)--1973(line=74,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(a0[7352],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7353],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7352]),T2Pvar(a1[7353])))))))))
          def pyxtnm1639(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1903(line=72,offs=3)--1908(line=72,offs=8))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1609(arg1): ## timp: strn_print(1040)
              pyxtnm1605 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1608 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1606);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1606))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1607 = XATSDAPP(XATS2PY_strn_print(pyxtnm1605))
              pyxtnm1608 = pyxtnm1607
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1608))
              return pyxtnm1608
            ## endtimp(strn_print(1040))
            pyxtnm1610 = XATSDAPP(pyxtnm1609(XATSSTRN("t0up2(")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1919(line=73,offs=3)--1926(line=73,offs=10))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[7352])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
            def pyxtnm1617(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1615(arg1): ## timp: strn_print(1040)
                pyxtnm1611 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1614 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1612);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1612))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1613 = XATSDAPP(XATS2PY_strn_print(pyxtnm1611))
                pyxtnm1614 = pyxtnm1613
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1614))
                return pyxtnm1614
              ## endtimp(strn_print(1040))
              pyxtnm1616 = XATSDAPP(pyxtnm1615(XATSSTRN("sint")))
              ## I1CMP:return:I1Vtnm(I1TNM(1616))
              return pyxtnm1616
            ## endtimp(g_ptype(202))
            pyxtnm1618 = XATSDAPP(pyxtnm1617())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1934(line=73,offs=18)--1939(line=73,offs=23))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1623(arg1): ## timp: strn_print(1040)
              pyxtnm1619 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1622 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1620);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1620))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1621 = XATSDAPP(XATS2PY_strn_print(pyxtnm1619))
              pyxtnm1622 = pyxtnm1621
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1622))
              return pyxtnm1622
            ## endtimp(strn_print(1040))
            pyxtnm1624 = XATSDAPP(pyxtnm1623(XATSSTRN(",")))
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1947(line=74,offs=3)--1954(line=74,offs=10))
            ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[7353])))))
            ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
            ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
            def pyxtnm1631(): ## timp: g_ptype(202)
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
              ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
              ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
              ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
              def pyxtnm1629(arg1): ## timp: strn_print(1040)
                pyxtnm1625 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1628 = None
                ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1626);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1626))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                pyxtnm1627 = XATSDAPP(XATS2PY_strn_print(pyxtnm1625))
                pyxtnm1628 = pyxtnm1627
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1628))
                return pyxtnm1628
              ## endtimp(strn_print(1040))
              pyxtnm1630 = XATSDAPP(pyxtnm1629(XATSSTRN("sint")))
              ## I1CMP:return:I1Vtnm(I1TNM(1630))
              return pyxtnm1630
            ## endtimp(g_ptype(202))
            pyxtnm1632 = XATSDAPP(pyxtnm1631())
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1962(line=74,offs=18)--1967(line=74,offs=23))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1637(arg1): ## timp: strn_print(1040)
              pyxtnm1633 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1636 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1634);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1634))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1635 = XATSDAPP(XATS2PY_strn_print(pyxtnm1633))
              pyxtnm1636 = pyxtnm1635
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1636))
              return pyxtnm1636
            ## endtimp(strn_print(1040))
            pyxtnm1638 = XATSDAPP(pyxtnm1637(XATSSTRN(")")))
            ## I1CMP:return:I1Vtnm(I1TNM(1638))
            return pyxtnm1638
          ## endtimp(g_ptype(202))
          pyxtnm1640 = XATSDAPP(pyxtnm1639())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1645(arg1): ## timp: strn_print(1040)
            pyxtnm1641 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1644 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1642);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1642))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1643 = XATSDAPP(XATS2PY_strn_print(pyxtnm1641))
            pyxtnm1644 = pyxtnm1643
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1644))
            return pyxtnm1644
          ## endtimp(strn_print(1040))
          pyxtnm1646 = XATSDAPP(pyxtnm1645(XATSSTRN(")")))
          ## I1CMP:return:I1Vtnm(I1TNM(1646))
          return pyxtnm1646
        ## endtimp(g_ptype(202))
        pyxtnm1648 = XATSDAPP(pyxtnm1647())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(2132(line=93,offs=18)--2137(line=93,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm1653(arg1): ## timp: strn_print(1040)
          pyxtnm1649 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1652 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1650);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1650))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm1651 = XATSDAPP(XATS2PY_strn_print(pyxtnm1649))
          pyxtnm1652 = pyxtnm1651
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1652))
          return pyxtnm1652
        ## endtimp(strn_print(1040))
        pyxtnm1654 = XATSDAPP(pyxtnm1653(XATSSTRN(")")))
        ## I1CMP:return:I1Vtnm(I1TNM(1654))
        return pyxtnm1654
      ## endtimp(g_ptype(202))
      pyxtnm1656 = XATSDAPP(pyxtnm1655())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1676(line=60,offs=18)--1681(line=60,offs=23))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm1661(arg1): ## timp: strn_print(1040)
        pyxtnm1657 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1660 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1658);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1658))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm1659 = XATSDAPP(XATS2PY_strn_print(pyxtnm1657))
        pyxtnm1660 = pyxtnm1659
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1660))
        return pyxtnm1660
      ## endtimp(strn_print(1040))
      pyxtnm1662 = XATSDAPP(pyxtnm1661(XATSSTRN(",")))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1689(line=61,offs=3)--1696(line=61,offs=10))
      ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(x0[6652])))))
      ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1835(line=66,offs=1)--1973(line=74,offs=29)))
      ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(a0[7352],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7353],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7352]),T2Pvar(a1[7353])))))))))
      def pyxtnm1725(): ## timp: g_ptype(202)
        ## I1CMP:start
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1903(line=72,offs=3)--1908(line=72,offs=8))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm1667(arg1): ## timp: strn_print(1040)
          pyxtnm1663 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1666 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1664);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1664))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm1665 = XATSDAPP(XATS2PY_strn_print(pyxtnm1663))
          pyxtnm1666 = pyxtnm1665
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1666))
          return pyxtnm1666
        ## endtimp(strn_print(1040))
        pyxtnm1668 = XATSDAPP(pyxtnm1667(XATSSTRN("t0up2(")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1919(line=73,offs=3)--1926(line=73,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[7352])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
        def pyxtnm1675(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1673(arg1): ## timp: strn_print(1040)
            pyxtnm1669 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1672 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1670);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1670))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1671 = XATSDAPP(XATS2PY_strn_print(pyxtnm1669))
            pyxtnm1672 = pyxtnm1671
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1672))
            return pyxtnm1672
          ## endtimp(strn_print(1040))
          pyxtnm1674 = XATSDAPP(pyxtnm1673(XATSSTRN("sint")))
          ## I1CMP:return:I1Vtnm(I1TNM(1674))
          return pyxtnm1674
        ## endtimp(g_ptype(202))
        pyxtnm1676 = XATSDAPP(pyxtnm1675())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1934(line=73,offs=18)--1939(line=73,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm1681(arg1): ## timp: strn_print(1040)
          pyxtnm1677 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1680 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1678);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1678))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm1679 = XATSDAPP(XATS2PY_strn_print(pyxtnm1677))
          pyxtnm1680 = pyxtnm1679
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1680))
          return pyxtnm1680
        ## endtimp(strn_print(1040))
        pyxtnm1682 = XATSDAPP(pyxtnm1681(XATSSTRN(",")))
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1947(line=74,offs=3)--1954(line=74,offs=10))
        ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[7353])))))
        ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1835(line=66,offs=1)--1973(line=74,offs=29)))
        ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(a0[7352],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7353],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7352]),T2Pvar(a1[7353])))))))))
        def pyxtnm1717(): ## timp: g_ptype(202)
          ## I1CMP:start
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1903(line=72,offs=3)--1908(line=72,offs=8))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1687(arg1): ## timp: strn_print(1040)
            pyxtnm1683 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1686 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1684);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1684))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1685 = XATSDAPP(XATS2PY_strn_print(pyxtnm1683))
            pyxtnm1686 = pyxtnm1685
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1686))
            return pyxtnm1686
          ## endtimp(strn_print(1040))
          pyxtnm1688 = XATSDAPP(pyxtnm1687(XATSSTRN("t0up2(")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1919(line=73,offs=3)--1926(line=73,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a0[7352])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          def pyxtnm1695(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1693(arg1): ## timp: strn_print(1040)
              pyxtnm1689 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1692 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1690);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1690))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1691 = XATSDAPP(XATS2PY_strn_print(pyxtnm1689))
              pyxtnm1692 = pyxtnm1691
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1692))
              return pyxtnm1692
            ## endtimp(strn_print(1040))
            pyxtnm1694 = XATSDAPP(pyxtnm1693(XATSSTRN("sint")))
            ## I1CMP:return:I1Vtnm(I1TNM(1694))
            return pyxtnm1694
          ## endtimp(g_ptype(202))
          pyxtnm1696 = XATSDAPP(pyxtnm1695())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1934(line=73,offs=18)--1939(line=73,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1701(arg1): ## timp: strn_print(1040)
            pyxtnm1697 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1700 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1698);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1698))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1699 = XATSDAPP(XATS2PY_strn_print(pyxtnm1697))
            pyxtnm1700 = pyxtnm1699
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1700))
            return pyxtnm1700
          ## endtimp(strn_print(1040))
          pyxtnm1702 = XATSDAPP(pyxtnm1701(XATSSTRN(",")))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1947(line=74,offs=3)--1954(line=74,offs=10))
          ## I0Etapq(I0Ecst(g_ptype(202)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2386(line=100,offs=1)--2393(line=100,offs=8))));$list(T2JAG($list(T2Pvar(a1[7353])))))
          ## T1IMPallx(g_ptype(202), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2708(line=146,offs=1)--2762(line=149,offs=29)))
          ## T1IMPallx(g_ptype(202)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_ptype(202);$list(@(vw[773],T2Pcst(sint)))))))
          def pyxtnm1709(): ## timp: g_ptype(202)
            ## I1CMP:start
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2749(line=149,offs=16)--2754(line=149,offs=21))
            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
            def pyxtnm1707(arg1): ## timp: strn_print(1040)
              pyxtnm1703 = arg1
              ## I1CMP:start
              ## let
              pyxtnm1706 = None
              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1704);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1704))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
              pyxtnm1705 = XATSDAPP(XATS2PY_strn_print(pyxtnm1703))
              pyxtnm1706 = pyxtnm1705
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1706))
              return pyxtnm1706
            ## endtimp(strn_print(1040))
            pyxtnm1708 = XATSDAPP(pyxtnm1707(XATSSTRN("sint")))
            ## I1CMP:return:I1Vtnm(I1TNM(1708))
            return pyxtnm1708
          ## endtimp(g_ptype(202))
          pyxtnm1710 = XATSDAPP(pyxtnm1709())
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1962(line=74,offs=18)--1967(line=74,offs=23))
          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
          def pyxtnm1715(arg1): ## timp: strn_print(1040)
            pyxtnm1711 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1714 = None
            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1712);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1712))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
            pyxtnm1713 = XATSDAPP(XATS2PY_strn_print(pyxtnm1711))
            pyxtnm1714 = pyxtnm1713
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1714))
            return pyxtnm1714
          ## endtimp(strn_print(1040))
          pyxtnm1716 = XATSDAPP(pyxtnm1715(XATSSTRN(")")))
          ## I1CMP:return:I1Vtnm(I1TNM(1716))
          return pyxtnm1716
        ## endtimp(g_ptype(202))
        pyxtnm1718 = XATSDAPP(pyxtnm1717())
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(1962(line=74,offs=18)--1967(line=74,offs=23))
        ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
        ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
        ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
        def pyxtnm1723(arg1): ## timp: strn_print(1040)
          pyxtnm1719 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1722 = None
          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1720);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1720))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
          pyxtnm1721 = XATSDAPP(XATS2PY_strn_print(pyxtnm1719))
          pyxtnm1722 = pyxtnm1721
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1722))
          return pyxtnm1722
        ## endtimp(strn_print(1040))
        pyxtnm1724 = XATSDAPP(pyxtnm1723(XATSSTRN(")")))
        ## I1CMP:return:I1Vtnm(I1TNM(1724))
        return pyxtnm1724
      ## endtimp(g_ptype(202))
      pyxtnm1726 = XATSDAPP(pyxtnm1725())
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1704(line=61,offs=18)--1709(line=61,offs=23))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm1731(arg1): ## timp: strn_print(1040)
        pyxtnm1727 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1730 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1728);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1728))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm1729 = XATSDAPP(XATS2PY_strn_print(pyxtnm1727))
        pyxtnm1730 = pyxtnm1729
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1730))
        return pyxtnm1730
      ## endtimp(strn_print(1040))
      pyxtnm1732 = XATSDAPP(pyxtnm1731(XATSSTRN(")")))
      ## I1CMP:return:I1Vtnm(I1TNM(1732))
      return pyxtnm1732
    ## endtimp(g_ptype(202))
    pyxtnm1734 = XATSDAPP(pyxtnm1733())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2397(line=123,offs=18)--2402(line=123,offs=23))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm1739(arg1): ## timp: strn_print(1040)
      pyxtnm1735 = arg1
      ## I1CMP:start
      ## let
      pyxtnm1738 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1736);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1736))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm1737 = XATSDAPP(XATS2PY_strn_print(pyxtnm1735))
      pyxtnm1738 = pyxtnm1737
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(1738))
      return pyxtnm1738
    ## endtimp(strn_print(1040))
    pyxtnm1740 = XATSDAPP(pyxtnm1739(XATSSTRN(":")))
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2408(line=124,offs=3)--2415(line=124,offs=10))
    ## I0Etapq(I0Ecst(g_psort(201)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gdbg000.sats)@(2346(line=97,offs=1)--2353(line=97,offs=8))));$list(T2JAG($list(T2Pvar(t0[5762])))))
    ## T1IMPallx(g_psort(201), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1776(line=69,offs=1)--1830(line=73,offs=22)))
    ## T1IMPallx(g_psort(201)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))))>;I1Dtmpsub($list(@(t0[5754],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))));I1Dimplmnt0(DIMPLone2(g_psort(201);$list(@(vw[772],T2Pvar(t0[5754])))))))
    def pyxtnm1747(): ## timp: g_psort(201)
      ## I1CMP:start
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(1811(line=73,offs=3)--1821(line=73,offs=13))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm1745(arg1): ## timp: strn_print(1040)
        pyxtnm1741 = arg1
        ## I1CMP:start
        ## let
        pyxtnm1744 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1742);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1742))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm1743 = XATSDAPP(XATS2PY_strn_print(pyxtnm1741))
        pyxtnm1744 = pyxtnm1743
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(1744))
        return pyxtnm1744
      ## endtimp(strn_print(1040))
      pyxtnm1746 = XATSDAPP(pyxtnm1745(XATSSTRN("type")))
      ## I1CMP:return:I1Vtnm(I1TNM(1746))
      return pyxtnm1746
    ## endtimp(g_psort(201))
    pyxtnm1748 = XATSDAPP(pyxtnm1747())
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gdbg000.dats)@(2423(line=124,offs=18)--2428(line=124,offs=23))
    ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
    ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
    ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
    def pyxtnm1753(arg1): ## timp: strn_print(1040)
      pyxtnm1749 = arg1
      ## I1CMP:start
      ## let
      pyxtnm1752 = None
      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1750);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1750))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
      pyxtnm1751 = XATSDAPP(XATS2PY_strn_print(pyxtnm1749))
      pyxtnm1752 = pyxtnm1751
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(1752))
      return pyxtnm1752
    ## endtimp(strn_print(1040))
    pyxtnm1754 = XATSDAPP(pyxtnm1753(XATSSTRN(")")))
    ## I1CMP:return:I1Vtnm(I1TNM(1754))
    return pyxtnm1754
  ## endtimp(g_print(39))
  pyxtnm1756 = XATSDAPP(pyxtnm1755(pyxtnm1382))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21501(line=1328,offs=20)--21513(line=1328,offs=32))
  ## I0Etapq(I0Ecst(gs_print$sep(803)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11637(line=733,offs=1)--11649(line=733,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$sep(803), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20753(line=1271,offs=1)--20791(line=1273,offs=20)))
  ## T1IMPallx(gs_print$sep(803)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$sep(803);$list()))))
  def pyxtnm1758(): ## timp: gs_print$sep(803)
    ## I1CMP:start
    pyxtnm1757 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(1757))
    return pyxtnm1757
  ## endtimp(gs_print$sep(803))
  pyxtnm1759 = XATSDAPP(pyxtnm1758())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21518(line=1329,offs=3)--21525(line=1329,offs=10))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x2[7022])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm1765 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm1764(arg1): ## timp: strn_print(1040)
    pyxtnm1760 = arg1
    ## I1CMP:start
    ## let
    pyxtnm1763 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(1761);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(1761))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm1762 = XATSDAPP(XATS2PY_strn_print(pyxtnm1760))
    pyxtnm1763 = pyxtnm1762
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(1763))
    return pyxtnm1763
  ## endtimp(strn_print(1040))
  pyxtnm1765 = pyxtnm1764
  pyxtnm1766 = XATSDAPP(pyxtnm1765(pyxtnm1383))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(21535(line=1329,offs=20)--21547(line=1329,offs=32))
  ## I0Etapq(I0Ecst(gs_print$end(804)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gsyn000.sats)@(11672(line=736,offs=1)--11684(line=736,offs=13))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print$end(804), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gsyn000.dats)@(20792(line=1274,offs=1)--20830(line=1276,offs=20)))
  ## T1IMPallx(gs_print$end(804)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print$end(804);$list()))))
  def pyxtnm1768(): ## timp: gs_print$end(804)
    ## I1CMP:start
    pyxtnm1767 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(1767))
    return pyxtnm1767
  ## endtimp(gs_print$end(804))
  pyxtnm1769 = XATSDAPP(pyxtnm1768())
  pyxtnm1770 = pyxtnm1769
  ## end-of(let)
  ## I1CMP:return:I1Vtnm(I1TNM(1770))
  return pyxtnm1770
## endtimp(gs_print_a3(808))
pyxtnm1772 = XATSDAPP(pyxtnm1771(XATSSTRN("xztup = "), pyxtnm1380, XATSSTRN("\n")))
pyxtnm1773 = pyxtnm1772
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(940(line=59,offs=1)--966(line=59,offs=27)))
## I1VALDCL
pyxtnm2019 = None
## LCSRCsome1(test07_gseq000.dats)@(952(line=59,offs=13)--959(line=59,offs=20))
## I0Etapq(I0Ecst(GSEQ_listize(251)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(3280(line=173,offs=1)--3292(line=173,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))
## T1IMPallx(GSEQ_listize(251), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2477(line=125,offs=1)--2579(line=132,offs=35)))
## T1IMPallx(GSEQ_listize(251)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6663],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6664],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(GSEQ_listize(251);$list(@(xs[829],T2Pvar(xs[6663])),@(x0[830],T2Pvar(x0[6664])))))))
def pyxtnm2017(arg1): ## timp: GSEQ_listize(251)
  pyxtnm1774 = arg1
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2532(line=131,offs=1)--2544(line=131,offs=13))
  ## I0Etapq(I0Ecst(gseq_listize(377)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(2446(line=117,offs=1)--2458(line=117,offs=13))));$list(T2JAG($list(T2Pvar(xs[6663]))),T2JAG($list(T2Pvar(x0[6664])))))
  ## T1IMPallx(gseq_listize(377), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1870(line=72,offs=1)--2083(line=88,offs=2)))
  ## T1IMPallx(gseq_listize(377)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6082],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6083],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_listize(377);$list(@(xs[1131],T2Pvar(xs[6082])),@(x0[1132],T2Pvar(x0[6083])))))))
  def pyxtnm2011(arg1): ## timp: gseq_listize(377)
    pyxtnm1775 = arg1
    ## I1CMP:start
    ## let
    pyxtnm2010 = None
    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1969(line=82,offs=1)--1991(line=82,offs=23)))
    ## I1VALDCL
    pyxtnm1777 = None
    pyxtnm1776 = XATSCAPP("list_vt_nil", [0])
    pyxtnm1777 = pyxtnm1776
    XATS000_patck(True)
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1992(line=83,offs=1)--2017(line=83,offs=26))
    ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(r0;S2Eapps(S2Ecst(list_vt);$list(S2Evar(x0[6083])))))))
    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2018(line=84,offs=1)--2081(line=87,offs=32)))
    ## I1Dimplmnt0(DIMPLone2(rfolditm$fopr(56);$list(@(x0[470],T2Pvar(x0[6083])),@(r0[471],T2Pcst(r0))))):timp
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(1925(line=78,offs=1)--1938(line=78,offs=14))
    ## I0Etapq(I0Ecst(gseq_rfolditm(411)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(8790(line=502,offs=1)--8803(line=502,offs=14))));$list(T2JAG($list(T2Pvar(xs[6082]))),T2JAG($list(T2Pvar(x0[6083]))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[6083]),T2Pnone0()))))))
    ## T1IMPallx(gseq_rfolditm(411), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8831(line=582,offs=1)--9143(line=608,offs=2)))
    ## T1IMPallx(gseq_rfolditm(411)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6140],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6141],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(r0[6142],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_rfolditm(411);$list(@(xs[1242],T2Pvar(xs[6140])),@(x0[1243],T2Pvar(x0[6141])),@(r0[1244],T2Pvar(r0[6142])))))))
    def pyxtnm2008(arg1, arg2): ## timp: gseq_rfolditm(411)
      pyxtnm1781 = arg1
      pyxtnm1782 = arg2
      ## I1CMP:start
      ## let
      pyxtnm2007 = None
      ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8911(line=590,offs=1)--8926(line=590,offs=16)))
      ## I1VARDCL
      ## I1CMP:start
      ## I1CMP:return:I1Vtnm(I1TNM(1782))
      pyxtnm1783 = XATSVAR1(pyxtnm1782)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8930(line=592,offs=1)--8948(line=592,offs=19)))
      ## I1VALDCL
      pyxtnm1784 = None
      pyxtnm1784 = XATSADDR(pyxtnm1783)
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8952(line=594,offs=1)--9138(line=606,offs=41)))
      ## I1VALDCL
      pyxtnm2005 = None
      ## let
      pyxtnm2004 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8998(line=599,offs=1)--9137(line=606,offs=40)))
      ## I1Dimplmnt0(DIMPLone2(rforitm$work(52);$list(@(x0[465],T2Pvar(x0[6141]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8963(line=596,offs=1)--8975(line=596,offs=13))
      ## I0Etapq(I0Ecst(gseq_rforitm(403)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7124(line=406,offs=1)--7136(line=406,offs=13))));$list(T2JAG($list(T2Pvar(xs[6140]))),T2JAG($list(T2Pvar(x0[6141])))))
      ## T1IMPallx(gseq_rforitm(403), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6837(line=439,offs=1)--7028(line=456,offs=2)))
      ## T1IMPallx(gseq_rforitm(403)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6122],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6123],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_rforitm(403);$list(@(xs[1217],T2Pvar(xs[6122])),@(x0[1218],T2Pvar(x0[6123])))))))
      def pyxtnm2002(arg1): ## timp: gseq_rforitm(403)
        pyxtnm1792 = arg1
        ## I1CMP:start
        ## let
        pyxtnm2001 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6949(line=451,offs=1)--7026(line=455,offs=33)))
        ## I1Dimplmnt0(DIMPLone2(rforall$test(48);$list(@(x0[461],T2Pvar(x0[6123]))))):timp
        ## let
        pyxtnm2000 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6896(line=446,offs=1)--6929(line=448,offs=13)))
        ## I1VALDCL
        pyxtnm1999 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6904(line=447,offs=1)--6916(line=447,offs=13))
        ## I0Etapq(I0Ecst(gseq_rforall(388)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3813(line=218,offs=1)--3825(line=218,offs=13))));$list(T2JAG($list(T2Pvar(xs[6122]))),T2JAG($list(T2Pvar(x0[6123])))))
        ## T1IMPallx(gseq_rforall(388), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(3626(line=202,offs=1)--3784(line=214,offs=2)))
        ## T1IMPallx(gseq_rforall(388)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6094],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6095],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_rforall(388);$list(@(xs[1171],T2Pvar(xs[6094])),@(x0[1172],T2Pvar(x0[6095])))))))
        def pyxtnm1997(arg1): ## timp: gseq_rforall(388)
          pyxtnm1797 = arg1
          ## I1CMP:start
          ## let
          pyxtnm1996 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(3738(line=212,offs=1)--3782(line=213,offs=36)))
          ## I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Pvar(x0[6095]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(3681(line=208,offs=1)--3696(line=208,offs=16))
          ## I0Etapq(I0Ecst(list_vt_forall0(2062)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1428(line=43,offs=1)--1443(line=43,offs=16))));$list(T2JAG($list(T2Pvar(x0[6095])))))
          ## T1IMPallx(list_vt_forall0(2062), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2021(line=82,offs=1)--2226(line=95,offs=4)))
          ## T1IMPallx(list_vt_forall0(2062)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8837],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(list_vt_forall0(2062);$list(@(x0[5290],T2Pvar(x0[8837])))))))
          def pyxtnm1832(arg1): ## timp: list_vt_forall0(2062)
            pyxtnm1798 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1831 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2073(line=87,offs=1)--2124(line=90,offs=24)))
            ## I1FUNDCL
            def test_2076(arg1): ## fun
              pyxtnm1799 = arg1
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2103(line=90,offs=3)--2115(line=90,offs=15))
              ## I0Etapq(I0Ecst(forall$test0(1422)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2108(line=107,offs=1)--2120(line=107,offs=13))));$list(T2JAG($list(T2Pvar(x0[8837])))))
              ## T1IMPallx(forall$test0(1422), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(3738(line=212,offs=1)--3782(line=213,offs=36)))
              ## T1IMPallx(forall$test0(1422)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6094],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6095],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(forall$test0(1422);$list(@(x0[3765],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
              pyxtnm1823 = None
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(3766(line=213,offs=20)--3778(line=213,offs=32))
              ## I0Etapq(I0Ecst(rforall$test(48)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2041(line=99,offs=1)--2053(line=99,offs=13))));$list(T2JAG($list(T2Pvar(x0[6095])))))
              ## T1IMPallx(rforall$test(48), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6949(line=451,offs=1)--7026(line=455,offs=33)))
              ## T1IMPallx(rforall$test(48)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6122],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6123],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(rforall$test(48);$list(@(x0[461],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
              def pyxtnm1822(arg1): ## timp: rforall$test(48)
                pyxtnm1800 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1821 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6985(line=454,offs=1)--7014(line=455,offs=21)))
                ## I1VALDCL
                pyxtnm1820 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6994(line=455,offs=1)--7006(line=455,offs=13))
                ## I0Etapq(I0Ecst(rforitm$work(52)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2379(line=127,offs=1)--2391(line=127,offs=13))));$list(T2JAG($list(T2Pvar(x0[6123])))))
                ## T1IMPallx(rforitm$work(52), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8998(line=599,offs=1)--9137(line=606,offs=40)))
                ## T1IMPallx(rforitm$work(52)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6140],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6141],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(r0[6142],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(rforitm$work(52);$list(@(x0[465],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
                def pyxtnm1818(arg1): ## timp: rforitm$work(52)
                  pyxtnm1801 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1817 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9068(line=605,offs=1)--9097(line=605,offs=30)))
                  ## I1VALDCL
                  pyxtnm1806 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9081(line=605,offs=14)--9089(line=605,offs=22))
                  ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Pvar(r0[6142])))))
                  ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                  ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                  def pyxtnm1804(arg1): ## timp: p2tr_get(2309)
                    pyxtnm1802 = arg1
                    ## I1CMP:start
                    pyxtnm1803 = XATS000_dp2tr(pyxtnm1802)
                    ## I1CMP:return:I1Vtnm(I1TNM(1803))
                    return pyxtnm1803
                  ## endtimp(p2tr_get(2309))
                  pyxtnm1805 = XATSDAPP(pyxtnm1804(pyxtnm1784))
                  pyxtnm1806 = pyxtnm1805
                  XATS000_patck(True)
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9098(line=606,offs=1)--9136(line=606,offs=39)))
                  ## I1VALDCL
                  pyxtnm1812 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9107(line=606,offs=10)--9120(line=606,offs=23))
                  ## I0Etapq(I0Ecst(rfolditm$fopr(56)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2598(line=145,offs=1)--2611(line=145,offs=14))));$list(T2JAG($list(T2Pvar(x0[6141]))),T2JAG($list(T2Pvar(r0[6142])))))
                  ## T1IMPallx(rfolditm$fopr(56), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2018(line=84,offs=1)--2081(line=87,offs=32)))
                  ## T1IMPallx(rfolditm$fopr(56)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6082],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6083],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(rfolditm$fopr(56);$list(@(x0[470],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(r0[471],T2Papps(T2Pcst(list_vt);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))))
                  def pyxtnm1810(arg1, arg2): ## timp: rfolditm$fopr(56)
                    pyxtnm1807 = arg1
                    pyxtnm1808 = arg2
                    ## I1CMP:start
                    pyxtnm1809 = XATSCAPP("list_vt_cons", [1, pyxtnm1807, pyxtnm1808])
                    ## I1CMP:return:I1Vtnm(I1TNM(1809))
                    return pyxtnm1809
                  ## endtimp(rfolditm$fopr(56))
                  pyxtnm1811 = XATSDAPP(pyxtnm1810(pyxtnm1801, pyxtnm1806))
                  pyxtnm1812 = pyxtnm1811
                  XATS000_patck(True)
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(9038(line=602,offs=7)--9046(line=602,offs=15))
                  ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Pvar(r0[6142])))))
                  ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                  ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                  def pyxtnm1815(arg1, arg2): ## timp: p2tr_set(2310)
                    pyxtnm1813 = arg1
                    pyxtnm1814 = arg2
                    ## I1CMP:start
                    XATS000_assgn(pyxtnm1813, pyxtnm1814)
                    ## I1CMP:return:I1V000()
                    return XATSVOID
                  ## endtimp(p2tr_set(2310))
                  pyxtnm1816 = XATSDAPP(pyxtnm1815(pyxtnm1784, pyxtnm1812))
                  pyxtnm1817 = pyxtnm1816
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1817))
                  return pyxtnm1817
                ## endtimp(rforitm$work(52))
                pyxtnm1819 = XATSDAPP(pyxtnm1818(pyxtnm1800))
                pyxtnm1820 = pyxtnm1819
                XATS000_patck(True)
                pyxtnm1821 = XATSBOOL(True)
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1821))
                return pyxtnm1821
              ## endtimp(rforall$test(48))
              pyxtnm1823 = pyxtnm1822
              pyxtnm1824 = XATSDAPP(pyxtnm1823(pyxtnm1799))
              ## I1CMP:return:I1Vtnm(I1TNM(1824))
              return pyxtnm1824
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2125(line=91,offs=1)--2165(line=92,offs=37)))
            ## I1FUNDCL
            def free_2128(arg1): ## fun
              pyxtnm1825 = arg1
              ## I1CMP:start
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/list000.dats)@(2151(line=92,offs=23)--2157(line=92,offs=29))
              ## I0Etapq(I0Ecst(g_free(23)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(1595(line=57,offs=1)--1601(line=57,offs=7))));$list(T2JAG($list(T2Pvar(x0[8837])))))
              ## T1IMPallx(g_free(23), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/tupl000_vt.dats)@(2935(line=152,offs=1)--2999(line=155,offs=38)))
              ## T1IMPallx(g_free(23)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(a0[8480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[8481],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_free(23);$list(@(a[431],T2Papps(T2Pcst(t0up_vt);$list(T2Pvar(a0[8480]),T2Pvar(a1[8481])))))))))
              def pyxtnm1828(arg1): ## timp: g_free(23)
                pyxtnm1826 = arg1
                ## I1CMP:start
                pyxtnm1827 = XATSTUP0([])
                ## I1CMP:return:I1Vtnm(I1TNM(1827))
                return pyxtnm1827
              ## endtimp(g_free(23))
              pyxtnm1829 = XATSDAPP(pyxtnm1828(pyxtnm1825))
              ## I1CMP:return:I1Vtnm(I1TNM(1829))
              return pyxtnm1829
            pyxtnm1830 = XATSDAPP(XATS2PY_list_vt_forall0_f1un(pyxtnm1798, test_2076, free_2128))
            pyxtnm1831 = pyxtnm1830
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1831))
            return pyxtnm1831
          ## endtimp(list_vt_forall0(2062))
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(3702(line=209,offs=2)--3715(line=209,offs=15))
          ## I0Etapq(I0Ecst(gseq_rlistize(380)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(2866(line=148,offs=1)--2879(line=148,offs=14))));$list(T2JAG($list(T2Pvar(xs[6094]))),T2JAG($list(T2Pvar(x0[6095])))))
          ## T1IMPallx(gseq_rlistize(380), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2142(line=92,offs=1)--2354(line=108,offs=2)))
          ## T1IMPallx(gseq_rlistize(380)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6084],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6085],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_rlistize(380);$list(@(xs[1143],T2Pvar(xs[6084])),@(x0[1144],T2Pvar(x0[6085])))))))
          def pyxtnm1993(arg1): ## timp: gseq_rlistize(380)
            pyxtnm1833 = arg1
            ## I1CMP:start
            ## let
            pyxtnm1992 = None
            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2241(line=102,offs=1)--2263(line=102,offs=23)))
            ## I1VALDCL
            pyxtnm1835 = None
            pyxtnm1834 = XATSCAPP("list_vt_nil", [0])
            pyxtnm1835 = pyxtnm1834
            XATS000_patck(True)
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2264(line=103,offs=1)--2289(line=103,offs=26))
            ## I1Di0dcl(I0Dd3ecl(D3Cd2ecl(D2Csexpdef(r0;S2Eapps(S2Ecst(list_vt);$list(S2Evar(x0[6085])))))))
            ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2290(line=104,offs=1)--2352(line=107,offs=32)))
            ## I1Dimplmnt0(DIMPLone2(folditm$fopr(55);$list(@(x0[468],T2Pvar(x0[6085])),@(r0[469],T2Pcst(r0))))):timp
            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2198(line=98,offs=1)--2210(line=98,offs=13))
            ## I0Etapq(I0Ecst(gseq_folditm(410)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(8733(line=497,offs=1)--8745(line=497,offs=13))));$list(T2JAG($list(T2Pvar(xs[6084]))),T2JAG($list(T2Pvar(x0[6085]))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[6085]),T2Pnone0()))))))
            ## T1IMPallx(gseq_folditm(410), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8229(line=538,offs=1)--8537(line=564,offs=2)))
            ## T1IMPallx(gseq_folditm(410)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6134],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6135],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(r0[6136],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_folditm(410);$list(@(xs[1239],T2Pvar(xs[6134])),@(x0[1240],T2Pvar(x0[6135])),@(r0[1241],T2Pvar(r0[6136])))))))
            def pyxtnm1990(arg1, arg2): ## timp: gseq_folditm(410)
              pyxtnm1839 = arg1
              pyxtnm1840 = arg2
              ## I1CMP:start
              ## let
              pyxtnm1989 = None
              ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8308(line=546,offs=1)--8323(line=546,offs=16)))
              ## I1VARDCL
              ## I1CMP:start
              ## I1CMP:return:I1Vtnm(I1TNM(1840))
              pyxtnm1841 = XATSVAR1(pyxtnm1840)
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8327(line=548,offs=1)--8345(line=548,offs=19)))
              ## I1VALDCL
              pyxtnm1842 = None
              pyxtnm1842 = XATSADDR(pyxtnm1841)
              XATS000_patck(True)
              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8349(line=550,offs=1)--8532(line=562,offs=40)))
              ## I1VALDCL
              pyxtnm1987 = None
              ## let
              pyxtnm1986 = None
              ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8394(line=555,offs=1)--8531(line=562,offs=39)))
              ## I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Pvar(x0[6135]))))):timp
              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8360(line=552,offs=1)--8371(line=552,offs=12))
              ## I0Etapq(I0Ecst(gseq_foritm(402)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(7078(line=402,offs=1)--7089(line=402,offs=12))));$list(T2JAG($list(T2Pvar(xs[6134]))),T2JAG($list(T2Pvar(x0[6135])))))
              ## T1IMPallx(gseq_foritm(402), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6401(line=407,offs=1)--6588(line=424,offs=2)))
              ## T1IMPallx(gseq_foritm(402)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6119],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_foritm(402);$list(@(xs[1215],T2Pvar(xs[6118])),@(x0[1216],T2Pvar(x0[6119])))))))
              def pyxtnm1984(arg1): ## timp: gseq_foritm(402)
                pyxtnm1850 = arg1
                ## I1CMP:start
                ## let
                pyxtnm1983 = None
                ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6119]))))):timp
                ## let
                pyxtnm1982 = None
                ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6459(line=414,offs=1)--6491(line=416,offs=13)))
                ## I1VALDCL
                pyxtnm1981 = None
                ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6467(line=415,offs=1)--6478(line=415,offs=12))
                ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6118]))),T2JAG($list(T2Pvar(x0[6119])))))
                ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3744(line=210,offs=1)--4061(line=236,offs=2)))
                ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6448],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6449],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6450],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(y0[6451],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(gx2seq);$list(T2Pvar(xs[6448]),T2Pvar(x0[6449]),T2Pvar(ys[6450]),T2Pvar(y0[6451])))),@(x0[1168],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6449])),S2LAB(LABint(1);T2Pvar(y0[6451]))))))))))
                def pyxtnm1979(arg1): ## timp: gseq_forall(386)
                  pyxtnm1855 = arg1
                  ## I1CMP:start
                  ## let
                  pyxtnm1978 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3897(line=227,offs=1)--3931(line=229,offs=26)))
                  ## I1VALDCL
                  pyxtnm1860 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3915(line=229,offs=10)--3925(line=229,offs=20))
                  ## I0Etapq(I0Ecst(x2tup_unmk(177)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(5757(line=387,offs=1)--5767(line=387,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(xs[6448]),T2Pvar(x0[6449]))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(ys[6450]),T2Pvar(y0[6451])))))))
                  ## T1IMPallx(x2tup_unmk(177), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1932(line=79,offs=1)--2000(line=83,offs=29)))
                  ## T1IMPallx(x2tup_unmk(177)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))>;I1Dtmpsub($list(@(a0[5808],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5809],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))));I1Dimplmnt0(DIMPLone2(x2tup_unmk(177);$list(@(xs[714],T2Pvar(a0[5808])),@(ys[715],T2Pvar(a1[5809])))))))
                  def pyxtnm1858(arg1): ## timp: x2tup_unmk(177)
                    pyxtnm1856 = arg1
                    ## I1CMP:start
                    pyxtnm1857 = XATSCAST("castxy_1839", [pyxtnm1856])
                    ## I1CMP:return:I1Vtnm(I1TNM(1857))
                    return pyxtnm1857
                  ## endtimp(x2tup_unmk(177))
                  pyxtnm1859 = XATSDAPP(pyxtnm1858(pyxtnm1855))
                  pyxtnm1860 = pyxtnm1859
                  XATS000_patck(True)
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3932(line=230,offs=1)--3993(line=231,offs=31)))
                  ## I1VALDCL
                  pyxtnm1865 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3941(line=230,offs=10)--3950(line=230,offs=19))
                  ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6448]))),T2JAG($list(T2Pvar(x0[6449])))))
                  ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
                  ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
                  def pyxtnm1863(arg1): ## timp: GSEQ_unmk(245)
                    pyxtnm1861 = arg1
                    ## I1CMP:start
                    pyxtnm1862 = XATSCAST("castxy_1839", [pyxtnm1861])
                    ## I1CMP:return:I1Vtnm(I1TNM(1862))
                    return pyxtnm1862
                  ## endtimp(GSEQ_unmk(245))
                  pyxtnm1864 = XATSDAPP(pyxtnm1863(XATSP0RJ(pyxtnm1860[0])))
                  pyxtnm1865 = pyxtnm1864
                  XATS000_patck(True)
                  ## I1VALDCL
                  pyxtnm1870 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3972(line=231,offs=10)--3981(line=231,offs=19))
                  ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(ys[6450]))),T2JAG($list(T2Pvar(y0[6451])))))
                  ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
                  ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(x0[6650],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
                  def pyxtnm1868(arg1): ## timp: GSEQ_unmk(245)
                    pyxtnm1866 = arg1
                    ## I1CMP:start
                    pyxtnm1867 = XATSCAST("castxy_1839", [pyxtnm1866])
                    ## I1CMP:return:I1Vtnm(I1TNM(1867))
                    return pyxtnm1867
                  ## endtimp(GSEQ_unmk(245))
                  pyxtnm1869 = XATSDAPP(pyxtnm1868(XATSP0RJ(pyxtnm1860[1])))
                  pyxtnm1870 = pyxtnm1869
                  XATS000_patck(True)
                  ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3997(line=233,offs=1)--4059(line=235,offs=40)))
                  ## I1Dimplmnt0(DIMPLone2(x2forall$test(178);$list(@(x1[716],T2Pvar(x0[6449])),@(x2[717],T2Pvar(y0[6451]))))):timp
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3846(line=222,offs=1)--3859(line=222,offs=14))
                  ## I0Etapq(I0Ecst(gseq_x2forall(578)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq002.sats)@(7231(line=463,offs=1)--7244(line=463,offs=14))));$list(T2JAG($list(T2Pvar(xs[6448]))),T2JAG($list(T2Pvar(x0[6449]))),T2JAG($list(T2Pvar(ys[6450]))),T2JAG($list(T2Pvar(y0[6451])))))
                  ## T1IMPallx(gseq_x2forall(578), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(9943(line=672,offs=1)--10253(line=698,offs=4)))
                  ## T1IMPallx(gseq_x2forall(578)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6496],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6498],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(y0[6499],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(gseq_x2forall(578);$list(@(xs[1794],T2Pvar(xs[6496])),@(x0[1795],T2Pvar(x0[6497])),@(ys[1796],T2Pvar(ys[6498])),@(y0[1797],T2Pvar(y0[6499])))))))
                  def pyxtnm1976(arg1, arg2): ## timp: gseq_x2forall(578)
                    pyxtnm1875 = arg1
                    pyxtnm1876 = arg2
                    ## I1CMP:start
                    ## let
                    pyxtnm1975 = None
                    ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10026(line=681,offs=1)--10151(line=689,offs=32)))
                    ## I1FUNDCL
                    def forall_test_x0_10029(arg1): ## fun
                      pyxtnm1877 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm1957 = None
                      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10089(line=687,offs=1)--10149(line=689,offs=30)))
                      ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(y0[6499]))))):timp
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10055(line=684,offs=3)--10066(line=684,offs=14))
                      ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(ys[6498]))),T2JAG($list(T2Pvar(y0[6499])))))
                      ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2157(line=87,offs=1)--2477(line=114,offs=2)))
                      ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6432],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6433],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6434],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6435],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(gz2seq);$list(T2Pvar(xs[6432]),T2Pvar(x0[6433]),T2Pvar(ys[6434]),T2Pvar(y0[6435])))),@(x0[1168],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6433])),S2LAB(LABint(1);T2Pvar(y0[6435]))))))))))
                      def pyxtnm1955(arg1): ## timp: gseq_forall(386)
                        pyxtnm1880 = arg1
                        ## I1CMP:start
                        ## let
                        pyxtnm1954 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2310(line=104,offs=1)--2344(line=106,offs=26)))
                        ## I1VALDCL
                        pyxtnm1885 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2328(line=106,offs=10)--2338(line=106,offs=20))
                        ## I0Etapq(I0Ecst(z2tup_unmk(135)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(2241(line=107,offs=1)--2251(line=107,offs=11))));$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(xs[6432]),T2Pvar(x0[6433]))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Pvar(ys[6434]),T2Pvar(y0[6435])))))))
                        ## T1IMPallx(z2tup_unmk(135), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gbas002.dats)@(1596(line=53,offs=1)--1664(line=57,offs=29)))
                        ## T1IMPallx(z2tup_unmk(135)<$list(T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2JAG($list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))>;I1Dtmpsub($list(@(a0[5802],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))),@(a1[5803],T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))));I1Dimplmnt0(DIMPLone2(z2tup_unmk(135);$list(@(xs[600],T2Pvar(a0[5802])),@(ys[601],T2Pvar(a1[5803])))))))
                        def pyxtnm1883(arg1): ## timp: z2tup_unmk(135)
                          pyxtnm1881 = arg1
                          ## I1CMP:start
                          pyxtnm1882 = XATSCAST("castxy_1839", [pyxtnm1881])
                          ## I1CMP:return:I1Vtnm(I1TNM(1882))
                          return pyxtnm1882
                        ## endtimp(z2tup_unmk(135))
                        pyxtnm1884 = XATSDAPP(pyxtnm1883(pyxtnm1880))
                        pyxtnm1885 = pyxtnm1884
                        XATS000_patck(True)
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2345(line=107,offs=1)--2406(line=108,offs=31)))
                        ## I1VALDCL
                        pyxtnm1890 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2354(line=107,offs=10)--2363(line=107,offs=19))
                        ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6432]))),T2JAG($list(T2Pvar(x0[6433])))))
                        ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
                        ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
                        def pyxtnm1888(arg1): ## timp: GSEQ_unmk(245)
                          pyxtnm1886 = arg1
                          ## I1CMP:start
                          pyxtnm1887 = XATSCAST("castxy_1839", [pyxtnm1886])
                          ## I1CMP:return:I1Vtnm(I1TNM(1887))
                          return pyxtnm1887
                        ## endtimp(GSEQ_unmk(245))
                        pyxtnm1889 = XATSDAPP(pyxtnm1888(XATSP0RJ(pyxtnm1885[0])))
                        pyxtnm1890 = pyxtnm1889
                        XATS000_patck(True)
                        ## I1VALDCL
                        pyxtnm1895 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2385(line=108,offs=10)--2394(line=108,offs=19))
                        ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(ys[6434]))),T2JAG($list(T2Pvar(y0[6435])))))
                        ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
                        ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6650],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
                        def pyxtnm1893(arg1): ## timp: GSEQ_unmk(245)
                          pyxtnm1891 = arg1
                          ## I1CMP:start
                          pyxtnm1892 = XATSCAST("castxy_1839", [pyxtnm1891])
                          ## I1CMP:return:I1Vtnm(I1TNM(1892))
                          return pyxtnm1892
                        ## endtimp(GSEQ_unmk(245))
                        pyxtnm1894 = XATSDAPP(pyxtnm1893(XATSP0RJ(pyxtnm1885[1])))
                        pyxtnm1895 = pyxtnm1894
                        XATS000_patck(True)
                        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2410(line=110,offs=1)--2472(line=112,offs=40)))
                        ## I1Dimplmnt0(DIMPLone2(z2forall$test(136);$list(@(x1[602],T2Pvar(x0[6433])),@(x2[603],T2Pvar(y0[6435]))))):timp
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2259(line=99,offs=1)--2272(line=99,offs=14))
                        ## I0Etapq(I0Ecst(gseq_z2forall(544)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq002.sats)@(2884(line=151,offs=1)--2897(line=151,offs=14))));$list(T2JAG($list(T2Pvar(xs[6432]))),T2JAG($list(T2Pvar(x0[6433]))),T2JAG($list(T2Pvar(ys[6434]))),T2JAG($list(T2Pvar(y0[6435])))))
                        ## T1IMPallx(gseq_z2forall(544), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats)@(2186(line=95,offs=1)--2284(line=101,offs=26)))
                        ## T1IMPallx(gseq_z2forall(544)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7582],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7582],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[7583],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[7583],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_z2forall(544);$list(@(xs[1644],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7582])))),@(x0[1645],T2Pvar(x0[7582])),@(ys[1646],T2Papps(T2Pcst(list);$list(T2Pvar(y0[7583])))),@(y0[1647],T2Pvar(y0[7583])))))))
                        pyxtnm1952 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats)@(2259(line=101,offs=1)--2272(line=101,offs=14))
                        ## I0Etapq(I0Ecst(list_z2forall(1275)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list002.sats)@(1436(line=44,offs=1)--1449(line=44,offs=14))));$list(T2JAG($list(T2Pvar(x0[7582]))),T2JAG($list(T2Pvar(y0[7583])))))
                        ## T1IMPallx(list_z2forall(1275), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats)@(1802(line=64,offs=1)--2142(line=93,offs=2)))
                        ## T1IMPallx(list_z2forall(1275)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7580],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(y0[7581],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_z2forall(1275);$list(@(x0[3510],T2Pvar(x0[7580])),@(y0[3511],T2Pvar(y0[7581])))))))
                        def pyxtnm1951(arg1, arg2): ## timp: list_z2forall(1275)
                          pyxtnm1900 = arg1
                          pyxtnm1901 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm1950 = None
                          ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats)@(1889(line=72,offs=1)--2140(line=92,offs=35)))
                          ## I1FUNDCL
                          def auxloop_1892(arg1, arg2): ## fun
                            pyxtnm1902 = arg1
                            pyxtnm1903 = arg2
                            ## I1CMP:start
                            pyxtnm1948 = None
                            while True: ## do {
                              ## { // cls
                              ## I1GPTpat(I1BNDcons(I1TNM(1904);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
                              if (XATS000_ctgeq(pyxtnm1902, XATSCTAG("list_nil",0))): ## { // gpt
                                pyxtnm1904 = pyxtnm1902
                                pyxtnm1948 = XATSBOOL(True)
                                break ## cls
                              ## } // gpt
                              ## } // cls
                              ## { // cls
                              ## I1GPTpat(I1BNDcons(I1TNM(1905);I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2690)),I0Pvar(xs(2691))));$list(@(x1(2690),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1905));0)),@(xs(2691),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1905));1)))))
                              if (XATS000_ctgeq(pyxtnm1902, XATSCTAG("list_cons",1))): ## { // gpt
                                pyxtnm1905 = pyxtnm1902
                                pyxtnm1947 = None
                                while True: ## do {
                                  ## { // cls
                                  ## I1GPTpat(I1BNDcons(I1TNM(1906);I0Pdapp(I0Pcon(list_nil(8));$list());$list()))
                                  if (XATS000_ctgeq(pyxtnm1903, XATSCTAG("list_nil",0))): ## { // gpt
                                    pyxtnm1906 = pyxtnm1903
                                    pyxtnm1947 = XATSBOOL(True)
                                    break ## cls
                                  ## } // gpt
                                  ## } // cls
                                  ## { // cls
                                  ## I1GPTpat(I1BNDcons(I1TNM(1907);I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(y1(2692)),I0Pvar(ys(2693))));$list(@(y1(2692),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1907));0)),@(ys(2693),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1907));1)))))
                                  if (XATS000_ctgeq(pyxtnm1903, XATSCTAG("list_cons",1))): ## { // gpt
                                    pyxtnm1907 = pyxtnm1903
                                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list002.dats)@(2075(line=90,offs=1)--2088(line=90,offs=14))
                                    ## I0Etapq(I0Ecst(z2forall$test(136)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(2355(line=117,offs=1)--2368(line=117,offs=14))));$list(T2JAG($list(T2Pvar(x0[7580]))),T2JAG($list(T2Pvar(y0[7581])))))
                                    ## T1IMPallx(z2forall$test(136), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2410(line=110,offs=1)--2472(line=112,offs=40)))
                                    ## T1IMPallx(z2forall$test(136)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6432],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6433],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6434],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(y0[6435],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(z2forall$test(136);$list(@(x1[602],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[603],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                                    def pyxtnm1943(arg1, arg2): ## timp: z2forall$test(136)
                                      pyxtnm1908 = arg1
                                      pyxtnm1909 = arg2
                                      ## I1CMP:start
                                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(2452(line=112,offs=20)--2463(line=112,offs=31))
                                      ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6433])),S2LAB(LABint(1);T2Pvar(y0[6435]))))))))
                                      ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10089(line=687,offs=1)--10149(line=689,offs=30)))
                                      ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6496],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6498],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(y0[6499],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                                      def pyxtnm1940(arg1): ## timp: forall$test(47)
                                        pyxtnm1910 = arg1
                                        ## I1CMP:start
                                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10120(line=689,offs=1)--10133(line=689,offs=14))
                                        ## I0Etapq(I0Ecst(x2forall$test(178)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas002.sats)@(5871(line=397,offs=1)--5884(line=397,offs=14))));$list(T2JAG($list(T2Pvar(x0[6497]))),T2JAG($list(T2Pvar(y0[6499])))))
                                        ## T1IMPallx(x2forall$test(178), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(3997(line=233,offs=1)--4059(line=235,offs=40)))
                                        ## T1IMPallx(x2forall$test(178)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(xs[6448],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6449],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6450],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(y0[6451],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(x2forall$test(178);$list(@(x1[716],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x2[717],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))
                                        def pyxtnm1938(arg1, arg2): ## timp: x2forall$test(178)
                                          pyxtnm1911 = arg1
                                          pyxtnm1912 = arg2
                                          ## I1CMP:start
                                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(4039(line=235,offs=20)--4050(line=235,offs=31))
                                          ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Pvar(x0[6449])),S2LAB(LABint(1);T2Pvar(y0[6451]))))))))
                                          ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6511(line=419,offs=1)--6586(line=423,offs=32)))
                                          ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6118],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6119],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
                                          def pyxtnm1935(arg1): ## timp: forall$test(47)
                                            pyxtnm1913 = arg1
                                            ## I1CMP:start
                                            ## let
                                            pyxtnm1934 = None
                                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6546(line=422,offs=1)--6574(line=423,offs=20)))
                                            ## I1VALDCL
                                            pyxtnm1933 = None
                                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(6555(line=423,offs=1)--6566(line=423,offs=12))
                                            ## I0Etapq(I0Ecst(foritm$work(51)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2341(line=124,offs=1)--2352(line=124,offs=12))));$list(T2JAG($list(T2Pvar(x0[6119])))))
                                            ## T1IMPallx(foritm$work(51), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8394(line=555,offs=1)--8531(line=562,offs=39)))
                                            ## T1IMPallx(foritm$work(51)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6134],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6135],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(r0[6136],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(foritm$work(51);$list(@(x0[464],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
                                            def pyxtnm1931(arg1): ## timp: foritm$work(51)
                                              pyxtnm1914 = arg1
                                              ## I1CMP:start
                                              ## let
                                              pyxtnm1930 = None
                                              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8463(line=561,offs=1)--8492(line=561,offs=30)))
                                              ## I1VALDCL
                                              pyxtnm1919 = None
                                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8476(line=561,offs=14)--8484(line=561,offs=22))
                                              ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Pvar(r0[6136])))))
                                              ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                                              ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                                              def pyxtnm1917(arg1): ## timp: p2tr_get(2309)
                                                pyxtnm1915 = arg1
                                                ## I1CMP:start
                                                pyxtnm1916 = XATS000_dp2tr(pyxtnm1915)
                                                ## I1CMP:return:I1Vtnm(I1TNM(1916))
                                                return pyxtnm1916
                                              ## endtimp(p2tr_get(2309))
                                              pyxtnm1918 = XATSDAPP(pyxtnm1917(pyxtnm1842))
                                              pyxtnm1919 = pyxtnm1918
                                              XATS000_patck(True)
                                              ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8493(line=562,offs=1)--8530(line=562,offs=38)))
                                              ## I1VALDCL
                                              pyxtnm1925 = None
                                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8502(line=562,offs=10)--8514(line=562,offs=22))
                                              ## I0Etapq(I0Ecst(folditm$fopr(55)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2551(line=141,offs=1)--2563(line=141,offs=13))));$list(T2JAG($list(T2Pvar(x0[6135]))),T2JAG($list(T2Pvar(r0[6136])))))
                                              ## T1IMPallx(folditm$fopr(55), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(2290(line=104,offs=1)--2352(line=107,offs=32)))
                                              ## T1IMPallx(folditm$fopr(55)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6084],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6085],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(folditm$fopr(55);$list(@(x0[468],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(r0[469],T2Papps(T2Pcst(list_vt);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))))
                                              def pyxtnm1923(arg1, arg2): ## timp: folditm$fopr(55)
                                                pyxtnm1920 = arg1
                                                pyxtnm1921 = arg2
                                                ## I1CMP:start
                                                pyxtnm1922 = XATSCAPP("list_vt_cons", [1, pyxtnm1921, pyxtnm1920])
                                                ## I1CMP:return:I1Vtnm(I1TNM(1922))
                                                return pyxtnm1922
                                              ## endtimp(folditm$fopr(55))
                                              pyxtnm1924 = XATSDAPP(pyxtnm1923(pyxtnm1919, pyxtnm1914))
                                              pyxtnm1925 = pyxtnm1924
                                              XATS000_patck(True)
                                              ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq001.dats)@(8433(line=558,offs=7)--8441(line=558,offs=15))
                                              ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Pvar(r0[6136])))))
                                              ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                                              ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                                              def pyxtnm1928(arg1, arg2): ## timp: p2tr_set(2310)
                                                pyxtnm1926 = arg1
                                                pyxtnm1927 = arg2
                                                ## I1CMP:start
                                                XATS000_assgn(pyxtnm1926, pyxtnm1927)
                                                ## I1CMP:return:I1V000()
                                                return XATSVOID
                                              ## endtimp(p2tr_set(2310))
                                              pyxtnm1929 = XATSDAPP(pyxtnm1928(pyxtnm1842, pyxtnm1925))
                                              pyxtnm1930 = pyxtnm1929
                                              ## end-of(let)
                                              ## I1CMP:return:I1Vtnm(I1TNM(1930))
                                              return pyxtnm1930
                                            ## endtimp(foritm$work(51))
                                            pyxtnm1932 = XATSDAPP(pyxtnm1931(pyxtnm1913))
                                            pyxtnm1933 = pyxtnm1932
                                            XATS000_patck(True)
                                            pyxtnm1934 = XATSBOOL(True)
                                            ## end-of(let)
                                            ## I1CMP:return:I1Vtnm(I1TNM(1934))
                                            return pyxtnm1934
                                          ## endtimp(forall$test(47))
                                          pyxtnm1936 = XATSTUP1(XATSTRCD(0), [pyxtnm1911, pyxtnm1912])
                                          pyxtnm1937 = XATSDAPP(pyxtnm1935(pyxtnm1936))
                                          ## I1CMP:return:I1Vtnm(I1TNM(1937))
                                          return pyxtnm1937
                                        ## endtimp(x2forall$test(178))
                                        pyxtnm1939 = XATSDAPP(pyxtnm1938(pyxtnm1877, pyxtnm1910))
                                        ## I1CMP:return:I1Vtnm(I1TNM(1939))
                                        return pyxtnm1939
                                      ## endtimp(forall$test(47))
                                      pyxtnm1941 = XATSTUP1(XATSTRCD(0), [pyxtnm1908, pyxtnm1909])
                                      pyxtnm1942 = XATSDAPP(pyxtnm1940(pyxtnm1941))
                                      ## I1CMP:return:I1Vtnm(I1TNM(1942))
                                      return pyxtnm1942
                                    ## endtimp(z2forall$test(136))
                                    pyxtnm1944 = XATSDAPP(pyxtnm1943(XATSP1CN("list_cons", pyxtnm1905[0+1]), XATSP1CN("list_cons", pyxtnm1907[0+1])))
                                    pyxtnm1946 = None
                                    if (pyxtnm1944):
                                      pyxtnm1945 = XATSDAPP(auxloop_1892(XATSP1CN("list_cons", pyxtnm1905[1+1]), XATSP1CN("list_cons", pyxtnm1907[1+1])))
                                      pyxtnm1946 = pyxtnm1945
                                    else:
                                      pyxtnm1946 = XATSBOOL(False)
                                    ## end-of(if)
                                    pyxtnm1947 = pyxtnm1946
                                    break ## cls
                                  ## } // gpt
                                  ## } // cls
                                  XATS000_cfail()
                                ## } while True // end-of(do-cls)
                                pyxtnm1948 = pyxtnm1947
                                break ## cls
                              ## } // gpt
                              ## } // cls
                              XATS000_cfail()
                            ## } while True // end-of(do-cls)
                            ## I1CMP:return:I1Vtnm(I1TNM(1948))
                            return pyxtnm1948
                          pyxtnm1949 = XATSDAPP(auxloop_1892(pyxtnm1900, pyxtnm1901))
                          pyxtnm1950 = pyxtnm1949
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(1950))
                          return pyxtnm1950
                        ## endtimp(list_z2forall(1275))
                        pyxtnm1952 = pyxtnm1951
                        pyxtnm1953 = XATSDAPP(pyxtnm1952(pyxtnm1890, pyxtnm1895))
                        pyxtnm1954 = pyxtnm1953
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(1954))
                        return pyxtnm1954
                      ## endtimp(gseq_forall(386))
                      pyxtnm1956 = XATSDAPP(pyxtnm1955(pyxtnm1876))
                      pyxtnm1957 = pyxtnm1956
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(1957))
                      return pyxtnm1957
                    ## let
                    pyxtnm1974 = None
                    ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10200(line=695,offs=1)--10241(line=696,offs=33)))
                    ## I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Pvar(x0[6497]))))):timp
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10167(line=693,offs=3)--10178(line=693,offs=14))
                    ## I0Etapq(I0Ecst(gseq_forall(386)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq001.sats)@(3721(line=210,offs=1)--3732(line=210,offs=12))));$list(T2JAG($list(T2Pvar(xs[6496]))),T2JAG($list(T2Pvar(x0[6497])))))
                    ## T1IMPallx(gseq_forall(386), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1841(line=78,offs=1)--1904(line=81,offs=33)))
                    ## T1IMPallx(gseq_forall(386)<$list(T2JAG($list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(x0[7480],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gseq_forall(386);$list(@(xs[1167],T2Papps(T2Pcst(list);$list(T2Pvar(x0[7480])))),@(x0[1168],T2Pvar(x0[7480])))))))
                    pyxtnm1972 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1889(line=81,offs=18)--1900(line=81,offs=29))
                    ## I0Etapq(I0Ecst(list_forall(1222)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/list001.sats)@(2160(line=92,offs=1)--2171(line=92,offs=12))));$list(T2JAG($list(T2Pvar(x0[7480])))))
                    ## T1IMPallx(list_forall(1222), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1591(line=53,offs=1)--1837(line=76,offs=2)))
                    ## T1IMPallx(list_forall(1222)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[7479],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(list_forall(1222);$list(@(x0[3422],T2Pvar(x0[7479])))))))
                    def pyxtnm1971(arg1): ## timp: list_forall(1222)
                      pyxtnm1958 = arg1
                      ## I1CMP:start
                      ## let
                      pyxtnm1970 = None
                      ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1657(line=60,offs=1)--1835(line=75,offs=31)))
                      ## I1FUNDCL
                      def loop_1660(arg1): ## fun
                        pyxtnm1959 = arg1
                        ## I1CMP:start
                        pyxtnm1968 = None
                        while True: ## do {
                          ## { // cls
                          ## I1GPTpat(I1BNDcons(I1TNM(1960);I0Pfree(I0Pdapp(I0Pcon(list_nil(8));$list()));$list()))
                          if (XATS000_ctgeq(pyxtnm1959, XATSCTAG("list_nil",0))): ## { // gpt
                            pyxtnm1960 = pyxtnm1959
                            pyxtnm1968 = XATSBOOL(True)
                            break ## cls
                          ## } // gpt
                          ## } // cls
                          ## { // cls
                          ## I1GPTpat(I1BNDcons(I1TNM(1961);I0Pfree(I0Pdapp(I0Pcon(list_cons(9));$list(I0Pvar(x1(2573)),I0Pvar(xs(2574)))));$list(@(x1(2573),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1961));0)),@(xs(2574),I1Vp1cn(I0Pcon(list_cons(9));I1Vtnm(I1TNM(1961));1)))))
                          if (XATS000_ctgeq(pyxtnm1959, XATSCTAG("list_cons",1))): ## { // gpt
                            pyxtnm1961 = pyxtnm1959
                            ## let
                            pyxtnm1967 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1761(line=71,offs=1)--1791(line=72,offs=20)))
                            ## I1VALDCL
                            pyxtnm1964 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/list001.dats)@(1772(line=72,offs=1)--1783(line=72,offs=12))
                            ## I0Etapq(I0Ecst(forall$test(47)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas001.sats)@(2003(line=96,offs=1)--2014(line=96,offs=12))));$list(T2JAG($list(T2Pvar(x0[7479])))))
                            ## T1IMPallx(forall$test(47), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gseq002.dats)@(10200(line=695,offs=1)--10241(line=696,offs=33)))
                            ## T1IMPallx(forall$test(47)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(xs[6496],T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0()))),@(x0[6497],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(ys[6498],T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))),@(y0[6499],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(forall$test(47);$list(@(x0[460],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))
                            pyxtnm1962 = None
                            pyxtnm1962 = forall_test_x0_10029
                            pyxtnm1963 = XATSDAPP(pyxtnm1962(XATSP1CN("list_cons", pyxtnm1961[0+1])))
                            pyxtnm1964 = pyxtnm1963
                            XATS000_patck(True)
                            pyxtnm1966 = None
                            if (pyxtnm1964):
                              pyxtnm1965 = XATSDAPP(loop_1660(XATSP1CN("list_cons", pyxtnm1961[1+1])))
                              pyxtnm1966 = pyxtnm1965
                            else:
                              pyxtnm1966 = XATSBOOL(False)
                            ## end-of(if)
                            pyxtnm1967 = pyxtnm1966
                            ## end-of(let)
                            pyxtnm1968 = pyxtnm1967
                            break ## cls
                          ## } // gpt
                          ## } // cls
                          XATS000_cfail()
                        ## } while True // end-of(do-cls)
                        ## I1CMP:return:I1Vtnm(I1TNM(1968))
                        return pyxtnm1968
                      pyxtnm1969 = XATSDAPP(loop_1660(pyxtnm1958))
                      pyxtnm1970 = pyxtnm1969
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(1970))
                      return pyxtnm1970
                    ## endtimp(list_forall(1222))
                    pyxtnm1972 = pyxtnm1971
                    pyxtnm1973 = XATSDAPP(pyxtnm1972(pyxtnm1875))
                    pyxtnm1974 = pyxtnm1973
                    ## end-of(let)
                    pyxtnm1975 = pyxtnm1974
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(1975))
                    return pyxtnm1975
                  ## endtimp(gseq_x2forall(578))
                  pyxtnm1977 = XATSDAPP(pyxtnm1976(pyxtnm1865, pyxtnm1870))
                  pyxtnm1978 = pyxtnm1977
                  ## end-of(let)
                  ## I1CMP:return:I1Vtnm(I1TNM(1978))
                  return pyxtnm1978
                ## endtimp(gseq_forall(386))
                pyxtnm1980 = XATSDAPP(pyxtnm1979(pyxtnm1850))
                pyxtnm1981 = pyxtnm1980
                XATS000_patck(True)
                pyxtnm1982 = XATSVOID
                ## end-of(let)
                pyxtnm1983 = pyxtnm1982
                ## end-of(let)
                ## I1CMP:return:I1Vtnm(I1TNM(1983))
                return pyxtnm1983
              ## endtimp(gseq_foritm(402))
              pyxtnm1985 = XATSDAPP(pyxtnm1984(pyxtnm1839))
              pyxtnm1986 = pyxtnm1985
              ## end-of(let)
              pyxtnm1987 = pyxtnm1986
              XATS000_patck(True)
              pyxtnm1988 = XATSFLAT(pyxtnm1841)
              pyxtnm1989 = pyxtnm1988
              ## end-of(let)
              ## I1CMP:return:I1Vtnm(I1TNM(1989))
              return pyxtnm1989
            ## endtimp(gseq_folditm(410))
            pyxtnm1991 = XATSDAPP(pyxtnm1990(pyxtnm1833, pyxtnm1835))
            pyxtnm1992 = pyxtnm1991
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(1992))
            return pyxtnm1992
          ## endtimp(gseq_rlistize(380))
          pyxtnm1994 = XATSDAPP(pyxtnm1993(pyxtnm1797))
          pyxtnm1995 = XATSDAPP(pyxtnm1832(pyxtnm1994))
          pyxtnm1996 = pyxtnm1995
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(1996))
          return pyxtnm1996
        ## endtimp(gseq_rforall(388))
        pyxtnm1998 = XATSDAPP(pyxtnm1997(pyxtnm1792))
        pyxtnm1999 = pyxtnm1998
        XATS000_patck(True)
        pyxtnm2000 = XATSVOID
        ## end-of(let)
        pyxtnm2001 = pyxtnm2000
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(2001))
        return pyxtnm2001
      ## endtimp(gseq_rforitm(403))
      pyxtnm2003 = XATSDAPP(pyxtnm2002(pyxtnm1781))
      pyxtnm2004 = pyxtnm2003
      ## end-of(let)
      pyxtnm2005 = pyxtnm2004
      XATS000_patck(True)
      pyxtnm2006 = XATSFLAT(pyxtnm1783)
      pyxtnm2007 = pyxtnm2006
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(2007))
      return pyxtnm2007
    ## endtimp(gseq_rfolditm(411))
    pyxtnm2009 = XATSDAPP(pyxtnm2008(pyxtnm1775, pyxtnm1777))
    pyxtnm2010 = pyxtnm2009
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(2010))
    return pyxtnm2010
  ## endtimp(gseq_listize(377))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(2554(line=132,offs=10)--2563(line=132,offs=19))
  ## I0Etapq(I0Ecst(GSEQ_unmk(245)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gcls000.sats)@(2269(line=102,offs=1)--2278(line=102,offs=10))));$list(T2JAG($list(T2Pvar(xs[6663]))),T2JAG($list(T2Pvar(x0[6664])))))
  ## T1IMPallx(GSEQ_unmk(245), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gcls000.dats)@(1499(line=45,offs=1)--1572(line=51,offs=20)))
  ## T1IMPallx(GSEQ_unmk(245)<$list(T2JAG($list(T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[6649],T2Papps(T2Pcst(x2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(z2tup_type);$list(T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))),T2Papps(T2Pcst(GSEQ_type);$list(T2Papps(T2Pcst(list_t0_i0_tx);$list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())),T2Pnone0())),T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))),T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))),@(x0[6650],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(GSEQ_unmk(245);$list(@(xs[817],T2Pvar(xs[6649])),@(x0[818],T2Pvar(x0[6650])))))))
  def pyxtnm2014(arg1): ## timp: GSEQ_unmk(245)
    pyxtnm2012 = arg1
    ## I1CMP:start
    pyxtnm2013 = XATSCAST("castxy_1839", [pyxtnm2012])
    ## I1CMP:return:I1Vtnm(I1TNM(2013))
    return pyxtnm2013
  ## endtimp(GSEQ_unmk(245))
  pyxtnm2015 = XATSDAPP(pyxtnm2014(pyxtnm1774))
  pyxtnm2016 = XATSDAPP(pyxtnm2011(pyxtnm2015))
  ## I1CMP:return:I1Vtnm(I1TNM(2016))
  return pyxtnm2016
## endtimp(GSEQ_listize(251))
pyxtnm2018 = XATSDAPP(pyxtnm2017(pyxtnm1380))
pyxtnm2019 = pyxtnm2018
XATS000_patck(True)
## I1Dvaldclist(LCSRCsome1(test07_gseq000.dats)@(967(line=60,offs=1)--1020(line=61,offs=42)))
## I1VALDCL
pyxtnm2255 = None
## LCSRCsome1(test07_gseq000.dats)@(979(line=61,offs=1)--986(line=61,offs=8))
## I0Etapq(I0Ecst(gs_print1_a3(1988)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(3614(line=218,offs=1)--3626(line=218,offs=13))));$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))))))
## T1IMPallx(gs_print1_a3(1988), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5507(line=274,offs=1)--5674(line=283,offs=21)))
## T1IMPallx(gs_print1_a3(1988)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8381],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))),@(x1[8382],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x2[8383],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(gs_print1_a3(1988);$list(@(x0[5119],T2Pvar(x0[8381])),@(x1[5120],T2Pvar(x1[8382])),@(x2[5121],T2Pvar(x2[8383])))))))
def pyxtnm2253(arg1, arg2, arg3): ## timp: gs_print1_a3(1988)
  pyxtnm2020 = arg1
  pyxtnm2021 = arg2
  pyxtnm2022 = arg3
  ## I1CMP:start
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5578(line=280,offs=3)--5591(line=280,offs=16))
  ## I0Etapq(I0Ecst(gs_print1$beg(1972)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1528(line=52,offs=1)--1541(line=52,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print1$beg(1972), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5090(line=241,offs=1)--5129(line=243,offs=21)))
  ## T1IMPallx(gs_print1$beg(1972)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$beg(1972);$list()))))
  def pyxtnm2024(): ## timp: gs_print1$beg(1972)
    ## I1CMP:start
    pyxtnm2023 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(2023))
    return pyxtnm2023
  ## endtimp(gs_print1$beg(1972))
  pyxtnm2025 = XATSDAPP(pyxtnm2024())
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5599(line=281,offs=3)--5607(line=281,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[8381])))))
  ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
  pyxtnm2032 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm2031 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm2030(arg1): ## timp: strn_print(1040)
    pyxtnm2026 = arg1
    ## I1CMP:start
    ## let
    pyxtnm2029 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2027);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2027))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm2028 = XATSDAPP(XATS2PY_strn_print(pyxtnm2026))
    pyxtnm2029 = pyxtnm2028
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(2029))
    return pyxtnm2029
  ## endtimp(strn_print(1040))
  pyxtnm2031 = pyxtnm2030
  pyxtnm2032 = pyxtnm2031
  pyxtnm2033 = XATSDAPP(pyxtnm2032(pyxtnm2020))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5618(line=282,offs=3)--5626(line=282,offs=11))
  ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x1[8382])))))
  ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2935(line=156,offs=1)--3019(line=162,offs=2)))
  ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8498],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8498])))))))))
  def pyxtnm2240(arg1): ## timp: g_print1(1412)
    pyxtnm2034 = arg1
    ## I1CMP:start
    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2985(line=161,offs=1)--2996(line=161,offs=12))
    ## I0Etapq(I0Ecst(gseq_print1(1687)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq000_vt.sats)@(3999(line=245,offs=1)--4010(line=245,offs=12))));$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Pvar(x0[8498]),T2Pnone0())))),T2JAG($list(T2Pvar(x0[8498])))))
    ## T1IMPallx(gseq_print1(1687), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4483(line=284,offs=1)--4800(line=309,offs=7)))
    ## T1IMPallx(gseq_print1(1687)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x0[7906],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_print1(1687);$list(@(xs[4221],T2Pvar(xs[7905])),@(x0[4222],T2Pvar(x0[7906])))))))
    def pyxtnm2238(arg1): ## timp: gseq_print1(1687)
      pyxtnm2035 = arg1
      ## I1CMP:start
      ## let
      pyxtnm2237 = None
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4534(line=289,offs=1)--4576(line=291,offs=21)))
      ## I1VALDCL
      pyxtnm2044 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4543(line=290,offs=1)--4553(line=290,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm2040(arg1): ## timp: strn_print(1040)
        pyxtnm2036 = arg1
        ## I1CMP:start
        ## let
        pyxtnm2039 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2037);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2037))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm2038 = XATSDAPP(XATS2PY_strn_print(pyxtnm2036))
        pyxtnm2039 = pyxtnm2038
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(2039))
        return pyxtnm2039
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4557(line=291,offs=2)--4565(line=291,offs=10))
      ## I0Etapq(I0Ecst(gseq$beg(346)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2390(line=130,offs=1)--2398(line=130,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$beg(346), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2728(line=141,offs=1)--2788(line=144,offs=33)))
      ## T1IMPallx(gseq$beg(346)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8496],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(x0[8496],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq$beg(346);$list(@(xs[1067],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8496])))),@(x0[1068],T2Pvar(x0[8496])))))))
      def pyxtnm2041(): ## timp: gseq$beg(346)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN("list_vt(")
      ## endtimp(gseq$beg(346))
      pyxtnm2042 = XATSDAPP(pyxtnm2041())
      pyxtnm2043 = XATSDAPP(pyxtnm2040(pyxtnm2042))
      pyxtnm2044 = pyxtnm2043
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4577(line=292,offs=1)--4751(line=306,offs=2)))
      ## I1VALDCL
      pyxtnm2227 = None
      ## let
      pyxtnm2226 = None
      ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
      ## I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Pvar(x0[7906]))))):timp
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4588(line=294,offs=1)--4601(line=294,offs=14))
      ## I0Etapq(I0Ecst(gseq_iforitm1(1760)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(10899(line=588,offs=1)--10912(line=588,offs=14))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq_iforitm1(1760), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(9997(line=678,offs=1)--10202(line=695,offs=2)))
      ## T1IMPallx(gseq_iforitm1(1760)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x0[8041],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_iforitm1(1760);$list(@(xs[4404],T2Pvar(xs[8040])),@(x0[4405],T2Pvar(x0[8041])))))))
      def pyxtnm2224(arg1): ## timp: gseq_iforitm1(1760)
        pyxtnm2054 = arg1
        ## I1CMP:start
        ## let
        pyxtnm2223 = None
        ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
        ## I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Pvar(x0[8041]))))):timp
        ## let
        pyxtnm2222 = None
        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10057(line=685,offs=1)--10093(line=687,offs=15)))
        ## I1VALDCL
        pyxtnm2221 = None
        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10065(line=686,offs=1)--10078(line=686,offs=14))
        ## I0Etapq(I0Ecst(gseq_iforall1(1736)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(6529(line=346,offs=1)--6542(line=346,offs=14))));$list(T2JAG($list(T2Pvar(xs[8040]))),T2JAG($list(T2Pvar(x0[8041])))))
        ## T1IMPallx(gseq_iforall1(1736), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6019(line=377,offs=1)--6322(line=403,offs=2)))
        ## T1IMPallx(gseq_iforall1(1736)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x0[8009],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_iforall1(1736);$list(@(xs[4356],T2Pvar(xs[8008])),@(x0[4357],T2Pvar(x0[8009])))))))
        def pyxtnm2219(arg1): ## timp: gseq_iforall1(1736)
          pyxtnm2060 = arg1
          ## I1CMP:start
          ## let
          pyxtnm2218 = None
          ## I1Dvardclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6087(line=384,offs=1)--6103(line=384,offs=17)))
          ## I1VARDCL
          ## I1CMP:start
          ## I1CMP:return:I1Vint(T_INT01(0))
          pyxtnm2061 = XATSVAR1(XATSINT1(0))
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6107(line=386,offs=1)--6125(line=386,offs=19)))
          ## I1VALDCL
          pyxtnm2062 = None
          pyxtnm2062 = XATSADDR(pyxtnm2061)
          XATS000_patck(True)
          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6129(line=388,offs=1)--6317(line=401,offs=2)))
          ## I1VALDCL
          pyxtnm2217 = None
          ## let
          pyxtnm2216 = None
          ## I1Dimplmnt0(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
          ## I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Pvar(x0[8009]))))):timp
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6140(line=390,offs=1)--6152(line=390,offs=13))
          ## I0Etapq(I0Ecst(gseq_forall1(1720)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gseq001_vt.sats)@(3696(line=185,offs=1)--3708(line=185,offs=13))));$list(T2JAG($list(T2Pvar(xs[8008]))),T2JAG($list(T2Pvar(x0[8009])))))
          ## T1IMPallx(gseq_forall1(1720), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2048(line=94,offs=1)--2119(line=97,offs=40)))
          ## T1IMPallx(gseq_forall1(1720)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8546],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(x0[8546],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq_forall1(1720);$list(@(xs[4324],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8546])))),@(x0[4325],T2Pvar(x0[8546])))))))
          pyxtnm2214 = None
          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(2100(line=97,offs=21)--2115(line=97,offs=36))
          ## I0Etapq(I0Ecst(list_vt_forall1(2063)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/list001_vt.sats)@(1481(line=47,offs=1)--1496(line=47,offs=16))));$list(T2JAG($list(T2Pvar(x0[8546])))))
          ## T1IMPallx(list_vt_forall1(2063), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1707(line=67,offs=1)--1964(line=88,offs=2)))
          ## T1IMPallx(list_vt_forall1(2063)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8544],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(list_vt_forall1(2063);$list(@(x0[5291],T2Pvar(x0[8544])))))))
          def pyxtnm2213(arg1): ## timp: list_vt_forall1(2063)
            pyxtnm2071 = arg1
            ## I1CMP:start
            ## let
            pyxtnm2212 = None
            ## I1Dfundclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1777(line=74,offs=1)--1962(line=87,offs=38)))
            ## I1FUNDCL
            def loop_1780(arg1): ## fun
              pyxtnm2072 = arg1
              ## I1CMP:start
              pyxtnm2210 = None
              while True: ## do {
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(2073);I0Pdapp(I0Pcon(list_vt_nil(10));$list());$list()))
                if (XATS000_ctgeq(pyxtnm2072, XATSCTAG("list_vt_nil",0))): ## { // gpt
                  pyxtnm2073 = pyxtnm2072
                  pyxtnm2210 = XATSBOOL(True)
                  break ## cls
                ## } // gpt
                ## } // cls
                ## { // cls
                ## I1GPTpat(I1BNDcons(I1TNM(2074);I0Pdapp(I0Pcon(list_vt_cons(11));$list(I0Pvar(x1(4347)),I0Pvar(xs(4348))));$list(@(x1(4347),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(2074));0)),@(xs(4348),I1Vp1cn(I0Pcon(list_vt_cons(11));I1Vtnm(I1TNM(2074));1)))))
                if (XATS000_ctgeq(pyxtnm2072, XATSCTAG("list_vt_cons",1))): ## { // gpt
                  pyxtnm2074 = pyxtnm2072
                  ## let
                  pyxtnm2209 = None
                  ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1890(line=85,offs=1)--1921(line=86,offs=21)))
                  ## I1VALDCL
                  pyxtnm2206 = None
                  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list001_vt.dats)@(1901(line=86,offs=1)--1913(line=86,offs=13))
                  ## I0Etapq(I0Ecst(forall$test1(1423)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2148(line=110,offs=1)--2160(line=110,offs=13))));$list(T2JAG($list(T2Pvar(x0[8544])))))
                  ## T1IMPallx(forall$test1(1423), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6175(line=393,offs=1)--6315(line=400,offs=37)))
                  ## T1IMPallx(forall$test1(1423)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[8008],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x0[8009],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(forall$test1(1423);$list(@(x0[3766],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
                  def pyxtnm2204(arg1): ## timp: forall$test1(1423)
                    pyxtnm2075 = arg1
                    ## I1CMP:start
                    ## let
                    pyxtnm2203 = None
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6249(line=399,offs=1)--6278(line=399,offs=30)))
                    ## I1VALDCL
                    pyxtnm2080 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6262(line=399,offs=14)--6270(line=399,offs=22))
                    ## I0Etapq(I0Ecst(p2tr_get(2309)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2573(line=124,offs=1)--2581(line=124,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_get(2309), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(197(line=15,offs=1)--245(line=18,offs=17)))
                    ## T1IMPallx(p2tr_get(2309)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5908],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_get(2309);$list(@(a[5707],T2Pvar(a[5908])))))))
                    def pyxtnm2078(arg1): ## timp: p2tr_get(2309)
                      pyxtnm2076 = arg1
                      ## I1CMP:start
                      pyxtnm2077 = XATS000_dp2tr(pyxtnm2076)
                      ## I1CMP:return:I1Vtnm(I1TNM(2077))
                      return pyxtnm2077
                    ## endtimp(p2tr_get(2309))
                    pyxtnm2079 = XATSDAPP(pyxtnm2078(pyxtnm2062))
                    pyxtnm2080 = pyxtnm2079
                    XATS000_patck(True)
                    ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6279(line=400,offs=1)--6313(line=400,offs=35)))
                    ## I1VALDCL
                    pyxtnm2190 = None
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6288(line=400,offs=10)--6301(line=400,offs=23))
                    ## I0Etapq(I0Ecst(iforall$test1(1433)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(2611(line=148,offs=1)--2624(line=148,offs=14))));$list(T2JAG($list(T2Pvar(x0[8009])))))
                    ## T1IMPallx(iforall$test1(1433), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10113(line=690,offs=1)--10200(line=694,offs=38)))
                    ## T1IMPallx(iforall$test1(1433)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[8040],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x0[8041],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(iforall$test1(1433);$list(@(x0[3776],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
                    def pyxtnm2188(arg1, arg2): ## timp: iforall$test1(1433)
                      pyxtnm2081 = arg1
                      pyxtnm2082 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm2187 = None
                      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10154(line=693,offs=1)--10188(line=694,offs=26)))
                      ## I1VALDCL
                      pyxtnm2186 = None
                      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(10163(line=694,offs=1)--10176(line=694,offs=14))
                      ## I0Etapq(I0Ecst(iforitm$work1(1449)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas001_vt.sats)@(3334(line=206,offs=1)--3347(line=206,offs=14))));$list(T2JAG($list(T2Pvar(x0[8041])))))
                      ## T1IMPallx(iforitm$work1(1449), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4624(line=297,offs=1)--4749(line=305,offs=2)))
                      ## T1IMPallx(iforitm$work1(1449)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(xs[7905],T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0()))),@(x0[7906],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(iforitm$work1(1449);$list(@(x0[3792],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))))))))
                      def pyxtnm2184(arg1, arg2): ## timp: iforitm$work1(1449)
                        pyxtnm2083 = arg1
                        pyxtnm2084 = arg2
                        ## I1CMP:start
                        ## let
                        pyxtnm2183 = None
                        ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4691(line=302,offs=1)--4747(line=304,offs=33)))
                        ## I1VALDCL
                        pyxtnm2102 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4706(line=303,offs=7)--4707(line=303,offs=8))
                        ## I0Etapq(I0Ecst(sint_gt$sint(928)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(2103(line=87,offs=1)--2115(line=87,offs=13))));$list(T2JAG($list())))
                        ## T1IMPallx(sint_gt$sint(928), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1777(line=70,offs=1)--1938(line=82,offs=2)))
                        ## T1IMPallx(sint_gt$sint(928)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_gt$sint(928);$list()))))
                        def pyxtnm2091(arg1, arg2): ## timp: sint_gt$sint(928)
                          pyxtnm2085 = arg1
                          pyxtnm2086 = arg2
                          ## I1CMP:start
                          ## let
                          pyxtnm2090 = None
                          ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(1865(line=78,offs=1)--1936(line=81,offs=39)))
                          ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_gt$sint(2614));$list(I1FUNDCL(XATS2PY_sint_gt$sint(4866);$list(FJARGdarg($list(I1BNDcons(I1TNM(2087);I0Pvar(i1(4867));$list(@(i1(4867),I1Vtnm(I1TNM(2087))))),I1BNDcons(I1TNM(2088);I0Pvar(i2(4868));$list(@(i2(4868),I1Vtnm(I1TNM(2088))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_gt$sint);G1Nlist($list())))))))
                          pyxtnm2089 = XATSDAPP(XATS2PY_sint_gt_sint(pyxtnm2085, pyxtnm2086))
                          pyxtnm2090 = pyxtnm2089
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(2090))
                          return pyxtnm2090
                        ## endtimp(sint_gt$sint(928))
                        pyxtnm2092 = XATSDAPP(pyxtnm2091(pyxtnm2083, XATSINT1(0)))
                        pyxtnm2101 = None
                        if (pyxtnm2092):
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4715(line=304,offs=1)--4725(line=304,offs=11))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm2097(arg1): ## timp: strn_print(1040)
                            pyxtnm2093 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm2096 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2094);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2094))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm2095 = XATSDAPP(XATS2PY_strn_print(pyxtnm2093))
                            pyxtnm2096 = pyxtnm2095
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(2096))
                            return pyxtnm2096
                          ## endtimp(strn_print(1040))
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4728(line=304,offs=14)--4736(line=304,offs=22))
                          ## I0Etapq(I0Ecst(gseq$sep(348)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2474(line=138,offs=1)--2482(line=138,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
                          ## T1IMPallx(gseq$sep(348), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2620(line=133,offs=1)--2673(line=136,offs=26)))
                          ## T1IMPallx(gseq$sep(348)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8494],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(x0[8494],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq$sep(348);$list(@(xs[1071],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8494])))),@(x0[1072],T2Pvar(x0[8494])))))))
                          def pyxtnm2098(): ## timp: gseq$sep(348)
                            ## I1CMP:start
                            ## I1CMP:return:I1Vstr(...)
                            return XATSSTRN(",")
                          ## endtimp(gseq$sep(348))
                          pyxtnm2099 = XATSDAPP(pyxtnm2098())
                          pyxtnm2100 = XATSDAPP(pyxtnm2097(pyxtnm2099))
                          pyxtnm2101 = pyxtnm2100
                        ## else: None
                        ## end-of(if)
                        pyxtnm2102 = pyxtnm2101
                        XATS000_patck(True)
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4665(line=300,offs=3)--4673(line=300,offs=11))
                        ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x0[7906])))))
                        ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
                        ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8803],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
                        pyxtnm2181 = None
                        ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
                        ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
                        ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2567(line=116,offs=1)--2780(line=135,offs=4)))
                        ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(a0[7362],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7363],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7362]),T2Pvar(a1[7363])))))))))
                        def pyxtnm2180(arg1): ## timp: g_print(39)
                          pyxtnm2103 = arg1
                          ## I1CMP:start
                          ## let
                          pyxtnm2179 = None
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2635(line=124,offs=1)--2662(line=125,offs=19)))
                          ## I1VALDCL
                          pyxtnm2110 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2646(line=125,offs=3)--2656(line=125,offs=13))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm2108(arg1): ## timp: strn_print(1040)
                            pyxtnm2104 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm2107 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2105);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2105))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm2106 = XATSDAPP(XATS2PY_strn_print(pyxtnm2104))
                            pyxtnm2107 = pyxtnm2106
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(2107))
                            return pyxtnm2107
                          ## endtimp(strn_print(1040))
                          pyxtnm2109 = XATSDAPP(pyxtnm2108(XATSSTRN("@(")))
                          pyxtnm2110 = pyxtnm2109
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2663(line=126,offs=1)--2692(line=127,offs=21)))
                          ## I1VALDCL
                          pyxtnm2119 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2674(line=127,offs=3)--2681(line=127,offs=10))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(a0[7362])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                          pyxtnm2116 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                          ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                          ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                          def pyxtnm2115(arg1): ## timp: sint_print(922)
                            pyxtnm2111 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm2114 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(2112);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(2112))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                            pyxtnm2113 = XATSDAPP(XATS2PY_sint_print(pyxtnm2111))
                            pyxtnm2114 = pyxtnm2113
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(2114))
                            return pyxtnm2114
                          ## endtimp(sint_print(922))
                          pyxtnm2116 = pyxtnm2115
                          pyxtnm2117 = XATSPFLT(pyxtnm2103[0])
                          pyxtnm2118 = XATSDAPP(pyxtnm2116(pyxtnm2117))
                          pyxtnm2119 = pyxtnm2118
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2696(line=129,offs=1)--2715(line=129,offs=20)))
                          ## I1VALDCL
                          pyxtnm2126 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2705(line=129,offs=10)--2710(line=129,offs=15))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm2124(arg1): ## timp: strn_print(1040)
                            pyxtnm2120 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm2123 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2121);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2121))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm2122 = XATSDAPP(XATS2PY_strn_print(pyxtnm2120))
                            pyxtnm2123 = pyxtnm2122
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(2123))
                            return pyxtnm2123
                          ## endtimp(strn_print(1040))
                          pyxtnm2125 = XATSDAPP(pyxtnm2124(XATSSTRN(",")))
                          pyxtnm2126 = pyxtnm2125
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2716(line=130,offs=1)--2745(line=131,offs=21)))
                          ## I1VALDCL
                          pyxtnm2171 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2727(line=131,offs=3)--2734(line=131,offs=10))
                          ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(a1[7363])))))
                          ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2567(line=116,offs=1)--2780(line=135,offs=4)))
                          ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))>;I1Dtmpsub($list(@(a0[7362],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),@(a1[7363],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Papps(T2Pcst(t0up);$list(T2Pvar(a0[7362]),T2Pvar(a1[7363])))))))))
                          def pyxtnm2168(arg1): ## timp: g_print(39)
                            pyxtnm2127 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm2167 = None
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2635(line=124,offs=1)--2662(line=125,offs=19)))
                            ## I1VALDCL
                            pyxtnm2134 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2646(line=125,offs=3)--2656(line=125,offs=13))
                            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                            def pyxtnm2132(arg1): ## timp: strn_print(1040)
                              pyxtnm2128 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm2131 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2129);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2129))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                              pyxtnm2130 = XATSDAPP(XATS2PY_strn_print(pyxtnm2128))
                              pyxtnm2131 = pyxtnm2130
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(2131))
                              return pyxtnm2131
                            ## endtimp(strn_print(1040))
                            pyxtnm2133 = XATSDAPP(pyxtnm2132(XATSSTRN("@(")))
                            pyxtnm2134 = pyxtnm2133
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2663(line=126,offs=1)--2692(line=127,offs=21)))
                            ## I1VALDCL
                            pyxtnm2143 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2674(line=127,offs=3)--2681(line=127,offs=10))
                            ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(a0[7362])))))
                            ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                            ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                            pyxtnm2140 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                            ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                            ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                            def pyxtnm2139(arg1): ## timp: sint_print(922)
                              pyxtnm2135 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm2138 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(2136);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(2136))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                              pyxtnm2137 = XATSDAPP(XATS2PY_sint_print(pyxtnm2135))
                              pyxtnm2138 = pyxtnm2137
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(2138))
                              return pyxtnm2138
                            ## endtimp(sint_print(922))
                            pyxtnm2140 = pyxtnm2139
                            pyxtnm2141 = XATSPFLT(pyxtnm2127[0])
                            pyxtnm2142 = XATSDAPP(pyxtnm2140(pyxtnm2141))
                            pyxtnm2143 = pyxtnm2142
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2696(line=129,offs=1)--2715(line=129,offs=20)))
                            ## I1VALDCL
                            pyxtnm2150 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2705(line=129,offs=10)--2710(line=129,offs=15))
                            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                            def pyxtnm2148(arg1): ## timp: strn_print(1040)
                              pyxtnm2144 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm2147 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2145);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2145))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                              pyxtnm2146 = XATSDAPP(XATS2PY_strn_print(pyxtnm2144))
                              pyxtnm2147 = pyxtnm2146
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(2147))
                              return pyxtnm2147
                            ## endtimp(strn_print(1040))
                            pyxtnm2149 = XATSDAPP(pyxtnm2148(XATSSTRN(",")))
                            pyxtnm2150 = pyxtnm2149
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2716(line=130,offs=1)--2745(line=131,offs=21)))
                            ## I1VALDCL
                            pyxtnm2159 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2727(line=131,offs=3)--2734(line=131,offs=10))
                            ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(a1[7363])))))
                            ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2286(line=96,offs=1)--2321(line=97,offs=27)))
                            ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(si)))))))
                            pyxtnm2156 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/gint000.dats)@(2309(line=97,offs=15)--2319(line=97,offs=25))
                            ## I0Etapq(I0Ecst(sint_print(922)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(1506(line=49,offs=1)--1516(line=49,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(sint_print(922), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3560(line=218,offs=1)--3700(line=229,offs=2)))
                            ## T1IMPallx(sint_print(922)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_print(922);$list()))))
                            def pyxtnm2155(arg1): ## timp: sint_print(922)
                              pyxtnm2151 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm2154 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(3640(line=226,offs=1)--3698(line=228,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_print(2624));$list(I1FUNDCL(XATS2PY_sint_print(4915);$list(FJARGdarg($list(I1BNDcons(I1TNM(2152);I0Pvar(i0(4916));$list(@(i0(4916),I1Vtnm(I1TNM(2152))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_print);G1Nlist($list())))))))
                              pyxtnm2153 = XATSDAPP(XATS2PY_sint_print(pyxtnm2151))
                              pyxtnm2154 = pyxtnm2153
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(2154))
                              return pyxtnm2154
                            ## endtimp(sint_print(922))
                            pyxtnm2156 = pyxtnm2155
                            pyxtnm2157 = XATSPFLT(pyxtnm2127[1])
                            pyxtnm2158 = XATSDAPP(pyxtnm2156(pyxtnm2157))
                            pyxtnm2159 = pyxtnm2158
                            XATS000_patck(True)
                            ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2749(line=133,offs=1)--2773(line=133,offs=25)))
                            ## I1VALDCL
                            pyxtnm2166 = None
                            ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2758(line=133,offs=10)--2768(line=133,offs=20))
                            ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                            ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                            ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                            def pyxtnm2164(arg1): ## timp: strn_print(1040)
                              pyxtnm2160 = arg1
                              ## I1CMP:start
                              ## let
                              pyxtnm2163 = None
                              ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                              ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2161);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2161))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                              pyxtnm2162 = XATSDAPP(XATS2PY_strn_print(pyxtnm2160))
                              pyxtnm2163 = pyxtnm2162
                              ## end-of(let)
                              ## I1CMP:return:I1Vtnm(I1TNM(2163))
                              return pyxtnm2163
                            ## endtimp(strn_print(1040))
                            pyxtnm2165 = XATSDAPP(pyxtnm2164(XATSSTRN(")")))
                            pyxtnm2166 = pyxtnm2165
                            XATS000_patck(True)
                            pyxtnm2167 = XATSVOID
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(2167))
                            return pyxtnm2167
                          ## endtimp(g_print(39))
                          pyxtnm2169 = XATSPFLT(pyxtnm2103[1])
                          pyxtnm2170 = XATSDAPP(pyxtnm2168(pyxtnm2169))
                          pyxtnm2171 = pyxtnm2170
                          XATS000_patck(True)
                          ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2749(line=133,offs=1)--2773(line=133,offs=25)))
                          ## I1VALDCL
                          pyxtnm2178 = None
                          ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/tupl000.dats)@(2758(line=133,offs=10)--2768(line=133,offs=20))
                          ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
                          ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
                          ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
                          def pyxtnm2176(arg1): ## timp: strn_print(1040)
                            pyxtnm2172 = arg1
                            ## I1CMP:start
                            ## let
                            pyxtnm2175 = None
                            ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
                            ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2173);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2173))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
                            pyxtnm2174 = XATSDAPP(XATS2PY_strn_print(pyxtnm2172))
                            pyxtnm2175 = pyxtnm2174
                            ## end-of(let)
                            ## I1CMP:return:I1Vtnm(I1TNM(2175))
                            return pyxtnm2175
                          ## endtimp(strn_print(1040))
                          pyxtnm2177 = XATSDAPP(pyxtnm2176(XATSSTRN(")")))
                          pyxtnm2178 = pyxtnm2177
                          XATS000_patck(True)
                          pyxtnm2179 = XATSVOID
                          ## end-of(let)
                          ## I1CMP:return:I1Vtnm(I1TNM(2179))
                          return pyxtnm2179
                        ## endtimp(g_print(39))
                        pyxtnm2181 = pyxtnm2180
                        pyxtnm2182 = XATSDAPP(pyxtnm2181(pyxtnm2084))
                        pyxtnm2183 = pyxtnm2182
                        ## end-of(let)
                        ## I1CMP:return:I1Vtnm(I1TNM(2183))
                        return pyxtnm2183
                      ## endtimp(iforitm$work1(1449))
                      pyxtnm2185 = XATSDAPP(pyxtnm2184(pyxtnm2081, pyxtnm2082))
                      pyxtnm2186 = pyxtnm2185
                      XATS000_patck(True)
                      pyxtnm2187 = XATSBOOL(True)
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(2187))
                      return pyxtnm2187
                    ## endtimp(iforall$test1(1433))
                    pyxtnm2189 = XATSDAPP(pyxtnm2188(pyxtnm2080, pyxtnm2075))
                    pyxtnm2190 = pyxtnm2189
                    XATS000_patck(True)
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6213(line=396,offs=5)--6221(line=396,offs=13))
                    ## I0Etapq(I0Ecst(p2tr_set(2310)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/unsfx00.sats)@(2611(line=127,offs=1)--2619(line=127,offs=9))));$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))
                    ## T1IMPallx(p2tr_set(2310), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/unsfx00.dats)@(246(line=19,offs=1)--305(line=22,offs=27)))
                    ## T1IMPallx(p2tr_set(2310)<$list(T2JAG($list(T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))>;I1Dtmpsub($list(@(a[5909],T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))));I1Dimplmnt0(DIMPLone2(p2tr_set(2310);$list(@(a[5708],T2Pvar(a[5909])))))))
                    def pyxtnm2193(arg1, arg2): ## timp: p2tr_set(2310)
                      pyxtnm2191 = arg1
                      pyxtnm2192 = arg2
                      ## I1CMP:start
                      XATS000_assgn(pyxtnm2191, pyxtnm2192)
                      ## I1CMP:return:I1V000()
                      return XATSVOID
                    ## endtimp(p2tr_set(2310))
                    ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq001_vt.dats)@(6232(line=396,offs=24)--6233(line=396,offs=25))
                    ## I0Etapq(I0Ecst(sint_add$sint(936)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gint000.sats)@(3081(line=142,offs=1)--3094(line=142,offs=14))));$list(T2JAG($list())))
                    ## T1IMPallx(sint_add$sint(936), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2677(line=145,offs=1)--2841(line=157,offs=2)))
                    ## T1IMPallx(sint_add$sint(936)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(sint_add$sint(936);$list()))))
                    def pyxtnm2200(arg1, arg2): ## timp: sint_add$sint(936)
                      pyxtnm2194 = arg1
                      pyxtnm2195 = arg2
                      ## I1CMP:start
                      ## let
                      pyxtnm2199 = None
                      ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/gint000.dats)@(2767(line=153,offs=1)--2839(line=156,offs=39)))
                      ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_sint_add$sint(2619));$list(I1FUNDCL(XATS2PY_sint_add$sint(4891);$list(FJARGdarg($list(I1BNDcons(I1TNM(2196);I0Pvar(i1(4892));$list(@(i1(4892),I1Vtnm(I1TNM(2196))))),I1BNDcons(I1TNM(2197);I0Pvar(i2(4893));$list(@(i2(4893),I1Vtnm(I1TNM(2197))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_sint_add$sint);G1Nlist($list())))))))
                      pyxtnm2198 = XATSDAPP(XATS2PY_sint_add_sint(pyxtnm2194, pyxtnm2195))
                      pyxtnm2199 = pyxtnm2198
                      ## end-of(let)
                      ## I1CMP:return:I1Vtnm(I1TNM(2199))
                      return pyxtnm2199
                    ## endtimp(sint_add$sint(936))
                    pyxtnm2201 = XATSDAPP(pyxtnm2200(pyxtnm2080, XATSINT1(1)))
                    pyxtnm2202 = XATSDAPP(pyxtnm2193(pyxtnm2062, pyxtnm2201))
                    pyxtnm2203 = pyxtnm2190
                    ## end-of(let)
                    ## I1CMP:return:I1Vtnm(I1TNM(2203))
                    return pyxtnm2203
                  ## endtimp(forall$test1(1423))
                  pyxtnm2205 = XATSDAPP(pyxtnm2204(XATSP1CN("list_vt_cons", pyxtnm2074[0+1])))
                  pyxtnm2206 = pyxtnm2205
                  XATS000_patck(True)
                  pyxtnm2208 = None
                  if (pyxtnm2206):
                    pyxtnm2207 = XATSDAPP(loop_1780(XATSP1CN("list_vt_cons", pyxtnm2074[1+1])))
                    pyxtnm2208 = pyxtnm2207
                  else:
                    pyxtnm2208 = XATSBOOL(False)
                  ## end-of(if)
                  pyxtnm2209 = pyxtnm2208
                  ## end-of(let)
                  pyxtnm2210 = pyxtnm2209
                  break ## cls
                ## } // gpt
                ## } // cls
                XATS000_cfail()
              ## } while True // end-of(do-cls)
              ## I1CMP:return:I1Vtnm(I1TNM(2210))
              return pyxtnm2210
            pyxtnm2211 = XATSDAPP(loop_1780(pyxtnm2071))
            pyxtnm2212 = pyxtnm2211
            ## end-of(let)
            ## I1CMP:return:I1Vtnm(I1TNM(2212))
            return pyxtnm2212
          ## endtimp(list_vt_forall1(2063))
          pyxtnm2214 = pyxtnm2213
          pyxtnm2215 = XATSDAPP(pyxtnm2214(pyxtnm2060))
          pyxtnm2216 = pyxtnm2215
          ## end-of(let)
          pyxtnm2217 = pyxtnm2216
          XATS000_patck(True)
          pyxtnm2218 = pyxtnm2217
          ## end-of(let)
          ## I1CMP:return:I1Vtnm(I1TNM(2218))
          return pyxtnm2218
        ## endtimp(gseq_iforall1(1736))
        pyxtnm2220 = XATSDAPP(pyxtnm2219(pyxtnm2054))
        pyxtnm2221 = pyxtnm2220
        XATS000_patck(True)
        pyxtnm2222 = XATSVOID
        ## end-of(let)
        pyxtnm2223 = pyxtnm2222
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(2223))
        return pyxtnm2223
      ## endtimp(gseq_iforitm1(1760))
      pyxtnm2225 = XATSDAPP(pyxtnm2224(pyxtnm2035))
      pyxtnm2226 = pyxtnm2225
      ## end-of(let)
      pyxtnm2227 = pyxtnm2226
      XATS000_patck(True)
      ## I1Dvaldclist(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4752(line=307,offs=1)--4793(line=308,offs=33)))
      ## I1VALDCL
      pyxtnm2236 = None
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4761(line=308,offs=1)--4771(line=308,offs=11))
      ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
      ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
      ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
      def pyxtnm2232(arg1): ## timp: strn_print(1040)
        pyxtnm2228 = arg1
        ## I1CMP:start
        ## let
        pyxtnm2231 = None
        ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
        ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2229);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2229))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
        pyxtnm2230 = XATSDAPP(XATS2PY_strn_print(pyxtnm2228))
        pyxtnm2231 = pyxtnm2230
        ## end-of(let)
        ## I1CMP:return:I1Vtnm(I1TNM(2231))
        return pyxtnm2231
      ## endtimp(strn_print(1040))
      ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gseq000_vt.dats)@(4774(line=308,offs=14)--4782(line=308,offs=22))
      ## I0Etapq(I0Ecst(gseq$end(347)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gseq000.sats)@(2432(line=134,offs=1)--2440(line=134,offs=9))));$list(T2JAG($list(T2Pvar(xs[7905]))),T2JAG($list(T2Pvar(x0[7906])))))
      ## T1IMPallx(gseq$end(347), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/list000_vt.dats)@(2674(line=137,offs=1)--2727(line=140,offs=26)))
      ## T1IMPallx(gseq$end(347)<$list(T2JAG($list(T2Papps(T2Pcst(list_vt_i0_vx);$list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))),T2Pnone0())))),T2JAG($list(T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0())))))))))))>;I1Dtmpsub($list(@(x0[8495],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))),@(x0[8495],T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Ptrcd(TRCDflt0;-1;$list(S2LAB(LABint(0);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))),S2LAB(LABint(1);T2Papps(T2Pcst(gint_type);$list(T2Ptext(xats_sint_t;$list()),T2Pnone0()))))))))));I1Dimplmnt0(DIMPLone2(gseq$end(347);$list(@(xs[1069],T2Papps(T2Pcst(list_vt);$list(T2Pvar(x0[8495])))),@(x0[1070],T2Pvar(x0[8495])))))))
      def pyxtnm2233(): ## timp: gseq$end(347)
        ## I1CMP:start
        ## I1CMP:return:I1Vstr(...)
        return XATSSTRN(")")
      ## endtimp(gseq$end(347))
      pyxtnm2234 = XATSDAPP(pyxtnm2233())
      pyxtnm2235 = XATSDAPP(pyxtnm2232(pyxtnm2234))
      pyxtnm2236 = pyxtnm2235
      XATS000_patck(True)
      pyxtnm2237 = XATSVOID
      ## end-of(let)
      ## I1CMP:return:I1Vtnm(I1TNM(2237))
      return pyxtnm2237
    ## endtimp(gseq_print1(1687))
    pyxtnm2239 = XATSDAPP(pyxtnm2238(pyxtnm2034))
    ## I1CMP:return:I1Vtnm(I1TNM(2239))
    return pyxtnm2239
  ## endtimp(g_print1(1412))
  pyxtnm2241 = XATSDAPP(pyxtnm2240(pyxtnm2021))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5636(line=282,offs=21)--5644(line=282,offs=29))
  ## I0Etapq(I0Ecst(g_print1(1412)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gbas000_vt.sats)@(2117(line=109,offs=1)--2125(line=109,offs=9))));$list(T2JAG($list(T2Pvar(x2[8383])))))
  ## T1IMPallx(g_print1(1412), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1635(line=59,offs=1)--1680(line=61,offs=27)))
  ## T1IMPallx(g_print1(1412)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list(@(x0[8803],T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0()))));I1Dimplmnt0(DIMPLone2(g_print1(1412);$list(@(x0[3750],T2Pvar(x0[8803])))))))
  pyxtnm2248 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gxyz000_vt.dats)@(1669(line=61,offs=16)--1676(line=61,offs=23))
  ## I0Etapq(I0Ecst(g_print(39)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/gbas000.sats)@(2824(line=171,offs=1)--2831(line=171,offs=8))));$list(T2JAG($list(T2Pvar(x0[8803])))))
  ## T1IMPallx(g_print(39), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2143(line=94,offs=1)--2180(line=95,offs=29)))
  ## T1IMPallx(g_print(39)<$list(T2JAG($list(T2Papps(T2Pcst(string_i0_tx);$list(T2Pnone0())))))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(g_print(39);$list(@(x0[447],T2Pcst(strn)))))))
  pyxtnm2247 = None
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/strn000.dats)@(2168(line=95,offs=17)--2178(line=95,offs=27))
  ## I0Etapq(I0Ecst(strn_print(1040)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/strn000.sats)@(2592(line=122,offs=1)--2602(line=122,offs=11))));$list(T2JAG($list())))
  ## T1IMPallx(strn_print(1040), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1819(line=74,offs=1)--1959(line=85,offs=2)))
  ## T1IMPallx(strn_print(1040)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(strn_print(1040);$list()))))
  def pyxtnm2246(arg1): ## timp: strn_print(1040)
    pyxtnm2242 = arg1
    ## I1CMP:start
    ## let
    pyxtnm2245 = None
    ## I1Dextern(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/CATS/PY/strn000.dats)@(1899(line=82,offs=1)--1957(line=84,offs=47)))
    ## I1Dfundclst(T_FUN(FNKfn1);$list();$list(XATS2PY_strn_print(2648));$list(I1FUNDCL(XATS2PY_strn_print(5011);$list(FJARGdarg($list(I1BNDcons(I1TNM(2243);I0Pvar(cs(5012));$list(@(cs(5012),I1Vtnm(I1TNM(2243))))))));TEQI1CMPsome(T_EQ0();I1CMPcons($list();I1Vextnam(T_DLR_EXTNAM();I1Vvar(XATS2PY_strn_print);G1Nlist($list())))))))
    pyxtnm2244 = XATSDAPP(XATS2PY_strn_print(pyxtnm2242))
    pyxtnm2245 = pyxtnm2244
    ## end-of(let)
    ## I1CMP:return:I1Vtnm(I1TNM(2245))
    return pyxtnm2245
  ## endtimp(strn_print(1040))
  pyxtnm2247 = pyxtnm2246
  pyxtnm2248 = pyxtnm2247
  pyxtnm2249 = XATSDAPP(pyxtnm2248(pyxtnm2022))
  ## LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5656(line=283,offs=3)--5669(line=283,offs=16))
  ## I0Etapq(I0Ecst(gs_print1$end(1973)(LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/SATS/VT/gsyn000_vt.sats)@(1564(line=55,offs=1)--1577(line=55,offs=14))));$list(T2JAG($list())))
  ## T1IMPallx(gs_print1$end(1973), LCSRCsome1(/home/hwxi/Research/ATS-Xanadu/prelude/DATS/VT/gsyn000_vt.dats)@(5133(line=245,offs=1)--5172(line=247,offs=21)))
  ## T1IMPallx(gs_print1$end(1973)<$list(T2JAG($list()))>;I1Dtmpsub($list();I1Dimplmnt0(DIMPLone2(gs_print1$end(1973);$list()))))
  def pyxtnm2251(): ## timp: gs_print1$end(1973)
    ## I1CMP:start
    pyxtnm2250 = XATSTUP0([])
    ## I1CMP:return:I1Vtnm(I1TNM(2250))
    return pyxtnm2250
  ## endtimp(gs_print1$end(1973))
  pyxtnm2252 = XATSDAPP(pyxtnm2251())
  ## I1CMP:return:I1Vtnm(I1TNM(2252))
  return pyxtnm2252
## endtimp(gs_print1_a3(1988))
pyxtnm2254 = XATSDAPP(pyxtnm2253(XATSSTRN("listize(xztup) = "), pyxtnm2019, XATSSTRN("\n")))
pyxtnm2255 = pyxtnm2254
XATS000_patck(True)
## LCSRCsome1(test07_gseq000.dats)@(1283(line=69,offs=1)--1283(line=69,offs=1))
## I1Dnone1(I0Dnone1(LCSRCsome1(test07_gseq000.dats)@(1283(line=69,offs=1)--1283(line=69,offs=1));D3Cnone0()))
