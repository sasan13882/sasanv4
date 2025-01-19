# وب سایت فروش مصالح ساختمانی
 گزارش تکنیکال پروژه وب‌سایت فروشگاه آنلاین با استفاده از جنگو و ری‌اکت نیتیو

 1. تحلیل نیازمندی‌ها:

 شناسایی اهداف اصلی وب‌سایت:

هدف اصلی این پروژه طراحی و پیاده‌سازی یک وب‌سایت فروشگاه آنلاین با قابلیت فروش محصولات مختلف است. این وب‌سایت شامل بخش‌هایی مانند نمایش محصولات، مدیریت سبد خرید، ثبت‌نام و ورود کاربران، و مدیریت سفارش‌ها است. همچنین، کاربران باید بتوانند از طریق جستجو و فیلتر کردن محصولات در دسته‌بندی‌های مختلف، تجربه خرید بهتری داشته باشند.

 تعیین ویژگی‌های کلیدی و الزامی:

ویژگی‌های اصلی این وب‌سایت شامل موارد زیر می‌باشد:

- امکان نمایش محصولات در دسته‌بندی‌های مختلف.
- فیلتر و مرتب‌سازی محصولات بر اساس ویژگی‌های مختلف مانند قیمت و تاریخ.
- امکان مدیریت سفارش‌ها و سبد خرید.
- سیستم ثبت‌نام و ورود کاربران.
- قابلیت آپلود و مدیریت تصاویر برای دسته‌بندی‌ها و محصولات.
- مدیریت کامل کاربران (نظرات، تاریخچه خرید، و غیره).

 تحلیل بازار و رقبا:

برای طراحی این وب‌سایت، تحلیل رقبا و استفاده از ویژگی‌های مشابه در پلتفرم‌های بزرگ تجارت الکترونیک مانند دیجی‌کالا و آمازون انجام شد. هدف این است که تجربه کاربری ساده، سریع و لذت‌بخش با قابلیت جستجوی مؤثر و نمایش دسته‌بندی‌های مرتب برای کاربران ایجاد شود.

---

 2. طراحی مدل‌های داده:

 ایجاد جداول دیتابیس برای کاربران، محصولات، سفارش‌ها و غیره:

مدل‌های داده اصلی شامل جداول محصولات، دسته‌بندی‌ها، ویژگی‌های محصولات، تصاویر دسته‌بندی‌ها، و اطلاعات کاربران است. در این پروژه از دیتابیس PostgreSQL به عنوان سیستم مدیریت دیتابیس استفاده شده است.

مدل‌های داده:

- Categories: شامل اطلاعات دسته‌بندی‌ها.
- Products: شامل اطلاعات محصولات.
- ProductAttributes: ویژگی‌های اضافی محصولات.
- CategoryImages: تصاویر مرتبط با هر دسته‌بندی.
- Users: شامل اطلاعات کاربران.

```sql
CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES Categories(id) ON DELETE SET NULL,
    name VARCHAR(255) NOT NULL,
    details TEXT,
    original_price DECIMAL(10,2),
    sale_price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ProductAttributes (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES Products(id) ON DELETE CASCADE,
    attribute_name VARCHAR(255),
    attribute_value VARCHAR(255)
);

CREATE TABLE CategoryImages (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES Categories(id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

 تعریف روابط بین جداول:

مدل‌ها به‌طور منطقی به یکدیگر مرتبط هستند. به عنوان مثال، هر محصول می‌تواند به یک دسته‌بندی خاص تعلق داشته باشد و ویژگی‌های اضافی آن می‌تواند در جدول `ProductAttributes` ذخیره شود. تصاویر دسته‌بندی‌ها نیز در جدول `CategoryImages` ذخیره می‌شود.

---

 3. پیاده‌سازی بک‌اند با جنگو:

 تنظیم محیط توسعه جنگو:

در این پروژه، جنگو به عنوان فریم‌ورک اصلی بک‌اند استفاده می‌شود. ابتدا محیط توسعه جنگو تنظیم و پروژه جدید ایجاد شد. سپس اپلیکیشن‌های مختلف مانند shop و orders برای مدیریت محصولات و سفارش‌ها تعریف شدند.

 ایجاد اپلیکیشن‌های مرتبط:

در پروژه، اپلیکیشن‌های `shop` برای مدیریت محصولات و دسته‌بندی‌ها، و `orders` برای مدیریت سفارش‌ها و سبد خرید کاربران ایجاد شده است.

 تعریف مدل‌ها، نماها و سریالایزرها:

در اپلیکیشن `shop` مدل‌های محصولات و دسته‌بندی‌ها تعریف شدند. برای هر مدل، سریالایزرهایی برای تبدیل داده‌ها به فرمت JSON و برعکس ایجاد شد. نماها (Views) برای لیست، مشاهده، ایجاد، و ویرایش دسته‌بندی‌ها و محصولات پیاده‌سازی شده‌اند.

مثال مدل در جنگو:

```python
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    details = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

 ViewSets و URLs:

برای مدیریت درخواست‌های API، از `ViewSets` و `Routers` در جنگو استفاده شده است تا درخواست‌ها به درستی به نماها هدایت شوند.

---

 4. پیاده‌سازی فرانت‌اند با ری‌اکت نیتیو:

 تنظیم محیط توسعه ری‌اکت نیتیو:

محیط توسعه ری‌اکت نیتیو برای پلتفرم‌های iOS و Android تنظیم شده است. از `React Navigation` برای مدیریت ناوبری و `Redux` برای مدیریت وضعیت استفاده شده است.

 ایجاد صفحات و کامپوننت‌ها:

در پروژه، صفحات مختلفی مانند HomeScreen، ProductDetailScreen و CartScreen برای نمایش محصولات، جزئیات آن‌ها و سبد خرید ایجاد شده است. همچنین کامپوننت‌های ProductCard و Button برای استفاده مجدد در صفحات مختلف طراحی شده‌اند.

 اتصال به APIهای بک‌اند:

برای اتصال به بک‌اند و دریافت داده‌ها از API، از Axios و `ApiService.js` استفاده شده است.

---

 5. مدیریت دیتابیس با SQL:

 انتخاب سیستم مدیریت دیتابیس (PostgreSQL):

برای ذخیره‌سازی داده‌ها از PostgreSQL به عنوان سیستم مدیریت دیتابیس استفاده شده است. SQL برای ایجاد جداول و مدیریت روابط بین آن‌ها نوشته شده است.

 نوشتن اسکریپت‌های SQL:

اسکریپت‌های SQL برای ایجاد و مدیریت جداول (دسته‌بندی‌ها، محصولات، ویژگی‌ها و تصاویر) در دیتابیس نوشته شده است.

---

 6. ارتباط بین بخش‌ها:

 تعریف API endpoints:

APIهایی برای مدیریت داده‌های محصولات، دسته‌بندی‌ها و ویژگی‌های آن‌ها تعریف شده است. این APIها از طریق درخواست‌های GET، POST، PUT و DELETE به ارتباط بین بک‌اند و فرانت‌اند می‌پردازند.

 پیاده‌سازی احراز هویت و مجوزها:

برای احراز هویت کاربران از JWT استفاده شده است تا امنیت درخواست‌ها تأمین شود. مجوزهای لازم برای دسترسی به بخش‌های مختلف (مانند اضافه کردن محصولات یا ویرایش سبد خرید) در نظر گرفته شده است.

 اطمینان از ارتباط صحیح بین بک‌اند و فرانت‌اند:

با استفاده از Axios و APIهای مرتبط، اطمینان حاصل شده است که داده‌ها به درستی از بک‌اند به فرانت‌اند ارسال و دریافت می‌شوند.

---

 7. تست و استقرار:

 نوشتن تست‌های واحد و یکپارچه:

برای اطمینان از عملکرد درست سیستم، تست‌های واحد برای مدل‌ها و APIها نوشته شده است.

 استفاده از ابزارهای CI/CD:

از ابزارهایی مانند GitHub Actions برای استقرار خودکار پروژه در محیط‌های مختلف استفاده شده است.

 تنظیم سرور و استقرار نهایی وب‌سایت:

پروژه بر روی سرورهای AWS یا مشابه استقرار یافته است.

---

 8. مدیریت نسخه با GitHub:

 ایجاد مخزن GitHub:

یک مخزن GitHub برای پروژه ایجاد شده است تا کدها به صورت دسته‌بندی شده مدیریت شوند.

 تعریف شاخه‌های مختلف برای توسعه:

برای توسعه ویژگی‌های مختلف از شاخه‌های جداگانه استفاده شده است. پس از اتمام توسعه هر ویژگی، کدها به شاخه اصلی (main) merge می‌شوند.

 استفاده از Pull Requests برای بررسی کدها:

برای بررسی کدهای توسعه، از Pull Requests استفاده شده است تا کدها قبل از merge بررسی و تأیید شوند.

---
