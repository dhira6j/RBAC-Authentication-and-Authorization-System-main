from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Role
from .serializers import RoleSerializer, UserSerializer
from users.permissions import has_permission
from django.http import JsonResponse

# users/views.py
from django.http import JsonResponse

def tester(request):
    return JsonResponse({'message': 'This is the tester view.'})



class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleManagementView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_role = request.user.role.name if request.user.role else "No Role Assigned"
        return Response({"message": f"Hello {request.user.username}, you have the role: {user_role}"})


# New: Generic tester endpoint
def api_tester(request):
    return render(request, 'users/index.html')


# New: Tester view with role-based permissions
@has_permission('can_view_data')
def tester_view(request):
    # Example response for role-based access
    data = {
        "message": "You have access to this view!",
        "roles": ["Admin", "User", "Moderator"],
        "permissions": {
            "Admin": ["can_view_data", "can_edit_data", "can_delete_data"],
            "User": ["can_view_data"],
            "Moderator": ["can_view_data", "can_edit_data"]
        },
    }
    return JsonResponse(data)
