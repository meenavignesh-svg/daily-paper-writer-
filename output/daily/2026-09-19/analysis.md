## Scope of the evidence

The supplied bibliography contains only a small number of papers directly addressing protein-function prediction. The strongest direct evidence is Gligorijević et al. (2021), *Structure-based protein function prediction using graph convolutional networks*. Bordin et al. (2023) provides a broader review of machine learning in protein science, while Yu et al. (2022) focuses on metalloproteins. Several other papers concern protein structure prediction, protein–protein interactions, sequence design, virtual screening, or clinical prediction. These topics are relevant to protein-function inference, but they should not be treated as equivalent tasks.

Because the evidence supplied is primarily bibliographic metadata rather than full study descriptions, specific claims about datasets, model architectures, or reported performance require [VERIFY].

## How machine learning is being used

### Sequence-based prediction

A major approach is to represent proteins as amino-acid sequences and learn associations between sequence patterns and functional labels. Conventional models may use engineered descriptors, motifs, evolutionary profiles, or similarity-based features. More recent methods use protein language models, which learn sequence representations from large collections of unlabeled protein sequences. The 2023 review by Bordin et al. and the 2026 paper on protein language models and epistatic interactions indicate the growing importance of these representations, although the latter appears to focus on directed evolution rather than function annotation.

Sequence-based models can be used for:

- assigning Gene Ontology or other functional labels;
- predicting enzyme classes or catalytic properties;
- identifying binding or localization-related features;
- predicting the effects of mutations on activity or stability;
- transferring functional information to poorly characterized proteins.

The supplied evidence does not establish which particular language models, sequence databases, or function-label datasets were used in the cited studies [VERIFY].

### Structure-based prediction

Structure-based methods represent a protein as a graph, with residues or atoms as nodes and spatial proximity, chemical contacts, or other relationships as edges. Graph convolutional networks and related geometric deep-learning models can then learn structural patterns associated with function. This is the central methodological theme of Gligorijević et al. (2021).

Structural inputs may come from experimentally determined structures or computational predictions. AlphaFold and AlphaFold 3 are therefore important enabling technologies, but they are not themselves general protein-function predictors. Their primary outputs are predicted structures or biomolecular complexes. The AlphaFold Protein Structure Database can provide structural representations for proteins lacking experimental structures, potentially expanding the scope of downstream structure-based functional annotation.

The main attraction of structure-based prediction is that proteins with low sequence similarity may still share folds, active-site geometries, or interaction surfaces. Its effectiveness therefore depends on the quality of the structural representation and on whether the predicted structure captures the biologically relevant conformation. The extent to which these benefits were demonstrated in the cited function-prediction study requires [VERIFY].

### Interaction and network-based prediction

Protein–protein interaction prediction and graph learning provide another route to function inference. A protein’s interaction partners, complex membership, and position in a cellular network can be informative about its biological role. Gao et al. (2023) and Michalik and Kuder (2024) are relevant to this broader structural and interaction-modelling context.

However, predicting whether two proteins interact is not the same as predicting protein function. Interaction models can supply features for functional annotation, but their predictions may also inherit errors from incomplete or context-dependent interaction databases. The cited evidence does not show whether the interaction-focused papers evaluated downstream function prediction [VERIFY].

### Multimodal and application-specific models

The field is moving toward models that combine sequence, structure, evolutionary information, interaction networks, biochemical measurements, and possibly expression or other omics data. Such integration is attractive because protein function is determined by more than primary sequence alone. The general literature on informed machine learning and multi-omics supports this direction, but most of the multi-omics and clinical records in the supplied list predict disease states, treatment response, or biomarker outcomes rather than molecular protein function. They should not be used as direct evidence for the protein-function question.

## Datasets and labels

For direct protein-function prediction, the likely label sources include curated protein annotation databases and experimentally supported Gene Ontology annotations. Common benchmark resources in this area also include CAFA-style evaluation sets, protein sequence databases, structural repositories, and interaction databases [VERIFY]. The supplied records do not provide enough information to identify the exact datasets used by Gligorijević et al. or by the reviews.

Several types of data are likely to be involved:

1. **Protein sequences**  
   Large sequence repositories provide training material for language models and sequence classifiers. Their scale is much greater than the number of proteins with reliable experimental functional annotations.

2. **Functional annotations**  
   Gene Ontology terms are a common multilabel target, often divided into molecular function, biological process, and cellular component. Enzyme classifications, ligand-binding labels, metal-binding annotations, and subcellular localization are other possible targets [VERIFY].

3. **Experimental structures**  
   PDB structures can support structure-based training and evaluation, although their coverage is uneven across protein families and organisms.

4. **Predicted structures**  
   AlphaFold Database models greatly increase structural coverage, but predicted structures are not equivalent to experimentally observed structures and may be uncertain in disordered regions, flexible domains, or alternative conformations.

5. **Interaction and evolutionary data**  
   Protein-family alignments, profiles, coevolutionary information, and interaction networks can provide additional predictive features. Their use and preprocessing must be checked study by study [VERIFY].

A central difficulty is that these datasets are not independent. Closely related proteins may occur in both training and test sets, and annotations may be propagated through homology. This can make performance appear stronger than it would be for genuinely novel protein families. The general discussion of leakage and reproducibility by Kapoor and Narayanan is therefore highly relevant, although it is not specific to protein-function benchmarks.

## Evaluation metrics

Protein-function prediction is usually a multilabel and often hierarchical classification problem. A model may assign several function terms to one protein, and the terms are related through the Gene Ontology hierarchy. Consequently, a single accuracy value is usually inadequate.

Metrics that are commonly relevant include:

- precision, recall, and F1 score;
- area under the precision–recall curve (AUPR), particularly for imbalanced labels;
- area under the receiver-operating-characteristic curve (AUROC);
- maximum F-measure across decision thresholds, often reported as Fmax;
- coverage or ranking-based measures;
- ontology-aware measures such as semantic distance or Smin [VERIFY].

For rare functional classes, AUPR and per-class recall may be more informative than AUROC. Ranking quality is also important because annotation systems often present users with a prioritized list of candidate functions rather than a single prediction.

Evaluation should ideally include:

- a sequence-disjoint or family-disjoint test set;
- temporal splits that prevent later annotations from leaking into training;
- separate evaluation for common and rare functions;
- performance stratified by sequence similarity, structural coverage, and annotation quality;
- calibration or confidence assessment;
- external experimental validation where feasible.

The supplied bibliography does not report enough information to determine which of these protocols were used in the direct function-prediction studies [VERIFY].

## Main limitations

### Incomplete and biased labels

Protein annotations are unevenly distributed across species, protein families, and functional categories. Well-studied proteins tend to have many annotations, while newly discovered or evolutionarily distant proteins may be poorly characterized. Absence of an annotation therefore does not necessarily mean absence of the function. This creates noisy negative examples and can distort both training and evaluation.

### Homology and data leakage

Randomly splitting proteins is often inappropriate because homologous sequences can occur in both training and test sets. A model may then appear to infer function when it is partly recognizing family membership or annotation propagation. The leakage and reproducibility concerns emphasized by Kapoor and Narayanan are especially important here. Claims of high accuracy should therefore be interpreted alongside the split strategy and the degree of sequence or structural redundancy [VERIFY].

### Distribution shift

Models trained on proteins from common organisms or well-represented families may perform poorly on proteins from underrepresented taxa, remote homologues, novel folds, membrane proteins, disordered proteins, or proteins with context-dependent functions. A model can also fail when the relevant functional state depends on ligand binding, oligomerization, post-translational modification, cellular localization, or environmental conditions that are not represented in the input.

### Limits of predicted structures

Predicted structures have expanded the available structural data, but uncertainty is not uniform across a protein. Flexible regions, intrinsically disordered segments, multimeric states, ligand-induced conformations, and transient complexes may be represented poorly. A structure-based model can consequently inherit errors from the structure predictor or mistake a plausible geometry for a biologically active one.

### Correlation is not mechanism

Deep models can identify statistical associations without revealing why a protein performs a function. This is particularly problematic for active-site prediction, regulatory mechanisms, and mutation effects. Explainability tools such as SHAP may help examine feature attribution, but attribution is not the same as mechanistic proof, and protein-specific validation remains necessary [VERIFY].

### Functional ambiguity and ontology dependence

Protein functions are often context-dependent and can be described at different levels of specificity. A prediction may be correct at a broad ontology level but unsupported at a fine-grained level. Ontology structure also complicates comparisons between studies: different annotation versions, score thresholds, and treatment of parent and child terms can produce different metrics.

### Limited experimental validation

Many computational studies evaluate against existing annotations rather than testing new predictions experimentally. This makes benchmark performance useful for comparison but insufficient to establish biological validity. The supplied evidence includes several papers involving in vivo or drug-discovery validation, but those papers generally address therapeutic targets or disease mechanisms rather than systematic protein-function prediction.

## Overall assessment

Machine learning is being used for protein-function prediction through sequence representation learning, protein language models, structure-based graph networks, interaction and network modelling, and increasingly multimodal integration. The most directly relevant supplied study is the structure-based graph-convolutional work of Gligorijević et al.; AlphaFold-related papers are important mainly because they make structural inputs more available, not because they directly solve functional annotation.

The principal evaluation challenge is ensuring that apparent predictive success reflects genuine generalization rather than homology, annotation propagation, or information leakage. Reliable assessment requires carefully separated test sets, metrics suited to multilabel and imbalanced outputs, ontology-aware analysis, calibration, and—ultimately—experimental confirmation. The bibliography identifies the relevant methodological landscape, but it does not contain sufficient study-level detail to make firm claims about the exact datasets or reported metrics without consulting the full texts [VERIFY].