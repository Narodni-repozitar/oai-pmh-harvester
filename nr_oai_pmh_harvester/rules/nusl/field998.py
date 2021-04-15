from oarepo_oai_pmh_harvester.decorators import rule
from oarepo_oai_pmh_harvester.transformer import OAITransformer
from oarepo_taxonomies.utils import get_taxonomy_json


@rule("nusl", "marcxml", "/998__/a", phase="pre")
def call_provider(el, **kwargs):
    return provider(el, **kwargs)  # pragma: no cover


def provider(el, **kwargs):
    slug = provider_mapping().get(el)
    if not slug:  # pragma: no cover
        return OAITransformer.PROCESSED
    return {
        "_administration": {
            "state": "new",
            "primaryCommunity": slug,
            "communities": []
        },
        "provider": get_taxonomy_json(code="institutions",
                                      slug=slug).paginated_data
    }


def provider_mapping():
    return {
        "agritec": "agritec",
        "agrotest_fyto": "agrotest_fyto",
        "akademie_muzickych_umeni_v_praze": "amu",
        "akademie_vytvarnych_umeni": "avu",
        "archeologicky_ustav_brno": "arub_cas",
        "archeologicky_ustav_praha": "arup_cas",
        "archip": "archip",
        "archiv_ing_arch_jana_moucky": "j_moucka",
        "archiv_doc_jiri_soucek": "j_soucek",
        "arnika": "arnika",
        "astronomicky_ustav": "asu_cas",
        "biofyzikalni_ustav": "bfu_cas",
        "biologicke_centrum": "bc_cas",
        "biotechnologicky_ustav": "ibt_cas",
        "botanicky_ustav": "ibot_cas",
        "cenia": "cenia",
        "centrum_dopravniho_vyzkumu": "cdv",
        "centrum_pro_dopravu_a_energetiku": "cde",
        "centrum_pro_regionalni_rozvoj": "crr",
        "centrum_pro_studium_vysokeho_skolstvi": "csvs",
        "centrum_pro_vyzkum_verejneho_mineni": "cvvm",
        "centrum_vyzkumu_globalni_zmeny": "cvgz_cas",
        "ceska_asociace_ergoterapeutu": "cae",
        "ceska_asociace_paraplegiku": "czepa",
        "ceska_narodni_banka": "cnb",
        "ceska_spolecnost_ornitologicka": "birdlife",
        "ceska_zemedelska_univerzita": "czu",
        "cesky_statisticky_urad": "csu",
        "chmelarsky_institut": "chizatec",
        "clovek_v_tisni": "clovek_v_tisni",
        "crdm": "crdm",
        "cvut": "cvut",
        "ekodomov": "ekodomov",
        "entomologicky_ustav": "entu_cas",
        "etnologicky_ustav": "eu_cas",
        "evropske_hodnoty": "evropske_hodnoty",
        "fairtrade_cz_sk": "fairtrade_cz_sk",
        "filosoficky_ustav": "flu_cas",
        "fyzikalni_ustav": "fzu_cas",
        "fyziologicky_ustav": "fgu_cas",
        "galerie_vytvarneho_umeni_v_ostrave": "gvuo",
        "gender_studies": "gender_studies",
        "geofyzikalni_ustav": "ig_cas",
        "geologicky_ustav": "gli_cas",
        "gle": "gle",
        "hestia": "hestia",
        "historicky_ustav": "hiu_cas",
        "hydrobiologicky_ustav": "hbu_cas",
        "institut_umeni": "idu",
        "iuridicum_remedium": "iure",
        "jihoceska_univerzita_v_ceskych_budejovicich": "jcu",
        "jihomoravske_muzeum_ve_znojme": "jmm_znojmo",
        "knihovna_av_cr": "knav",
        "masarykova_univerzita": "muni",
        "masarykuv_ustav_a_archiv": "mua_cas",
        "matematicky_ustav": "math_cas",
        "mendelova_univerzita_v_brne": "mendelu",
        "mikrobiologicky_ustav": "mbu_cas",
        "ministerstvo_obrany": "mo_cr",
        "ministerstvo_spravedlnosti": "ms_cr",
        "ministerstvo_zivotniho_prostredi": "mzp_cr",
        "moravska_galerie": "moravska_gal",
        "moravska_zemska_knihovna": "mzk",
        "muzeum_brnenska": "muz_brnenska",
        "muzeum_vychodnich_cech": "muzeumhk",
        "nacr": "nacr",
        "nadace_promeny": "nadace_promeny",
        "narodni_informacni_a_poradenske_stredisko_pro_kulturu": "nipos",
        "narodni_knihovna": "nk_cr",
        "narodni_lekarska_knihovna": "nlk",
        "narodni_muzeum": "nm",
        "narodni_muzeum_v_prirode": "nmvp",
        "narodni_pamatkovy_ustav": "npu",
        "narodni_technicka_knihovna": "ntk",
        "narodni_technicke_muzeum": "ntm",
        "narodni_zemedelske_muzeum": "nzm",
        "narodohospodarsky_ustav": "nhu_cas",
        "nulk": "nulk",
        "nuv": "nuv",
        "orientalni_ustav": "orient_cas",
        "oseva": "oseva",
        "ostravska_univerzita": "osu",
        "pamatnik_narodniho_pisemnictvi": "pamatnik_np",
        "parazitologicky_ustav": "paru_cas",
        "parlamentni_institut": "pi_psp",
        "prague_college": "prague_college",
        "psychologicky_ustav": "psu_cas",
        "sdruzeni_pro_integraci_a_migraci": "simi",
        "severoceske_muzeum_v_liberci": "muzeumlb",
        "siriri": "siriri",
        "slezske_zemske_muzeum": "szm",
        "slovansky_ustav": "slu_cas",
        "sociologicky_ustav": "soc_cas",
        "surao": "surao",
        "szpi": "szpi",
        "technologicke_centrum": "tc_cas",
        "ujep": "ujep",
        "umeleckoprumyslove_museum": "umprum_museum",
        "univerzita_karlova_v_praze": "uk",
        "upce": "upce",
        "urad_prumysloveho_vlastnictvi": "upv",
        "ustav_analyticke_chemie": "uiach_cas",
        "ustav_anorganicke_chemie": "uach_cas",
        "ustav_archeologicke_pamatkove_pece_severozapadnich_cech": "uappmost",
        "ustav_biologie_obratlovcu": "ivb_cas",
        "ustav_chemickych_procesu": "icpf_cas",
        "ustav_dejin_umeni": "udu_cas",
        "ustav_experimentalni_botaniky": "ueb_cas",
        "ustav_experimentalni_mediciny": "iem_cas",
        "ustav_fotoniky_a_elektroniky": "ufe_cas",
        "ustav_fyzikalni_chemie_j_heyrovskeho": "jh_inst_cas",
        "ustav_fyziky_atmosfery": "ufa_cas",
        "ustav_fyziky_materialu": "ipm_cas",
        "ustav_fyziky_plazmatu": "ipp_cas",
        "ustav_geoniky": "ugn_cas",
        "ustav_informatiky": "ics_cas",
        "ustav_jaderne_fyziky": "ujf_cas",
        "ustav_makromolekularni_chemie": "imc_cas",
        "ustav_molekularni_biologie_rostlin": "umbr_cas",
        "ustav_molekularni_genetiky": "img_cas",
        "ustav_organicke_chemie_a_biochemie": "uochb_cas",
        "ustav_pristrojove_techniky": "upt_cas",
        "ustav_pro_ceskou_literaturu": "ucl_cas",
        "ustav_pro_elektrotechniku": "ue_cas",
        "ustav_pro_hydrodynamiku": "ih_cas",
        "ustav_pro_jazyk_cesky": "ujc_cas",
        "ustav_pro_soudobe_dejiny": "usd_cas",
        "ustav_pro_studium_totalitnich_rezimu": "ustrcz",
        "ustav_pudni_biologie": "upb_cas",
        "ustav_statu_a_prava": "ilaw_cas",
        "ustav_struktury_a_mechaniky_hornin": "irsm_cas",
        "ustav_teoreticke_a_aplikovane_mechaniky": "itam_cas",
        "ustav_teorie_informace_a_automatizace": "utia_cas",
        "ustav_termomechaniky": "it_cas",
        "ustav_zivocisne_fyziologie_a_genetiky": "iapg_cas",
        "vscht": "vscht",
        "vugtk": "vugtk",
        "vutbr": "vutbr",
        "vuv_tgm": "vuv_tgm",
        "vvud": "vvud",
        "vysoka_skola_ekonomicka_v_praze": "vse",
        "vysoka_skola_evropskych_a_regionalnich_studii": "vsers",
        "vysoka_skola_financni_a_spravni": "vsfs",
        "vysoka_skola_manazerske_informatiky_a_ekonomiky": "vsmie",
        "vyzkumny_ustav_bezpecnosti_prace": "vubp",
        "vyzkumny_ustav_lesniho_hospodarstvi_a_myslivosti": "vulhm",
        "vyzkumny_ustav_potravinarsky": "vupp",
        "vyzkumny_ustav_prace_a_socialnich_veci": "vupsv",
        "vyzkumny_ustav_rostlinne_vyroby": "vurv",
        "vyzkumny_ustav_silva_taroucy": "vukoz",
        "woodexpert": "woodexpert",
        "zapadoceska_univerzita": "zcu",
        "zapadoceske_muzeum_v_plzni": "zcm"
    }
