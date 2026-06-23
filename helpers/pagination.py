from flask import request 

PER_PAGE = 12 

def paginate(query): 
    page = request.args.get("page", type=int) 
    
    print(f"Requested page: {page}")
    
    if page is None: 
        return {"items": query.all(), "pagination": None}
    
    page = max(1, page)
    total = query.count()
    items = query.offset((page - 1) * PER_PAGE).limit(PER_PAGE).all()

    return {
        "items": items,
        "pagination": {
            "page": page,
            "per_page": PER_PAGE,
            "total": total,
            "pages": (total + PER_PAGE - 1) // PER_PAGE,
            "has_next": page * PER_PAGE < total,
            "has_prev": page > 1,
        }
    }