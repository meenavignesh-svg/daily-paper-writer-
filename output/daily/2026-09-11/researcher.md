# Evidence overview

## Bottom line

The supplied records provide **some directly relevant evidence** on machine learning (ML) for protein-function prediction, but the evidence base is mixed with papers on protein structure prediction, drug discovery, clinical prediction, docking, and protein design. The strongest direct record is:

- **Gligorijević et al. (2021), “Structure-based protein function prediction using graph convolutional networks.”**

Several reviews are also relevant for framing the field:

- **Yu et al. (2022), “Machine Learning Approaches for Metalloproteins.”**
- **Bordin et al. (2023), “Novel machine learning approaches revolutionize protein knowledge.”**
- **Greener et al. (2021), “A guide to machine learning for biologists.”**

However, the supplied metadata do not report the datasets, benchmark splits, numerical results, or evaluation metrics. **Full-text verification is therefore required before making specific claims about model performance or comparative effectiveness.**

---

## Relevance-ranked records

### Tier 1: Directly focused on protein-function prediction

| Record | Relevance and apparent contribution | Information requiring full-text verification |
|---|---|---|
| **Gligorijević et al. (2021), “Structure-based protein function prediction using graph convolutional networks.”** DOI: 10.1038/s41467-021-23303-9 | **Most directly relevant primary study.** It indicates the use of graph convolutional networks (GCNs) to predict protein function from structural information. This is important because proteins can be represented as residue or atom graphs, allowing a model to use spatial relationships that are not explicit in a linear sequence. | What structural representations were used; whether structures came from experimental databases or predicted models; which functional ontology or labels were predicted; training and test-set construction; treatment of homologues; evaluation metrics; performance relative to sequence-based baselines; whether predictions were experimentally validated. **Priority for full text.** Local PDF is listed. |
| **Yu et al. (2022), “Machine Learning Approaches for Metalloproteins.”** PMID: 35209064 | **Directly relevant review.** Metalloproteins are a useful case study because function depends on sequence, structure, metal-binding residues, coordination geometry, and sometimes metal identity. The review likely surveys ML methods for classification or prediction involving metalloproteins. | Exact tasks covered; datasets and sources of annotations; whether the focus is function prediction, metal-site prediction, structure prediction, or ligand binding; reported metrics and limitations. **Priority for full text.** |
| **Bordin et al. (2023), “Novel machine learning approaches revolutionize protein knowledge.”** PMID: 36504138 | **Broadly relevant review.** The title suggests coverage of newer protein ML approaches, potentially including protein language models, structure-aware models, protein representations, and functional annotation. | Which methods are discussed specifically for function prediction; how protein language models are evaluated; treatment of zero-shot or few-shot prediction; benchmark datasets; conclusions about generalization and annotation bias. **Priority for full text.** |
| **Zhang et al. (2025), “Sequence-based virtual screening using transformers.”** PMID: 40721411 | Relevant to sequence-based transformer representations of proteins, but the apparent application is **virtual screening rather than protein-function prediction**. It may still inform how transformer embeddings are used to represent protein sequences. | Whether functional annotation is included as a task; sequence datasets; labels and metrics; distinction between binding or activity prediction and general protein-function prediction. **Secondary priority.** |

### Tier 2: Relevant methodological or adjacent protein-ML evidence

| Record | Relevance and apparent contribution | Information requiring full-text verification |
|---|---|---|
| **Chen et al. (2024), “AI-Driven Deep Learning Techniques in Protein Structure Prediction.”** PMID: 39125995 | Relevant background for structure-based function prediction. Structural predictions can provide inputs for function models, but structure prediction itself is not equivalent to predicting biological function. | Whether the review discusses downstream function annotation; types of structural representations; reliability of predicted structures for functional inference; appropriate structure-confidence measures. **Full text needed.** |
| **Schauperl and Denny (2022), “AI-Based Protein Structure Prediction in Drug Discovery: Impacts and Challenges.”** PMID: 35727311 | Adjacent review concerning AI-generated or predicted structures. It can help assess the limitations of using predicted structures as inputs to function-prediction systems. | Discussion of function prediction versus structure prediction; effects of structural uncertainty; generalization across protein families; validation standards. **Full text needed if structure-derived function is being assessed.** |
| **Jumper et al. (2021), “Highly accurate protein structure prediction with AlphaFold.”** DOI: 10.1038/s41586-021-03819-2 | Foundational structure-prediction paper. It is relevant indirectly because predicted structures may support structure-based functional annotation. It does not, based on the title, directly establish a protein-function prediction method. | Whether the paper evaluates functional utility or only structural accuracy; how structural accuracy varies by protein region; implications for active sites, interfaces, and ligand-binding sites. **Full text available locally and should be checked for downstream-function claims.** |
| **Váradi et al. (2023), “AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences.”** DOI: 10.1093/nar/gkad1011 | Relevant as a potential source of predicted structures for large-scale function-prediction pipelines. The title reports extensive structural coverage, but database coverage is not the same as validated functional annotation. | How structures are indexed and confidence-scored; provenance of sequences; redundancy and homology issues; appropriate use of AlphaFold structures in ML training and evaluation. **Full text needed; PDF access failed in the supplied record.** |
| **Gao et al. (2023), “Hierarchical graph learning for protein-protein interaction.”** PMID: 36841846 | Relevant to a neighbouring task: predicting protein–protein interactions. Interaction predictions can provide functional evidence, but PPI prediction should not be treated as general protein-function prediction. | Whether the model predicts interaction existence, interaction type, or functional associations; interaction database and negative sampling; evaluation split; metrics; transfer to functional annotation. **Full text needed.** |
| **Michalik and Kuder (2024), “Machine Learning Methods in Protein-Protein Docking.”** PMID: 38987466 | Adjacent review on structural interaction modelling. It may inform function inference through interaction interfaces and molecular complexes. | Whether functional prediction is addressed; datasets, docking benchmarks, and metrics; relevance of docking accuracy to biological function. **Full text needed if interaction-based function prediction is in scope.** |
| **Odoemelam et al. (2025), “Computational modelling of olfactory receptors.”** PMID: 40441539 | Potentially relevant as a specialised protein-family application involving receptor structure and function. The title does not establish that ML-based functional annotation is the principal task. | Whether the work predicts receptor function, ligand specificity, structure, or signalling properties; data sources; validation against experiments. **Full text needed.** |

### Tier 3: Relevant to protein language models or protein design, but not clearly function prediction

| Record | Relevance and limitation |
|---|---|
| **Tran et al. (2026), “Rapid directed evolution guided by protein language models and epistatic interactions.”** | Relevant to protein language models and sequence-function relationships, but directed evolution and sequence optimisation are different from assigning functional annotations to previously uncharacterised proteins. Full text is needed to determine whether explicit function prediction is included. |
| **Dauparas et al. (2022), “Robust deep learning–based protein sequence design using ProteinMPNN.”** | Primarily a protein-design paper. It may use structural constraints to generate sequences, but sequence design is not the same as protein-function prediction. |
| **Abramson et al. (2024), “Accurate structure prediction of biomolecular interactions with AlphaFold 3.”** | Relevant to structural modelling of complexes and therefore potentially to interaction-mediated functional inference. It is not, from the title, a direct function-prediction study. |
| **Yoo et al. (2026), “Discovery of natural RORγt inhibitor using machine learning, virtual screening, and in vivo validation.”** | Uses ML in small-molecule discovery against a protein target. It concerns ligand discovery rather than prediction of the protein’s biological function. |
| **Wang et al. (2025), “Deciphering the mechanism of baicalein in cervical cancer via bioinformatics, machine learning and computational simulations: PIM1 and CDK2 are key target proteins.”** | Uses ML and computational analyses to identify or prioritise drug targets. This is not equivalent to predicting protein function from protein sequence or structure. |
| **Sahoo et al. (2021), “Artificial intelligence guided discovery of a barrier-protective therapy in inflammatory bowel disease.”** | Disease-therapy discovery rather than protein-function prediction. It may contain target-identification methods but is not a core record for this question. |
| **Li et al. (2025), “Machine learning driven prediction of drug efficacy in lung cancer: based on protein biomarkers and clinical features.”** | Predicts treatment efficacy using biomarkers and clinical variables, not intrinsic protein function. |
| **Kan et al. (2025), “Real-world clinical multi-omics analyses reveal bifurcation of ER-independent and ER-dependent drug resistance to CDK4/6 inhibitors.”** | Clinical multi-omics and drug-resistance analysis; not a protein-function prediction study. |

---

## What the records suggest about how ML is being used

The records point to several distinct uses of ML around protein function:

1. **Structure-based functional annotation**
   - The GCN paper is the clearest example.
   - Proteins can be represented as graphs in which nodes correspond to residues or atoms and edges encode spatial proximity, chemical contacts, or structural relationships.
   - Such models can potentially identify functional patterns that are distant in sequence but close in three-dimensional structure.

2. **Sequence-based representation learning**
   - Transformer and protein-language-model records indicate a trend toward learning contextual representations directly from amino-acid sequences.
   - These representations may be used for functional classification, interaction prediction, activity prediction, or downstream transfer learning.
   - The supplied records do not establish which specific function-prediction tasks were evaluated.

3. **Specialised prediction for protein classes**
   - Metalloproteins and olfactory receptors illustrate domain-specific applications.
   - In these settings, ML may combine sequence, structure, metal-binding features, receptor topology, ligand information, or evolutionary conservation.

4. **Interaction-mediated function inference**
   - PPI prediction and docking methods can provide indirect evidence about function by predicting interaction partners, interfaces, or complexes.
   - These tasks should be distinguished from direct annotation of functions such as enzymatic activity, molecular binding, cellular localisation, or Gene Ontology terms.

5. **Use of predicted structures**
   - AlphaFold and AlphaFold 3 are relevant mainly as infrastructure for generating structural inputs.
   - Their structural predictions may enable function inference, but high structural accuracy does not automatically imply correct functional annotation.

---

## Datasets and labels

The supplied records do not provide enough information to identify the datasets used in the direct function-prediction studies. Full texts should be checked for the following:

### Likely dataset categories to verify

- **Protein sequence databases**, such as UniProt or reviewed Swiss-Prot.
- **Gene Ontology annotations**, including molecular function, biological process, and cellular component.
- **Structure databases**, such as the Protein Data Bank and predicted-structure resources.
- **Protein-family or domain databases**, such as Pfam, InterPro, or SCOP/CATH.
- **Specialised datasets**, for example:
  - metalloprotein and metal-binding-site databases;
  - enzyme classification datasets;
  - protein–protein interaction databases;
  - receptor–ligand or activity datasets.

These are candidate resource types, not confirmed datasets for the listed studies.

### Dataset issues that are especially important

The full texts should be examined for:

- redundancy reduction and sequence-identity thresholds;
- separation of homologous protein families between training and test sets;
- temporal or taxonomic splits;
- the number of proteins and labels;
- long-tailed distribution of functional classes;
- incomplete or noisy functional annotations;
- handling of proteins with multiple functions;
- use of experimentally supported versus computationally propagated annotations;
- whether predicted structures were used during training or testing.

These choices strongly affect apparent performance. Random sequence-level splits can give overly optimistic results if close homologues occur in both training and test sets.

---

## Evaluation metrics

No numerical metrics are reported in the supplied bibliographic records. For full-text extraction, the following should be recorded separately for each study:

### For multilabel protein-function annotation

- precision and recall;
- micro- and macro-F1;
- area under the precision–recall curve;
- area under the receiver-operating-characteristic curve;
- maximum F-measure or ontology-specific F-measures;
- top-\(k\) accuracy or recall;
- hierarchical metrics that account for relationships between functional terms.

Protein-function prediction is often multilabel and highly imbalanced, so accuracy alone would be inadequate.

### For specialised classification tasks

- balanced accuracy;
- Matthews correlation coefficient;
- sensitivity and specificity;
- per-class performance;
- calibration or reliability of predicted probabilities.

### For interaction or structural tasks

- interaction precision/recall or F1;
- ranking metrics such as mean average precision or area under the precision–recall curve;
- interface or contact prediction measures;
- structural measures such as RMSD or TM-score, where relevant.

Structural metrics should not be substituted for function-prediction metrics. A model can produce a structurally plausible protein representation without correctly identifying its biological role.

---

## Remaining limitations

Across this evidence set, the main limitations to investigate are:

1. **Incomplete and biased labels**  
   Protein-function annotations are uneven across taxa and protein families. Well-studied proteins are more likely to be annotated, while poorly characterised proteins may be under-represented.

2. **Homology and data leakage**  
   Closely related proteins in training and test sets can make a model appear more generalisable than it is. The record on leakage and reproducibility is not protein-specific, but it is directly relevant to evaluating protein-ML benchmarks.

3. **Function is context-dependent**  
   Function can depend on cellular location, cofactors, interaction partners, post-translational modifications, oligomeric state, ligand availability, and environmental conditions. Sequence or isolated structure alone may be insufficient.

4. **Structure uncertainty**  
   Predicted structures can be inaccurate in flexible regions, disordered segments, alternative conformations, active sites, and protein interfaces. These uncertainties may propagate into structure-based function models.

5. **Class imbalance and multilabel complexity**  
   A protein may have several valid functional annotations, and some functions are rare. Aggregate metrics can conceal poor performance on uncommon but biologically important classes.

6. **Limited experimental validation**  
   Computational predictions may be benchmarked against existing annotations without independent biochemical or cellular confirmation. This tests agreement with databases, not necessarily discovery of new biology.

7. **Interpretability**  
   Deep models may identify predictive sequence or structural features without showing that those features are mechanistically causal. Attribution methods such as SHAP can aid interpretation, but explanations also require biological validation.

8. **Out-of-distribution generalisation**  
   Performance may decrease for new protein families, unusual folds, novel organisms, remote homologues, or proteins with no close representation in the training data.

9. **Confounding between related tasks**  
   Structure prediction, ligand binding, interaction prediction, protein design, and drug-response prediction are all related to protein biology but should not be presented as equivalent to direct protein-function prediction.

---

## Records that can be deprioritised or excluded

The following records are mainly outside the question’s scope:

- Tanabe et al. (2024), diabetes subtypes.
- Schade et al. (2024), TNBC therapy.
- Wu et al. (2025), renal transplantation injury.
- Zhang et al. (2025), HBV-related mortality.
- Pang et al. (2024), diabetic retinopathy.
- Arulraj et al. (2024), PD-1 response biomarkers.
- Ahmed et al. (2022), diabetes prediction.
- Chittora et al. (2021), chronic kidney disease.
- Most of the general AI, agriculture, clinical multi-omics, generative-AI, swarm-learning, and materials-science records.

They may provide general ML methodological context, but they do not directly address prediction of protein function.

## Full-text verification priorities

**Highest priority**

1. Gligorijević et al. (2021) — direct structure-based function prediction.
2. Yu et al. (2022) — metalloprotein ML review.
3. Bordin et al. (2023) — broad protein-ML review.
4. Zhang et al. (2025) — sequence-based transformer applications.
5. AlphaFold structure-prediction paper and AlphaFold Database paper — for assessing structural inputs and coverage.

**Second priority**

6. Gao et al. (2023) — interaction prediction.
7. Michalik and Kuder (2024) — ML for docking.
8. Odoemelam et al. (2025) — specialised receptor modelling.
9. Tran et al. (2026) — protein-language-model-guided sequence/function optimisation.

The current records support a cautious conclusion: **ML is being applied to protein-function inference through sequence representations, structural graphs, interaction modelling, and specialised protein-domain models, but the supplied evidence does not yet permit reliable comparison of datasets, metrics, or predictive performance.**