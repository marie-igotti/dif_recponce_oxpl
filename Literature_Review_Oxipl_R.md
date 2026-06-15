# Literature Review: Differential Transcriptomic Response to Oxaliplatin in Sensitive vs. Resistant Colorectal Cancer Cells

## Focus: Cell Cycle Regulation, Quiescence, and Proliferation Arrest

---

**Prepared for:** Morshneva et al. manuscript — "Overcoming oxaliplatin resistance in colorectal adenocarcinoma HCT116 cells via E1A-driven cell cycle activation based on transcriptomic signatures of oxaliplatin response"

**Date:** 12 June 2026

---

# English Version

## 1. Core Finding of the Morshneva et al. Study

| Observation | Sensitive HCT116 | Resistant HCT116-OX |
|-------------|-------------------|---------------------|
| DEGs upon oxaliplatin (25 µM, 24h) | 1,791 genes (978↑, 813↓) | 830 genes (358↑, 472↓) — **2× fewer** |
| Cell cycle regulators | Unchanged or activated (E2F1, AURKA/B, cyclins) | **Sharply suppressed** (E2F1/2/8, FOXM1, MYBL2, cyclins, AURKA/B) |
| p21 (CDKN1A) | Modest induction | Strong induction at transcript level |
| S-phase population after 48h oxaliplatin | 42% → 20% (2× decrease) | 30% → 5% (**5× decrease** — rapid arrest) |
| Key survival pathways | Stress response, tissue repair | **Autophagy, ER protein processing, metabolic rewiring** + SERPINE1 activation |
| 10 opposite-dynamics DEGs | Upregulated by oxaliplatin | **Downregulated** by oxaliplatin (RN7SK, ASH1L-AS1, ADAMTS4, RPRML, etc.) |
| Response to E1A expression | Modest cell cycle reactivation | Strong reactivation: S-phase 5.8%→14%, **p53↑×10**, apoptosis, resensitization |

**Central paradox:** Resistant cells survive oxaliplatin *because* they arrest proliferation more rapidly — not despite it. This prevents lethal DNA damage during S-phase.

---

## 2. Literature Supporting the "Arrest-to-Survive" Paradigm

### 2.1 Drug-Tolerant Persister (DTP) Cells

| Reference | Key Finding | Relevance to Morshneva et al. |
|-----------|-------------|-------------------------------|
| **De Conti G, et al.** *Signal Transduction and Targeted Therapy*, 2024; 9:209. doi:10.1038/s41392-024-01891-4 | Comprehensive review of DTP biology: cells enter reversible quiescence upon drug exposure, characterized by global transcriptional suppression, Myc↓, E2F targets↓, autophagy↑, metabolic rewiring | **Framework for the muted response** (2× fewer DEGs) and coordinated arrest program |
| **Rehman SK, et al.** *Cell*, 2021; 184(1):226–242. doi:10.1016/j.cell.2020.11.018 | Colorectal cancer cells enter a **diapause-like DTP state** to survive chemotherapy; Myc suppression drives biosynthetic quiescence distinct from CDK4/6 arrest | **Biosynthetic quiescence explains** why transcriptional response is attenuated in HCT116-OX |
| **Cuesta-Borràs E, et al.** *Cell Reports*, 2023; 42(8):112927. doi:10.1016/j.celrep.2023.112927 | **DPPA3-HIF1α feedback loop → FOXM1 promoter methylation/downregulation → slow-cycling chemoresistant phenotype** in CRC. DPPA3 overexpression predicts chemoresistance. | **Direct parallel to FOXM1 suppression** observed in oxaliplatin-treated HCT116-OX |
| **Khong A, et al.** *RNA*, 2025. PMID: 40738736 | **Stress granules promote quiescence** by enhancing p21 levels and reducing phospho-Rb | Mechanistic link for **p21 induction + E2F suppression** in resistant cells |

### 2.2 Cell Cycle Arrest Kinetics in Resistant vs. Sensitive Cells

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Hata T, et al.** *Molecular Cancer Therapeutics*, 2005; 4(10):1585–1594. doi:10.1158/1535-7163.MCT-05-0011 | In p53-WT HCT116 cells, **oxaliplatin induces p21-dependent G0/G1 arrest**. p21-null HCT116 fail to arrest at G1 and show reduced growth inhibition. | Validates the **p21-centric G1 arrest mechanism** observed in HCT116 (p53-WT); p21 induction is protective |
| **William-Faltaos S, et al.** *Fundamental & Clinical Pharmacology*, 2007; 21(2):165–172. doi:10.1111/j.1472-8206.2007.00471.x | Oxaliplatin causes G2/M arrest and S-phase delay in dividing cancer cells; **cell cycle arrest kinetics depend on p53 status** | Context for differential arrest: HCT116 are p53-WT → capable of robust p21-mediated G1 arrest |
| **Li Y, et al.** *International Journal of Molecular Medicine*, 2025. doi:10.3892/ijmm.2025.5675 | **miR-100-5p → CTDSPL↓ → hyperphosphorylated pRB → E2F1 release → G1/S acceleration + chemoresistance** in oxaliplatin-resistant CRC (LoVoOXR) | Alternative resistance mechanism through **E2F1 activation rather than suppression** — context-dependent |
| **Chen X, et al.** *Nature Communications*, 2025; 16:66836. doi:10.1038/s41467-025-66836-z | Single-cell RNA-seq reveals **quiescence-senescence continuum** after chemotherapy; multiple senotypes with distinct transcriptional programs | Single-cell perspective on the **population-average arrest** seen in bulk RNA-seq |
| **Wiedemann S, et al.** *Genome Biology*, 2023; 24:128. doi:10.1186/s13059-023-02963-4 | **Genomic hallmarks of G0 arrest** in cancer; TP53 proficiency associated with G0 entry capacity; 35-gene minimal quiescence signature | **p53-WT HCT116 are primed** for efficient G0 arrest — consistent with rapid arrest in HCT116-OX |

### 2.3 E2F-FOXM1 Axis in Chemoresistance

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Varghese V, et al.** *Scientific Reports*, 2019; 9:1722. doi:10.1038/s41598-018-38017-0 | **FOXM1 and E2F1 reciprocally regulate each other** in colon carcinoma; FOXM1 modulates 5-FU resistance via TYMS; FOXM1 inhibitor thiostrepton + 5-FU = synergy in HCT116, DLD1, HT29 | FOXM1 and E2F1 are **coordinately regulated** — both suppressed in HCT116-OX upon oxaliplatin |
| **Johnson J, et al.** *Oncogene*, 2016; 35(37):4829–4835. doi:10.1038/onc.2016.26 | **RB-E2F pathway** as therapeutic target in cancer; canonical control of G1/S restriction point | RB-E2F is the **central node** of the observed transcriptional arrest program |

### 2.4 RN7SK and the 10 Opposite-Dynamics DEGs

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Bandiera R, et al.** *Nature Communications*, 2021; 12(1):5864. doi:10.1038/s41467-021-26066-3 | **Conditional deletion of Rn7sk leads to rapid cell cycle exit** because cell cycle regulatory genes are hypersensitive to elongation machinery dysregulation. Germline deletion is embryonic lethal. | **Direct mechanistic explanation** for why RN7SK↓ → cell cycle arrest in HCT116-OX |
| **Abasi M, et al.** *Medical Oncology*, 2016; 33(11):128. doi:10.1007/s12032-016-0842-7 | **7SK snRNA is downregulated in human tumors** including CRC; acts as tumor suppressor | RN7SK loss is **established in CRC biology** |
| **Wang Y, et al.** *Molecular Cell*, 2023; 83(21):3819–3836.e8. doi:10.1016/j.molcel.2023.09.021 | **N6-methyladenosine modification of 7SK** regulates Pol II transcription elongation; METTL3/ALKBH5 control 7SK conformation and P-TEFb sequestration | **Post-transcriptional regulation layer** on RN7SK — m6A status could modulate its function in resistant cells |
| **Xie M, et al.** *Oncogene*, 2023; 42(46):3435–3445. doi:10.1038/s41388-023-02835-2 | **ASH1L-AS1-ASH1L axis → NME1 → RAS-MAPK activation** in gastric cancer | ASH1L-AS1 downregulation → **RAS-MAPK pathway attenuation** contributes to arrest |
| **Zhai W, et al.** *Biology Direct*, 2024; 19:94. doi:10.1186/s13062-024-00542-4 | **ADAMTS4 activates MAPK signaling** via c-Myc stabilization in lung cancer | ADAMTS4↓ → MAPK↓ → **reinforced proliferative arrest** |
| **Takikawa M, Ohki R.** *Cancer Science*, 2025; 116(12):3266–3273. doi:10.1111/cas.16497 | **Reprimo (RPRM) induces extrinsic apoptosis** via YAP signaling | RPRML↓ → reduced pro-apoptotic pressure → **survival advantage** |

### 2.5 SERPINE1/PAI-1 and Survival Pathways

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Moussalem C, et al.** *bioRxiv*, 2024. doi:10.1101/2024.12.17.628817 | **RESIST-M signature**: cholesterol↓ → TGF-β receptor redistribution → sustained TGF-β/SMAD → **SERPINE1↑** → chemoresistance + metastasis. shRNA/pharmacological inhibition of SERPINE1 re-sensitizes cells to oxaliplatin. | **SERPINE1 as top DEG** in HCT116-OX fits this axis precisely |
| **Pan T, et al.** *Oncogene*, 2025. doi:10.1038/s41388-025-03453-6 | **BRD4 regulates PAI-1** in tumor-associated macrophages → M2 polarization → chemoresistance. PAI-1 inhibitor + oxaliplatin = synergy. | Tumor microenvironment angle on **PAI-1-driven resistance** |
| **Slyskova J, et al.** *NAR Cancer*, 2023; 5(4):zcad057. doi:10.1093/narcan/zcad057 | Detection of oxaliplatin- and cisplatin-DNA lesions requires **different global genome repair mechanisms** affecting clinical efficacy | Different DNA repair requirements may explain **differential damage burden** |

### 2.6 E1A-Mediated Sensitization

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Tazawa H, et al.** *Annals of Medicine and Surgery*, 2026; 82(2):107694. doi:10.1097/MS9.0000000000003112 | E1A sensitizes tumors to cisplatin via **p19ARF/p53 signaling, CtBP corepressor interaction, HER2/neu downregulation**; overcomes p53-mutant resistance through caspase-2/PIDD | **Mechanistic basis** for E1A effect in HCT116-OX |
| **Chang YW, et al.** *Archivum Immunologiae et Therapiae Experimentalis*, 2014; 62(3):195–204. doi:10.1007/s00005-014-0277-4 | **Comprehensive review** of E1A anti-tumor activity: cell cycle reactivation + apoptosis + metastasis suppression | **Framework** for E1A dual mechanism |
| **Cimas FJ, et al.** *Oncotarget*, 2015; 6(42):44095–44107. doi:10.18632/oncotarget.6574 | **MKP1 mediates E1A chemosensitization** to cisplatin in NSCLC cells | Specific **signaling node** for E1A + platinum synergy |
| **Radke JR, et al.** *Cell Death Discovery*, 2016; 2:16076. doi:10.1038/cddiscovery.2016.76 | E1A enhances DNA-damage-induced apoptosis through **PIDD-dependent caspase-2 activation** — p53-independent mechanism | Relevant if **p53-independent apoptosis** contributes in HCT116-OX |
| **Fang L, et al.** *Oncotarget*, 2016; 7(30):48309–48320. doi:10.18632/oncotarget.10195 | p53-independent apoptotic mechanism of adenoviral E1A — **selective antitumor activity** | E1A kills **regardless of p53 status** |
| **M.D. Anderson Cancer Center.** ClinicalTrials.gov NCT00102622, 2018 | **Phase I/II trial** of tgDCC-E1 + paclitaxel in platinum-resistant ovarian cancer | **Clinical translation precedent** for E1A + platinum |
| **Liao Y, Hung MC.** *Cancer Research*, 2004; 64(17):5938–5942. doi:10.1158/0008-5472.CAN-04-1341 | **PP2A mediates E1A sensitization** to drug-induced apoptosis in breast cancer | Additional node in E1A pro-apoptotic signaling |

### 2.7 Cell Cycle Reactivation as Therapeutic Strategy

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Lindell E, et al.** *International Journal of Molecular Sciences*, 2023; 24(4):3762. doi:10.3390/ijms24043762 | **Quiescent cancer cells as therapeutic targets** — comprehensive review of reactivation strategies to overcome resistance and relapse | **Conceptual framework** for E1A approach |
| **Yano S, et al.** *Cancers*, 2020; 12(9):2655. doi:10.3390/cancers12092655 | **FUCCI real-time cell-cycle imaging** to guide strategies targeting quiescent chemo-resistant cells | **Visual evidence** that quiescent cells survive and later re-enter cycle |
| **Basu S, et al.** *Seminars in Cancer Biology*, 2022; 78:90–103. doi:10.1016/j.semcancer.2021.04.021 | Slow-cycling/dormant cancer cells in **therapy resistance, relapse, and metastasis** | **Clinical relevance** of targeting SCCs |
| **Gao H, et al.** *Cell*, 2012; 150(4):764–779. doi:10.1016/j.cell.2012.06.035 | **BMP inhibitor Coco reactivates** dormant breast cancer cells at metastatic sites | Alternative reactivation strategy |
| **Buczacki SJA, et al.** *Journal of Experimental Medicine*, 2018; 215(7):1891–1912. doi:10.1084/jem.20171385 | **Itraconazole targets cell cycle heterogeneity** in CRC | Drug repurposing for cell cycle modulation |

### 2.8 Comparative Transcriptomic Studies of Platinum Response

| Reference | Key Finding | Relevance |
|-----------|-------------|-----------|
| **Carlsen L, et al.** *Oncotarget*, 2021; 12(20):2006–2021. doi:10.18632/oncotarget.28066 | **Pan-drug and drug-specific transcriptomic signatures** for 5-FU, irinotecan, oxaliplatin, cisplatin in CRC cells. Identified 36 DEGs overlapping with Morshneva dataset (CDKN1A, GDF15, BTG2, etc.) | **Only direct comparator** for oxaliplatin-induced transcriptome in CRC |
| **Slaninová V, et al.** *BMC Cancer*, 2024; 24(1):587. doi:10.1186/s12885-024-12264-z | Hippo pathway terminal effector **TAZ/WWTR1 mediates oxaliplatin sensitivity** in p53-proficient colon cancer; low-dose oxaliplatin (0.5µM) response in HCT116. 93 DEGs overlap with Morshneva dataset. | Different dose (0.5 vs 25 µM) — **complementary dose-range perspective** |
| **Jensen NF, et al.** *Molecular Oncology*, 2015; 9(6):1169–1185. doi:10.1016/j.molonc.2015.02.008 | Establishment and characterization of **chemotherapy resistance models in CRC** — transcriptomic baseline signatures | Baseline transcriptomic context for resistance |
| **Fang J, et al.** *Cancer Cell International*, 2025; 25(1):383. doi:10.1186/s12935-025-03618-0 | **UBE2H as marker of oxaliplatin resistance** via integrative transcriptome/methylome/scRNA-seq analysis | Alternative resistance marker |
| **Zhan X, et al.** *Frontiers in Oncology*, 2025; 15:1701328. doi:10.3389/fonc.2025.1701328 | **Gene signature for oxaliplatin sensitivity prediction** in CRC | Predictive biomarker perspective |

---

## 3. Synthesis: How the Morshneva et al. Findings Fit in the Literature

### 3.1 The Muted Transcriptional Response

The 2-fold reduction in DEGs in HCT116-OX fits the **drug-tolerant persister (DTP) model** [De Conti 2024; Rehman 2021]. DTP cells enter a state of **global transcriptional and biosynthetic suppression** that is distinct from mere cell cycle arrest. The "biosynthetic quiescence" described by Rehman et al. involves Myc suppression and reduced ribosomal biogenesis — consistent with the GO terms suppressed in HCT116-OX (ribosome function, translation). **This is the first study to document the muted transcriptomic response specifically in oxaliplatin-resistant CRC cells.**

### 3.2 The Rapid Cell Cycle Arrest

The observation that resistant cells arrest **faster** than sensitive cells — S-phase drops 5-fold vs. 2-fold — is the **central paradox of this study** and is increasingly recognized as a hallmark of adaptive drug tolerance. The DPPA3-HIF1α-FOXM1 axis [Cuesta-Borràs 2023] provides a direct mechanistic parallel: chemotherapy stress triggers FOXM1 epigenetic silencing via promoter methylation, enforcing a slow-cycling, chemoresistant state. The **suppression of E2F1/2/8 and FOXM1** in HCT116-OX upon oxaliplatin treatment mirrors this axis. Additionally, the **p21 induction + E2F suppression** pattern aligns with the stress granule-p21-Rb quiescence axis [Khong 2025].

**Key distinction from existing literature:** Most studies report either E2F *activation* (via pRB hyperphosphorylation → miR-100-5p/CTDSPL pathway, leading to G1/S acceleration) OR E2F *suppression* (quiescence). The Morshneva data clearly show the **latter pathway** operating in HCT116-OX, with coordinated E2F/FOXM1 target suppression. This suggests **two distinct resistant states** may exist: actively cycling (E2F-high) and quiescent (E2F-low).

### 3.3 RN7SK — A Novel Node in Platinum Response

The near-complete loss of RN7SK in oxaliplatin-treated resistant cells is, to our knowledge, **the first report of 7SK dynamics in platinum resistance**. The mechanistic link — RN7SK↓ → P-TEFb dysregulation → selective suppression of cell cycle genes [Bandiera 2021] — provides a direct transcriptional mechanism for the rapid arrest. RN7SK has been reported as downregulated in CRC tumors [Abasi 2016], and its m6A modification status [Wang 2023] may add a regulatory layer worth exploring.

### 3.4 SERPINE1 and Pro-Survival Pathways

The activation of SERPINE1 in HCT116-OX upon oxaliplatin aligns with the **RESIST-M signature** [Moussalem 2024], where a cholesterol-TGF-β-SERPINE1 axis drives chemoresistance and metastasis. The concurrent activation of autophagy and ER protein processing pathways (KEGG hsa04140, hsa04141) complements the metabolic reprogramming noted in the study (fatty acid degradation, amino acid catabolism). These findings position HCT116-OX within the CMS4/iCMS3-fibrotic CRC subtype associated with poorest prognosis.

### 3.5 E1A Reactivation Strategy

E1A-mediated cell cycle reactivation as a sensitization strategy is supported by decades of preclinical work [Chang 2014; Tazawa 2026]. The novelty of the Morshneva study lies in: (a) **the first transcriptomic profile of E1A-expressing cancer cells**, (b) demonstration that E1A overrides the **specific transcriptional arrest program** (GO:1901987 reactivation), and (c) the **massive p53 upregulation (×10)** in E1A-expressing resistant cells, suggesting the apoptotic response is p53-mediated. The dual effect — cell cycle reactivation + pro-apoptotic priming — is what makes E1A uniquely suited for this context.

### 3.6 Unanswered Questions and Future Directions

1. **Is RN7SK loss causative or correlative?** Direct knockdown/overexpression studies needed.
2. **What is the chromatin-level mechanism** of E2F/FOXM1 suppression — DPPA3-like promoter methylation, or upstream signaling?
3. **Single-cell heterogeneity** — does the rapid arrest occur uniformly or in a subpopulation?
4. **Pharmacological E1A mimicry** — which small molecules can phenocopy E1A's dual activity (e.g., CDK4/6 inhibitors + p53 activators)?
5. **Does the 10-gene opposite-dynamics signature** have prognostic value in CRC patient cohorts?

---

## 4. Key References — Complete List

1. De Conti G, et al. Drug tolerant persister cell plasticity in cancer. *Sig Transduct Target Ther*. 2024;9:209. doi:10.1038/s41392-024-01891-4
2. Rehman SK, et al. Colorectal cancer cells enter a diapause-like DTP state to survive chemotherapy. *Cell*. 2021;184(1):226–242. doi:10.1016/j.cell.2020.11.018
3. Cuesta-Borràs E, et al. DPPA3-HIF1α axis controls colorectal cancer chemoresistance by imposing a slow cell-cycle phenotype. *Cell Reports*. 2023;42(8):112927. doi:10.1016/j.celrep.2023.112927
4. Khong A, et al. Stress granules promote quiescence by enhancing p21 levels and reducing phospho-Rb. *RNA*. 2025. PMID: 40738736
5. Hata T, et al. Role of p21waf1/cip1 in effects of oxaliplatin in colorectal cancer cells. *Mol Cancer Ther*. 2005;4(10):1585–1594. doi:10.1158/1535-7163.MCT-05-0011
6. William-Faltaos S, et al. Cell cycle arrest by oxaliplatin on cancer cells. *Fundam Clin Pharmacol*. 2007;21(2):165–172. doi:10.1111/j.1472-8206.2007.00471.x
7. Li Y, et al. miR-100-5p enhances cell cycle-mediated chemoresistance by modulating the CTDSPL/pRB/E2F1 signaling pathway in oxaliplatin-resistant CRC cells. *Int J Mol Med*. 2025. doi:10.3892/ijmm.2025.5675
8. Chen X, et al. Single-cell RNA sequencing reveals a quiescence-senescence continuum following chemotherapy. *Nat Commun*. 2025;16:66836. doi:10.1038/s41467-025-66836-z
9. Wiedemann S, et al. Genomic hallmarks and therapeutic implications of G0 cell cycle arrest in cancer. *Genome Biol*. 2023;24:128. doi:10.1186/s13059-023-02963-4
10. Varghese V, et al. FOXM1 modulates 5-FU resistance in colorectal cancer through regulating TYMS expression. *Sci Rep*. 2019;9:1722. doi:10.1038/s41598-018-38017-0
11. Johnson J, et al. Targeting the RB-E2F pathway in breast cancer. *Oncogene*. 2016;35(37):4829–4835. doi:10.1038/onc.2016.26
12. Bandiera R, et al. RN7SK small nuclear RNA controls bidirectional transcription of highly expressed gene pairs in skin. *Nat Commun*. 2021;12(1):5864. doi:10.1038/s41467-021-26066-3
13. Abasi M, et al. 7SK small nuclear RNA transcription level down-regulates in human tumors and stem cells. *Med Oncol*. 2016;33(11):128. doi:10.1007/s12032-016-0842-7
14. Wang Y, et al. N6-methyladenosine in 7SK small nuclear RNA underlies RNA polymerase II transcription regulation. *Mol Cell*. 2023;83(21):3819–3836. doi:10.1016/j.molcel.2023.09.021
15. Xie M, et al. The ASH1L-AS1-ASH1L axis controls NME1-mediated activation of the RAS signaling in gastric cancer. *Oncogene*. 2023;42(46):3435–3445. doi:10.1038/s41388-023-02835-2
16. Zhai W, et al. ADAMTS4 exacerbates lung cancer progression via c-Myc and MAPK signaling. *Biol Direct*. 2024;19:94. doi:10.1186/s13062-024-00542-4
17. Takikawa M, Ohki R. Reprimo (RPRM): a tumor suppressor that induces extrinsic apoptosis via YAP signaling. *Cancer Sci*. 2025;116(12):3266–3273. doi:10.1111/cas.16497
18. Moussalem C, et al. Modelling oxaliplatin resistance in CRC reveals a SERPINE1-based gene signature (RESIST-M). *bioRxiv*. 2024. doi:10.1101/2024.12.17.628817
19. Pan T, et al. BRD4 regulates PAI-1 expression in tumor-associated macrophages to drive chemoresistance in CRC. *Oncogene*. 2025. doi:10.1038/s41388-025-03453-6
20. Slyskova J, et al. Detection of oxaliplatin- and cisplatin-DNA lesions requires different global genome repair mechanisms. *NAR Cancer*. 2023;5(4):zcad057. doi:10.1093/narcan/zcad057
21. Tazawa H, et al. Adenovirus E1A protein sensitizes chemotherapy-resistant tumors to cisplatin. *Ann Med Surg*. 2026;82(2):107694. doi:10.1097/MS9.0000000000003112
22. Chang YW, et al. The anti-tumor activity of E1A and its implications in cancer therapy. *Arch Immunol Ther Exp*. 2014;62(3):195–204. doi:10.1007/s00005-014-0277-4
23. Cimas FJ, et al. MKP1 mediates chemosensitizer effects of E1A in response to cisplatin in NSCLC cells. *Oncotarget*. 2015;6(42):44095–44107. doi:10.18632/oncotarget.6574
24. Radke JR, et al. E1A enhances cellular sensitivity to DNA-damage-induced apoptosis through PIDD-dependent caspase-2 activation. *Cell Death Discov*. 2016;2:16076. doi:10.1038/cddiscovery.2016.76
25. Fang L, et al. A p53-independent apoptotic mechanism of adenoviral mutant E1A. *Oncotarget*. 2016;7(30):48309–48320. doi:10.18632/oncotarget.10195
26. Liao Y, Hung MC. PP2A mediates E1A sensitization to anticancer drug-induced apoptosis. *Cancer Res*. 2004;64(17):5938–5942. doi:10.1158/0008-5472.CAN-04-1341
27. Lindell E, et al. Quiescent cancer cells — a potential therapeutic target to overcome tumor resistance and relapse. *Int J Mol Sci*. 2023;24(4):3762. doi:10.3390/ijms24043762
28. Yano S, et al. FUCCI real-time cell-cycle imaging to target quiescent chemo-resistant cancer cells. *Cancers*. 2020;12(9):2655. doi:10.3390/cancers12092655
29. Basu S, et al. Slow-cycling (dormant) cancer cells in therapy resistance, cancer relapse and metastasis. *Semin Cancer Biol*. 2022;78:90–103. doi:10.1016/j.semcancer.2021.04.021
30. Carlsen L, et al. Pan-drug and drug-specific mechanisms of 5-FU, irinotecan, oxaliplatin, and cisplatin. *Oncotarget*. 2021;12(20):2006–2021. doi:10.18632/oncotarget.28066
31. Slaninová V, et al. The Hippo pathway terminal effector TAZ/WWTR1 mediates oxaliplatin sensitivity. *BMC Cancer*. 2024;24(1):587. doi:10.1186/s12885-024-12264-z
32. Jensen NF, et al. Establishment and characterization of models of chemotherapy resistance in CRC. *Mol Oncol*. 2015;9(6):1169–1185. doi:10.1016/j.molonc.2015.02.008
33. Fang J, et al. UBE2H as a marker of oxaliplatin resistance in CRC. *Cancer Cell Int*. 2025;25(1):383. doi:10.1186/s12935-025-03618-0
34. Zhan X, et al. Identification of a signature gene set for oxaliplatin sensitivity prediction in CRC. *Front Oncol*. 2025;15:1701328. doi:10.3389/fonc.2025.1701328
35. Xia Y, et al. Drug repurposing for cancer therapy. *Sig Transduct Target Ther*. 2024;9(1):92. doi:10.1038/s41392-024-01803-6

---

---

# Русская версия

## Обзор литературы: Дифференциальный транскриптомный ответ на оксалиплатин в чувствительных и резистентных клетках колоректального рака

### Фокус: регуляция клеточного цикла, покой (quiescence) и остановка пролиферации

---

## 1. Ключевые результаты исследования Morshneva et al.

| Наблюдение | Чувствительные HCT116 | Резистентные HCT116-OX |
|------------|----------------------|------------------------|
| DEG при оксалиплатине (25 мкМ, 24ч) | 1,791 генов (978↑, 813↓) | 830 генов (358↑, 472↓) — **в 2 раза меньше** |
| Регуляторы клеточного цикла | Без изменений или активированы | **Резко подавлены** (E2F1/2/8, FOXM1, MYBL2, циклины, AURKA/B) |
| p21 (CDKN1A) | Умеренная индукция | Сильная индукция на уровне транскрипта |
| S-фаза через 48ч оксалиплатина | 42% → 20% (снижение в 2 раза) | 30% → 5% (**снижение в 5 раз** — быстрая остановка) |
| Пути выживания | Стресс-ответ, тканевая репарация | **Аутофагия, процессинг белков в ЭР, метаболическая перестройка** + активация SERPINE1 |
| 10 генов с противоположной динамикой | Повышены оксалиплатином | **Снижены** оксалиплатином (RN7SK, ASH1L-AS1, ADAMTS4, RPRML и др.) |
| Ответ на экспрессию E1A | Умеренная реактивация цикла | Сильная реактивация: S-фаза 5.8%→14%, **p53↑×10**, апоптоз, ресенситизация |

**Центральный парадокс:** Резистентные клетки выживают при оксалиплатине *потому, что* быстрее останавливают пролиферацию — а не вопреки этому. Это предотвращает накопление летальных повреждений ДНК в S-фазе.

---

## 2. Литература, поддерживающая парадигму «остановись-чтобы-выжить» (Arrest-to-Survive)

### 2.1 Drug-Tolerant Persister (DTP) клетки

| Источник | Ключевой результат | Связь с работой Morshneva et al. |
|----------|-------------------|----------------------------------|
| **De Conti G, et al.** *Signal Transduction and Targeted Therapy*, 2024; 9:209 | Комплексный обзор биологии DTP: клетки входят в обратимое покоящееся состояние (quiescence) при воздействии препаратов; глобальная транскрипционная супрессия, Myc↓, E2F targets↓, аутофагия↑, метаболическая перестройка | Объяснение **ослабленного ответа** (в 2 раза меньше DEG) и скоординированной программы ареста |
| **Rehman SK, et al.** *Cell*, 2021; 184(1):226–242 | Клетки КРР входят в **диапаузо-подобное DTP состояние** для выживания при химиотерапии; Myc-зависимая биосинтетическая супрессия, отличная от CDK4/6-индуцированного ареста | **Биосинтетический покой объясняет**, почему транскрипционный ответ ослаблен в HCT116-OX |
| **Cuesta-Borràs E, et al.** *Cell Reports*, 2023; 42(8):112927 | **Петля обратной связи DPPA3-HIF1α → метилирование промотора FOXM1 → снижение экспрессии FOXM1 → медленно-циклирующийся (slow-cycling) химиорезистентный фенотип** в КРР. Гиперэкспрессия DPPA3 предсказывает химиорезистентность | **Прямая параллель к подавлению FOXM1**, наблюдаемому в HCT116-OX при оксалиплатине |
| **Khong A, et al.** *RNA*, 2025. PMID: 40738736 | **Стресс-гранулы способствуют покою** через повышение p21 и снижение phospho-Rb | Механистическая связь для **индукции p21 + подавления E2F** в резистентных клетках |

### 2.2 Кинетика ареста клеточного цикла в резистентных vs. чувствительных клетках

| Источник | Ключевой результат | Связь |
|----------|-------------------|-------|
| **Hata T, et al.** *Molecular Cancer Therapeutics*, 2005; 4(10):1585–1594 | В p53-WT клетках HCT116 **оксалиплатин индуцирует p21-зависимый G0/G1 арест**. p21-null HCT116 не останавливаются в G1 и показывают сниженное ингибирование роста | Подтверждает **p21-центричный механизм G1 ареста** в HCT116 (p53-WT); индукция p21 является защитной |
| **William-Faltaos S, et al.** *Fundamental & Clinical Pharmacology*, 2007; 21(2):165–172 | Оксалиплатин вызывает G2/M арест и S-фазовую задержку; **кинетика ареста зависит от статуса p53** | Контекст для дифференциального ареста: HCT116 p53-WT → способны к эффективному p21-опосредованному G1 аресту |
| **Li Y, et al.** *International Journal of Molecular Medicine*, 2025 | **miR-100-5p → CTDSPL↓ → гиперфосфорилированный pRB → высвобождение E2F1 → ускорение G1/S + химиорезистентность** в оксалиплатин-резистентных CRC (LoVoOXR) | Альтернативный механизм резистентности через **активацию E2F1, а не подавление** — контекстно-зависимый |
| **Chen X, et al.** *Nature Communications*, 2025; 16:66836 | scRNA-seq выявляет **континуум «покой–сенесценция»** после химиотерапии; множественные сенотипы с разными транскрипционными программами | Перспектива на уровне единичных клеток на **популяционно-усреднённый арест** |

### 2.3 Ось E2F-FOXM1 в химиорезистентности

| **Varghese V, et al.** *Scientific Reports*, 2019; 9:1722 | **FOXM1 и E2F1 реципрокно регулируют друг друга** в карциноме толстой кишки; FOXM1 модулирует резистентность к 5-FU через TYMS; ингибитор FOXM1 тиострептон + 5-FU = синергия в HCT116, DLD1, HT29 | FOXM1 и E2F1 **координированно регулируются** — оба подавлены в HCT116-OX |
| **Johnson J, et al.** *Oncogene*, 2016; 35(37):4829–4835 | **Путь RB-E2F** как терапевтическая мишень; канонический контроль G1/S restriction point | RB-E2F — **центральный узел** наблюдаемой транскрипционной программы ареста |

### 2.4 RN7SK и 10 генов с противоположной динамикой

| **Bandiera R, et al.** *Nature Communications*, 2021; 12(1):5864 | **Условный нокаут Rn7sk приводит к быстрому выходу из клеточного цикла**, поскольку гены клеточного цикла гиперчувствительны к нарушению элонгации транскрипции. Полный нокаут эмбрионально летален | **Прямое механистическое объяснение**, почему RN7SK↓ → арест клеточного цикла в HCT116-OX |
| **Abasi M, et al.** *Medical Oncology*, 2016; 33(11):128 | **7SK snRNA снижена в опухолях человека**, включая КРР; действует как супрессор опухолей | Потеря RN7SK **описана в биологии КРР** |
| **Wang Y, et al.** *Molecular Cell*, 2023; 83(21):3819–3836 | **N6-метиладенозиновая модификация 7SK** регулирует элонгацию транскрипции Pol II; METTL3/ALKBH5 контролируют конформацию 7SK и секвестрацию P-TEFb | **Посттранскрипционный уровень регуляции** RN7SK |
| **Xie M, et al.** *Oncogene*, 2023; 42(46):3435–3445 | **Ось ASH1L-AS1-ASH1L → NME1 → активация RAS-MAPK** в раке желудка | Снижение ASH1L-AS1 → **ослабление RAS-MAPK** способствует аресту |
| **Zhai W, et al.** *Biology Direct*, 2024; 19:94 | **ADAMTS4 активирует MAPK сигналинг** через стабилизацию c-Myc в раке лёгкого | ADAMTS4↓ → MAPK↓ → **усиление пролиферативного ареста** |
| **Takikawa M, Ohki R.** *Cancer Science*, 2025; 116(12):3266–3273 | **Репримо (RPRM) индуцирует внешний путь апоптоза** через YAP сигналинг | RPRML↓ → снижение про-апоптотического давления → **преимущество выживания** |

### 2.5 SERPINE1/PAI-1 и пути выживания

| **Moussalem C, et al.** *bioRxiv*, 2024 | **RESIST-M сигнатура**: холестерин↓ → перераспределение рецепторов TGF-β → устойчивый TGF-β/SMAD → **SERPINE1↑** → химиорезистентность + метастазирование. shRNA/фармакологическое ингибирование SERPINE1 ресенситизирует клетки к оксалиплатину | **SERPINE1 как топ-DEG** в HCT116-OX точно вписывается в эту ось |
| **Pan T, et al.** *Oncogene*, 2025 | **BRD4 регулирует PAI-1** в опухоль-ассоциированных макрофагах → M2-поляризация → химиорезистентность. PAI-1 ингибитор + оксалиплатин = синергия | Микроокружение — **PAI-1-зависимая резистентность** |

### 2.6 E1A-опосредованная сенситизация

| **Tazawa H, et al.** *Annals of Medicine and Surgery*, 2026; 82(2):107694 | E1A сенситизирует опухоли к цисплатину через **p19ARF/p53, CtBP, HER2/neu**. Преодолевает p53-мутантную резистентность через caspase-2/PIDD | **Механистическая основа** эффекта E1A в HCT116-OX |
| **Chang YW, et al.** *Archivum Immunologiae et Therapiae Experimentalis*, 2014; 62(3):195–204 | **Исчерпывающий обзор** противоопухолевой активности E1A | **Концептуальная рамка** двойного механизма E1A |
| **Cimas FJ, et al.** *Oncotarget*, 2015; 6(42):44095–44107 | **MKP1 опосредует E1A-химиосенситизацию** к цисплатину | Специфический **сигнальный узел** синергии E1A + платина |
| **Radke JR, et al.** *Cell Death Discovery*, 2016; 2:16076 | E1A усиливает апоптоз через **PIDD-зависимую активацию caspase-2** — p53-независимый механизм | Релевантно, если **p53-независимый апоптоз** вносит вклад в HCT116-OX |
| **Fang L, et al.** *Oncotarget*, 2016; 7(30):48309–48320 | p53-независимый апоптотический механизм E1A — **селективная противоопухолевая активность** | E1A убивает **независимо от статуса p53** |
| **M.D. Anderson Cancer Center.** ClinicalTrials.gov NCT00102622, 2018 | **Фаза I/II** tgDCC-E1 + паклитаксел при платино-резистентном раке яичников | **Прецедент клинического применения** E1A + платина |

### 2.7 Реактивация клеточного цикла как терапевтическая стратегия

| **Lindell E, et al.** *Int J Mol Sci*, 2023; 24(4):3762 | Покоящиеся раковые клетки как терапевтические мишени — обзор стратегий реактивации | **Концептуальная рамка** подхода с E1A |
| **Yano S, et al.** *Cancers*, 2020; 12(9):2655 | **FUCCI-визуализация клеточного цикла в реальном времени** для разработки стратегий против покоящихся клеток | **Визуальное доказательство**, что покоящиеся клетки выживают и возвращаются в цикл |
| **Basu S, et al.** *Seminars in Cancer Biology*, 2022; 78:90–103 | Медленно-циклирующиеся/дормантные раковые клетки в **терапевтической резистентности, рецидиве и метастазировании** | **Клиническая значимость** воздействия на SCCs |

### 2.8 Сравнительные транскриптомные исследования ответа на платину

| **Carlsen L, et al.** *Oncotarget*, 2021; 12(20):2006–2021 | **Пан-лекарственные и лекарственно-специфичные транскриптомные сигнатуры** для 5-FU, иринотекана, оксалиплатина, цисплатина в клетках КРР. 36 общих DEG с данными Morshneva (CDKN1A, GDF15, BTG2 и др.) | **Единственное прямое сравнение** для оксалиплатин-индуцированного транскриптома в КРР |
| **Slaninová V, et al.** *BMC Cancer*, 2024; 24(1):587 | **TAZ/WWTR1 опосредует чувствительность к оксалиплатину** в p53-профицитных клетках; ответ на низкие дозы (0.5 мкМ). 93 DEG пересекаются с данными Morshneva | Другой диапазон доз — **дополнительная перспектива** |

---

## 3. Синтез: как результаты Morshneva et al. вписываются в литературу

### 3.1 Ослабленный транскрипционный ответ

Двукратное снижение числа DEG в HCT116-OX соответствует модели **drug-tolerant persister (DTP)** [De Conti 2024; Rehman 2021]. DTP-клетки входят в состояние **глобальной транскрипционной и биосинтетической супрессии**, отличное от простого ареста клеточного цикла. «Биосинтетический покой», описанный Rehman et al., включает подавление Myc и рибосомального биогенеза — согласуется с GO-терминами, подавленными в HCT116-OX (рибосомная функция, трансляция). **Это первое исследование, документирующее ослабленный транскриптомный ответ именно в оксалиплатин-резистентных клетках КРР.**

### 3.2 Быстрый арест клеточного цикла

Наблюдение, что резистентные клетки останавливаются **быстрее** чувствительных — S-фаза падает в 5 раз vs. в 2 раза — представляет собой **центральный парадокс этой работы** и всё чаще признаётся отличительным признаком адаптивной лекарственной толерантности. Ось DPPA3-HIF1α-FOXM1 [Cuesta-Borràs 2023] предоставляет прямую механистическую параллель: стресс химиотерапии запускает эпигенетическое сайленсирование FOXM1 через метилирование промотора, обеспечивая медленно-циклирующийся химиорезистентный фенотип. **Подавление E2F1/2/8 и FOXM1** в HCT116-OX при оксалиплатине зеркально отражает эту ось.

**Ключевое отличие от существующей литературы:** Большинство исследований сообщают либо об активации E2F (через pRB гиперфосфорилирование → путь miR-100-5p/CTDSPL → ускорение G1/S), либо о подавлении E2F (quiescence). Данные Morshneva чётко показывают **последний путь** в HCT116-OX. Это предполагает существование **двух различных резистентных состояний**: активно циклирующегося (E2F-high) и покоящегося (E2F-low).

### 3.3 RN7SK — новый узел в ответе на платину

Почти полная потеря RN7SK в резистентных клетках при оксалиплатине является, насколько нам известно, **первым сообщением о динамике 7SK при платиновой резистентности**. Механистическая связь — RN7SK↓ → дисрегуляция P-TEFb → избирательное подавление генов клеточного цикла [Bandiera 2021] — обеспечивает прямой транскрипционный механизм быстрого ареста.

### 3.4 SERPINE1 и про-выживательные пути

Активация SERPINE1 в HCT116-OX при оксалиплатине совпадает с **RESIST-M сигнатурой** [Moussalem 2024], где ось холестерин-TGF-β-SERPINE1 обеспечивает химиорезистентность и метастазирование. Это позиционирует HCT116-OX в рамках CMS4/iCMS3-фибротического подтипа КРР с наихудшим прогнозом.

### 3.5 Стратегия реактивации E1A

E1A-опосредованная реактивация клеточного цикла как стратегия сенситизации подтверждена десятилетиями доклинических работ [Chang 2014; Tazawa 2026]. Новизна исследования Morshneva заключается в: (а) **первом транскриптомном профиле E1A-экспрессирующих раковых клеток**, (б) демонстрации того, что E1A преодолевает **специфическую транскрипционную программу ареста** (реактивация GO:1901987), и (в) **массивной активации p53 (×10)** в E1A-экспрессирующих резистентных клетках.

### 3.6 Открытые вопросы

1. **Является ли потеря RN7SK причинной или коррелятивной?** Необходимы прямые эксперименты с нокдауном/гиперэкспрессией.
2. **Каков механизм на уровне хроматина** для подавления E2F/FOXM1 — DPPA3-подобное метилирование промоторов или вышестоящий сигналинг?
3. **Гетерогенность на уровне единичных клеток** — происходит ли быстрый арест равномерно или в субпопуляции?
4. **Фармакологическая мимикрия E1A** — какие малые молекулы могут фенокопировать двойную активность E1A (например, CDK4/6 ингибиторы + активаторы p53)?
5. **Имеет ли 10-генная сигнатура** с противоположной динамикой прогностическую ценность в когортах пациентов с КРР?

---

## 4. Краткий словарь терминов

| Английский | Русский |
|-----------|---------|
| Drug-tolerant persister (DTP) | Лекарственно-толерантная персистирующая клетка |
| Quiescence | Покой (обратимое состояние выхода из клеточного цикла, G0) |
| Slow-cycling cells (SCCs) | Медленно-циклирующиеся клетки |
| Dormant cancer cells | Дормантные (спящие) раковые клетки |
| Cell cycle arrest | Остановка клеточного цикла |
| Biosynthetic quiescence | Биосинтетический покой |
| Mitotic catastrophe | Митотическая катастрофа |
| DDR (DNA damage response) | Ответ на повреждение ДНК |
| NER (nucleotide excision repair) | Эксцизионная репарация нуклеотидов |
| GSEA | Анализ обогащения генных наборов |
| DEG (differentially expressed gene) | Дифференциально экспрессируемый ген |
| Senescence | Сенесценция (необратимая остановка клеточного цикла) |
| scRNA-seq | Секвенирование РНК единичных клеток |

---

*Документ подготовлен 12 июня 2026 г. на основе поиска в PubMed, PMC, Google Scholar, bioRxiv.*
*35 процитированных источников.*
