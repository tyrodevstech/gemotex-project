from django.db import models

# Define Product Category Model
class ProductCategoryModel(models.Model):
    category_name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


# Define Product Subcategory Model
class ProductSubcategoryModel(models.Model):
    category = models.ForeignKey(
        ProductCategoryModel,
        on_delete=models.CASCADE,
        null=True,
        related_name="subcategories",
    )
    subcategory_name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"


# Define Product Model
class ProductModel(models.Model):
    title = models.CharField(max_length=122, null=True, verbose_name="Product Title")
    category = models.ForeignKey(
        ProductCategoryModel,
        on_delete=models.CASCADE,
        null=True,
        related_name="products",
    )
    subcategory = models.ForeignKey(
        ProductSubcategoryModel,
        on_delete=models.CASCADE,
        null=True,
        related_name="products",
    )
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Product Details"
    )
    info = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Additional Information"
    )
    tag = models.CharField(max_length=6, null=True, default="NEW")

    cover_image = models.ImageField(
        upload_to="product-cover-image/%Y/%d/%b",
        null=True,
        help_text="Size Direction: W:800PX & H:975PX",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-id"]


# Define Product Images Model
class ProductImagesModel(models.Model):
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, null=True, related_name="images"
    )
    image = models.ImageField(upload_to="products-images/%Y/%d/%b", null=True)

    def __str__(self):
        return f"{self.id} - {self.product.title}"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


# Define Contact Information Model
class HeaderSliderModel(models.Model):
    title = models.CharField(null=True, blank=True, max_length=125)
    promo = models.TextField(null=True, blank=True, max_length=225)
    cta_text = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="button text"
    )
    cta_link = models.URLField(null=True, blank=True, verbose_name="button link")
    bg_img = models.ImageField(
        upload_to="headersliderbg",
        null=True,
        verbose_name="background image",
        help_text="image size: w-1920px x h-1100",
    )
    active = models.BooleanField(default=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Header Slider"
        verbose_name_plural = "Header Sliders"


class BrandGalleryModel(models.Model):
    obj_name = models.CharField(null=True, max_length=125, default="Brand Gallery Object", verbose_name="object name")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    left_img = models.ImageField(
        upload_to="brand-gallery",
        null=True,
        verbose_name="left site image",
        help_text="image size: w-1000px x h-1000",
    )

    top_img = models.ImageField(
        upload_to="brand-gallery",
        null=True,
        verbose_name="top site image",
        help_text="image size: w-1000px x h-480",
    )

    bottom_img = models.ImageField(
        upload_to="brand-gallery",
        null=True,
        verbose_name="bottom site image",
        help_text="image size: w-1000px x h-480",
    )

    def __str__(self):
        return f"{self.obj_name}"

    class Meta:
        verbose_name = "Brand Gallery"
        verbose_name_plural = "Brand Gallery"


class PartnerCompanyModel(models.Model):
    partner_name = models.CharField(null=True, max_length=125, verbose_name="partner company name")
    logo = models.ImageField(
        upload_to="partner-company-logos",
        null=True,
        help_text="image size: w-230px x h-140",
    )

    def __str__(self):
        return f"{self.partner_name} | N.B: you can add only 6 objects in this table."

    class Meta:
        verbose_name = "Partner Company Logo"
        verbose_name_plural = "Partner Company Logos"
        


class ShortAboutInfoModel(models.Model):
    title = models.CharField(null=True, max_length=200)
    summary = models.TextField(null=True, max_length=555)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Short About Information"
        verbose_name_plural = "Short About Informations"


class IntroVideoModel(models.Model):
    title = models.CharField(null=True, max_length=200, default="Gemotex Intro Video")
    link = models.URLField(null=True, verbose_name="video link")
    thumbnail = models.ImageField(
        upload_to="intro-thumbnail",
        null=True,
        verbose_name="video thumbnail",
        help_text="image size: w-1920px x h-700px",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Introduction Video"
        verbose_name_plural = "Introduction Video"


class AboutCardModel(models.Model):
    title = models.CharField(null=True, max_length=150)
    sub_title = models.CharField(null=True, max_length=50)
    btn_text = models.CharField(null=True, max_length=100)
    btn_link = models.URLField(null=True, verbose_name="video link")
    details = models.TextField(null=True, max_length=525, verbose_name="card details")
    card_img = models.ImageField(
        upload_to="about-card-images",
        null=True,
        verbose_name="card image",
        help_text="image size: w-800px x h-800px",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "About Card"
        verbose_name_plural = "About Cards"



class AboutVideoModel(models.Model):
    title = models.CharField(null=True, max_length=200, default="Gemotex About Video")
    link = models.URLField(null=True, verbose_name="video link")
    thumbnail = models.ImageField(
        upload_to="about-thumbnail",
        null=True,
        verbose_name="video thumbnail",
        help_text="image size: w-1920px x h-700px",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "About Video"
        verbose_name_plural = "About Video"



class ReviewModel(models.Model):
    details = models.TextField(null=True, max_length=525, verbose_name="client comment")
    profile = models.ImageField(
        upload_to="client-review-profiles",
        null=True,
        blank=True,
        verbose_name="person image",
    )
    name = models.CharField(max_length=225, null=True, verbose_name="client name")
    position = models.CharField(
        max_length=225, null=True, verbose_name="job description"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}- review"

    class Meta:
        verbose_name = "Client Review"
        verbose_name_plural = "Client Reviews"

        ordering = ["-id"]


class ContactInformationModel(models.Model):
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Short Summary"
    )
    phone = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    address = models.TextField(null=True, blank=True, max_length=325)
    work = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Working Date & Time"
    )

    def __str__(self):
        return f"{self.id} - Contact Info"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"
        ordering = ["-id"]


# Define Footer Information Model
class FooterInformationModel(models.Model):
    details = models.TextField(null=True, max_length=325, verbose_name="Short Summary")
    facebook_link = models.URLField(null=True, blank=True, verbose_name="Facebook Link")
    twitter_link = models.URLField(null=True, blank=True, verbose_name="Twitter Link")
    instagram_link = models.URLField(
        null=True, blank=True, verbose_name="Instagram Link"
    )
    youtube_link = models.URLField(null=True, blank=True, verbose_name="YouTube Link")

    def __str__(self):
        return f"{self.id} - Footer Info"

    class Meta:
        verbose_name = "Footer Information"
        verbose_name_plural = "Footer Informations"
        ordering = ["-id"]
