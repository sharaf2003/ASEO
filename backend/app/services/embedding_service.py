from abc import ABC, abstractmethod



class EmbeddingProvider(ABC):

    """
    Base interface for embedding providers.

    Allows switching between:

    - OpenAI embeddings
    - Local embedding models
    """



    @abstractmethod
    def create_embedding(

        self,

        text: str

    ) -> list[float]:

        pass





class MockEmbeddingProvider(EmbeddingProvider):

    """
    Temporary embedding provider.

    Used until real AI provider
    is connected.

    Keeps architecture ready
    for OpenAI / Local models.
    """



    def create_embedding(

        self,

        text: str

    ) -> list[float]:


        # Temporary vector

        return [

            0.0

        ] * 1536





class EmbeddingService:

    """
    Central service responsible
    for generating embeddings.
    """



    def __init__(

        self,

        provider: EmbeddingProvider | None = None

    ):


        self.provider = (

            provider

            or MockEmbeddingProvider()

        )



    def create_embedding(

        self,

        text: str

    ) -> list[float]:


        return self.provider.create_embedding(

            text

        )