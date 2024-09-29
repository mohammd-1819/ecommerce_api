from rest_framework import permissions
from . import views


class ReadOnlyUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if isinstance(view, views.CategoryListView) or isinstance(view, views.CategoryDetailView):
            return request.user.has_perm('app.view_category')
        elif isinstance(view, views.ProductListView) or isinstance(view, views.ProductDetailView):
            return request.user.has_perm('app.view_product')
        elif isinstance(view, views.ColorListView) or isinstance(view, views.ColorDetailView):
            return request.user.has_perm('app.view_color')
        elif isinstance(view, views.SizeListView) or isinstance(view, views.SizeDetailView):
            return request.user.has_perm('app.view_size')
        elif isinstance(view, views.CommentListView) or isinstance(view, views.CommentDetailView):
            return request.user.has_perm('app.view_comment')
        elif isinstance(view, views.ProductReviewListView) or isinstance(view, views.ProductReviewDetailView):
            return request.user.has_perm('app.view_product_review')
        return False


# ------------------------------------------------------------------------------------

class ProductUpdater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.change_product')


class ProductDeleter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.delete_product')


class ProductCreater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.create_product')


# ------------------------------------------------------------------------------------
class CategoryUpdater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.change_category')


class CategoryDeleter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.delete_category')


class CategoryCreater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.create_category')


# ------------------------------------------------------------------------------------

class ColorUpdater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.change_color')


class ColorDeleter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.delete_color')


class ColorCreater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.create_color')


# ------------------------------------------------------------------------------------


class SizeUpdater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.change_size')


class SizeDeleter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.delete_size')


class SizeCreater(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('app.create_size')
