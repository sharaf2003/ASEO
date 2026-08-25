from sqlalchemy.orm import Session

from app.models.invoice import Invoice





class InvoiceRepository:

    """
    ASEO Invoice Repository.
    """



    # =====================================
    # Create Invoice
    # =====================================


    def create(

        self,

        db: Session,

        invoice: Invoice

    ):


        db.add(invoice)

        db.commit()

        db.refresh(invoice)


        return invoice





    # =====================================
    # Get Organization Invoices
    # =====================================


    def get_by_organization(

        self,

        db: Session,

        organization_id: int

    ):


        return (

            db.query(Invoice)

            .filter(

                Invoice.organization_id == organization_id

            )

            .order_by(

                Invoice.created_at.desc()

            )

            .all()

        )





    # =====================================
    # Get By Invoice Number
    # =====================================


    def get_by_number(

        self,

        db: Session,

        invoice_number: str

    ):


        return (

            db.query(Invoice)

            .filter(

                Invoice.invoice_number == invoice_number

            )

            .first()

        )


    # =====================================
    # Get Invoice By ID
    # =====================================


    def get_by_id(

        self,

        db: Session,

        invoice_id: int

    ):


        return (

            db.query(Invoice)

            .filter(

                Invoice.id == invoice_id

            )

            .first()

        )


    # =====================================
    # Update Invoice
    # =====================================


    def update(

        self,

        db: Session,

        invoice: Invoice,

        data: dict

    ):


        for key, value in data.items():

            setattr(

                invoice,

                key,

                value

            )


        db.commit()

        db.refresh(invoice)


        return invoice