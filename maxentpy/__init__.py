try:
    from maxent import score5, score3, load_matrix5, load_matrix3
except ImportError:
    from .maxent import score5, score3, load_matrix5, load_matrix3
