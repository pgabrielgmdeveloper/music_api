import aioboto3
from src.configs.settings import settings

class S3Client:
    def __init__(self) -> None:
        self._region = 'us-east-2'
        self._client = None
        self.__session = aioboto3.Session(
            aws_access_key_id=settings.access_key,
            aws_secret_access_key=settings.secret_key
        )

    async def _create_client(self):
        if not self._client:
            self._client = await self.__session.client('s3', region_name=self._region).__aenter__()
        return

    async def put(self, file, object_name: str):
        await self._create_client()
        try:
            # Verifique se `file.file` é um objeto semelhante a um arquivo
            await self._client.upload_fileobj(file.file, settings.bucket_name, object_name)
        except Exception as e:
            print(f"Error uploading file: {e}")

    async def get_objects(self, key: str):
        await self._create_client()
        try:
            download_url = await self._client.generate_presigned_url(
                'get_object',
                Params={'Bucket': settings.bucket_name, 'Key': key},
                ExpiresIn=3600  # URL válida por 1 hora
            )
            return download_url
        except Exception as e:
            print(f"Error generating presigned URL: {e}")

