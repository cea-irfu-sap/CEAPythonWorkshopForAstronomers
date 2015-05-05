module futils
contains
    function f(x) result(res)
        implicit none
        real(8), intent(in) :: x
        real(8) :: res
                
        res = 4.d0/(1.d0 + x*x)
    end function f
    

    subroutine compPi_fortran(pi, error, niter)
        implicit none
        
        integer, intent(in) :: niter
        real(8), intent(out) :: pi, error
        real(8) :: h, x
        integer :: i        

        h = 1.d0/niter
        pi = 0.d0
        error = 0.d0
        
        do i = 1, niter
            x = h*(i - 0.5d0)
            pi = pi + f(x)
        enddo
        pi = pi*h
        
        error = abs(acos(-1.d0) - pi)/acos(-1.d0)
    end subroutine compPi_fortran

end module futils